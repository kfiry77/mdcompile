# Non-UML Examples with PlantUML

This document contains a collection of UML diagrams created using PlantUML.

### 1. Gantt Chart

```plantuml
@startgantt
[Prototype design] requires 15 days
[Test prototype] requires  10 days

[Prototype design] starts D+0
[Test prototype] starts D+15
@endgantt
```
This Gantt chart shows a simple project timeline with three tasks and their durations.

### 2. Mind Map 
```plantuml

@startmindmap
* Core Idea
** Branch 1
*** Sub-branch 1
*** Sub-branch 2
** Branch 2
*** Sub-branch 3
** Branch 3
@endmindmap
```
This mind map represents a central idea with three branches and various sub-branches.

### 3. JSON 

```plantuml

@startjson
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}
@endjson


```

### 4. Information Engineering Digram

```plantuml 
@startuml

' hide the spot
' hide circle

' avoid problems with angled crows feet
skinparam linetype ortho

entity "User" as e01 {
  *user_id : number <<generated>>
  --
  *name : text
  description : text
}

entity "Card" as e02 {
  *card_id : number <<generated>>
  sync_enabled: boolean
  version: number
  last_sync_version: number
  --
  *user_id : number <<FK>>
  other_details : text
}

entity "CardHistory" as e05 {
  *card_history_id : number <<generated>>
  version : number
  --
  *card_id : number <<FK>>
  other_details : text
}

entity "CardsAccounts" as e04 {
  *id : number <<generated>>
  --
  card_id : number <<FK>>
  account_id : number <<FK>>
  other_details : text
}


entity "Account" as e03 {
  *account_id : number <<generated>>
  --
  user_id : number <<FK>>
  other_details : text
}

entity "Stream" as e06 {
  *id : number <<generated>>
  version: number
  searchingText: string
  --
  owner_id : number <<FK>>
  follower_id : number <<FK>>
  card_id: number <<FK>>
  other_details : text
}


e01 }|..|| e02
e01 }|..|| e03

e02 }|..|| e05

e02 }|..|| e04
e03 }|..|| e04

e02 }|..|| e06
e03 }|..|| e06


@enduml

```