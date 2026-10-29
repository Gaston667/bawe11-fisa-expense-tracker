# Expense Tracker — Organisation Agile

## 1. Présentation du projet

Le projet consiste à développer une application web de gestion de dépenses personnelles.

L'utilisateur pourra :

- créer un compte ;
- se connecter et se déconnecter ;
- enregistrer ses dépenses ;
- modifier ou supprimer ses dépenses ;
- classer ses dépenses par catégorie ;
- définir un budget mensuel ;
- suivre le montant dépensé et le montant restant ;
- consulter un tableau de bord ;
- filtrer et rechercher ses dépenses ;
- utiliser l'application en français ou en anglais ;
- utiliser l'application sur ordinateur et téléphone.

### Technologies prévues

- **Backend :** Flask
- **Base de données :** SQLite
- **Frontend :** HTML / CSS / JavaScript
- **Architecture :** MVC léger

### Tables prévues

- `users`
- `categories`
- `expenses`

---

# 2. Méthode Agile

Le projet est organisé sur **2 semaines**, avec :

- **2 sprints**
- **1 sprint = 1 semaine**

Chaque User Story possède un nombre de **Story Points (SP)** permettant d'estimer sa complexité relative.

### Échelle des Story Points

| Story Points | Complexité |
|---:|---|
| 1 | Très faible |
| 2 | Faible |
| 3 | Moyenne |
| 5 | Importante |

---

# 3. Product Backlog

## EPIC 1 — Authentification et compte

| ID | User Story | SP |
|---|---|---:|
| US01 | En tant que visiteur, je veux créer un compte avec un pseudo, un email, un mot de passe et un budget mensuel afin d'utiliser l'application. | 3 |
| US02 | En tant que visiteur, je veux être informé lorsque les données d'inscription sont invalides ou que l'email existe déjà. | 2 |
| US03 | En tant qu'utilisateur, je veux que mon mot de passe soit stocké de manière sécurisée afin de protéger mon compte. | 2 |
| US04 | En tant qu'utilisateur, je veux me connecter avec mon email et mon mot de passe afin d'accéder à mes données. | 3 |
| US05 | En tant qu'utilisateur, je veux rester connecté pendant ma navigation et pouvoir me déconnecter. | 2 |
| US06 | En tant que visiteur non connecté, je ne veux pas pouvoir accéder aux pages privées de l'application. | 2 |

---

## EPIC 2 — Gestion des dépenses

| ID | User Story | SP |
|---|---|---:|
| US07 | En tant qu'utilisateur, je veux voir la liste de mes dépenses afin de suivre mes achats. | 2 |
| US08 | En tant qu'utilisateur, je veux ajouter une dépense avec une description, un montant, une date et une catégorie. | 3 |
| US09 | En tant qu'utilisateur, je veux être averti si les informations saisies pour une dépense sont invalides. | 2 |
| US10 | En tant qu'utilisateur, je veux modifier une dépense afin de corriger une erreur. | 3 |
| US11 | En tant qu'utilisateur, je veux supprimer une dépense avec confirmation afin d'éviter une suppression accidentelle. | 2 |
| US12 | En tant qu'utilisateur, je veux uniquement voir et modifier mes propres dépenses afin de protéger mes données. | 3 |
| US13 | En tant qu'utilisateur, je veux voir mes dépenses les plus récentes en premier. | 1 |

---

## EPIC 3 — Catégories et filtres

| ID | User Story | SP |
|---|---|---:|
| US14 | En tant qu'utilisateur, je veux disposer de catégories prédéfinies afin de classer mes dépenses. | 1 |
| US15 | En tant qu'utilisateur, je veux filtrer mes dépenses par catégorie et par mois afin de retrouver plus facilement certaines dépenses. | 3 |
| US16 | En tant qu'utilisateur, je veux pouvoir réinitialiser les filtres afin d'afficher à nouveau toutes mes dépenses. | 1 |
| US17 | En tant qu'utilisateur, je veux rechercher une dépense par son nom afin de la retrouver rapidement. | 2 |

---

## EPIC 4 — Budget et dashboard

