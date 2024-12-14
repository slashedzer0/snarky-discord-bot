# discord-snarky-bot-llama

## Setup and Usage

This guide will walk you through setting up and using the Discord Snarky Bot, powered by Llama-3.1-8B-Instruct. You can run this bot either locally or using GitHub Actions.

### Prerequisites

- Python 3.11 or later
- A Discord bot token
- GitHub Personal Access Token (PAT)
- Azure AI Inference credentials

### Local Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/slashedzer0/discord-snarky-bot-llama.git
    cd discord-snarky-bot-llama
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the bot:**

    Ensure you have the following environment variables set:

    ```sh
    export DISCORD_TOKEN="your_discord_bot_token"
    export TARGET_USER_ID="target_user_id"
    export GH_PAT_TOKEN="your_github_pat_token"
    ```

    Then run:

    ```sh
    python main.py
    ```

### Obtaining Required Secrets

1. **DISCORD_TOKEN:**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and provide a name for your bot.
   - Navigate to the "Bot" section and click on "Add Bot".
   - Copy the "Token". This is your `DISCORD_TOKEN`.

2. **TARGET_USER_ID:**

   - Open Discord and go to "User Settings".
   - Under "Advanced", enable "Developer Mode".
   - Right-click on the target user and select "Copy ID". This is your `TARGET_USER_ID`.

3. **GitHub Personal Access Token (GH_PAT_TOKEN):**

   - Go to [GitHub Settings](https://github.com/settings/tokens).
   - Click on "Generate new token" and check none.
   - Copy the generated token. This is your `GH_PAT_TOKEN`.

### GitHub Actions Setup

1. **Configure Secrets:**

    Go to your repository settings on GitHub and add the following secrets:

    - `DISCORD_TOKEN`
    - `TARGET_USER_ID`
    - `GH_PAT_TOKEN`

2. **Setup GitHub Actions Workflow:**

    The repository already includes a GitHub Actions workflow file [here](https://github.com/slashedzer0/discord-snarky-bot-llama/blob/main/.github/workflows/bot.yml).

### Development Container

The repository includes a development container configuration in `.devcontainer/devcontainer.json` for VS Code. This allows you to work in a consistent environment.

### Additional Configuration

The `.vscode/launch.json` file is configured to help you run and debug the bot using VS Code. Make sure to update the `envFile` path if necessary.

```json
{
    "configurations": [
        {
            "name": "Run Python Sample",
            "program": "${file}",
            "cwd": "${fileDirname}",
            "envFile": "${workspaceFolder}/.env",
            "redirectOutput": false,
            "request": "launch",
            "type": "debugpy"
        }
    ]
}
