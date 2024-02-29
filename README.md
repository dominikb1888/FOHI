# Foundations of Health Informatics - Networking and Data Exchange in Healthcare

Course Project: https://github.com/dominikb1888/fohispital

In our course project we will try and apply the core topics of our course directly and hands-on by building a web service of a ficticious hospital serving FHIR/JSON of many relevant types of healthcare data.

## Literature

Hands-on: [https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954](https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954)

Recommended Reading: https://link.springer.com/book/10.1007/978-3-030-58721-5

## Goals:

- 1 and 2: Gain the technical basics to provide and retrieve data over computer networks
- 3 and 4: Understand

## Topics:

### 1. Computer Networking, Security, and Identity

- Understand and apply network protocols (TCP, UDP)
- Understand and apply Application protocols (HTTP)
- Gain a basic overview on network and application security (Type Safety, Pen Testing)
- Understand digital identities and authentication

### 2. Storing and accessing data

- What is health data and information?
- Which technologies exist for storing it (File, Database, Graph Database)
- Which technologies (CSV, JSON, ND-JSON, JSON-LD, RDF) and standards exist for making it interoperable (DICOM, FHIR, Snomed, ICD-10, Loinc)
- Which technologies exist for accessing it (SQL, REST APIs, GraphQL, SPARQL)


### 3. Understanding healthcare data

- How are decision and action created in healthcare?
- How is FHIR applied in clinical documents and workflows?
- What are common Ontologies, Terminologies, and Code Sets?


### 4. Designing healthcare data applications

- Cloud Computing and Hybrid Cloud Computing in Healthcare
- Web Application Development
- Big data analytics and processing


## Deliverables

You are required to submit a set of ungraded deliverables during the course of the semester. I will provide feedback as we go. Please complete these deliverables before each session. The first deliverable is required for session 1. So,please work on this before the first class.

- Until Session 1: Develop HTTP client and server: https://beej.us/guide/bgnet0/html/#project-http-client-and-server
- Until Session 3: Develop a better Web Server: https://beej.us/guide/bgnet0/html/#project-a-better-web-server
- Until Session 6: Analyze Network Traffic of your Server: https://www.youtube.com/watch?v=ty8bEFuVM-I
- Until Session 8: Develop a Multiuser (Doctor-Patient) Chat Client and Server: https://beej.us/guide/bgnet0/html/#project-multiuser-chat-client-and-server
- Until Session 10: Allow your users to exchange valid(!) FHIR Data as JSON. Serve the data correctly to all authenticated and authorized users.
- Until Session 13: Allow users to add Imaging and/or Sensor data to your FHIR application using the correct FHIR Resources. Serve the data again to all authenticated and authorized users
- Until Session 15: Make your app deployable to the cloud using Docker and Github Codespaces, Remove as many dependencies as possible.

## Sessions

Health Informatics is the application of digital methods and tools to processes around health and healthcare. This may be within a clinical environment or before that. The reason data  becomes health data is the question we ask to that data or the task we want to automate based on it. Storing and accessing this data and making it useful for healthcare professionals is key.

### 1. Networking Basics and HTTP (Chapter 1-5: https://beej.us/guide/bgnet0/html/#networking-overview)

- Understand the OSI model
- Explain the basic interactions of client-servers on the internet
- Be able to program and reason about HTTP clients and servers

- Reading (HTTP Guide): https://developer.mozilla.org/en-US/docs/Web/HTTP

### 2. IP (Chapter 6-13: https://beej.us/guide/bgnet0/html/#the-internet-protocol-ip)

### 3. TCP and UDP (Chapter 14 - 16: https://beej.us/guide/bgnet0/html/#transmission-control-protocol-tcp)

- Building a Server from Scratch using Sockets API: https://beej.us/guide/bgnet/html/

### 4. IP Subnets, Routing and ARP (Chapter 17 - 23: https://beej.us/guide/bgnet0/html/#ip-subnets-and-subnet-masks)

### 5. Network Security: Packet Tracing, Port Scanning and Firewalls (Chapter 24-30: https://beej.us/guide/bgnet0/html/#network-hardware)

- Further Reading:
    - https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=30673923&query=
    - https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=31009083&query=web%20security

### 6. DNS, NAT, DHCP, Firewalls (Chapter 31-36: https://beej.us/guide/bgnet0/html/#domain-name-system-dns)

- Port Scanning and Packet Tracing: https://www.redhat.com/sysadmin/quick-nmap-inventory

### 7. HTTP Security: Trusting Users and User Data (Chapter 37: https://beej.us/guide/bgnet0/html/#trusting-user-data)

- Reading (HTTP Security, HTTP access control (CORS), HTTP authentication): https://developer.mozilla.org/en-US/docs/Web/HTTP

- Authentication Methods (Basic, Session, Token, JWT, OAuth, SSO): https://testdriven.io/blog/web-authentication-methods/, https://byby.dev/auth-methods
- Further Reading:
    - https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=31071624&query=web%20application%20security
    - https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=30330504&query=
    - https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=7114316&query=authentication


### 8. Health Informatics and Healthcare Data

1. Lecture:  What is Health-care Data, why health informatics?
- History of Health, Healthcare, Biomedical Informatics
- What is health data? How does data become health data, healthcare data, medical data?
- What are current trends and stati in different regions
- Goals: What is this course about: Data Engineering for health systems

2. Hands-on: Technical Framework and Process: Nix, Docker, Postgresql, Rust, Python, Java, Neo4j, RDF
- How to build replicable systems
- How to run and serve microservices
- How to store and server health data
- How to build data intensive applications
- Setting up our Dev Environment
- Building a simple HIS from scratch using FHIR
- Running Synthea
- Using Jupyter Notebooks


### 9. Interoperability: Standardized vocabularies in healthcare

### 10. Document Data: Electronic Health Records (EHR)

### 11. Imaging Data (DICOM, PACS)

### 12. Sensor Data: Deep Dive: Wearable Device Data (Garmin)
  - https://martin-ueding.de/posts/heart-rate-monitor-with-python/

### 13. Data Normalization and Harmonization

### 14. Building and Deploying Systems (Cloud Computing, Dev Ops, Dependency Management)



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
