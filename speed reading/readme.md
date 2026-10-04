# RSVP Speed Reader

A desktop speed reading app built with Python. It uses RSVP (Rapid Serial Visual Presentation), which flashes one word at a time in a fixed spot so your eyes never have to move across the page. The middle letter of each word is highlighted in red as a focal point.
https://www.taylorfrancis.com/chapters/edit/10.4324/9780429505379-5/rapid-serial-visual-presentation-rsvp-mary-potter
source to the study which inspired this program.

## How it works

- **pypdf** extracts the text from a PDF and splits it into a list of words
- **tkinter** provides the display window
- A timer built on `root.after()` steps through the list one word at a time without freezing the UI

## What I learned

Event-driven GUI programming, why loops block a window's event loop, and how to schedule repeating work with timers.

## Run it

1. Install Python 3.x
2. `pip install pypdf`
3. Run `python speedReading.py`

## Planned features

- File picker
- Adjustable WPM slider
- Start/stop controls

![Demo](demo.gif)