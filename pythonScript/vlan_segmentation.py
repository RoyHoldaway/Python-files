# MAC-Based VLAN Segmentation Tool
# Roy Holdaway - Colorado State University Network Engineering Internship
# Automates moving student devices (gaming consoles, etc.) from private to public VLAN
# via Aruba ClearPass by reading their submitted request form and entering the MAC address.
#
# IMPORTANT: Operator must watch the screen at all times.
# Move mouse to top-left corner to stop the script at any point.

import pyautogui
import time

pyautogui.FAILSAFE = True

# Move to top-left to calibrate and signal script has started
pyautogui.moveTo(0, 0)
time.sleep(2)
print("Calibrated. Starting in 3 seconds...")
time.sleep(3)

# --- Replace the coordinates below with your actual screen positions ---
# These are the fields in the student request form and Aruba ClearPass

# TODO: Roy to fill in real x,y coordinates and field order from ClearPass
FIELDS = [
    (000, 000),  # Field 1
    (000, 000),  # Field 2
    (000, 000),  # Field 3
    (000, 000),  # Field 4
    (000, 000),  # Field 5
    (000, 000),  # Field 6
    (000, 000),  # Field 7 (submit)
]

# Copy MAC from student form
pyautogui.click(000, 000)   # TODO: click the MAC field on the request form
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Paste into each ClearPass field
for x, y in FIELDS:
    pyautogui.click(x, y)
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.4)

print("Done.")
