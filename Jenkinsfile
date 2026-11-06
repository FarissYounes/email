
# Documentation – Provisioning des environnements Liberty / MyCloud

**Version de référence : 4.4**

Cette documentation concerne les releases de provisioning des environnements Liberty / MyCloud associées aux templates suivants :

- `BPCE-IT-PAD-PROVISIONNING_CIB_ASHTAG_LIBERTY_MYCLOUD`
- `BPCE-IT-PAD-PROVISIONNING_DOM_LIBERTY_MYCLOUD`

## Historique des versions

| Version | Évolutions apportées |
|---|---|
| 2.0 | Ajout de Tomcat dans la couche applicative, gestion des habilitations dans XL Deploy (XLD), automatisation du paramétrage des credentials des VM dans XLD, création des conteneurs sur les VM et ajout d'un contrôle spécifique aux environnements Bunker. |
| 2.1 | Modification des DNS Alias IIS et suppression des bindings. |
| 2.2 | Ajout du moniteur Load Balancer (LB) associé au middleware. |
| 2.3 | Exposition du paramètre `sqlCollation` pour SQL Server. |
| 3.0 | Introduction du POD Bunker Vega, de la résilience et du mécanisme de Zero Downtime Deployment. |
| 3.1 | Prise en charge d'Oracle, JBoss, IIS et ARR sur le socle convergé, avec intégration de BP Network 3.1. |
| 3.2 | Prise en charge de RHEL 8 et d'Oracle Data Guard. |
| 3.3 | Intégration de nouvelles vagues de patchs. |
| 4.0 | Refonte complète du socle convergé Linux et ajout de nouveaux blueprints : LB avec DNS Alias multiples, Windows Server (couches application et data) et On-Premises Data Gateway. Réorganisation de l'articulation avec les sous-releases de déploiement du socle applicatif. |
| 4.1 | Amélioration de la gestion des comptes de service et correction de plusieurs anomalies. |
| 4.2 | Ajout de la gestion de PHP sous RHEL 9 et mise en place d'une interface avec `GET_MYCLOUD_REQUIRED_SERVICES` et `INIT-XLD-ENVIRONMENT-CONFIGURATION`. |
| 4.3 | Adaptations liées à la réorganisation de la direction DPM_PPR, notamment la séparation du SEP en PBS et PCS. |
| 4.4 | Refonte et évolutions du processus de provisioning. |

## 1. Objet

Le template `BPCE-IT-PAD-PROVISIONNING` permet de provisionner des environnements dans MyCloud, conformément au modèle PAD.

Depuis la version 4.0, le mécanisme de *pattern* a été supprimé afin d'apporter davantage de souplesse dans la configuration des environnements.

Le provisioning repose désormais sur un ensemble de services disponibles pour chaque couche du modèle PAD (Présentation, Application et Data). Chaque service peut être sélectionné indépendamment, selon les besoins de l'environnement à provisionner.

## 2. Évolutions de la version 4.4

La version 4.4 constitue la version de référence actuelle. Elle introduit deux nouvelles releases destinées à accompagner la migration progressive des services vers le nouveau fournisseur de cloud privé Liberty.

Ces releases permettent de gérer les souscriptions Liberty pour les différentes couches du modèle PAD :

- **Couche Présentation et couche Application :** les souscriptions sont désormais gérées sur Liberty.
- **Couche Data :** cette couche reste temporairement hors du périmètre MyCloud, dans l'attente de la finalisation de la migration des services vers le nouveau fournisseur de cloud privé.

Les deux nouvelles releases sont les suivantes :

- `BPCE-IT-PAD-PROVISIONNING_CIB_ASHTAG_LIBERTY_MYCLOUD`
- `BPCE-IT-PAD-PROVISIONNING_DOM_LIBERTY_MYCLOUD`

Elles répondent à deux périmètres de souscription distincts :

- **Release CIB :** permet de commander les souscriptions associées au domaine CIB.
- **Release DOM :** permet de commander les souscriptions associées au domaine DOM, notamment sur `dom101`.

Cette évolution permet d'accompagner la transition vers Liberty tout en maintenant une gestion distincte des souscriptions selon les domaines concernés.
