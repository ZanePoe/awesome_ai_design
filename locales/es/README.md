🌐 [English](../../README.md) · [简体中文](../zh/README.md) · **Español** · [हिन्दी](../hi/README.md) · [Français](../fr/README.md)

# Awesome AI Design

Colección de diseño con IA para diseñadores, equipos de producto y coding agents. Reúne design Skills reutilizables, agentes, editores y herramientas puente que funcionan, y artículos y benchmarks que permiten revisar por cuenta propia las conclusiones de la investigación.

«Diseño con IA» significa aquí que un agente participa en la creación, la modificación, la revisión y la entrega de interfaces, prototipos, gráficos vectoriales, diagramas, presentaciones, carteles y otras piezas gráficas o sistemas de diseño. Los modelos puros de texto-a-imagen, los coding agents genéricos y los SaaS sin repositorio verificable no se incluyen como herramientas centrales. Las guías oficiales de integración y los índices de sistemas de diseño se indican aparte; la ya existente [colección de vídeo con IA](https://github.com/ZanePoe/awesome_ai_video_creation) cubre la generación y la edición de vídeo.

## Ir a una categoría

[Agentes de diseño y bancos de trabajo de prototipos](#agentes-de-diseño-y-bancos-de-trabajo-de-prototipos) · [Lienzos editables y diseño vectorial](#lienzos-editables-y-diseño-vectorial) · [Skills de diseño front-end, animación y revisión](#skills-de-diseño-front-end-animación-y-revisión) · [Sistemas de diseño y DESIGN.md](#sistemas-de-diseño-y-designmd) · [De diseño a código y puentes MCP](#de-diseño-a-código-y-puentes-mcp) · [Diagramas y expresión visual](#diagramas-y-expresión-visual) · [Diseño gráfico e imágenes](#diseño-gráfico-e-imágenes) · [Presentaciones y diseño de documentos](#presentaciones-y-diseño-de-documentos) · [Artículos, benchmarks y conjuntos de datos](#artículos-benchmarks-y-conjuntos-de-datos) · [Proyectos históricos y archivados](#proyectos-históricos-y-archivados)

## Catálogo actual

**38 proyectos, de los cuales 4 son proyectos de referencia del usuario y 34 se han añadido en esta ronda.** Verificación funcional: 2026-11-26; instantánea de métricas: `2026-11-27T11:24:24+00:00` (UTC).

Dentro de cada categoría se estratifica primero por estado de mantenimiento y luego se ordena combinando estrellas (40%), commits en la rama por defecto a 90 días (35%) y último commit (25%). La puntuación de mantenimiento no representa la calidad del diseño, la capacidad de los modelos, la accesibilidad ni la madurez de producción.

## Vistazo rápido a los proyectos nucleares activos

Solo se muestran los candidatos principales con licencia abierta verificada y commits en los últimos 90 días; las licencias restringidas, los benchmarks de investigación y las herramientas adyacentes no entran en esta tabla.

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento |
| --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | Aporta a los coding agents vocabulario de diseño y órdenes de refinado, crítica y revisión para iterar sobre interfaces existentes. | 117,779 | 2,234 | 2026-11-26 | 99.6 |
| [OpenDesign](https://github.com/nexu-io/open-design) | Genera prototipos fieles a sistemas de diseño con un coding agent local o con OpenDesign Cloud, y compártelos e itéralos en el banco de trabajo del equipo. | 109,748 | 412 | 2026-11-27 | 98.9 |
| [Penpot](https://github.com/penpot/penpot) | Plataforma de diseño colaborativa autoalojable con design tokens, componentes e interfaz MCP para conectar diseño y código. | 62,809 | 1,628 | 2026-11-27 | 98.4 |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | Genera diagramas de arquitectura, flujo o datos como HTML/SVG autocontenido con estilo de marca. | 74,193 | 368 | 2026-11-26 | 97.1 |
| [OpenPencil (open-pencil)](https://github.com/open-pencil/open-pencil) | Editor de diseño programable con IA, CLI y MCP que puede abrir archivos .fig y .pen. | 10,151 | 1,611 | 2026-11-27 | 92.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent Skill que sugiere estilo, paletas, tipografía y sistemas de diseño para varios stacks de front-end. | 154,842 | 100 | 2026-11-27 | 90.9 |
| [OpenPencil (ZSeven-W)](https://github.com/ZSeven-W/openpencil) | Convierte lenguaje natural en interfaces editables sobre el lienzo, con diseño en paralelo de varios agentes y operaciones MCP. | 7,384 | 879 | 2026-11-25 | 90.3 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | Agente de diseño de escritorio local que convierte prompts en artefactos de diseño previsibles y permite conectar los modelos que elija cada usuario. | 8,265 | 146 | 2026-11-27 | 84.3 |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | Adapta al coding agent las design Skills, el sistema de diseño de marca y los ejemplos de OpenDesign. | 1,206 | 435 | 2026-11-26 | 83.6 |
| [Onlook](https://github.com/onlook-dev/onlook) | Editor visual de código local-first en el que trabajan agentes ya existentes del proyecto, como Claude Code o Codex. | 27,995 | 47 | 2026-11-27 | 82.3 |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) | Skills de interfaz y animación para diseñadores e ingenieros: elección de movimiento, revisión y mejoras de rendimiento. | 60,274 | 19 | 2026-11-15 | 77.0 |
| [StyleSeed](https://github.com/bitjaru/styleseed) | Genera un sistema de diseño inicial para el producto (apariencia, paleta, escala tipográfica, espaciado, radio y movimiento), fija las decisiones en STYLESEED.md y tokens CSS y hace que el coding agent las respete en cada pantalla mediante 74 reglas craft y una puerta de puntuación 0-100. | 1,065 | 100 | 2026-11-27 | 75.1 |

## Índice de categorías

`★Referencia del usuario` indica proyectos aportados directamente por el usuario. Cada repositorio aparece en una sola categoría principal; la ficha detallada de proyectos registra dependencias y limitaciones.

| Categoría | Cantidad | Proyectos mejor posicionados por mantenimiento |
| --- | --- | --- |
| Agentes de diseño y bancos de trabajo de prototipos | 5 | OpenDesign, Open CoDesign, GitHub Replica |
| Lienzos editables y diseño vectorial | 5 | Penpot, OpenPencil (open-pencil), OpenPencil (ZSeven-W) |
| Skills de diseño front-end, animación y revisión | 9 | Impeccable, UI UX Pro Max, Open Design Agent Kit |
| Sistemas de diseño y DESIGN.md | 5 | StyleSeed, Stitch Design Skills, Google DESIGN.md |
| De diseño a código y puentes MCP | 4 | Screenshot to Code, Guía oficial de Figma MCP, Framelink Figma MCP |
| Diagramas y expresión visual | 3 | Diagram Design, Excalidraw MCP Server, Spotkit |
| Diseño gráfico e imágenes | 1 | Vane GPT Image Skills |
| Presentaciones y diseño de documentos | 1 | PPT Agent Skill |
| Artículos, benchmarks y conjuntos de datos | 3 | DesignBench, Design2Code, WebDesignAgent |
| Proyectos históricos y archivados | 2 | SuperDesign IDE (heredado), Penpot MCP (archivado) |

### Agentes de diseño y bancos de trabajo de prototipos

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [OpenDesign](https://github.com/nexu-io/open-design) · ★Referencia del usuario | Genera prototipos fieles a sistemas de diseño con un coding agent local o con OpenDesign Cloud, y compártelos e itéralos en el banco de trabajo del equipo. | 109,748 | 412 | 2026-11-27 | 98.9 | Apache-2.0 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | Agente de diseño de escritorio local que convierte prompts en artefactos de diseño previsibles y permite conectar los modelos que elija cada usuario. | 8,265 | 146 | 2026-11-27 | 84.3 | MIT |
| [GitHub Replica](https://github.com/github/replica) · ★Referencia del usuario | Genera e itera prototipos interactivos con GitHub Copilot a partir de los componentes, patrones y guías de diseño que el equipo ya tiene. | 388 | 137 | 2026-11-27 | 73.4 | MIT |
| [fx0](https://github.com/vercel-labs/fx0) | Agente de diseño ligero basado en libfx que itera en lenguaje natural y exporta páginas HTML de archivo único. | 444 | 134 | 2026-11-18 | 71.3 | Apache-2.0 |
| [LangChain Content Studio](https://github.com/langchain-ai/design-agent) | Agente de diseño de marca para equipos que recibe materiales y requisitos por Slack y entrega mockups estáticos, presentaciones o contenido dinámico. | 777 | 72 | 2026-11-23 | 71.3 | Apache-2.0 |

### Lienzos editables y diseño vectorial

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [Penpot](https://github.com/penpot/penpot) | Plataforma de diseño colaborativa autoalojable con design tokens, componentes e interfaz MCP para conectar diseño y código. | 62,809 | 1,628 | 2026-11-27 | 98.4 | MPL-2.0 |
| [OpenPencil (open-pencil)](https://github.com/open-pencil/open-pencil) | Editor de diseño programable con IA, CLI y MCP que puede abrir archivos .fig y .pen. | 10,151 | 1,611 | 2026-11-27 | 92.0 | MIT |
| [OpenPencil (ZSeven-W)](https://github.com/ZSeven-W/openpencil) | Convierte lenguaje natural en interfaces editables sobre el lienzo, con diseño en paralelo de varios agentes y operaciones MCP. | 7,384 | 879 | 2026-11-25 | 90.3 | MIT |
| [Onlook](https://github.com/onlook-dev/onlook) | Editor visual de código local-first en el que trabajan agentes ya existentes del proyecto, como Claude Code o Codex. | 27,995 | 47 | 2026-11-27 | 82.3 | Apache-2.0 |
| [Velloo](https://github.com/velloo-design/velloo) | Permite que un coding agent explore varias direcciones en un lienzo local usando los componentes de la aplicación existente y luego escriba en la app el diseño elegido. | 10 | 252 | 2026-11-26 | 64.2 | Apache-2.0 |

### Skills de diseño front-end, animación y revisión

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | Aporta a los coding agents vocabulario de diseño y órdenes de refinado, crítica y revisión para iterar sobre interfaces existentes. | 117,779 | 2,234 | 2026-11-26 | 99.6 | Apache-2.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent Skill que sugiere estilo, paletas, tipografía y sistemas de diseño para varios stacks de front-end. | 154,842 | 100 | 2026-11-27 | 90.9 | MIT |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | Adapta al coding agent las design Skills, el sistema de diseño de marca y los ejemplos de OpenDesign. | 1,206 | 435 | 2026-11-26 | 83.6 | MIT |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) · ★Referencia del usuario | Skills de interfaz y animación para diseñadores e ingenieros: elección de movimiento, revisión y mejoras de rendimiento. | 60,274 | 19 | 2026-11-15 | 77.0 | MIT |
| [Logo Design Skill](https://github.com/kaankiziltug/logo-design-skill) · Aviso de licencia | Skill de diseño de logos que va del brief al SVG entregable y a las guías de identidad, con una biblioteca de referencia de más de 1.400 logos reales, reglas de geometría y corrección óptica y comprobaciones en Python sin dependencias. | 7,913 | 32 | 2026-11-13 | 72.3 | MIT (código y skills) + biblioteca de logos de terceros con marca registrada excluida |
| [Make Interfaces Feel Better](https://github.com/jakubkrehel/make-interfaces-feel-better) | Skill de agente para los pequeños detalles que hacen que una interfaz se sienta mejor: animación, tipografía, iconos, estados hover, alineación óptica y radios concéntricos, instalable con un comando de skills CLI. | 4,328 | 3 | 2026-11-18 | 59.4 | MIT |
| [cc-skills](https://github.com/samber/cc-skills) | Colección transversal de skills de agente que se cargan bajo demanda; su skill frontend-design-deslop quita el aspecto genérico de IA a los frontends web. | 306 | 14 | 2026-11-01 | 53.8 | MIT |
| [Better Design](https://github.com/Moddingflow/better-design) | Proceso repetible de diseño de interfaces para agentes de codificación: dirección de arte específica del producto, un DESIGN.md compartido, tipografía y especificaciones de controles medidas, con scripts de validación y una demo navegable. | 94 | 9 | 2026-10-27 | 46.5 | MIT |
| [Frontend AI Skills](https://github.com/JustineBijuPaul/frontend-ai-skills) | Skills modulares de front-end cargables bajo demanda, que cubren animación, interacción, accesibilidad y otros temas. | 12 | 86 | 2026-09-04 | 43.9 | MIT |

### Sistemas de diseño y DESIGN.md

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [StyleSeed](https://github.com/bitjaru/styleseed) | Genera un sistema de diseño inicial para el producto (apariencia, paleta, escala tipográfica, espaciado, radio y movimiento), fija las decisiones en STYLESEED.md y tokens CSS y hace que el coding agent las respete en cada pantalla mediante 74 reglas craft y una puerta de puntuación 0-100. | 1,065 | 100 | 2026-11-27 | 75.1 | MIT |
| [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills) | Conjunto oficial de skills y plugins para Google Stitch que conecta los agentes con su flujo de diseño. | 13,435 | 22 | 2026-11-24 | 75.0 | Apache-2.0 |
| [Google DESIGN.md](https://github.com/google-labs-code/design.md) | Especificación de identidad visual que reúne en un mismo archivo design tokens legibles por máquina y principios de diseño para la lectura de los agentes. | 29,171 | 9 | 2026-11-18 | 71.2 | Apache-2.0 |
| [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) | Recopilación de documentos DESIGN.md de referencia reutilizables que aportan a los agentes estilos de marca, tipografía, color y convenciones de componentes. | 129,317 | 8 | 2026-10-28 | 70.3 | MIT |
| [extract-design-system](https://github.com/arvindrk/extract-design-system) | Hace ingeniería inversa de design tokens (colores, tipografía, espaciado, radio y sombras) de cualquier sitio público y emite un tokens.json compatible con W3C más un archivo de propiedades personalizadas de CSS. | 329 | 0 | 2026-06-19 | 24.3 | MIT |

### De diseño a código y puentes MCP

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [Screenshot to Code](https://github.com/abi/screenshot-to-code) | Convierte capturas de pantalla, prototipos, diseños de Figma o grabaciones de pantalla en código de interfaz con la ayuda de modelos. | 81,464 | 6 | 2026-11-15 | 72.2 | MIT |
| [Guía oficial de Figma MCP](https://github.com/figma/mcp-server-guide) · Aviso de licencia | Guía oficial de integración de Figma que explica cómo obtienen contexto de diseño los agentes y algunos flujos de escritura remota. | 2,241 | 30 | 2026-11-24 | 70.4 | Sin confirmar |
| [Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP) | Aporta a los coding agents el contexto de diseño de los archivos de Figma para ayudar a implementar interfaces ya diseñadas. | 16,328 | 0 | 2026-06-24 | 38.1 | MIT |
| [Talk to Figma MCP](https://github.com/grab/cursor-talk-to-figma-mcp) | Permite a los agentes leer y modificar diseños de Figma mediante un servicio MCP, un plugin de Figma y un puente WebSocket. | 7,134 | 0 | 2026-07-26 | 37.1 | MIT |

### Diagramas y expresión visual

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) · ★Referencia del usuario | Genera diagramas de arquitectura, flujo o datos como HTML/SVG autocontenido con estilo de marca. | 74,193 | 368 | 2026-11-26 | 97.1 | MIT |
| [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw) | Ofrece un lienzo Excalidraw legible y editable que permite modificar y guardar diagramas mediante CLI, Skill o MCP. | 2,693 | 33 | 2026-11-10 | 68.0 | MIT |
| [Spotkit](https://github.com/Devesh-Shirsath/spotkit) | Skill de Claude Code que convierte una descripción de funcionalidad en ilustraciones abstractas de producto en SVG real: primero determina qué hace la función y qué relación expresa, y luego elige 2-5 primitivas de UI y un layout. | 148 | 33 | 2026-10-08 | 51.6 | MIT |

### Diseño gráfico e imágenes

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [Vane GPT Image Skills](https://github.com/VaneAi888/vane-gpt-image-skills) | Colección de skills de GPT Image que incluye un diseñador de carteles cinematográficos con 36 composiciones: elige composición y jerarquía tipográfica según el tono, la historia y el material de la película, y entrega una propuesta, un prompt listo para copiar o una imagen real. | 1,561 | 51 | 2026-11-24 | 71.9 | MIT |

### Presentaciones y diseño de documentos

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) | Skill de Claude Code que reproduce el flujo de un estudio de presentaciones de gama alta: investigación, recopilación de material, esquema, plan de diapositivas, diseño HTML y posprocesado a SVG y PPTX editable, de una frase a un entregable. | 221 | 11 | 2026-11-18 | 55.4 | MIT |

### Artículos, benchmarks y conjuntos de datos

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [DesignBench](https://github.com/WebPAI/DesignBench) · Aviso de licencia | Benchmark de investigación que evalúa generación, edición y reparación de código front-end multi-framework. | 61 | 0 | 2026-07-27 | 20.7 | Sin confirmar |
| [Design2Code](https://github.com/NoviScl/Design2Code) | Benchmark de captura-a-código sobre páginas web reales, con conjunto de datos y herramientas de evaluación automática. | 605 | 0 | 2024-11-02 | 22.3 | MIT |
| [WebDesignAgent](https://github.com/DAMO-NLP-SG/WebDesignAgent) | Prototipo de investigación sobre generación de sitios web que muestra un flujo de diseño impulsado por descripciones, layouts de referencia, imágenes y retroalimentación. | 267 | 0 | 2024-09-20 | 19.4 | Apache-2.0 |

### Proyectos históricos y archivados

| Proyecto | Propósito | Estrellas | Commits 90 d | Último commit UTC | Puntuación de mantenimiento | Licencia |
| --- | --- | --- | --- | --- | --- | --- |
| [SuperDesign IDE (heredado)](https://github.com/superdesigndev/superdesign) · Archivado/histórico · Aviso de licencia | Extensión de diseño de interfaces para IDE que conserva el código abierto original; el producto actual homónimo ya es una aplicación web. | 7,651 | 0 | 2026-06-29 | 35.7 | AGPL-3.0 + condiciones comerciales |
| [Penpot MCP (archivado)](https://github.com/penpot/penpot-mcp) · Archivado/histórico | El contenido del antiguo repositorio independiente se integró en el directorio mcp del repositorio principal de Penpot. | 537 | 0 | 2026-03-19 | 23.4 | MPL-2.0 |

## Cómo elegir

- Si ya tienes una librería de componentes y necesitas que el equipo genere prototipos interactivos: mira primero [GitHub Replica](https://github.com/github/replica); depende de la app de GitHub Copilot. Si prefieres elegir tú el agente o el modelo, mira [OpenDesign](https://github.com/nexu-io/open-design).
- Si ya tienes una página web o un archivo de diseño y necesitas seguir editándolo: para un espacio de trabajo orientado al código, mira [Onlook](https://github.com/onlook-dev/onlook); si necesitas leer y escribir archivos de diseño y controlarlos con scripts, mira [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil).
- Si ya tienes una página y solo quieres mejorar la animación o la calidad del diseño: para el movimiento, mira [Emil Kowalski Skills](https://github.com/emilkowalski/skills); para revisar layout y accesibilidad, puedes probar primero [Impeccable](https://github.com/pbakaus/impeccable) y validar después con navegadores reales, teclado y tecnologías de asistencia.
- Si necesitas diagramas de arquitectura con estilo de marca, o que un agente edite repetidamente sobre un lienzo: mira respectivamente [Diagram Design](https://github.com/cathrynlavery/diagram-design) y [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw).
- Si solo tienes una frase y necesitas un entregable cuyo PPTX siga siendo editable: mira [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill); revisa las dependencias de exportación y la atribución de upstream antes de publicar.
- Si necesitas un cartel, una portada o una imagen para redes, no una interfaz: mira [Vane GPT Image Skills](https://github.com/VaneAi888/vane-gpt-image-skills); la imagen final depende de las herramientas de generación del entorno y no hay que inventar títulos, marcas ni datos de estreno.
- Si quieres reutilizar el mismo lenguaje visual en varios agentes: describe primero color, tipografía y reglas de layout con la [especificación DESIGN.md](https://github.com/google-labs-code/design.md); los ejemplos de marcas de terceros son solo referencia.

Para la primera prueba, conviene elegir una página o un diagrama publicable, comprobar si el entregable sigue siendo editable, revisar las fuentes y el camino de los datos hacia modelos remotos, y comparar después los proyectos candidatos con la misma entrada.

## Datos y mantenimiento

- [Ficha detallada de proyectos y evidencia en versiones fijas](docs/projects.md)
- [Ordenaciones combinada, por estrellas, por actividad y por último commit](docs/rankings.md)
- [Artículos y benchmarks](docs/research.md)
- [Decisiones de búsqueda e inclusión](../../research/README.md)
- [Metodología de ordenación](docs/methodology.md)
- [Guía de contribución](CONTRIBUTING.md)

## Licencias

La compilación original y los scripts de este catálogo están bajo [MIT](../../LICENSE); los proyectos enlazados, los servicios gestionados, los conjuntos de datos, el material y las fuentes siguen sus propias condiciones. Parte de los scripts de mantenimiento reutilizan la implementación MIT de la [colección de vídeo con IA](https://github.com/ZanePoe/awesome_ai_video_creation).

Los registros de verificación y las decisiones de inclusión de este catálogo conservan el texto original tal como se redactó en el momento de cada verificación (en chino), para poder auditar el origen y la formulación de cada juicio; el directorio `research/` y los registros de cambios no se traducen automáticamente.
