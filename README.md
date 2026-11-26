🌐 **English** · [简体中文](locales/zh/README.md) · [Español](locales/es/README.md) · [हिन्दी](locales/hi/README.md) · [Français](locales/fr/README.md)

# Awesome AI Design

An AI design catalogue for designers, product teams and coding agents. It collects reusable design Skills, runnable design agents, editors and bridging tools, plus the papers and benchmarks behind the research conclusions.

Here, "AI design" means agents taking part in creating, modifying, reviewing or handing off interfaces, prototypes, vector graphics, diagrams, presentations or design systems. Pure text-to-image models, general coding agents and SaaS without a verifiable repository are not listed as core tools. Official integration guides and design-system indexes are marked separately; the existing [AI video catalogue](https://github.com/ZanePoe/awesome_ai_video_creation) covers video generation and editing.

## Jump to a category

[Design agents and prototyping workbenches](#design-agents-and-prototyping-workbenches) · [Editable canvas and vector design](#editable-canvas-and-vector-design) · [Front-end design, motion and review Skills](#front-end-design-motion-and-review-skills) · [Design systems and DESIGN.md](#design-systems-and-designmd) · [Design-to-code and MCP bridges](#design-to-code-and-mcp-bridges) · [Diagrams and visual expression](#diagrams-and-visual-expression) · [Presentations and document design](#presentations-and-document-design) · [Papers, benchmarks and datasets](#papers-benchmarks-and-datasets) · [Historical and archived projects](#historical-and-archived-projects)

## Current coverage

**36 projects, of which 4 are user-reference projects and 32 were added in this round.** Feature verification: 2026-11-26; metrics snapshot: `2026-11-26T04:03:50+00:00` (UTC).

Within each category, projects are first tiered by maintenance status, then ranked by a blend of stars (40%), 90-day default-branch commits (35%) and recency of the last commit (25%). The maintenance score does not represent design quality, model capability, accessibility or production readiness.

## Active core projects at a glance

Shows only core candidates with a verified open license and commits in the last 90 days; restricted-license projects, research benchmarks and adjacent tools are excluded from this table.

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score |
| --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | Design vocabulary, polish, critique and review commands for coding agents iterating on existing interfaces. | 116,989 | 2,259 | 2026-11-26 | 100.0 |
| [Penpot](https://github.com/penpot/penpot) | Self-hostable collaborative design platform with design tokens, components and an MCP interface bridging design and code. | 62,748 | 1,619 | 2026-11-25 | 98.3 |
| [OpenDesign](https://github.com/nexu-io/open-design) | Generate design-system-compliant prototypes with a local coding agent or OpenDesign Cloud, then share and iterate on a team workbench. | 109,524 | 415 | 2026-11-23 | 98.2 |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | Outputs architecture, flow and data diagrams as self-contained HTML/SVG with brand styling. | 73,182 | 364 | 2026-11-25 | 96.9 |
| [OpenPencil (open-source design editor)](https://github.com/open-pencil/open-pencil) | Programmable design editor with AI, CLI and MCP that opens .fig and .pen files. | 10,117 | 1,580 | 2026-11-25 | 91.9 |
| [OpenPencil (AI-native vector design tool)](https://github.com/ZSeven-W/openpencil) | Turns natural language into editable interfaces on the canvas, with parallel multi-agent design and MCP operations. | 7,367 | 914 | 2026-11-25 | 90.7 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent Skill offering style, color, typography and design-system guidance across multiple front-end stacks. | 154,266 | 94 | 2026-11-25 | 90.6 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | Local desktop design agent that turns prompts into previewable design artifacts and lets you connect models of your choice. | 8,258 | 145 | 2026-11-25 | 84.2 |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | Ports OpenDesign's design Skills, brand design system and examples for use inside coding agents. | 1,197 | 429 | 2026-11-25 | 83.7 |
| [Onlook](https://github.com/onlook-dev/onlook) | Local-first visual code editor in which existing agents such as Claude Code or Codex work inside your project. | 27,952 | 40 | 2026-11-26 | 81.5 |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) | UI and motion Skills for designers and engineers, covering motion choices, review and performance improvements. | 59,678 | 19 | 2026-11-15 | 77.3 |
| [GitHub Replica](https://github.com/github/replica) | Generate and iterate interactive prototypes with GitHub Copilot using the team's existing components, patterns and design guidance. | 382 | 126 | 2026-11-25 | 72.8 |

## Category index

`★User reference` marks projects provided directly by the user. Each repository appears in one primary category only; the project detail table records dependencies and limitations.

| Category | Count | Top projects by maintenance rank |
| --- | --- | --- |
| Design agents and prototyping workbenches | 5 | OpenDesign, Open CoDesign, GitHub Replica |
| Editable canvas and vector design | 5 | Penpot, OpenPencil (open-source design editor), OpenPencil (AI-native vector design tool) |
| Front-end design, motion and review Skills | 9 | Impeccable, UI UX Pro Max, Open Design Agent Kit |
| Design systems and DESIGN.md | 4 | Stitch Design Skills, Google DESIGN.md, Awesome DESIGN.md |
| Design-to-code and MCP bridges | 4 | Screenshot to Code, Figma MCP Server Guide, Framelink Figma MCP |
| Diagrams and visual expression | 3 | Diagram Design, Excalidraw MCP Server, Spotkit |
| Presentations and document design | 1 | PPT Agent Skill |
| Papers, benchmarks and datasets | 3 | DesignBench, Design2Code, WebDesignAgent |
| Historical and archived projects | 2 | SuperDesign IDE Extension (legacy), Penpot MCP Server (archived repository) |

### Design agents and prototyping workbenches

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [OpenDesign](https://github.com/nexu-io/open-design) · ★User reference | Generate design-system-compliant prototypes with a local coding agent or OpenDesign Cloud, then share and iterate on a team workbench. | 109,524 | 415 | 2026-11-23 | 98.2 | Apache-2.0 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | Local desktop design agent that turns prompts into previewable design artifacts and lets you connect models of your choice. | 8,258 | 145 | 2026-11-25 | 84.2 | MIT |
| [GitHub Replica](https://github.com/github/replica) · ★User reference | Generate and iterate interactive prototypes with GitHub Copilot using the team's existing components, patterns and design guidance. | 382 | 126 | 2026-11-25 | 72.8 | MIT |
| [fx0](https://github.com/vercel-labs/fx0) | Lightweight design agent built on libfx that iterates through natural language and exports single-file HTML pages. | 442 | 134 | 2026-11-18 | 71.7 | Apache-2.0 |
| [LangChain Content Studio](https://github.com/langchain-ai/design-agent) | Brand design agent for teams that receives assets and requests from Slack and delivers wireframes, presentations or dynamic content. | 767 | 72 | 2026-11-23 | 71.6 | Apache-2.0 |

### Editable canvas and vector design

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [Penpot](https://github.com/penpot/penpot) | Self-hostable collaborative design platform with design tokens, components and an MCP interface bridging design and code. | 62,748 | 1,619 | 2026-11-25 | 98.3 | MPL-2.0 |
| [OpenPencil (open-source design editor)](https://github.com/open-pencil/open-pencil) | Programmable design editor with AI, CLI and MCP that opens .fig and .pen files. | 10,117 | 1,580 | 2026-11-25 | 91.9 | MIT |
| [OpenPencil (AI-native vector design tool)](https://github.com/ZSeven-W/openpencil) | Turns natural language into editable interfaces on the canvas, with parallel multi-agent design and MCP operations. | 7,367 | 914 | 2026-11-25 | 90.7 | MIT |
| [Onlook](https://github.com/onlook-dev/onlook) | Local-first visual code editor in which existing agents such as Claude Code or Codex work inside your project. | 27,952 | 40 | 2026-11-26 | 81.5 | Apache-2.0 |
| [Velloo](https://github.com/velloo-design/velloo) | Lets coding agents explore multiple directions on a local canvas using existing app components, then write the chosen design back into the app. | 10 | 261 | 2026-11-17 | 62.4 | Apache-2.0 |

### Front-end design, motion and review Skills

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | Design vocabulary, polish, critique and review commands for coding agents iterating on existing interfaces. | 116,989 | 2,259 | 2026-11-26 | 100.0 | Apache-2.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent Skill offering style, color, typography and design-system guidance across multiple front-end stacks. | 154,266 | 94 | 2026-11-25 | 90.6 | MIT |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | Ports OpenDesign's design Skills, brand design system and examples for use inside coding agents. | 1,197 | 429 | 2026-11-25 | 83.7 | MIT |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) · ★User reference | UI and motion Skills for designers and engineers, covering motion choices, review and performance improvements. | 59,678 | 19 | 2026-11-15 | 77.3 | MIT |
| [Logo Design Skill](https://github.com/kaankiziltug/logo-design-skill) · License caution | A logo-design skill running from brief to deliverable SVG and brand guidelines, with a 1,400+ real-logo reference library, geometry and optical correction rules and dependency-free Python checks. | 7,782 | 32 | 2026-11-13 | 72.6 | MIT (code and skills) + third-party trademarked logo library excluded |
| [Make Interfaces Feel Better](https://github.com/jakubkrehel/make-interfaces-feel-better) | An agent skill for the small details that make interfaces feel better: animation, typography, icons, hover states, optical alignment and concentric radii, installed with one skills CLI command. | 4,294 | 3 | 2026-11-18 | 59.7 | MIT |
| [cc-skills](https://github.com/samber/cc-skills) | Cross-domain collection of agent skills loaded on demand; its frontend-design-deslop skill strips the generic AI look from web frontends. | 283 | 16 | 2026-11-01 | 54.5 | MIT |
| [Better Design](https://github.com/Moddingflow/better-design) | A repeatable interface-design process for coding agents: product-specific art direction, a shared DESIGN.md, measured typography and control specs, plus validation scripts and a clickable demo. | 79 | 9 | 2026-10-27 | 46.2 | MIT |
| [Frontend AI Skills](https://github.com/JustineBijuPaul/frontend-ai-skills) | Modular front-end Skills loaded on demand, covering motion, interaction, accessibility and related topics. | 11 | 86 | 2026-09-04 | 43.8 | MIT |

### Design systems and DESIGN.md

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills) | Official skills and plugins collection for Google Stitch, connecting agents to its design workflow. | 13,026 | 22 | 2026-11-24 | 75.2 | Apache-2.0 |
| [Google DESIGN.md](https://github.com/google-labs-code/design.md) | Visual-identity specification that puts machine-readable design tokens and agent-readable design principles in one file. | 29,129 | 9 | 2026-11-18 | 71.5 | Apache-2.0 |
| [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) | Collection of reusable DESIGN.md reference documents giving agents brand style, typography, color and component conventions. | 129,098 | 8 | 2026-10-28 | 70.6 | MIT |
| [extract-design-system](https://github.com/arvindrk/extract-design-system) | Reverse-engineers design tokens - colors, typography, spacing, radius and shadows - from any public website and emits W3C-compatible tokens.json plus a CSS custom-properties file. | 316 | 0 | 2026-06-19 | 24.3 | MIT |

### Design-to-code and MCP bridges

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [Screenshot to Code](https://github.com/abi/screenshot-to-code) | Uses models to turn screenshots, prototypes, Figma designs or screen recordings into interface code. | 81,446 | 6 | 2026-11-15 | 72.5 | MIT |
| [Figma MCP Server Guide](https://github.com/figma/mcp-server-guide) · License caution | Official Figma integration guide describing how agents obtain design context and some remote write workflows. | 2,235 | 30 | 2026-11-24 | 70.7 | Unverified |
| [Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP) | Provides coding agents with design context from Figma files to help implement existing interfaces. | 16,314 | 0 | 2026-06-24 | 38.2 | MIT |
| [Talk to Figma MCP](https://github.com/grab/cursor-talk-to-figma-mcp) | Lets agents read and modify Figma designs through an MCP server, a Figma plugin and a WebSocket bridge. | 7,130 | 0 | 2026-07-26 | 37.2 | MIT |

### Diagrams and visual expression

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) · ★User reference | Outputs architecture, flow and data diagrams as self-contained HTML/SVG with brand styling. | 73,182 | 364 | 2026-11-25 | 96.9 | MIT |
| [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw) | Provides a readable, writable Excalidraw canvas that modifies and saves diagrams via CLI, Skill or MCP. | 2,687 | 33 | 2026-11-10 | 68.3 | MIT |
| [Spotkit](https://github.com/Devesh-Shirsath/spotkit) | A Claude Code skill that turns a feature description into real SVG abstract product illustrations, first working out what the feature does and which relationship it expresses, then picking 2-5 UI primitives and a layout. | 130 | 33 | 2026-10-08 | 51.3 | MIT |

### Presentations and document design

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) | A Claude Code Skill that runs the workflow of a high-end presentation studio: research, source gathering, outline, deck plan, HTML slide design, then post-processing into SVG and editable PPTX, from one sentence to a deliverable deck. | 209 | 11 | 2026-11-18 | 55.5 | MIT |

### Papers, benchmarks and datasets

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [DesignBench](https://github.com/WebPAI/DesignBench) · License caution | Research benchmark evaluating multi-framework front-end code generation, editing and repair. | 61 | 0 | 2026-07-27 | 20.8 | Unverified |
| [Design2Code](https://github.com/NoviScl/Design2Code) | Screenshot-to-code research on real web pages, with datasets and automatic evaluation tooling. | 605 | 0 | 2024-11-02 | 22.3 | MIT |
| [WebDesignAgent](https://github.com/DAMO-NLP-SG/WebDesignAgent) | Website-generation research prototype showing a design flow driven by descriptions, reference layouts, images and feedback. | 267 | 0 | 2024-09-20 | 19.4 | Apache-2.0 |

### Historical and archived projects

| Project | Positioning | Stars | 90-day commits | Last commit (UTC) | Maintenance score | License |
| --- | --- | --- | --- | --- | --- | --- |
| [SuperDesign IDE Extension (legacy)](https://github.com/superdesigndev/superdesign) · Archived/historical · License caution | IDE interface-design extension preserving the original open code; the current same-name product is now a web app. | 7,648 | 0 | 2026-06-29 | 35.8 | AGPL-3.0 + commercial terms |
| [Penpot MCP Server (archived repository)](https://github.com/penpot/penpot-mcp) · Archived/historical | The contents of this historical standalone repository have been merged into the mcp directory of the main Penpot repository. | 537 | 0 | 2026-03-19 | 23.4 | MPL-2.0 |

## How to choose

- You have a component library and need the team to generate interactive prototypes: start with [GitHub Replica](https://github.com/github/replica); it depends on the GitHub Copilot app. When you want to choose the agent or model yourself, look at [OpenDesign](https://github.com/nexu-io/open-design).
- You have an existing web page or design file to keep editing: for a code workspace, see [Onlook](https://github.com/onlook-dev/onlook); for reading and writing design files with scripted control, see [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil).
- You only want better motion or design quality on existing pages: for motion, see [Emil Kowalski Skills](https://github.com/emilkowalski/skills); for layout and accessibility review, try [Impeccable](https://github.com/pbakaus/impeccable) first, then validate in real browsers, with keyboards and assistive technology.
- You need architecture diagrams with brand styling, or agents editing repeatedly on a canvas: see [Diagram Design](https://github.com/cathrynlavery/diagram-design) and [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw) respectively.
- You only have one sentence and need a deck whose PPTX stays editable: see [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill); check the export dependencies and the upstream attribution before shipping.
- You want to reuse one visual language across several agents: write the color, typography and layout rules first with the [DESIGN.md specification](https://github.com/google-labs-code/design.md); third-party brand samples are for reference only.

For a first trial, pick one page or diagram you can publish, check that the deliverable stays editable, inspect the data paths of fonts and remote models, then compare the alternatives with the same input.

## Data and maintenance

- [Project notes and pinned-version evidence](docs/projects.md)
- [Balanced, stars, activity and recent-commit rankings](docs/rankings.md)
- [Papers and benchmarks](docs/research.md)
- [Search and inclusion decisions](research/README.md)
- [Ranking method](docs/methodology.md)
- [Contributing guide](CONTRIBUTING.md)

## Licenses

Original curation and scripts in this catalogue use the [MIT](LICENSE) license. Linked projects, hosted services, datasets, assets and fonts follow their own terms. Some maintenance scripts reuse the MIT implementation from the [AI video catalogue](https://github.com/ZanePoe/awesome_ai_video_creation).

Verification records and inclusion decisions in this catalogue keep the wording used at verification time (Chinese), so the source and original phrasing of every judgement stay auditable; the `research/` directory and change records are not machine-translated.
