# Elden Ring Item Explorer 🛡️

A fun and lightweight Python GUI app to browse Elden Ring items using the [Elden Ring Fan API](https://eldenring.fanapis.com/). Built with `tkinter` for the interface and `requests` for API access.

## Features
- Grid of buttons for different Elden Ring item categories (e.g., Talismans, Ammos, Armors, etc.)
- Clicking a category fetches data from the Elden Ring API and displays item details
- Modular structure: `eldenring.py` (main GUI) + `eldenringtalismans.py` (API logic)

## Preview
🖼️ *GUI with category buttons and result display area*

> (Optional: You can include a screenshot here if you’d like!)

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/python_projects.git
   cd python_projects/elden_ring

2. Install dependencies:
pip install requests Pillow

3. Run the app:
python eldenringmain.py

Requirements
Python 3.8+

requests

Pillow (used for image handling; could be expanded in future)
