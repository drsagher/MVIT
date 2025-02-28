# Lesson 04 Network System Architectures
Network system architectures define the structure and protocols used for communication between devices in a network. Two of the most widely recognized frameworks are the OSI (Open Systems Interconnection) model and the TCP/IP (Transmission Control Protocol/Internet Protocol) model. These models provide a systematic way to understand how data is transmitted across networks, from physical hardware to application-level interactions.

1. OSI Model
The OSI model is a conceptual framework developed by the International Organization for Standardization (ISO) to standardize network communication. It divides the networking process into seven layers , each with specific functions and responsibilities:

Physical Layer :
Deals with the physical transmission of data over hardware (e.g., cables, switches, and network cards).
Focuses on bit-level transmission, voltage levels, and physical connectors.
Data Link Layer :
Ensures reliable data transfer between two directly connected nodes.
Handles error detection and correction, as well as framing data into packets.
Examples: Ethernet, MAC addresses.
Network Layer :
Responsible for routing data packets across multiple networks.
Determines the best path for data to travel using IP addresses.
Protocols: IPv4, IPv6, ICMP.
Transport Layer :
Ensures end-to-end communication and data integrity.
Breaks data into segments and reassembles them at the destination.
Protocols: TCP (reliable, connection-oriented), UDP (lightweight, connectionless).
Session Layer :
Manages sessions or connections between applications.
Establishes, maintains, and terminates sessions.
Example: Remote Procedure Calls (RPC).
Presentation Layer :
Translates data into a format suitable for the application layer.
Handles encryption, compression, and data formatting.
Example: SSL/TLS for secure communication.
Application Layer :
Provides network services directly to end-users or applications.
Includes protocols like HTTP, FTP, SMTP, and DNS.
The OSI model is primarily a theoretical framework used to understand and troubleshoot network communication.

2. TCP/IP Model
The TCP/IP model is a practical, real-world implementation of network communication protocols. It consists of four layers , which align closely with the OSI model but are more streamlined:

Network Interface Layer :
Combines the Physical and Data Link layers of the OSI model.
Manages hardware addressing (MAC addresses) and physical transmission.
Example: Ethernet, Wi-Fi.
Internet Layer :
Corresponds to the Network layer in the OSI model.
Handles logical addressing (IP addresses) and packet routing.
Protocols: IP, ARP, ICMP.
Transport Layer :
Similar to the Transport layer in the OSI model.
Ensures reliable data delivery and manages flow control.
Protocols: TCP, UDP.
Application Layer :
Combines the Session, Presentation, and Application layers of the OSI model.
Provides high-level protocols for user interaction and application services.
Protocols: HTTP, HTTPS, FTP, SMTP, DNS.
The TCP/IP model is the foundation of modern internet communication and is widely used in practice.


