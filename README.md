# Orbit Discord Bot 🤖

A Python-based Discord bot designed for productivity and fun. Inspired by Indently, FreeCodeCamp, and other open-source community resources.

## 🚀 Features

### Fun & Social
- **!quote**: Get a random inspirational quote (via ZenQuotes API).
- **!affirm**: Receive a positive affirmation.
- **!flip**: Flip a coin to make quick decisions.
- **!insult**: Generate a random "evil" insult for a bit of humor.
- **!hi**: Get a friendly greeting.

### AI-Powered
- **!orbit**: Ask the AI anything! Powered by OpenAI's GPT models (currently configured for `gpt-4.1-nano` style productivity).

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SAMMYShyper/sam_discord_bot.git
   cd sam_discord_bot
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install discord.py python-dotenv openai requests
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory with the following:
   ```env
   SAMSTOKEN = your_discord_bot_token
   GPTKEY = your_openai_api_key
   ```
   *Note: You can change the variable name `SAMSTOKEN` in `Orbit/discord/main.py` if you prefer something more intuitive like `DISCORD_TOKEN`.*

4. **Project Structure**:
   - `Orbit/run.py`: The entry point for the bot.
   - `Orbit/discord/main.py`: Contains the Discord client logic and command handlers.
   - `Orbit/opennai/opennnai.py`: Handles interactions with the OpenAI API.

## 🏃 Running the Bot

To start the bot, run the following command from the root directory:
```bash
python Orbit/run.py
```

## 📝 Commands Summary
Use `!help` in Discord to see the built-in help menu:
- `!quote` — Random quote
- `!affirm` — Positive affirmation
- `!flip` — Coin flip
- `!orbit <query>` — AI productivity assistant
- `!insult` — Random insult

## 🤝 Acknowledgments
- Inspired by Indently and FreeCodeCamp.
- Powered by OpenAI, ZenQuotes, and EvilInsult APIs.

---
*Created by [SAMMYShyper](https://github.com/SAMMYShyper). For feature suggestions or questions, contact @sammyhi.*