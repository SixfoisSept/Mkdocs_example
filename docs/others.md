# Tables
Voici l'exemple d'une table. 


![Cadran Logo](assets/Cadran_logo.png){: style="height:80px" align=left }


## Où vit-on le mieux en France? 
:wink: Le Cadran pour l'Express

| Ville         | Population (en millions) | Département           | Région                   |
|---------------|--------------------------|-----------------------|--------------------------|
| Paris         | 2.14                     | Paris (75)            | Île-de-France            |
| Marseille     | 0.86                     | Bouches-du-Rhône (13) | Provence-Alpes-Côte d'Azur |
| Rennes        | 0.22                     | Ille-et-Vilaine (35)  | Bretagne                 |
| Bordeaux      | 0.25                     | Gironde (33)          | Nouvelle-Aquitaine       |
| Lorient       | 0.21                     | Morbihan (56)         | Bretagne                 |

!!! note
    L'ordre des villes ne represente pas leur classement. 

# Mermaid

Mermaid permet de décrire des schémas en symboles qui seront traduits au rendu de la page web.

Source : [mermaid](https://mermaid.js.org/intro/)

## Diagrammes 

Documentation : [mermaid](https://mermaid.js.org/syntax/flowchart.html)

```mermaid
flowchart LR
A(mon API) <-->|récupération des codes|B[(B)]
A -->|appel avec les codes| C(une autre API)
C -- Une autre façon de faire un lien --> D[Autre chose]
D <== Lien plus épais ==> B
```

````
```mermaid
flowchart LR
A(mon API) <-->|récupération des codes|B[(B)]
A -->|appel avec les codes| C(une autre API)
C -- Une autre façon de faire un lien --> D[Autre chose]
D <== Lien plus épais ==> B
```
````

```mermaid
flowchart TD
A(mon API) -->|récupération des codes|B[(B)]
A -->|appel avec les codes| C(une autre API)
C -- Une autre façon de faire un lien --> D[Autre chose]
D == Lien plus épais ==> B
```

````
```mermaid
flowchart TD
A(mon API) -->|récupération des codes|B[(B)]
A -->|appel avec les codes| C(une autre API)
C -- Une autre façon de faire un lien --> D[Autre chose]
D == Lien plus épais ==> B
```
````

## Diagrammes de séquence

```mermaid
sequenceDiagram
mon API ->> Une autre API: GET /informations
Une autre API -->> mon API: Les informations
Note over mon API,Une autre API: Une demande d'informations
```

````
```mermaid
sequenceDiagram
mon API ->> Une autre API: GET /informations
Une autre API -->> mon API: Les informations
Note over mon API,Une autre API: Une demande d'informations
```
````

```mermaid
sequenceDiagram
actor A as Utilisateur
participant B as API B
participant C as API C
participant D as Service D
A->>B: Recherche d'informations
loop Chaque minute
    B-->A: Les voilà
end
A->>C: Autres infos
C->>D: Infos partielles
D-)C: Infos
C-)A: Informations
Note right of D: Appel au 6x7
Note over B,C: Pas d'appel direct au 6x7
Note over A,B: Une autre note

```

````
```mermaid
sequenceDiagram
actor A as Utilisateur
participant B as API B
participant C as API C
participant D as Service D
A->>B: Recherche d'informations
loop Chaque minute
    B-->A: Les voilà
end
A->>C: Autres infos
C->>D: Infos partielles
D-)C: Infos
C-)A: Informations
Note right of D: Appel au 6x7
Note over B,C: Pas d'appel direct au 6x7
Note over A,B: Une autre note
```
````

