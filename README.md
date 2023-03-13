# Foundations of Health Informatics

Course Project: https://github.com/dominikb1888/fohispital

In our course project we will try and apply the core topics of our course directly and hands-on by building a web service of a ficticious hospital serving FHIR/JSON of many relevant types of healthcare data.

## Literature

Hands-on: [https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954](https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954)

Recommended Reading: https://link.springer.com/book/10.1007/978-3-030-58721-5

## Goals:

Sections 1 and 2: Knowledge Pyramid with focus on health and healthcare
Sections 3 and 4: Data Analytics and Application Development with Python

### 1. Storing and accessing data

- What is health data and information?
- Which technologies exist for storing it (File, Database, Graph Database)
- Which technologies (CSV, JSON, ND-JSON, JSON-LD, RDF) and standards exist for making it interoperable (DICOM, FHIR, Snomed, ICD-10, Loinc)
- Which technologies exist for accessing it (SQL, REST APIs, GraphQL, SPARQL)


### 2. Understanding healthcare data

- How are decision and action created in healthcare?
- How is FHIR applied in clinical documents and workflows?
- What are common Ontologies, Terminologies, and Code Sets?


### 3. Analyzing data

- What is data quality in healthcare and how to assess it?
- What are sources of healthcare data? (Wearables, Devices, Systems, Reports)
- How can machine learning and natural language processing be applied?
- What are the potentials of deep learning and AI in healthcare?


### 4. Designing data applications

- Cloud Computing and Hybrid Cloud Computing in Healthcare
- Web Application Development
- Big data analytics and processing


## Sessions

Health Informatics is the application of digital methods and tools to processes around health and healthcare. This may be within a clinical environment or before that. The reason data  becomes health data is the question we ask to that data or the task we want to automate based on it. Storing and accessing this data and making it useful for healthcare professionals is key.


### A. Introduction to Health Informatics

1. What is Health-care Data, why health informatics?
- History of Health, Healthcare, Biomedical Informatics
- What is health data? How does data become health data, healthcare data, medical data?
- What are current trends and stati in different regions
- Goals: What is this course about: Data Engineering for health systems

2. Technical Framework and Process: Nix, Docker, Postgresql, Python, Java, Neo4j, RDF
- How to build replicable systems
- How to run and serve microservices
- How to store and server health data
- How to build data intensive applications
- Setting up our Dev Environment
- Building a very simple HIS from scratch with FastAPI and FHIR
- Running Synthea
- Using Jupyter Notebooks

### B. Data and Data Formats

3. Interoperability: Standardized vocabularies in healthcare
4. Deep Dive: Electronic Health Records (EHR)
5. Deep Dive: Imaging Data (DICOM, PACS)
6. Deep Dive: Wearable Device Data (Garmin)
7. Deep Dive: Lab Devices and Data
8. Deep Dive: Claims Data

### C. Data Analytics, ML, and Graphs

9. Analytics and ML
10. Federated Learning
11. NLP
12. Data Normalization and Harmonization
13. Graphs and Graph-based Analytics


### D. Building and Deploying Systems

14. Cloud Computing
15. Dev Ops



### Literature:

- Theory: Biomedical Informatics (https://link.springer.com/book/10.1007/978-3-030-58721-5)
- Hands-on: https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=29441724
- https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954


### Additional Readings:

- Interoperability and Modeling: https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=4562479
- https://link.springer.com/book/10.1007/978-3-030-91563-6
- https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=7021286
- https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6715215
- https://link.springer.com/chapter/10.1007/978-1-4842-6870-4_1 (Good Intro to Regression Analysis)
- https://link.springer.com/book/10.1007/978-3-030-18626-5 (Precision and Personalized Med Info)
- https://link.springer.com/book/10.1007/978-3-319-98779-8 (Medical Research Informatics)
- https://link.springer.com/book/10.1007/978-3-030-81030-6 (Cardio Tech)


### Future Topics:

https://link.springer.com/book/10.1007/978-3-031-11302-4



## Exercise and Tutorials
- RESTful APIs: https://www.restapitutorial.com/
- Testing Database Interactions with Python: https://medium.com/@geoffreykoh/fun-with-fixtures-for-database-applications-8253eaf1a6d
- Process Mining in Healthcare: https://medium.com/@c3_62722/process-mining-with-python-tutorial-a-healthcare-application-part-1-ae02027a050

## Toolbox

- NeuroKit:  https://neuropsychology.github.io/NeuroKit
- HeartPy: https://github.com/paulvangentcom/heartrate_analysis_python
- Data focused Python (FHIR): https://briankolowitz.github.io/data-focused-python/resources
- DICOM to FHIR converter: https://github.com/LinuxForHealth/dicom-fhir-converter
- Synthea Patient Data Generator: https://github.com/synthetichealth/synthea
- HAPI FHIR: https://github.com/hapifhir/hapi-fhir
- ORTHANC: FOSS Lightweight DICOM Server: https://www.orthanc-server.com/
- FHIRtoRDF: https://github.com/BD2KOnFHIR/fhirtordf

## Additional Reading

Python for Data Analysis: https://wesmckinney.com/pages/book.html
