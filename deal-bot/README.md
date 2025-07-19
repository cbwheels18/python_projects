# Deal Bot 🤖

A simple Discord bot that responds to car search queries and provides quick links to KSL car listings.

## Features
- Responds to basic commands like `!hello`, `!car`, and `!ksl`
- Builds KSL car search URLs based on user input
- Two hardcoded example links for specific diesel truck engine sizes (`6.7L` and `5.9L`)

## Commands
- `!hello` — Responds with "Hello"
- `!car` — Returns a car info prompt
- `!ksl` — Sends a direct link to [cars.ksl.com](https://cars.ksl.com)
- `!search <make> <mileage> <price> <transmission> <fuel>` — Builds a search URL

  **Example:**
!search Dodge 100000 20000 Automatic Diesel


## Requirements
- Python 3.8+
- `discord.py`
- `python-dotenv`

## Setup

1. Install dependencies:
 ```bash
 pip install discord.py python-dotenv

2. Create a .env file in the project folder with your bot token:

TOKEN=your_discord_bot_token_here

3. Run the bot:

python deal_bot.py

