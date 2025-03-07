# Table Mapping

## Source data
 (link to api)

| Source Header | Sample Source Data |
| --------------| -------------|
| category | anti-social-behaviour |
| location_type | Force |
| context | | 
| outcome_status | | 
| persistent_id | |
| id | 116208978 | 
| location_subtype | |
| month | 2024-01 |
| location.latitude | 52.628462 | 
| location.street.id | 1738792 |
| location.street.name | On or near De Montfort Square |
| location.longitude | -1.126029 | 
| outcome_status.category | Action to be taken by another organisation |
| outcome_status.date | 2024-03 | 

## Source Table Name 

impt_police_street_crime

## Dimensions

### d_street_crime_category 

| Source Table | Source Header | Target Header | Transformation | Data Type | PK / FK / NatID | 
| ----- | -----| -----| -----| -----| -----|
| impt_police_street_crime | auto generated ID | d_street_crime_category_ID | N/A | int | PK |
| impt_police_street_crime | category | street_crime_category | N/A | VARCHAR (250) | NatID|

### d_street_crime_location

| Source Table | Source Header | Target Header | Transformation | Data Type | PK / FK / NatID | 
| ----- | -----| -----| -----| -----| ----|
| impt_police_street_crime | auto generated ID | d_street_crime_location_ID | N/A | int | PK |
| impt_police_street_crime | location_street_name | location_name | N/A | VARCHAR (250) | N/A |
| impt_police_street_crime | N/A | location_name_NatID | CONCAT(location_street_name, '\|\| ', location_street_id) | VARCHAR (250) | NatID |

### d_street_crime_outcome

| Source Table | Source Header | Target Header | Transformation | Data Type | PK / FK / NatID | 
| ----- | -----| -----| -----| -----| -----|
| impt_police_street_crime | auto generated ID | d_street_crime_outcome_ID | N/A | int | PK | 
| impt_police_street_crime | outcome_status_category | street_crime_outcome | N/A | VARCHAR (250) | NatD |

## Fact

### f_police_street_crime 

| Source Table | Source Header | Target Header | Transformation | Data Type | PK / FK / NatID | Table JOIN | Table JOIN ON |   
| ----- | -----| -----| -----| -----| -----| -----| -----|
| impt_police_street_crime | auto generated ID | street_crime_case_id | N/A | int | PK | N/A | N/A |
| impt_police_street_crime | id | street_crime_case_id | N/A | int | N/A | N/A | N/A
| impt_police_street_crime | outcome_status_date | case_status_date | N/A | DATE | N/A | N/A | N/A |
| impt_police_street_crime | CONCAT(location_street_name, "\|\|", location_street_id) | FK_location_nameID | CONCAT(location_street_name, "\|\|", location_street_id) | VARCHAR (250) | FK | d_street_crime_location | location_name_NatID | 
| impt_police_street_crime | outcome_status_category | FK_street_crime_outcome_statusID | N/A | VARCHAR (250) | FK | d_street_crime_outcome | street_crime_outcome | N/A | VARCHAR (250) | FK | d_street_crime_category | street_crime_category | 


