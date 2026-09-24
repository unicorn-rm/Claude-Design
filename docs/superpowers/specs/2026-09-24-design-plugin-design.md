# Спека: плагин `design` — «Senior дизайн-компаньон»

**Дата:** 2026-09-24
**Статус:** дизайн согласован владельцем.
**Публикация:** `unicorn-rm/Claude-Design` → маркетплейс `claude-design` (свой репо; без владельца не пушить).

## Вводные (утв. владельцем)
- **Для дизайнеров.** Большой охват, senior-компаньон. Работает со шрифтами, графикой, 3D.
- **Главное:** создаёт дизайн **не ИИшный** — интенциональный, с точкой зрения, грунтованный реальными референсами.
- **Выход:** дизайн, который отгружается — реальный HTML/CSS/React/Tailwind + claude.ai-артефакты, опираясь на библиотеки.
- **Доктрина «не ИИшности»:** агностичная + грунтована конкретными эталонами (Anthropic-CSS, awwwards-уровень) как доказательством, не как навязанным стилем.
- **3D/мошн:** полноценно, но оркеструя (Three.js/R3F/Spline/GSAP + сорсинг Sketchfab/poly.pizza/Vectary), не переизобретая библиотеки.
- **Авто-срабатывание:** плагин включается сам, когда речь о сайте/дизайне/UI/бренде/цвете/шрифте/3D/артефакте.
- **Источники:** большой список владельца + мои добавки + GitHub как первоклассный источник готового кода.
- **Инструменты:** WebFetch, браузер, GitHub, существующие скиллы threejs-*/gsap/artifact-*.

## Архитектура — 5 слоёв
1. Backbone (доктрина + грунтование). 2. Домены-скиллы. 3. Агенты. 4. Команды. 5. Валидатор + эвалы (хуков нет — нет разрушительных операций).

## Backbone (2)
- **`distinctive-design`** (аналог gate, «анти-слоп»). Срабатывает всегда при рождении/ревью дизайна. Каталог ИИ-тэллов (центр-всё, фиолет-градиенты, глассморфизм/`backdrop-filter`, Inter на всё, эмодзи-заголовки, 3 одинаковые карточки, hero→фичи→CTA под копирку, мягкие тени на белом, переоскругление, нет точки зрения) → приёмы против (точка зрения, реальная типографика, оптический трим, сдержанность, тёплая палитра/текстура/зерно, редакторский/асимметричный лейаут, один изинг, осмысленный мошн). Грунтована разбором Anthropic-CSS. ref: `ai-design-tells.md`.
- **`design-grounding`** (аналог docs-grounding). Решения от реальных курируемых источников и реальных спек, не выдумывать hex/шрифты/классы/имена компонентов/контраст. Реестр источников + модель доступа (WebFetch/браузер/API/логин-гейт/GitHub). refs: `sources-registry.md`, `design-direction-schema.md`.

## Домены (22)
- **Foundations (6):** color-systems, typography, layout-and-composition, design-systems, iconography, illustration-and-imagery.
- **Web/UI (6):** web-design, ui-components, responsive-design, accessibility, ux-principles, landing-pages.
- **Motion/3D/creative (4):** motion-and-interaction, web-3d, 3d-assets-and-shaders, generative-and-creative-coding.
- **Process/delivery (6):** design-research, visual-critique, design-to-artifact, brand-identity, dev-handoff, data-visualization.

**Итого 24 скилла** (2 backbone + 22 доменных).

## Агенты (6)
art-director · ui-designer · design-critic · motion-3d-designer · brand-designer · design-researcher.

## Команды (8)
/brief (праймер → `.design/brief.md`) · /moodboard · /critique · /palette · /typeset · /artifact · /design-review · /handoff.

## Реестр источников
Color (Coolors/Colorhunt/Adobe Color/Happy Hues/Khroma/uicolors + Realtime Colors/Radix Colors/Open Color/Tailwind/Leonardo/WebAIM) · Type (Google/Adobe Fonts/Typewolf/Fontpair + Fontshare/Fontsource/Modern Font Stacks/type-scale/Wakamai Fondue) · Inspiration (awwwards/land-book/lapa/mobbin/refero/siteinspire/recent.design/dribbble/behance/pinterest/artstation + Godly/SaaSLandingPage/Landingfolio/Httpster/Minimal.gallery/Screenlane/CSSDA/FWA/Page Flows) · Components (shadcn/21st/Aceternity/Magic UI/Tailwind/Radix/HyperUI/Flowbite + Tailwind UI/daisyUI/Park UI/Tremor/Origin·Cult·Kokonut UI/Motion/Headless UI) · 3D/graphics (Spline/Sketchfab/poly.pizza/Vectary/DrawKit + R3F·drei/Three.js Journey/Poly Haven/Quaternius/Shadertoy/Rive/Lottie/Haikei/Hero Patterns/unDraw·Blush·Humaaans) · Icons (Lucide/Heroicons/Phosphor/Tabler/Iconify/Simple Icons) · **GitHub** (реальный код, awesome-списки).
Модель доступа: публичные → WebFetch/браузер; API → Google Fonts/poly.pizza/Sketchfab; код → GitHub; логин-гейт → именованные референсы + просить экраны у владельца.

## Инфраструктура
- Валидатор `tools/validate_plugin.py`: backbone на месте; производящие/критикующие скиллы → `distinctive-design`+`design-grounding`; остальные → `design-grounding`; словарь references; NOTICE; ≥5 эвалов. Хуков нет.
- Эвалы (5): отвергает ИИ-слоп/критик называет тэллы; палитру+шрифты грунтует реальными; /moodboard — направление с точкой зрения из реальных референсов; контраст WCAG посчитан; /artifact — отгружаемый HTML по доктрине.

## Фазы
- Ф0: фундамент (2 backbone + refs + /brief + manifest + marketplace + валидатор + NOTICE + LICENSE/README).
- Ф1 «отличимый лендинг»: web-design + layout-and-composition + color-systems + typography + ui-components + design-to-artifact + `art-director` + /moodboard /artifact /palette /typeset.
- Ф2 критика+ресёрч+a11y: design-research + visual-critique + accessibility + ux-principles + responsive-design + `design-critic`,`design-researcher` + /critique /design-review.
- Ф3 motion+3D: motion-and-interaction + web-3d + 3d-assets-and-shaders + generative-and-creative-coding + `motion-3d-designer`.
- Ф4 остаток: design-systems + iconography + illustration-and-imagery + landing-pages + brand-identity + data-visualization + dev-handoff + `ui-designer`,`brand-designer` + /handoff.

**Границы:** владеет дизайн-крафтом + design-to-code/артефактами; полную инженерию → будущий dev/frontend, деплой → devops. Контент авторский, grounded реальными источниками (донора нет).
