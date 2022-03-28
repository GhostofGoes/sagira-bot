# Sagira
Sagira, yet another Destiny 2 Discord Bot with a focus on statistics and adding cool features that aren't in Charlemagne.

# Requirements
- Docker
- Docker Compose
- Python 3.9+
- Pip
- Poetry

# Running the bot with Docker
1. Create a poetry virtual environment and install dependencies
   ```bash
   poetry install
   ```

1. Setup a Discord server for testing (or use dedicated channel on an existing server) and add the bot to it
1. Create a `.env` file in this folder with the bot token. Change debug or command prefix if desired.
    ```
    SAGIRA_TOKEN="<token>"
    SAGIRA_DEBUG=true
    SAGIRA_PREFIX="!"
    ```

1. Start services
    ```bash
    docker-compose up -d db
    # Watch logs and wait for services to finish starting
    docker-compose logs -f --since 1m
    ```

1. Run the bot
    ```bash
    poetry run task start
    ```


# Credits
This bot heavily derives from [Python Discord's](https://github.com/python-discord) projects, including their [bots](https://github.com/python-discord/bot).

# License
MIT license. If you use this code in your projects, we'd appreciate a shoutout!
