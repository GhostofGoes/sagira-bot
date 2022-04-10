# Sagira
Sagira, yet another Destiny 2 Discord Bot with a focus on statistics and adding cool features that aren't in Charlemagne.

# Requirements
- Python 3.9+
- Pip
- [Poetry](https://python-poetry.org/docs/#installation)
- Docker
- Docker Compose

# Setting up a development environment and running the bot
1. Create a poetry virtual environment and install dependencies
   ```bash
   poetry install
   ```
1. Setup a Discord server for testing (or use dedicated channel on an existing server) and add the bot to it
1. Create a `.env` file in this folder with the bot token. Change debug or command prefix if desired.
    ```
    # Enable debugging
    DEBUG=true

    # These fields come from the Discord application page
    DISCORD_TOKEN="<token>"
    DISCORD_APP_ID="<app-id>"
    DISCORD_PUBLIC_KEY="<public-key>"

    # ID of the Discord server to run bot in
    DISCORD_GUILD_ID="<server-id>"

    # These values come from the bungie.net page for your API application
    BUNGIE_API_KEY="<api-key"
    BUNGIE_OAUTH_CLIENT_ID="<oauth-client-id>"
    BUNGIE_OAUTH_CLIENT_SECRET="<oauth-client-secret>"

    # These can be whatever values you want. Make them relatively strong.
    ELASTIC_PASSWORD="<elastic-password>"
    KIBANA_PASSWORD="<kibana-password>"
    ```

1. Run the bot (NOTE: to test Elasticsearch, bring it up using `docker-compose up -d elasticsearch`)
    ```bash
    poetry run task start
    ```


# Running the bot with Docker
1. Ensure `vm.max_map_count` is set for whatever is running Docker. If you're on Windows, then this is your WSL2 distro. **Once this is configured, close any open terminals and restart the Docker daemon**.
    ```bash
    sudo bash -c "echo 'vm.max_map_count=262144' >> /etc/sysctl.conf"
    sudo sysctl -p
    ```
1. Start the services and bot
    ```bash
    docker-compose up -d
    ```
1. Verify everything is working
    ```bash
    docker-compose logs -f
    ```

# Credits
This bot heavily derives from [Python Discord's](https://github.com/python-discord) projects, including their [bots](https://github.com/python-discord/bot).

# License
MIT license. If you use this code in your projects, we'd appreciate a shoutout!