| ID | User Story | SP |
|---|---|---:|
| US18 | En tant qu'utilisateur, je veux définir et consulter mon budget mensuel afin de suivre ma limite de dépenses. | 2 |
| US19 | En tant qu'utilisateur, je veux voir le total dépensé et le montant restant pour le mois courant. | 3 |
| US20 | En tant qu'utilisateur, je veux visualiser la proportion de mon budget consommée et être averti si je dépasse mon budget. | 2 |
| US21 | En tant qu'utilisateur, je veux disposer d'un dashboard regroupant mon budget, mes dépenses récentes et les informations principales. | 3 |
| US22 | En tant qu'utilisateur, je veux voir la répartition de mes dépenses par catégorie sous forme de graphique. | 3 |

---

## EPIC 5 — Interface et navigation

| ID | User Story | SP |
|---|---|---:|
| US23 | En tant qu'utilisateur, je veux disposer d'une navigation commune afin d'accéder facilement au dashboard, aux dépenses et à la déconnexion. | 2 |
| US24 | En tant qu'utilisateur, je veux retrouver une zone de crédits/contact sur toutes les pages. | 1 |

---

## EPIC 6 — Français / Anglais

| ID | User Story | SP |
|---|---|---:|
| US25 | En tant qu'utilisateur, je veux pouvoir passer l'ensemble du site du français à l'anglais grâce à un bouton FR/EN. | 3 |
| US26 | En tant qu'utilisateur, je veux conserver la langue sélectionnée lorsque je change de page. | 2 |

---

## EPIC 7 — Responsive et compatibilité

| ID | User Story | SP |
|---|---|---:|
| US27 | En tant qu'utilisateur, je veux utiliser l'application confortablement sur ordinateur et téléphone avec une interface adaptée à chaque écran. | 5 |
| US28 | En tant qu'utilisateur, je veux pouvoir utiliser toutes les fonctionnalités du site sur Firefox Linux et Firefox Android. | 3 |

---

# 4. Sprint 1 — Semaine 1

## Objectif du sprint

Obtenir une première version fonctionnelle permettant à un utilisateur de :

1. créer un compte ;
2. se connecter ;
3. accéder à ses pages privées ;
4. ajouter des dépenses ;
5. consulter ses dépenses ;
6. modifier ou supprimer ses dépenses ;
7. se déconnecter.

## Sprint Backlog

| ID | User Story | SP |
|---|---|---:|
| US01 | Créer un compte avec pseudo, email, mot de passe et budget mensuel. | 3 |
| US02 | Signaler les erreurs d'inscription et les emails déjà utilisés. | 2 |
| US03 | Stocker le mot de passe de manière sécurisée. | 2 |
| US04 | Se connecter avec email et mot de passe. | 3 |
| US05 | Garder la session ouverte et permettre la déconnexion. | 2 |
| US06 | Bloquer l'accès aux pages privées pour les visiteurs non connectés. | 2 |
| US07 | Afficher la liste des dépenses. | 2 |
| US08 | Ajouter une dépense avec description, montant, date et catégorie. | 3 |
| US09 | Vérifier les données saisies pour une dépense. | 2 |
| US10 | Modifier une dépense. | 3 |
| US11 | Supprimer une dépense avec confirmation. | 2 |
| US12 | Empêcher un utilisateur de voir ou modifier les dépenses d'un autre utilisateur. | 3 |
| US13 | Trier les dépenses de la plus récente à la plus ancienne. | 1 |
| US14 | Utiliser des catégories prédéfinies. | 1 |

### Total Sprint 1

**31 Story Points**

---

# 5. Sprint 2 — Semaine 2

## Objectif du sprint

Transformer le MVP en application complète de suivi budgétaire et finaliser les exigences du projet.

## Sprint Backlog

