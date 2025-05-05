# Foundations of Health Informatics - Networking and Data Exchange in Healthcare


## Course Project: [FHIRedit](TBD)

In our course project we will build an interactive web application for collaborating on healthcare data between doctors and patients. We will (step-by-step) extend our Text Editor (https://github.com/dominikb1888/rim) and apply our knowledge on Networking, Healthcare Data and Security.

## Literature

- Networking: [https://beej.us/guide/bgnet0/html/](https://beej.us/guide/bgnet0/html/)
- Healthcare Data: [https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954](https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6272954)
- Security: [https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=7114316](https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=7114316)

## Online Course Materials (Cisco Networking Basics)

- https://skillsforall.com/course/networking-basics?courseLang=en-US


Recommended Reading: https://link.springer.com/book/10.1007/978-3-030-58721-5

## Goals:

- Networking: Gain the technical basics to provide and retrieve data over computer networks
- Interoperability: Understand healthcare data and exchange formats
- Security: Understand basic pitfalls of security in web applications

## Objectives and Topics:

### 1.Networking: Computer Networking, Security, and Identity

- Understand and apply network protocols (TCP, UDP)
- Understand and apply Application protocols (HTTP)
- Gain a basic overview on network and application security (Type Safety, Pen-Testing)
- Understand digital identities and authentication

### 2. Interoperability: Understanding, Storing and accessing healthcare data

- Which technologies exist for storing it (File, Database, Graph Database)
- Which technologies (CSV, JSON, ND-JSON, JSON-LD, RDF) and standards exist for making it interoperable (DICOM, FHIR, Snomed, ICD-10, Loinc)
- Which technologies exist for accessing it (SQL, REST APIs, GraphQL, SPARQL)
- How is FHIR applied in clinical documents and workflows?

### 3. Security: Designing a secure healthcare application back-end

- Cloud Computing and Hybrid Cloud Computing in Healthcare
- Web Application Development (back-end)
- Basics of Web Application Security and Pen-Testing


## Deliverables

You are required to submit a set of ungraded deliverables during the course of the semester. I will provide feedback as we go. Please complete these deliverables before each session. The first deliverable is required for session 1. So,please work on this before the first class.

- Until Session 1: Create a virtual machine with KALI Linux (https://www.kali.org/) and get comfortable
- Until Session 1: Develop HTTP client and server: https://beej.us/guide/bgnet0/html/#project-http-client-and-server

- Until Session 3: Develop a better Web Server: https://beej.us/guide/bgnet0/html/#project-a-better-web-server
- Until Session 6: Validating a TCP Packet: https://beej.us/guide/bgnet0/html/#transmission-control-protocol-tcp
- Until Session 8: Develop a multi-user (Doctor-Patient) Chat Client and Server: https://beej.us/guide/bgnet0/html/#project-multiuser-chat-client-and-server
- Until Session 10: Allow your users to exchange valid(!) FHIR Data as JSON. Serve the data correctly to all authenticated and authorized users.
- Until Session 13: Allow users to add Imaging and/or Sensor data to your FHIR application using the correct FHIR Resources. Serve the data again to all authenticated and authorized users.
- Until Session 15: Make your app deployable to the cloud using Docker and Github Codespaces, Remove as many dependencies as possible. Show a simple pen-testing strategy.


## Sessions

Health Informatics is the application of digital methods and tools to processes around health and healthcare. This may be within a clinical environment or before that. The reason data  becomes health data is the question we ask to that data or the task we want to automate based on it. Storing and accessing this data and making it useful for healthcare professionals is key.

Structure:

- Presentations (You Show, I feedback): Demonstration of Deliverables (30 min)
- Lecture (I Show, You question): Networking, Health Data or Security Topic (60-90min)
- Exercise (You do, I support): Applied networking, healthcare data and security (60-90min)


### 1. Networking Basics and HTTP

Lecture (Chapter 1-5: https://beej.us/guide/bgnet0/html/#networking-overview, Chapter 2: https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=60):
- Understand the OSI model
- Explain the basic interactions of client-servers on the internet
- Understand the Sockets API and its implementation different programming languages
- Be able to program and reason about HTTP clients and servers

Exercise (Chapter 4: https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=138):
- Overview on Network Analysis and Security Tools (Kali Linux, Burp, Wirshark, nmap)
- Starting the Knowledge Check on Networking (https://skillsforall.com/course/networking-basics?courseLang=en-US)

Recommended Reading:
- Reading (HTTP Guide): https://developer.mozilla.org/en-US/docs/Web/HTTP


### 2. IP

Lecture (Chapter 6-13: https://beej.us/guide/bgnet0/html/#the-internet-protocol-ip):
- Know and understand the difference between different protocols (IPv4, IPv6, ICMP, IPSec)
- Understand dynamic and static addresses as well as subnets in bother IPv4, IPv6
- Understand and apply Endianness
- Understanding packets and their parsing

Exercise ([Chapter 5 + 8](https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=246)):
- Finding Protocol Vulnerabilities
- Network Traffic Analysis
- Hacker 101 CTF |  Micro CMS: https://ctf.hacker101.com/ctf/start/2 (Sign-in via https://ctf.hacker101.com/ctf)


### 3. TCP and UDP

Lecture (Chapter 14 - 16: https://beej.us/guide/bgnet0/html/#transmission-control-protocol-tcp):
- Building a Server from Scratch using Sockets API: https://beej.us/guide/bgnet/html/
- Validating a TCP Packet

Exercise (Chapter 10b: https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=328):
- Layer 4 TCP and UDP Attacks
- TCP Sequence Attacks
- Session Hijacking

Readings:
- https://inc0x0.com/tcp-ip-packets-introduction/
- https://medium.com/@sarunyouwhangbunyapirat/packet-manipulation-with-netcat-and-scapy-9403ebaa82de


### 4. IP Subnets, IP Routing and ARP

Lecture (Chapter 17 - 23: https://beej.us/guide/bgnet0/html/#ip-subnets-and-subnet-masks):
- Understand subnet masks
- Understand routing tables and algorithms
- Computing and finding subnets
- Know what the Link Layer
- Understand IP to MAC address resolution (ARP)

Exercise (Chapter 12: https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=386)
- Implement Dijkstra's Algorithm in Python
- Sniffing ARP Packets with Wireshark
- Creating ICMP Packets: https://inc0x0.com/icmp-ip-packets-ping-manually-create-and-send-icmp-ip-packets/

### 5. Network Security: Packet Tracing, Port Scanning and Firewalls

Lecture (Chapter 24-30: https://beej.us/guide/bgnet0/html/#network-hardware):
- Know and understand common network hardware components and metrics
- Building and analysing small computer networks
- Understanding virtual networks components in cloud environments
- Understand and use the Select Function from Sockets API

Exercise ():
- Creating a network of microservices for scalable web applications (DB, API, Load Balancer, Reverse Proxy)


### 6. DNS, NAT, DHCP, Firewalls

Lecture (Chapter 31-36: https://beej.us/guide/bgnet0/html/#domain-name-system-dns):
- Programming Network Components
- Cloud, Virtualization and Network Components

Exercise (Chapter 8: https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=246):
- Network Traffic Analysis
- Eavesdropping
- Port Scanning and Packet Tracing: https://www.redhat.com/sysadmin/quick-nmap-inventory




### 7. Health Informatics and Healthcare Data

1. Lecture:  What is Health-care Data, why health informatics?

2. Hands-on: Technical Framework and Process: Nix, Docker, Postgresql, Rust, Python, Java, Neo4j, RDF
- Setting up our Dev Environment
- Running Synthea to create FHIR Bundles
- Using Jupyter Notebooks


Additional Reading:
- Encryption Methods
- HTTP Security, HTTP access control (CORS), HTTP authentication: https://developer.mozilla.org/en-US/docs/Web/HTTP):
- Authentication Methods (Basic, Session, Token, JWT, OAuth, SSO): https://testdriven.io/blog/web-authentication-methods/, https://byby.dev/auth-methods)

Exercise:
- https://ebookcentral.proquest.com/lib/th-deggendorf/reader.action?docID=7114316&ppg=446


### 8. Interoperability: Standardized Vocabularies in Healthcare

Lecture:

- HL 7
- Snomed, ICD
- HL7 FHIR

Hands-on:

- Validating HL7 and HL7 FHIR


### 9. Interoperability: Profiling

Lecture:
- FHIR Profiles: https://www.devdays.com/wp-content/uploads/2021/12/DD21US_20210608_Mirjam_Baltus_Introduction_to_Profiling.pdf


Resources:
- FHIR Packages: https://registry.fhir.org/learn
- FHIR Registry: https://www.fhir.org/guides/registry/
- https://simplifier.net/

Hands-on:
- Extending our Chat Application with Validation of FHIR resources
- Adding Heart Rate Data (https://build.fhir.org/observation-example-heart-rate.html)

- Conceptualizing additional Context with FHIR Profiles

Reading:
- https://www.health-samurai.io/articles/aidbox-for-wearable-and-medical-devices


### 10. Imaging Data (DICOM, PACS)

Lecture:
- PACS,
- Imaging and Imaging Data

Hands-on:
- Analysing DICOM Data


### 11. Sensor Data: Deep Dive

Lecture:
- Introduction to Signals and Signal Processing: https://jackschaedler.github.io/circles-sines-signals/index.html

Hands-on:
- Capturing and Filtering Sound Signals with Python and Matplotlib
- ECG vs. PPG: https://www.ti.com/video/5423211783001#:~:text=First%20of%20all%2C%20ECG%20is,determine%20a%20patient's%20heart%20rate.
- PPG Signals: https://github.com/paulvangentcom/heartrate_analysis_python/blob/master/examples/1_regular_PPG/Analysing_a_PPG_signal.ipynb\
- Smartwatch Data: https://github.com/paulvangent:qcom/heartrate_analysis_python/tree/master/examples/3_smartwatch_data
- HRV: https://github.com/stetelepta/exploring-heart-rate-variability/

Further Reading:
- https://hackaday.com/2020/09/03/choosing-the-optimal-sampling-rate-for-your-diy-heart-rate-monitor/
- https://iopscience.iop.org/article/10.1088/1361-6579/aa5efa
- https://www.sciencedirect.com/science/article/pii/S1746809421001865
- https://dl.acm.org/doi/10.1145/3266157.3266209

Poincare Diagrams:
- https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=2391&context=elektrik
- https://xn--hrv-herzratenvariabilitt-dcc.de/2017/07/berechnung-des-poincare-diagramms-aus-rr-intervallen/
- https://hrvhealth.org/blog/?p=124
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8533203/
- https://www.sciencedirect.com/science/article/abs/pii/S0010482519301246
- https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-016-0252-0

### 12. Data Normalization and Harmonization

Lecture:
- What is data quality in wearable devices?
-

Hands-on:


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
