# Aruba ClearPass VLAN Automation

A lightweight Python mouse automation script built during a Network Engineering Internship at Colorado State University — Housing & Dining Services.

## The Problem

Students living in CSU residence halls regularly submitted IT tickets requesting their devices (gaming consoles, smart TVs, etc.) be moved from the private dorm VLAN to the public VLAN so they could access features like online multiplayer. Each ticket required manually opening the student's request form, copying their MAC address, and entering it across 6–7 fields in the Aruba ClearPass web interface.

With a high volume of these tickets, the process was repetitive and time-consuming especially seasonally during move in week — a good candidate for automation.

## The Solution

A simple `pyautogui` script that:

1. Moves the mouse to the top-left corner to calibrate and signal it's running
2. Clicks into the MAC address field on the student's submitted request form and copies it
3. Navigates to the Aruba ClearPass interface and pastes the MAC into each required field
4. Submits the configuration, moving the device to the public VLAN

## Results

- Closed **200+ service tickets** in under one year
- Script remained in **active production** at CSU after the internship ended

## Design Decision

The reason the script was written as a very bare bones mouse moving script is because due to a security concern about having the script running unsupervised and with full access to the schools private ticketing system, we as a networking operations center (NOC) wanted to ensure my script could not be abused by a resident trying to gain access to something malicious.
The solution I found was mouse movement functions allowing me to have a fail safe to always interfere in case there was anything that raised concerns about the ticket. This 

## Usage

> **Note:** Coordinates are specific to the machine and screen resolution this was built on. If running on a new machine, you will need to update the x,y values in the script to match your screen layout.

```bash
pip install pyautogui
python vlan_segmentation.py
```

## Requirements

- Python 3.x
- pyautogui