| ID | User Story | SP |
|---|---|---:|
| US15 | Filtrer les dépenses par catégorie et par mois. | 3 |
| US16 | Réinitialiser les filtres. | 1 |
| US17 | Rechercher une dépense par son nom. | 2 |
| US18 | Définir et consulter son budget mensuel. | 2 |
| US19 | Afficher le total dépensé et le montant restant. | 3 |
| US20 | Afficher la progression du budget et signaler un dépassement. | 2 |
| US21 | Afficher un dashboard avec les principales informations. | 3 |
| US22 | Afficher les dépenses par catégorie sous forme de graphique. | 3 |
| US23 | Ajouter une navigation commune à toutes les pages. | 2 |
| US24 | Ajouter les crédits/contact sur toutes les pages. | 1 |
| US25 | Permettre de traduire tout le site en FR/EN. | 3 |
| US26 | Conserver la langue choisie pendant la navigation. | 2 |
| US27 | Adapter l'interface aux ordinateurs et téléphones. | 5 |
| US28 | Vérifier le fonctionnement sous Firefox Linux et Firefox Android. | 3 |

### Total Sprint 2

**35 Story Points**

---

# 6. Tâches techniques de livraison

Ces tâches ne sont pas considérées comme des User Stories métier.

| ID | Tâche |
|---|---|
| T01 | Rédiger le README. |
| T02 | Documenter l'initialisation de la base de données. |
| T03 | Rédiger le rapport final. |
| T04 | Réaliser les captures des versions française et anglaise. |
| T05 | Réaliser les captures des versions mobile et desktop. |
| T06 | Vérifier le nombre de fichiers client et serveur. |
| T07 | Vérifier que la base contient au maximum 3 tables. |
| T08 | Tester l'installation et le lancement sur une VM propre. |
| T09 | Vérifier la taille finale du projet et générer l'archive de rendu. |

---

# 7. Workflow Agile

Chaque élément du Sprint Backlog suit les états suivants :

```text
TODO -> IN PROGRESS -> TEST -> DONE
```

### TODO

La User Story n'a pas encore été commencée.

### IN PROGRESS

La User Story est actuellement en cours de développement.

### TEST

Le développement est terminé et la fonctionnalité doit être vérifiée.

### DONE

La fonctionnalité respecte la Definition of Done.

---

# 8. Definition of Done

Une User Story peut être déplacée dans **DONE** uniquement si :

- la fonctionnalité est entièrement développée ;
- la fonctionnalité fonctionne correctement ;
- les données sont correctement enregistrées lorsque la base de données est utilisée ;
- les accès aux données respectent l'utilisateur connecté ;
- aucune erreur importante n'est présente dans la console ;
- le code est suffisamment lisible ;
- les commentaires présents dans le code sont écrits en anglais ;
- la fonctionnalité a été testée sur Firefox ;
- les modifications ont été enregistrées dans Git.

Pour une User Story concernant l'interface, il faut également vérifier :

- l'affichage desktop ;
- l'affichage mobile ;
- la version française ;
- la version anglaise.

---

# 9. Résumé des sprints

## Sprint 1

**Thème : Authentification + CRUD des dépenses**

Objectif :

```text
Créer un compte
        |
        v
Se connecter
        |
        v
Ajouter une dépense
        |
        v
Afficher ses dépenses
        |
        v
Modifier / supprimer
        |
        v
Se déconnecter
```

**31 SP**

---

## Sprint 2

**Thème : Budget + Dashboard + Interface + Livraison**

Objectif :

```text
Budget
  +
Dashboard
  +
Filtres
  +
Graphiques
  +
FR / EN
  +
Responsive
  +
Compatibilité Firefox
  +
Livraison
```

**35 SP**

---

# 10. Contraintes principales du projet

- 3 tables SQL maximum ;
- partie client limitée en nombre de fichiers ;
- partie serveur limitée en nombre de fichiers ;
- présence de JavaScript ;
- lecture et écriture dans la base de données ;
- interface disponible en français et en anglais ;
- interface adaptée au desktop et au mobile ;
- fonctionnement sous Firefox Linux et Firefox Android ;
- commentaires du code en anglais ;
- archive finale inférieure ou égale à 3 Mo ;
- technologies et dépendances supplémentaires limitées à environ 500 Mo ;
- README obligatoire ;
- rapport final obligatoire.
