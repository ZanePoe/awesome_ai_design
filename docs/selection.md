## How to choose

- You have a component library and need the team to generate interactive prototypes: start with [GitHub Replica](https://github.com/github/replica); it depends on the GitHub Copilot app. When you want to choose the agent or model yourself, look at [OpenDesign](https://github.com/nexu-io/open-design).
- You have an existing web page or design file to keep editing: for a code workspace, see [Onlook](https://github.com/onlook-dev/onlook); for reading and writing design files with scripted control, see [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil).
- You only want better motion or design quality on existing pages: for motion, see [Emil Kowalski Skills](https://github.com/emilkowalski/skills); for layout and accessibility review, try [Impeccable](https://github.com/pbakaus/impeccable) first, then validate in real browsers, with keyboards and assistive technology.
- You need architecture diagrams with brand styling, or agents editing repeatedly on a canvas: see [Diagram Design](https://github.com/cathrynlavery/diagram-design) and [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw) respectively.
- You only have one sentence and need a deck whose PPTX stays editable: see [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill); check the export dependencies and the upstream attribution before shipping.
- You need a poster, cover or social-image deliverable rather than an interface: see [Vane GPT Image Skills](https://github.com/VaneAi888/vane-gpt-image-skills); the actual image depends on the host's image-generation tools, and titles, trademarks and release facts must not be invented.
- You want to reuse one visual language across several agents: write the color, typography and layout rules first with the [DESIGN.md specification](https://github.com/google-labs-code/design.md); third-party brand samples are for reference only.

For a first trial, pick one page or diagram you can publish, check that the deliverable stays editable, inspect the data paths of fonts and remote models, then compare the alternatives with the same input.
