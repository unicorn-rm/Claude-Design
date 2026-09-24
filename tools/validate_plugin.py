#!/usr/bin/env python3
"""Dependency-free structural validator for the `design` plugin.
Exit 0 if valid, else exit 1 and print errors. No external deps."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "design"
DESC_CAP = 1536

def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:]
    fm, key = {}, None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if re.match(r"^\s*-\s+", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(line.strip()[2:].strip().strip('"\''))
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            fm[key] = val.strip('"\'') if val else []
    return fm, body

REQUIRED_BACKBONE = ["distinctive-design", "design-grounding"]
BACKBONE_REFS = {
    "distinctive-design": ["ai-design-tells.md"],
    "design-grounding": ["sources-registry.md", "design-direction-schema.md"],
}

# Skills that produce or critique actual visual design -> reference BOTH
# distinctive-design (anti-slop) AND design-grounding.
PRODUCING_SKILLS = [
    "web-design", "ui-components", "landing-pages", "layout-and-composition",
    "color-systems", "typography", "illustration-and-imagery", "iconography",
    "motion-and-interaction", "web-3d", "3d-assets-and-shaders",
    "generative-and-creative-coding", "design-to-artifact", "brand-identity",
    "design-systems", "data-visualization", "design-critique",
]
# Knowledge/process skills -> reference design-grounding.
GROUNDED_SKILLS = [
    "responsive-design", "accessibility", "ux-principles", "design-research",
    "design-handoff",
]
ALL_DOMAIN = PRODUCING_SKILLS + GROUNDED_SKILLS

REQUIRED_REFERENCES = {
    "typography": ["type-pairing.md"],
    "ui-components": ["component-libraries.md"],
    "web-3d": ["threejs-and-spline.md"],
    "design-research": ["reference-sourcing.md"],
    "web-design": ["section-patterns.md"],
}

def validate():
    errors = []
    mf = PLUGIN / ".claude-plugin" / "plugin.json"
    if not mf.exists():
        return [f"missing manifest: {mf}"]
    try:
        data = json.loads(mf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"plugin.json invalid JSON: {e}"]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", data.get("name", "")):
        errors.append(f"plugin.json name not kebab-case: {data.get('name')!r}")
    if not data.get("version"):
        errors.append("plugin.json missing version")

    for skill_md in (PLUGIN / "skills").glob("*/SKILL.md"):
        fm, _ = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        desc = (fm.get("description") or "")
        wtu = (fm.get("when_to_use") or "")
        if not isinstance(desc, str) or not desc:
            errors.append(f"{skill_md}: missing description")
        if len(str(desc)) + len(str(wtu)) > DESC_CAP:
            errors.append(f"{skill_md}: description+when_to_use over {DESC_CAP}")

    for cmd_md in (PLUGIN / "commands").glob("*.md"):
        fm, _ = parse_frontmatter(cmd_md.read_text(encoding="utf-8"))
        if not fm.get("description"):
            errors.append(f"{cmd_md}: missing description")

    for ag_md in (PLUGIN / "agents").glob("*.md"):
        fm, _ = parse_frontmatter(ag_md.read_text(encoding="utf-8"))
        if not fm.get("name"):
            errors.append(f"{ag_md}: missing name")
        if not fm.get("description"):
            errors.append(f"{ag_md}: missing description")

    for rs in REQUIRED_BACKBONE:
        if not (PLUGIN / "skills" / rs / "SKILL.md").exists():
            errors.append(f"missing required backbone skill: {rs}")
    for sk, refs in BACKBONE_REFS.items():
        for rf in refs:
            if not (PLUGIN / "skills" / sk / "references" / rf).exists():
                errors.append(f"missing reference: {sk}/references/{rf}")

    for ps in PRODUCING_SKILLS:
        sp = PLUGIN / "skills" / ps / "SKILL.md"
        if not sp.exists():
            errors.append(f"missing producing skill: {ps}")
            continue
        _, body = parse_frontmatter(sp.read_text(encoding="utf-8"))
        for marker in ["distinctive-design", "design-grounding"]:
            if marker not in body:
                errors.append(f"{ps}: body must reference {marker}")

    for gs in GROUNDED_SKILLS:
        sp = PLUGIN / "skills" / gs / "SKILL.md"
        if not sp.exists():
            errors.append(f"missing skill: {gs}")
            continue
        _, body = parse_frontmatter(sp.read_text(encoding="utf-8"))
        if "design-grounding" not in body:
            errors.append(f"{gs}: body must reference design-grounding")

    for skill_name, ref_files in REQUIRED_REFERENCES.items():
        if (PLUGIN / "skills" / skill_name / "SKILL.md").exists():
            for rf in ref_files:
                if not (PLUGIN / "skills" / skill_name / "references" / rf).exists():
                    errors.append(f"missing reference: {skill_name}/references/{rf}")

    if not (PLUGIN / "NOTICE.md").exists():
        errors.append("missing NOTICE.md")

    eval_dir = PLUGIN / "evals"
    eval_cases = [d for d in eval_dir.glob("*") if d.is_dir()] if eval_dir.exists() else []
    if len(eval_cases) < 5:
        errors.append(f"eval suite has {len(eval_cases)} cases, expected >= 5")
    for case in eval_cases:
        if not (case / "prompt.md").exists():
            errors.append(f"eval case {case.name}: missing prompt.md")
        graders = list((case / "graders").glob("*.md")) if (case / "graders").exists() else []
        if not graders:
            errors.append(f"eval case {case.name}: no graders")
    return errors

def main():
    errs = validate()
    if errs:
        print("FAIL:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print("OK: plugin structure valid")
    sys.exit(0)

if __name__ == "__main__":
    main()
