# Project notes and evidence

Each positioning statement comes from the official README at a pinned commit; not every project was installed and run. Metrics refreshes do not automatically re-audit features or licenses.


## [OpenDesign](https://github.com/nexu-io/open-design)

Generate design-system-compliant prototypes with a local coding agent or OpenDesign Cloud, then share and iterate on a team workbench.

- Category: Design agents and prototyping workbenches; Core candidate.
- Scope boundary: Treat the local workflow, the managed Cloud and the Go plan separately; terms for models, templates and brand assets are counted separately.
- Maintenance: Commits within the last 90 days; 84 commits in 30 days, 436 commits in 90 days.
- License: [Apache-2.0](https://github.com/nexu-io/open-design/blob/23812a9d081945704e5e1cdd63b41f653c208d9a/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/nexu-io/open-design/blob/23812a9d081945704e5e1cdd63b41f653c208d9a/README.md#L30) · [Source 2](https://github.com/nexu-io/open-design/blob/23812a9d081945704e5e1cdd63b41f653c208d9a/README.md#L105).

## [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign)

Local desktop design agent that turns prompts into previewable design artifacts and lets you connect models of your choice.

- Category: Design agents and prototyping workbenches; Core candidate.
- Scope boundary: A local workspace does not mean inference runs fully offline; concrete output formats and capabilities vary by model and release.
- Maintenance: Commits within the last 90 days; 17 commits in 30 days, 141 commits in 90 days.
- License: [MIT](https://github.com/OpenCoworkAI/open-codesign/blob/1779bb5b0f15c734ff8ba06e2eb2463b5578e5b6/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/OpenCoworkAI/open-codesign/blob/1779bb5b0f15c734ff8ba06e2eb2463b5578e5b6/README.md#L7).

## [GitHub Replica](https://github.com/github/replica)

Generate and iterate interactive prototypes with GitHub Copilot using the team's existing components, patterns and design guidance.

- Category: Design agents and prototyping workbenches; Core candidate.
- Scope boundary: The local flow depends on the GitHub Copilot app, Git and Node.js, officially listed for macOS/Linux; the optional Replica Hub is team-hosted.
- Maintenance: Commits within the last 90 days; 69 commits in 30 days, 121 commits in 90 days.
- License: [MIT](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/LICENSE); Open license verified. MIT covers the project's own code; the root NOTICE.md lists SIL OFL 1.1 licenses for fonts such as Mona Sans.
- Feature verified: 2026-11-18; [Source 1](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/README.md#L7) · [Source 2](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/README.md#L53) · [Source 3](https://github.com/github/replica/blob/f468721924f63d885343acf61076dacb3c3dafc0/NOTICE.md#L3).

## [fx0](https://github.com/vercel-labs/fx0)

Lightweight design agent built on libfx that iterates through natural language and exports single-file HTML pages.

- Category: Design agents and prototyping workbenches; Core candidate.
- Scope boundary: The official deployment path involves Vercel and AI Gateway; a single-file artifact is not a full product codebase.
- Maintenance: Commits within the last 90 days; 67 commits in 30 days, 134 commits in 90 days.
- License: [Apache-2.0](https://github.com/vercel-labs/fx0/blob/ebc177ea055c863f6da50bfe4241fc8381a6b0c8/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/vercel-labs/fx0/blob/ebc177ea055c863f6da50bfe4241fc8381a6b0c8/README.md#L3).

## [LangChain Content Studio](https://github.com/langchain-ai/design-agent)

Brand design agent for teams that receives assets and requests from Slack and delivers wireframes, presentations or dynamic content.

- Category: Design agents and prototyping workbenches; Core candidate.
- Scope boundary: The official Slack deployment path depends on Managed Deep Agents; open-source code does not mean the hosted service is free.
- Maintenance: Commits within the last 90 days; 40 commits in 30 days, 72 commits in 90 days.
- License: [Apache-2.0](https://github.com/langchain-ai/design-agent/blob/8134d7ccdc3f91a0192d45499dc368e9f89d7910/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/langchain-ai/design-agent/blob/8134d7ccdc3f91a0192d45499dc368e9f89d7910/README.md#L26).

## [Penpot](https://github.com/penpot/penpot)

Self-hostable collaborative design platform with design tokens, components and an MCP interface bridging design and code.

- Category: Editable canvas and vector design; Core candidate.
- Scope boundary: The editor works standalone; the MCP is an integration capability, not a built-in generation model.
- Maintenance: Commits within the last 90 days; 676 commits in 30 days, 1615 commits in 90 days.
- License: [MPL-2.0](https://github.com/penpot/penpot/blob/14abaf93f4ec220970b07e85e915446e7a11150d/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/penpot/penpot/blob/14abaf93f4ec220970b07e85e915446e7a11150d/README.md#L47).

## [OpenPencil (open-source design editor)](https://github.com/open-pencil/open-pencil)

Programmable design editor with AI, CLI and MCP that opens .fig and .pen files.

- Category: Editable canvas and vector design; Core candidate.
- Scope boundary: Still under active development; node, font and file round-trip fidelity must be verified against real files; it is not the same repository as the similarly named ZSeven-W project.
- Maintenance: Commits within the last 90 days; 675 commits in 30 days, 1560 commits in 90 days.
- License: [MIT](https://github.com/open-pencil/open-pencil/blob/82e3d6ad5e94a6017c1b55f4fc61c58803063644/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/open-pencil/open-pencil/blob/82e3d6ad5e94a6017c1b55f4fc61c58803063644/README.md#L9).

## [OpenPencil (AI-native vector design tool)](https://github.com/ZSeven-W/openpencil)

Turns natural language into editable interfaces on the canvas, with parallel multi-agent design and MCP operations.

- Category: Editable canvas and vector design; Core candidate.
- Scope boundary: Model integration and framework export need to be verified item by item; it is a separate repository and is not merged with open-pencil for metrics.
- Maintenance: Commits within the last 90 days; 245 commits in 30 days, 941 commits in 90 days.
- License: [MIT](https://github.com/ZSeven-W/openpencil/blob/2bbc658caba5139cdfeb768b65da7f6f0080a703/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/ZSeven-W/openpencil/blob/2bbc658caba5139cdfeb768b65da7f6f0080a703/README.md#L44).

## [Onlook](https://github.com/onlook-dev/onlook)

Local-first visual code editor in which existing agents such as Claude Code or Codex work inside your project.

- Category: Editable canvas and vector design; Core candidate.
- Scope boundary: Does not ship its own model; the code license does not cover some branding, fonts and third-party assets in the repository.
- Maintenance: Commits within the last 90 days; 22 commits in 30 days, 22 commits in 90 days.
- License: [Apache-2.0](https://github.com/onlook-dev/onlook/blob/7b17f48c59adb7ac4ec30a6982e4971f22846c2b/LICENSE); Open license verified. Apache-2.0 covers the source code, but the README and NOTICE state that some fonts, logos and images are not included in the code grant.
- Feature verified: 2026-11-18; [Source 1](https://github.com/onlook-dev/onlook/blob/7b17f48c59adb7ac4ec30a6982e4971f22846c2b/README.md#L45) · [Source 2](https://github.com/onlook-dev/onlook/blob/7b17f48c59adb7ac4ec30a6982e4971f22846c2b/README.md#L148).

## [Velloo](https://github.com/velloo-design/velloo)

Lets coding agents explore multiple directions on a local canvas using existing app components, then write the chosen design back into the app.

- Category: Editable canvas and vector design; Core candidate.
- Scope boundary: Aimed mainly at design iteration for existing apps; cross-framework support and actual write-back results are untested.
- Maintenance: Commits within the last 90 days; 39 commits in 30 days, 280 commits in 90 days.
- License: [Apache-2.0](https://github.com/velloo-design/velloo/blob/8c1f140049bcc1db4e1d6d5c578eddcd2ef74e4a/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/velloo-design/velloo/blob/8c1f140049bcc1db4e1d6d5c578eddcd2ef74e4a/README.md#L12).

## [Impeccable](https://github.com/pbakaus/impeccable)

Design vocabulary, polish, critique and review commands for coding agents iterating on existing interfaces.

- Category: Front-end design, motion and review Skills; Core candidate.
- Scope boundary: Skill guidance and checks are not a human design review or an accessibility certification.
- Maintenance: Commits within the last 90 days; 1172 commits in 30 days, 2154 commits in 90 days.
- License: [Apache-2.0](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/README.md#L3).

## [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

Agent Skill offering style, color, typography and design-system guidance across multiple front-end stacks.

- Category: Front-end design, motion and review Skills; Core candidate.
- Scope boundary: Rules and generated results are a design starting point; accessibility and the final implementation still need testing.
- Maintenance: Commits within the last 90 days; 33 commits in 30 days, 90 commits in 90 days.
- License: [MIT](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7436a6e0b6dc3add7c12d5b6ef1ccd3d410dd7fd/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/7436a6e0b6dc3add7c12d5b6ef1ccd3d410dd7fd/README.md#L30).

## [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit)

Ports OpenDesign's design Skills, brand design system and examples for use inside coding agents.

- Category: Front-end design, motion and review Skills; Core candidate.
- Scope boundary: Not the OpenDesign desktop app; examples, brand resources and generated results must be checked under their own use conditions.
- Maintenance: Commits within the last 90 days; 220 commits in 30 days, 422 commits in 90 days.
- License: [MIT](https://github.com/feimacode/open-design-agent-kit/blob/1b3832c3452720f028a96b1bdab805ecc1aa3213/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/feimacode/open-design-agent-kit/blob/1b3832c3452720f028a96b1bdab805ecc1aa3213/README.md#L7).

## [Emil Kowalski Skills](https://github.com/emilkowalski/skills)

UI and motion Skills for designers and engineers, covering motion choices, review and performance improvements.

- Category: Front-end design, motion and review Skills; Core candidate.
- Scope boundary: Rules come from the author's design-engineering practice; apply them together with user testing, reduced-motion preferences and real-device behavior.
- Maintenance: Commits within the last 90 days; 12 commits in 30 days, 19 commits in 90 days.
- License: [MIT](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/README.md#L11) · [Source 2](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/README.md#L45).

## [Frontend AI Skills](https://github.com/JustineBijuPaul/frontend-ai-skills)

Modular front-end Skills loaded on demand, covering motion, interaction, accessibility and related topics.

- Category: Front-end design, motion and review Skills; Core candidate.
- Scope boundary: Also includes general front-end engineering knowledge; focus on the design and interaction modules.
- Maintenance: Commits within the last 90 days; 0 commits in 30 days, 86 commits in 90 days.
- License: [MIT](https://github.com/JustineBijuPaul/frontend-ai-skills/blob/f52d23c5b8f51caefccb97ea2bc88f6db7bc6120/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/JustineBijuPaul/frontend-ai-skills/blob/f52d23c5b8f51caefccb97ea2bc88f6db7bc6120/README.md#L5).

## [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills)

Official skills and plugins collection for Google Stitch, connecting agents to its design workflow.

- Category: Design systems and DESIGN.md; Adjacent infrastructure.
- Scope boundary: The skills and plugins are open source; Stitch service capabilities, accounts and usage follow the service terms.
- Maintenance: Commits within the last 90 days; 18 commits in 30 days, 18 commits in 90 days.
- License: [Apache-2.0](https://github.com/google-labs-code/stitch-skills/blob/4cf4db8e4143b09e40f9bc887429d81f41ab3947/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/google-labs-code/stitch-skills/blob/4cf4db8e4143b09e40f9bc887429d81f41ab3947/README.md#L3).

## [Google DESIGN.md](https://github.com/google-labs-code/design.md)

Visual-identity specification that puts machine-readable design tokens and agent-readable design principles in one file.

- Category: Design systems and DESIGN.md; Core candidate.
- Scope boundary: It is a portable specification and tooling, not a design agent; host support for the specification may differ.
- Maintenance: Commits within the last 90 days; 8 commits in 30 days, 9 commits in 90 days.
- License: [Apache-2.0](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/google-labs-code/design.md/blob/db977b3c1d1f309269f43d5d17ae828d54bd6ae3/README.md#L3).

## [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md)

Collection of reusable DESIGN.md reference documents giving agents brand style, typography, color and component conventions.

- Category: Design systems and DESIGN.md; Adjacent infrastructure.
- Scope boundary: This is a reference collection, not a generator; third-party rights such as brand identities and fonts are not covered by the repository's MIT license.
- Maintenance: Commits within the last 90 days; 3 commits in 30 days, 8 commits in 90 days.
- License: [MIT](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/VoltAgent/awesome-design-md/blob/fcc70284932276d085f01ef9f83edde90b1258cb/README.md#L30).

## [Screenshot to Code](https://github.com/abi/screenshot-to-code)

Uses models to turn screenshots, prototypes, Figma designs or screen recordings into interface code.

- Category: Design-to-code and MCP bridges; Core candidate.
- Scope boundary: Model cost, data flow and export stack depend on configuration; visual approximation is not maintainable or accessible code.
- Maintenance: Commits within the last 90 days; 4 commits in 30 days, 6 commits in 90 days.
- License: [MIT](https://github.com/abi/screenshot-to-code/blob/f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/abi/screenshot-to-code/blob/f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30/README.md#L3).

## [Figma MCP Server Guide](https://github.com/figma/mcp-server-guide)

Official Figma integration guide describing how agents obtain design context and some remote write workflows.

- Category: Design-to-code and MCP bridges; Adjacent infrastructure.
- Scope boundary: The repository is documentation, not a self-hostable service; read, write, seat and rate-limit rules differ.
- Maintenance: Commits within the last 90 days; 8 commits in 30 days, 29 commits in 90 days.
- License: [Unverified](https://github.com/figma/mcp-server-guide/blob/490a73c7537123cb1f0bcaced658585f0ee32fd9/README.md); License unverified. No license confirmed in the repository root; included as a public reference, not as granted reuse permission.
- Feature verified: 2026-11-18; [Source 1](https://github.com/figma/mcp-server-guide/blob/490a73c7537123cb1f0bcaced658585f0ee32fd9/README.md#L3).

## [Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP)

Provides coding agents with design context from Figma files to help implement existing interfaces.

- Category: Design-to-code and MCP bridges; Core candidate.
- Scope boundary: Requires authorized Figma access; it is a context bridge, not a standalone canvas or an official hosted MCP.
- Maintenance: No commits for 91–365 days; 0 commits in 30 days, 0 commits in 90 days.
- License: [MIT](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md#L28).

## [Talk to Figma MCP](https://github.com/grab/cursor-talk-to-figma-mcp)

Lets agents read and modify Figma designs through an MCP server, a Figma plugin and a WebSocket bridge.

- Category: Design-to-code and MCP bridges; Core candidate.
- Scope boundary: Check the plugin, file write permissions and connection scope; the old address sonnylazuardi/cursor-talk-to-figma-mcp redirects to this repository.
- Maintenance: No commits for 91–365 days; 0 commits in 30 days, 0 commits in 90 days.
- License: [MIT](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/grab/cursor-talk-to-figma-mcp/blob/ddd90f3a6d454ea0b2fc29f1b084f50fd062b880/README.md#L3).

## [Diagram Design](https://github.com/cathrynlavery/diagram-design)

Outputs architecture, flow and data diagrams as self-contained HTML/SVG with brand styling.

- Category: Diagrams and visual expression; Core candidate.
- Scope boundary: It is an Agent Skill; copyright of imported files, third-party dependencies and accessibility need separate checks.
- Maintenance: Commits within the last 90 days; 108 commits in 30 days, 355 commits in 90 days.
- License: [MIT](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/LICENSE); Open license verified. Its own code is MIT; bundled dependencies are listed in THIRD_PARTY_LICENSES.md.
- Feature verified: 2026-11-18; [Source 1](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/README.md#L10) · [Source 2](https://github.com/cathrynlavery/diagram-design/blob/f6db0decea96de66b901331a0f79a8d4b147ebae/README.md#L51).

## [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw)

Provides a readable, writable Excalidraw canvas that modifies and saves diagrams via CLI, Skill or MCP.

- Category: Diagrams and visual expression; Core candidate.
- Scope boundary: Requires a matching canvas or service environment; multiplayer collaboration and export fidelity need deployment testing.
- Maintenance: Commits within the last 90 days; 7 commits in 30 days, 33 commits in 90 days.
- License: [MIT](https://github.com/yctimlin/mcp_excalidraw/blob/81720ac819d2325177cd6137c6ad41d52d0f5374/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/yctimlin/mcp_excalidraw/blob/81720ac819d2325177cd6137c6ad41d52d0f5374/README.md#L8).

## [DesignBench](https://github.com/WebPAI/DesignBench)

Research benchmark evaluating multi-framework front-end code generation, editing and repair.

- Category: Papers, benchmarks and datasets; Research/benchmark.
- Scope boundary: No license confirmed in the repository root yet; the paper, code and data each have separate terms of use.
- Maintenance: No commits for 91–365 days; 0 commits in 30 days, 0 commits in 90 days.
- License: [Unverified](https://github.com/WebPAI/DesignBench/blob/a1e58d66ecbf1f77848bc5529ee7bbbe33bc25ba/README.md); License unverified. No license confirmed in the repository root; included as a public reference, not as granted reuse permission.
- Feature verified: 2026-11-18; [Source 1](https://github.com/WebPAI/DesignBench/blob/a1e58d66ecbf1f77848bc5529ee7bbbe33bc25ba/README.md#L8).

## [Design2Code](https://github.com/NoviScl/Design2Code)

Screenshot-to-code research on real web pages, with datasets and automatic evaluation tooling.

- Category: Papers, benchmarks and datasets; Research/benchmark.
- Scope boundary: The code license does not replace dataset and model weight terms; its results are not mixed with the catalogue's maintenance score.
- Maintenance: No commits for over 365 days; 0 commits in 30 days, 0 commits in 90 days.
- License: [MIT](https://github.com/NoviScl/Design2Code/blob/7a575e4c33f417c4be5c64072b8f5798de0d0f99/CODE_LICENSE); Open license verified. MIT covers the code; the dataset follows the repository's DATA_LICENSE, and model weights need checking on the publication page.
- Feature verified: 2026-11-18; [Source 1](https://github.com/NoviScl/Design2Code/blob/7a575e4c33f417c4be5c64072b8f5798de0d0f99/README.md#L13).

## [WebDesignAgent](https://github.com/DAMO-NLP-SG/WebDesignAgent)

Website-generation research prototype showing a design flow driven by descriptions, reference layouts, images and feedback.

- Category: Papers, benchmarks and datasets; Research/benchmark.
- Scope boundary: Academic prototype and examples; not assumed to serve directly as a production design workbench.
- Maintenance: No commits for over 365 days; 0 commits in 30 days, 0 commits in 90 days.
- License: [Apache-2.0](https://github.com/DAMO-NLP-SG/WebDesignAgent/blob/03707c4654c1627b4f8ec254147d31495955f44e/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/DAMO-NLP-SG/WebDesignAgent/blob/03707c4654c1627b4f8ec254147d31495955f44e/README.md#L6).

## [SuperDesign IDE Extension (legacy)](https://github.com/superdesigndev/superdesign)

IDE interface-design extension preserving the original open code; the current same-name product is now a web app.

- Category: Historical and archived projects; Historical reference.
- Scope boundary: The old extension is no longer actively maintained; the current web product is not the self-hosted version of this repository.
- Maintenance: Archived / historical; 0 commits in 30 days, 0 commits in 90 days.
- License: [AGPL-3.0 + commercial terms](https://github.com/superdesigndev/superdesign/blob/49e2b9dd9615c6dae936b326b1ddb85d4f1d6f19/LICENSE); Composite/conditional license. Most files are under AGPLv3; files marked Enterprise fall under a separate commercial license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/superdesigndev/superdesign/blob/49e2b9dd9615c6dae936b326b1ddb85d4f1d6f19/README.md#L4).

## [Penpot MCP Server (archived repository)](https://github.com/penpot/penpot-mcp)

The contents of this historical standalone repository have been merged into the mcp directory of the main Penpot repository.

- Category: Historical and archived projects; Historical reference.
- Scope boundary: New users should enter through the Penpot main repository; the old repository is kept only for migration traceability.
- Maintenance: Archived / historical; 0 commits in 30 days, 0 commits in 90 days.
- License: [MPL-2.0](https://github.com/penpot/penpot-mcp/blob/73e0cd21853dd03103f7ac675042b1277ee0b736/LICENSE); Open license verified. Repository license file verified; third-party assets, fonts, data and hosted services are not automatically covered by the code license.
- Feature verified: 2026-11-18; [Source 1](https://github.com/penpot/penpot-mcp/blob/73e0cd21853dd03103f7ac675042b1277ee0b736/README.md#L2).
