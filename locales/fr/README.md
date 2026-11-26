🌐 [English](../../README.md) · [简体中文](../zh/README.md) · [Español](../es/README.md) · [हिन्दी](../hi/README.md) · **Français**

# Awesome AI Design

Collection de design par IA pour les designers, les équipes produit et les coding agents. Elle recense des Skills de design réutilisables, des agents, éditeurs et outils de pontage conçus pour l'IA, ainsi que les articles et benchmarks permettant de vérifier les conclusions de recherche.

Le « design par IA » désigne ici la participation d'agents à la création, la modification, la revue et le transfert d'interfaces, de prototypes, de graphiques vectoriels, de diagrammes, de présentations ou de systèmes de design. Les modèles purement texte-image, les coding agents généralistes et les SaaS sans dépôt vérifiable ne sont pas retenus comme outils principaux. Les guides d'intégration officiels et les index de systèmes de design sont signalés séparément ; le [catalogue vidéo IA](https://github.com/ZanePoe/awesome_ai_video_creation) existant couvre la génération et le montage vidéo.

## Aller à une catégorie

[Agents de design et ateliers de prototypage](#agents-de-design-et-ateliers-de-prototypage) · [Canvas éditables et conception vectorielle](#canvas-éditables-et-conception-vectorielle) · [Skills de design front-end, motion et revue](#skills-de-design-front-end-motion-et-revue) · [Systèmes de design et DESIGN.md](#systèmes-de-design-et-designmd) · [Design-vers-code et ponts MCP](#design-vers-code-et-ponts-mcp) · [Diagrammes et expression visuelle](#diagrammes-et-expression-visuelle) · [Présentations et conception de documents](#présentations-et-conception-de-documents) · [Articles, benchmarks et jeux de données](#articles-benchmarks-et-jeux-de-données) · [Projets historiques et archivés](#projets-historiques-et-archivés)

## Sélection actuelle

**36 projets, dont 4 référencés par l'utilisateur et 32 ajoutés lors de cette passe.** Vérification fonctionnelle : 2026-11-26 ; instantané des métriques : `2026-11-26T04:03:50+00:00` (UTC).

Dans chaque catégorie, les projets sont d'abord stratifiés par état de maintenance, puis classés par une combinaison d'étoiles (40 %), de commits sur la branche par défaut à 90 jours (35 %) et de récence du dernier commit (25 %). Le score de maintenance ne représente ni la qualité des designs, ni la capacité des modèles, ni l'accessibilité, ni la maturité de production.

## Aperçu des projets principaux actifs

N'affiche que les candidats principaux, à licence ouverte vérifiée, avec un commit sur les 90 derniers jours ; les licences restreintes, les benchmarks de recherche et les outils adjacents n'entrent pas dans ce tableau.

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance |
| --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | Commandes de vocabulaire de design, de polissage, de critique et de revue pour coding agents, afin d'itérer des interfaces existantes. | 116,989 | 2,259 | 2026-11-26 | 100.0 |
| [Penpot](https://github.com/penpot/penpot) | Plateforme de design collaborative auto-hébergeable offrant jetons de design, composants et interface MCP pour relier design et code. | 62,748 | 1,619 | 2026-11-25 | 98.3 |
| [OpenDesign](https://github.com/nexu-io/open-design) | Génère des prototypes respectant le design system via un coding agent local ou OpenDesign Cloud, puis les partage et les fait itérer dans l'espace de travail d'équipe. | 109,524 | 415 | 2026-11-23 | 98.2 |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | Produit des diagrammes d'architecture, de flux ou de données en HTML/SVG autonomes au style de la marque. | 73,182 | 364 | 2026-11-25 | 96.9 |
| [OpenPencil (open-pencil)](https://github.com/open-pencil/open-pencil) | Éditeur de design programmable avec IA, CLI et MCP, capable d'ouvrir les fichiers .fig et .pen. | 10,117 | 1,580 | 2026-11-25 | 91.9 |
| [OpenPencil (ZSeven-W)](https://github.com/ZSeven-W/openpencil) | Convertit le langage naturel en interfaces éditables sur le canvas, avec conception parallèle par plusieurs agents et opérations MCP. | 7,367 | 914 | 2026-11-25 | 90.7 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent Skill proposant style, palette, typographie et conseils de design system pour plusieurs stacks front-end. | 154,266 | 94 | 2026-11-25 | 90.6 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | Agent de design de bureau local qui transforme les prompts en livrables de design prévisualisables, avec la possibilité de connecter un modèle au choix. | 8,258 | 145 | 2026-11-25 | 84.2 |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | Porte les Skills de design d'OpenDesign, ses design systems de marque et ses exemples pour un usage dans les coding agents. | 1,197 | 429 | 2026-11-25 | 83.7 |
| [Onlook](https://github.com/onlook-dev/onlook) | Éditeur visuel local-first pour le code, où des agents existants comme Claude Code ou Codex travaillent directement dans le projet. | 27,952 | 40 | 2026-11-26 | 81.5 |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) | Skills d'UI et de motion pour designers et ingénieurs : choix du motion, revue et amélioration des performances. | 59,678 | 19 | 2026-11-15 | 77.3 |
| [GitHub Replica](https://github.com/github/replica) | Génère et fait itérer des prototypes interactifs via GitHub Copilot en réutilisant les composants, motifs et directives de design déjà présents dans l'équipe. | 382 | 126 | 2026-11-25 | 72.8 |

## Index par catégorie

`★référence utilisateur` signale un projet fourni directement par l'utilisateur. Chaque dépôt n'apparaît que dans une catégorie principale ; les fiches projets documentent les dépendances et les limites.

| Catégorie | Nombre | Projets les mieux classés en maintenance |
| --- | --- | --- |
| Agents de design et ateliers de prototypage | 5 | OpenDesign, Open CoDesign, GitHub Replica |
| Canvas éditables et conception vectorielle | 5 | Penpot, OpenPencil (open-pencil), OpenPencil (ZSeven-W) |
| Skills de design front-end, motion et revue | 9 | Impeccable, UI UX Pro Max, Open Design Agent Kit |
| Systèmes de design et DESIGN.md | 4 | Stitch Design Skills, Google DESIGN.md, Awesome DESIGN.md |
| Design-vers-code et ponts MCP | 4 | Screenshot to Code, Guide officiel MCP Figma, Framelink Figma MCP |
| Diagrammes et expression visuelle | 3 | Diagram Design, Excalidraw MCP Server, Spotkit |
| Présentations et conception de documents | 1 | PPT Agent Skill |
| Articles, benchmarks et jeux de données | 3 | DesignBench, Design2Code, WebDesignAgent |
| Projets historiques et archivés | 2 | SuperDesign IDE (hérité), Penpot MCP (archivé) |

### Agents de design et ateliers de prototypage

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [OpenDesign](https://github.com/nexu-io/open-design) · ★référence utilisateur | Génère des prototypes respectant le design system via un coding agent local ou OpenDesign Cloud, puis les partage et les fait itérer dans l'espace de travail d'équipe. | 109,524 | 415 | 2026-11-23 | 98.2 | Apache-2.0 |
| [Open CoDesign](https://github.com/OpenCoworkAI/open-codesign) | Agent de design de bureau local qui transforme les prompts en livrables de design prévisualisables, avec la possibilité de connecter un modèle au choix. | 8,258 | 145 | 2026-11-25 | 84.2 | MIT |
| [GitHub Replica](https://github.com/github/replica) · ★référence utilisateur | Génère et fait itérer des prototypes interactifs via GitHub Copilot en réutilisant les composants, motifs et directives de design déjà présents dans l'équipe. | 382 | 126 | 2026-11-25 | 72.8 | MIT |
| [fx0](https://github.com/vercel-labs/fx0) | Agent de design léger basé sur libfx qui itère en langage naturel et exporte des pages HTML mono-fichier. | 442 | 134 | 2026-11-18 | 71.7 | Apache-2.0 |
| [LangChain Content Studio](https://github.com/langchain-ai/design-agent) | Agent de design de marque pour les équipes : reçoit ressources et exigences depuis Slack et livre des maquettes, des présentations ou du contenu animé. | 767 | 72 | 2026-11-23 | 71.6 | Apache-2.0 |

### Canvas éditables et conception vectorielle

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [Penpot](https://github.com/penpot/penpot) | Plateforme de design collaborative auto-hébergeable offrant jetons de design, composants et interface MCP pour relier design et code. | 62,748 | 1,619 | 2026-11-25 | 98.3 | MPL-2.0 |
| [OpenPencil (open-pencil)](https://github.com/open-pencil/open-pencil) | Éditeur de design programmable avec IA, CLI et MCP, capable d'ouvrir les fichiers .fig et .pen. | 10,117 | 1,580 | 2026-11-25 | 91.9 | MIT |
| [OpenPencil (ZSeven-W)](https://github.com/ZSeven-W/openpencil) | Convertit le langage naturel en interfaces éditables sur le canvas, avec conception parallèle par plusieurs agents et opérations MCP. | 7,367 | 914 | 2026-11-25 | 90.7 | MIT |
| [Onlook](https://github.com/onlook-dev/onlook) | Éditeur visuel local-first pour le code, où des agents existants comme Claude Code ou Codex travaillent directement dans le projet. | 27,952 | 40 | 2026-11-26 | 81.5 | Apache-2.0 |
| [Velloo](https://github.com/velloo-design/velloo) | Permet aux coding agents d'explorer plusieurs directions sur un canvas local en réutilisant les composants de l'application existante, puis de réinjecter le design retenu dans l'application. | 10 | 261 | 2026-11-17 | 62.4 | Apache-2.0 |

### Skills de design front-end, motion et revue

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) | Commandes de vocabulaire de design, de polissage, de critique et de revue pour coding agents, afin d'itérer des interfaces existantes. | 116,989 | 2,259 | 2026-11-26 | 100.0 | Apache-2.0 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent Skill proposant style, palette, typographie et conseils de design system pour plusieurs stacks front-end. | 154,266 | 94 | 2026-11-25 | 90.6 | MIT |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | Porte les Skills de design d'OpenDesign, ses design systems de marque et ses exemples pour un usage dans les coding agents. | 1,197 | 429 | 2026-11-25 | 83.7 | MIT |
| [Emil Kowalski Skills](https://github.com/emilkowalski/skills) · ★référence utilisateur | Skills d'UI et de motion pour designers et ingénieurs : choix du motion, revue et amélioration des performances. | 59,678 | 19 | 2026-11-15 | 77.3 | MIT |
| [Logo Design Skill](https://github.com/kaankiziltug/logo-design-skill) · Attention licence | Skill de design de logo allant du brief au SVG livrable et aux guidelines de marque, avec une bibliothèque de référence de plus de 1 400 logos réels, des règles de géométrie et de correction optique et des outils Python sans dépendances. | 7,782 | 32 | 2026-11-13 | 72.6 | MIT (code et skills) + bibliothèque de logos tiers sous marque déposée exclue |
| [Make Interfaces Feel Better](https://github.com/jakubkrehel/make-interfaces-feel-better) | Skill d'agent pour les menus détails qui rendent une interface meilleure : animation, typographie, icônes, états de survol, alignement optique et rayons concentriques, installable d'une commande skills CLI. | 4,294 | 3 | 2026-11-18 | 59.7 | MIT |
| [cc-skills](https://github.com/samber/cc-skills) | Collection transverse de skills d'agent chargées à la demande ; sa skill frontend-design-deslop retire le rendu générique « fait par IA » des interfaces web. | 283 | 16 | 2026-11-01 | 54.5 | MIT |
| [Better Design](https://github.com/Moddingflow/better-design) | Un processus répétable de conception d'interface pour agents de codage : direction artistique propre au produit, DESIGN.md partagé, typographie et spécifications de contrôles mesurées, avec scripts de validation et une démo cliquable. | 79 | 9 | 2026-10-27 | 46.2 | MIT |
| [Frontend AI Skills](https://github.com/JustineBijuPaul/frontend-ai-skills) | Skills front-end modulaires chargés à la demande, couvrant entre autres le motion, les interactions et l'accessibilité. | 11 | 86 | 2026-09-04 | 43.8 | MIT |

### Systèmes de design et DESIGN.md

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills) | Ensemble officiel de skills et de plugins pour Google Stitch, reliant les agents à son flux de design. | 13,026 | 22 | 2026-11-24 | 75.2 | Apache-2.0 |
| [Google DESIGN.md](https://github.com/google-labs-code/design.md) | Spécification d'identité visuelle réunissant dans un même fichier les jetons de design lisibles par machine et les principes de design lisibles par les agents. | 29,129 | 9 | 2026-11-18 | 71.5 | Apache-2.0 |
| [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) | Rassemble des références DESIGN.md réutilisables pour donner aux agents le style de marque, la typographie, les couleurs et les conventions de composants. | 129,098 | 8 | 2026-10-28 | 70.6 | MIT |
| [extract-design-system](https://github.com/arvindrk/extract-design-system) | Reconstitue les design tokens (couleurs, typographie, espacement, rayon, ombres) de n'importe quel site public et produit un tokens.json compatible W3C plus un fichier de propriétés personnalisées CSS. | 316 | 0 | 2026-06-19 | 24.3 | MIT |

### Design-vers-code et ponts MCP

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [Screenshot to Code](https://github.com/abi/screenshot-to-code) | Convertit captures d'écran, maquettes, designs Figma ou enregistrements d'écran en code d'interface à l'aide de modèles. | 81,446 | 6 | 2026-11-15 | 72.5 | MIT |
| [Guide officiel MCP Figma](https://github.com/figma/mcp-server-guide) · Attention licence | Guide d'intégration officiel de Figma expliquant comment les agents obtiennent le contexte de design et quelques flux d'écriture à distance. | 2,235 | 30 | 2026-11-24 | 70.7 | Non confirmée |
| [Framelink Figma MCP](https://github.com/GLips/Figma-Context-MCP) | Fournit aux coding agents le contexte de design des fichiers Figma pour les aider à implémenter les interfaces existantes. | 16,314 | 0 | 2026-06-24 | 38.2 | MIT |
| [Talk to Figma MCP](https://github.com/grab/cursor-talk-to-figma-mcp) | Permet aux agents de lire et de modifier les designs Figma via un service MCP, un plugin Figma et un pont WebSocket. | 7,130 | 0 | 2026-07-26 | 37.2 | MIT |

### Diagrammes et expression visuelle

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) · ★référence utilisateur | Produit des diagrammes d'architecture, de flux ou de données en HTML/SVG autonomes au style de la marque. | 73,182 | 364 | 2026-11-25 | 96.9 | MIT |
| [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw) | Offre un canvas Excalidraw en lecture-écriture, modifiant et sauvegardant les diagrammes via CLI, Skill ou MCP. | 2,687 | 33 | 2026-11-10 | 68.3 | MIT |
| [Spotkit](https://github.com/Devesh-Shirsath/spotkit) | Skill Claude Code qui transforme une description de fonctionnalité en illustrations produit abstraites en SVG réel : elle détermine d'abord ce que fait la fonctionnalité et quelle relation elle exprime, puis choisit 2 à 5 primitives d'interface et une mise en page. | 130 | 33 | 2026-10-08 | 51.3 | MIT |

### Présentations et conception de documents

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) | Skill Claude Code qui reproduit le flux d'un studio de présentations haut de gamme : veille, collecte de sources, plan, scénario de slides, design HTML puis post-traitement en SVG et PPTX éditable, d'une phrase à un livrable. | 209 | 11 | 2026-11-18 | 55.5 | MIT |

### Articles, benchmarks et jeux de données

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [DesignBench](https://github.com/WebPAI/DesignBench) · Attention licence | Benchmark de recherche évaluant la génération, l'édition et la réparation de code front-end dans plusieurs frameworks. | 61 | 0 | 2026-07-27 | 20.8 | Non confirmée |
| [Design2Code](https://github.com/NoviScl/Design2Code) | Benchmark de capture-d'écran-vers-code sur des pages web réelles, avec jeu de données et outils d'évaluation automatique. | 605 | 0 | 2024-11-02 | 22.3 | MIT |
| [WebDesignAgent](https://github.com/DAMO-NLP-SG/WebDesignAgent) | Prototype de recherche de génération de sites web illustrant un flux de design piloté par la description, les gabarits de référence, les images et les retours. | 267 | 0 | 2024-09-20 | 19.4 | Apache-2.0 |

### Projets historiques et archivés

| Projet | Positionnement | Étoiles | Commits 90 j | Dernier commit UTC | Score de maintenance | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| [SuperDesign IDE (hérité)](https://github.com/superdesigndev/superdesign) · Archivé/historique · Attention licence | Extension IDE de design d'interfaces conservant le code ouvert d'origine ; le produit homonyme actuel est devenu une application web. | 7,648 | 0 | 2026-06-29 | 35.8 | AGPL-3.0 + conditions commerciales |
| [Penpot MCP (archivé)](https://github.com/penpot/penpot-mcp) · Archivé/historique | Le contenu de l'ancien dépôt autonome a été fusionné dans le répertoire mcp du dépôt principal de Penpot. | 537 | 0 | 2026-03-19 | 23.4 | MPL-2.0 |

## Comment choisir

- Vous avez déjà une bibliothèque de composants et l'équipe doit générer des prototypes interactifs : commencez par [GitHub Replica](https://github.com/github/replica) ; il dépend de l'application GitHub Copilot. Pour choisir vous-même l'agent ou le modèle, regardez [OpenDesign](https://github.com/nexu-io/open-design).
- Vous avez déjà une page web ou un fichier de design et devez continuer à l'éditer : pour un espace de travail centré sur le code, [Onlook](https://github.com/onlook-dev/onlook) ; pour la lecture-écriture de fichiers de design et le pilotage par scripts, [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil).
- Vous avez une page existante et voulez seulement améliorer le motion design ou la qualité du design : pour le motion, [Emil Kowalski Skills](https://github.com/emilkowalski/skills) ; pour la revue de mise en page et d'accessibilité, essayez d'abord [Impeccable](https://github.com/pbakaus/impeccable), puis validez avec un vrai navigateur, un vrai clavier et des technologies d'assistance.
- Vous voulez des diagrammes d'architecture au style de votre marque, ou un agent qui édite en continu sur un canvas : voir respectivement [Diagram Design](https://github.com/cathrynlavery/diagram-design) et [Excalidraw MCP Server](https://github.com/yctimlin/mcp_excalidraw).
- Vous n'avez qu'une phrase et il vous faut un livrable dont le PPTX reste éditable : voir [PPT Agent Skill](https://github.com/Akxan/ppt-agent-skill) ; vérifiez les dépendances d'export et l'attribution amont avant la livraison.
- Vous voulez réutiliser le même langage visuel dans plusieurs agents : rédigez d'abord couleurs, typographie et règles de mise en page avec la [spécification DESIGN.md](https://github.com/google-labs-code/design.md) ; les exemples de marques tiers ne servent que de référence.

Pour un premier essai, choisissez une page ou un diagramme pouvant être rendu public, vérifiez que le livrable reste éditable, inspectez les chemins des polices et des données vers les modèles distants, puis comparez les candidats sur la même entrée.

## Données et maintenance

- [Fiches projets et preuves à version figée](docs/projects.md)
- [Classements composite, étoiles, activité, récence](docs/rankings.md)
- [Articles et benchmarks](docs/research.md)
- [Recherche et décisions d'inclusion](../../research/README.md)
- [Méthode de classement](docs/methodology.md)
- [Guide de contribution](CONTRIBUTING.md)

## Licences

Le travail éditorial original et les scripts de ce catalogue sont sous [licence MIT](../../LICENSE). Les projets liés, les services hébergés, les jeux de données, les ressources et les polices suivent leurs propres conditions. Certains scripts de maintenance reprennent l'implémentation MIT du [catalogue vidéo IA](https://github.com/ZanePoe/awesome_ai_video_creation).

Les notes de vérification et les décisions d'inclusion de ce catalogue conservent le texte d'origine (en chinois) tel qu'il était au moment de la vérification, afin d'auditer la source et la formulation de chaque décision ; le répertoire `research/` et les journaux de modifications ne sont pas traduits automatiquement.
