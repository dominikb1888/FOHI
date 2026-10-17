# Foundations of Health Informatics - Networking and Data Exchange in Healthcare

In our course project we will explore the basics of computer network with a focus on applications in healthcare.

## Required Reading

- [Computer Networking a Top-Down Approach](https://ebookcentral.proquest.com/lib/th-deggendorf/detail.action?docID=6644664)
- Additional Resources: https://gaia.cs.umass.edu/kurose_ross/online_lectures.htm


## Online Exercise Materials (Cisco Networking Basics)

- Networking Basics: https://skillsforall.com/course/networking-basics?courseLang=en-US
- Cisco Packet Tracer: https://www.netacad.com/resources/lab-downloads?courseLang=en-US


## Goals:

- Networking: Gain the technical basics to provide and retrieve data over computer networks
- Interoperability: Understand healthcare data and exchange formats
- Security: Understand basic pitfalls of security in web applications

## Objectives:

- Understand and apply network protocols (TCP, UDP)
- Understand and apply Application protocols (HTTP)
- Apply Wireshark for basic network and packet analysis
- Gain a basic overview on network and application security (Type Safety, Pen-Testing)
- Write network focused programs in Rust

## Deliverables

You are required to submit a set of ungraded deliverables during the course of the semester. I will provide feedback as we go. Please complete these deliverables before each session.

Until Session...

- 02 - [Simple Socket Server](Deliverables/2_simple_socket_server.md)
- 04 - [Web Server](Deliverables/4_WebServer.md)
- 06 - [UDP Pinger](Deliverables/6_UDP_Pinger)
- 08 - [HTTP Web Proxy](Deliverables/8_Web_Proxy.md)
- 10 - [ICMP Pinger](Deliverables/10_ICMP_ping.md)
- 12 - [Traceroute](Deliverables/12_Traceroute.md)
- 14 - [Video Streaming](Deliverables/14_VideoStreaming.md)

## Sessions

Health Informatics is the application of digital methods and tools to processes around health and healthcare. This may be within a clinical environment or before that. The reason data  becomes health data is the question we ask to that data or the task we want to automate based on it. Storing and accessing this data and making it useful for healthcare professionals is key.

Structure:
- Lecture (I Show, You question): Networking, Health Data or Security Topic (60 min)
- Interactive Networking Lab (You do, I support): Applied networking, healthcare data and security (30 min)

### 1. Introduction - Computer Networks and the Internet

Content:
- Course Introduction
- Networks and Internet
- Network Core
- Protocols and OSI Model
- Current Topics in Digital Health

Reading:
- Chapter 1: Computer Networks and the Internet, pp. 31-108
- Network Hardware: https://beej.us/guide/bgnet0/html/split/network-hardware.html

Lab:
- Direct Connection: https://beej.us/guide/bgnet0/html/split/project-packet-tracer-connect-two-computers.html#project-packet-tracer-connect-two-computers
- Switch: https://beej.us/guide/bgnet0/html/split/project-packet-tracer-using-a-switch.html
-= Router: https://beej.us/guide/bgnet0/html/split/project-packet-tracer-using-a-router.html

Deliverable:
- Network Knowledge Check-up

### 2. The Application Layer (2 Sessions)

Content:
- Application Layer Principles
- Protocols (HTTP, SMTP, DNS)
- P2P and Streaming

Reading:
- Chapter 2: Application Layer, pp. 111-208

Labs:
- Intro
- HTTP
- DNS

Deliverable:
- Socket Programming



### 3. The Transport Layer (2 Sessison)

Content:
- UDP
- Principles of Reliable Data Transfer
- TCP
- Congestion Control Mechanisms

Reading:
- Chapter 3: Transport Layer, pp. 211-331

Labs:
- TCP
- UDP

Deliverable:
- Web Server

### 4. The Network Layer: Data Plane (2 Sessions)

Content:
- Network Layer Overview
- Routers
- IPv4 and IPv6
- Forwarding, SDN, Middleboxes

Reading:
- Chapter 4: Network Layer: Data Plane, pp. 333-405

Labs:
- IP

Deliverable:

### 5. The Network Layer: Control Plane (2 Sessions)

Content:
- Routing
- SDN
- ICMP
- SNMP

Reading:
- Chapter 5: Network Layer: Control Plane, pp. 407-476

Labs:
- NAT

### 6. The Data Link Layer (2 Sessions)

Content:
- Introduction
- Link Layer
- Multi-Acces Links
- Switched LANs
- Link Virtualization
- Data Center Networking

Reading:
- Chapter 6: The Link Layer and LANs, pp. 479-558

Labs:
- DHCP
- Ethernet & ARP

### 7. Wireless and Mobile Networks (2 Sessions)

Content:
- Wifi
- Cellular Networks
- Mobility Management: Principles & Practice

Reading:
- Chapter 7: Wireless and Mobile Networks, pp. 561-633


Labs:
- WiFi

### 8. Security in Computer Networks (optional)
