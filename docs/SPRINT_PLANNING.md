# Expense Tracker — Sprint Planning

## Organisation générale

Le projet est organisé en **2 sprints d'une semaine**.

- **Début du projet :** jeudi 29 octobre 2026
- **Sprint 1 :** du 29 octobre au 4 novembre 2026
- **Sprint 2 :** du 5 novembre au 11 novembre 2026

Le Product Backlog contient **28 User Stories**.

---

# Sprint 1 — Du 29 octobre au 4 novembre 2026

## Sprint Goal

Obtenir un **MVP fonctionnel** permettant à un utilisateur de :

- créer un compte ;
- se connecter ;
- conserver sa session ;
- accéder uniquement à ses données ;
- ajouter une dépense ;
- afficher ses dépenses ;
- modifier une dépense ;
- supprimer une dépense ;
- se déconnecter.

## Sprint Backlog

| Date | Jour | User Stories | Travail prévu | SP |
|---|---|---|---|---:|
| **29/10/2026** | Jeudi | US01, US02, US03 | Création du compte, validation des données d'inscription, vérification de l'email et stockage sécurisé du mot de passe. | 7 |
| **30/10/2026** | Vendredi | US04, US05, US06 | Connexion, gestion de session, déconnexion et protection des pages privées. | 7 |
| **02/11/2026** | Lundi | US07, US08, US14 | Affichage des dépenses, ajout d'une dépense et mise en place des catégories prédéfinies. | 6 |
| **03/11/2026** | Mardi | US09, US10, US13 | Validation des données d'une dépense, modification et tri par date. | 6 |
| **04/11/2026** | Mercredi | US11, US12 | Suppression avec confirmation, isolation des données entre utilisateurs et tests du Sprint. | 5 |

### Total Sprint 1

**31 Story Points**

## Résultat attendu

À la fin du Sprint 1, le parcours principal doit être fonctionnel :

```text
Créer un compte
        |
        v
Se connecter
        |
        v
Accéder à ses dépenses
        |
        v
Ajouter une dépense
        |
        v
Afficher les dépenses
        |
        v
Modifier / supprimer
        |
        v
Se déconnecter
```

## Sprint Review

À la fin du Sprint 1, les points suivants doivent être vérifiés :

- un utilisateur peut créer un compte ;
- le mot de passe n'est pas stocké en clair ;
- un utilisateur peut se connecter et se déconnecter ;
- les pages privées sont protégées ;
- un utilisateur peut ajouter, modifier et supprimer une dépense ;
- les catégories sont disponibles ;
- les dépenses sont triées de la plus récente à la plus ancienne ;
- un utilisateur ne peut pas consulter ou modifier les dépenses d'un autre utilisateur.

---

# Sprint 2 — Du 5 novembre au 11 novembre 2026

## Sprint Goal

Transformer le MVP en une application complète de suivi budgétaire et finaliser les exigences fonctionnelles et techniques du projet.

## Sprint Backlog

| Date | Jour | User Stories | Travail prévu | SP |
|---|---|---|---|---:|
| **05/11/2026** | Jeudi | US18, US19, US21 | Budget mensuel, total dépensé, montant restant et structure du dashboard. | 8 |
| **06/11/2026** | Vendredi | US20, US22 | Barre de progression du budget, alerte de dépassement et graphique par catégorie. | 5 |
| **09/11/2026** | Lundi | US15, US16, US17 | Filtres par catégorie et par mois, réinitialisation des filtres et recherche par nom. | 6 |
| **10/11/2026** | Mardi | US23, US24, US25, US26 | Navigation commune, zone crédits/contact, traduction FR/EN et conservation de la langue. | 8 |
| **11/11/2026** | Mercredi | US27, US28 | Responsive desktop/mobile, tests Firefox Linux et Android et corrections finales. | 8 |

### Total Sprint 2

**35 Story Points**

## Résultat attendu

À la fin du Sprint 2, l'application doit proposer :

```text
Budget mensuel
      +
Total dépensé
      +
Montant restant
      +
Dashboard
      +
Graphiques
      +
Filtres
      +
Recherche
      +
FR / EN
      +
Desktop / Mobile
      +
Compatibilité Firefox
```

---

# Tâches techniques de livraison

Les tâches techniques sont réparties sur le Sprint 2 afin de ne pas tout laisser pour le dernier jour.

| Date | ID | Tâche |
|---|---|---|
| **05/11/2026** | T01 | Commencer la rédaction du README. |
| **06/11/2026** | T02 | Documenter l'initialisation de la base de données. |
| **09/11/2026** | T03 | Commencer la rédaction du rapport final. |
| **10/11/2026** | T04 | Réaliser les captures des versions française et anglaise. |
| **10/11/2026** | T05 | Réaliser les captures des versions mobile et desktop. |
| **11/11/2026** | T06 | Vérifier le nombre de fichiers client et serveur. |
| **11/11/2026** | T07 | Vérifier que la base contient au maximum 3 tables. |
| **11/11/2026** | T08 | Tester l'installation et le lancement sur une VM propre. |
| **11/11/2026** | T09 | Vérifier la taille finale et générer l'archive de rendu. |

---

# Workflow du Sprint

Chaque User Story passe par les états suivants :

```text
TODO -> IN PROGRESS -> TEST -> DONE
```

## TODO

La User Story n'a pas encore été commencée.

## IN PROGRESS

La User Story est en cours de développement.

## TEST

Le développement est terminé et la fonctionnalité doit être vérifiée.

## DONE

La User Story respecte la Definition of Done.

---

# Definition of Done

Une User Story est considérée comme terminée uniquement si :

- la fonctionnalité est entièrement développée ;
- la fonctionnalité fonctionne correctement ;
- les données sont correctement enregistrées lorsque la base de données est utilisée ;
- les accès aux données respectent l'utilisateur connecté ;
- aucune erreur importante n'est présente dans la console ;
- le code est suffisamment lisible ;
- les commentaires dans le code sont rédigés en anglais ;
- la fonctionnalité a été testée sur Firefox ;
- les modifications ont été enregistrées dans Git.

Pour les User Stories concernant l'interface, il faut également vérifier :

- l'affichage desktop ;
- l'affichage mobile ;
- la version française ;
- la version anglaise.

---

# Vue globale du planning

```text
SPRINT 1
29/10 -> 04/11
────────────────────────────────
29/10  Inscription
30/10  Connexion / Session
02/11  Ajout / Liste / Catégories
03/11  Modification / Validation
04/11  Suppression / Sécurité / Tests

              |
              v

           MVP prêt


SPRINT 2
05/11 -> 11/11
────────────────────────────────
05/11  Dashboard / Budget
06/11  Progression / Graphiques
09/11  Filtres / Recherche
10/11  Navigation / FR-EN
11/11  Responsive / Firefox / Livraison

              |
              v

        Version finale prête
```

> **Remarque :** le 11 novembre est un jour férié en France. Si aucune séance de travail n'est prévue ce jour-là, les tâches du 11/11 peuvent être reportées au 12/11 sans modifier le contenu du Sprint.
