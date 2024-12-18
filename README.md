# PsyMeetPy - Psychological Meeting Management System

## Overview
PsyMeetPy is a Python-based system for managing online psychological consultations between clients and psychologists via Zoom platform.

## Classes

### Person (Base Class)
- Base class for both Client and Psychologist
- Attributes:
  - name (private)
- Methods:
  - setname(): Set person's name
  - getname(): Get person's name
  - getFullDetails(): Get formatted person details
  - displayInfo(): Abstract method for displaying information

### Client (Inherits from Person)
- Represents a client in the system
- Additional Attributes:
  - discount (private)
- Methods:
  - getdiscount(): Get client's discount
  - setdiscount(): Set client's discount
  - displayInfo(): Display client information

### Psychologist (Inherits from Person)
- Represents a psychologist in the system
- Additional Attributes:
  - cost (private)
- Methods:
  - getcost(): Get psychologist's consultation cost
  - setcost(): Set consultation cost
  - displayInfo(): Display psychologist information

### Zoom
- Manages Zoom meeting details
- Attributes:
  - URL (private)
  - time (private)
- Methods:
  - geturl(): Get Zoom meeting URL
  - gettime(): Get meeting time
  - settime(): Set meeting time
  - setURL(): Set Zoom URL

### Meeting
- Coordinates meetings between clients and psychologists
- Attributes:
  - client (private)
  - psychologist (private)
  - zoom (private)
- Methods:
  - doMeet(): Execute and display meeting details

## Usage Example
```python
client = Client("client1", 100)
psychologist = Psychologist("psy1", 2000)
zoom = Zoom("Zoom/UjwUdnO", "12/12/2024 11:00 PM")
meet = Meeting(client, psychologist, zoom)
meet.doMeet()
