## Session 1 - 20.03.2023

- What is healthcare data?
- Hands-on FOHIspital. Setting up FASTapi and basic http interactions
- Serving JSON Data of FHIR-Resources

## Session 2 - 27.03.2023

- Understanding the need for data validation (formal check for valid JSON)
- Allow to retrieve JSON Data
- https://github.com/dominikb1888/fohispital/tree/0a_FASTapi-JSON-post


## Session 3 - 17.04.2023

Agenda:
- [x] Recap
- [x] Getting the app on codespaces (Requirements.txt)
- [x] Setting up modular architecture for fastapi
- [x] Installing fhir_resources
- [x] Intro to typing and types in python

Achievements:
- Further Validation and Persistence
- Checking for JSON being valid FHIR
- https://github.com/dominikb1888/fohispital/tree/01_routes_patients

Homework:
- Pick any FHIR resource
- Add a similar route to our application
- Play around with actual data from that resource
- You might need to: Add a new folder for that data, overcome random errors


## Session 4 - 24.03.2023

Data Formats and Data Storage

Agenda:
- [ ] Recap Homework (checking routes and working on pull requests)
- [o] Data Formats (JSON, CSV) [ND-JSON, JSON-LD, RDF]
- [x] Build a database for our raw data (Options: Redis, SQLite, Postgres, BJSON, RDF)


## Session 5 - 08.05.2023

- Recap of the application so far

Homework in-class:
- [x] Pick any FHIR resource
- [x] Add a similar route to our application: related person

## Session 6 - 15.05.2023

- Extending our application. In-class groupwork

1. Make sure that the base system works for everybody in you group
2. Connecting (and maybe) extending the two existing resources/types (patient and related person)
3. Serving a list of connected persons on a specific URL
4. (Optional: Discuss advantages and disadvantages of the approach chosen (storing data in a document-oriented database)



- [ ] Play around with actual data from that resource: add a new list for related persons per patient
- [ ] Make sure your resource also works with the Redis DB: TODO
- [ ] You might need to: overcome random errors




## Session 7 - 22.05.2023

Accessing and Querying Data

Agenda:
- [ ] SQL
- [o] Redis
- [ ] GraphQL
- [ ] SPARQL
