# Classement de maintenance

Les métriques proviennent de GitHub GraphQL : étoiles, commits atteignables sur la branche par défaut durant les 30 et 90 derniers jours, dernier commit sur la branche par défaut, état d'archivage, etc. Les fenêtres temporelles se calculent sur l'instantané UTC ; il ne s'agit pas de compter les push sur toutes les branches.

1. Stratifier d'abord par état de maintenance : commit sur les 90 derniers jours, aucun commit depuis 91–365 jours, aucun commit depuis plus de 365 jours, archivé ou référence historique explicite.
2. Score de maintenance composite = 100 × (0.40 × terme étoiles + 0.35 × terme activité + 0.25 × terme fraîcheur). Le terme étoiles vaut log1p(Stars) / log1p(100000), le terme activité vaut log1p(commits sur 90 jours) / log1p(500), tous deux plafonnés à 1 ; le terme fraîcheur vaut exp(−jours depuis le dernier commit / 90).
3. Quatre vues sont fournies : composite, étoiles, commits sur 90 jours, dernier commit ; à égalité, l'ordre stable se décide par les étoiles puis le nom du dépôt. L'aperçu des candidats principaux actifs exige en plus une licence ouverte vérifiée.

Les étoiles mesurent l'attention ; le nombre de commits dépend de la taille du dépôt, des migrations d'historique et des mises à jour de documentation. Les métriques d'un dépôt ne résument pas la maintenance d'un Skill pris isolément, ni la qualité des livrables, la fidélité des reproductions, l'accessibilité ou la possibilité d'usage commercial.

Le flux de maintenance rafraîchit régulièrement métriques, README, CSV et fiches projets. Les constats sur les fonctionnalités et les licences conservent leur date de vérification manuelle et leur preuve à commit figé, et ne se réécrivent pas automatiquement avec l'instantané.
