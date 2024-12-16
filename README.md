# 🤖 snarky-discord-bot

## 🚀 Setup and Usage

This guide will walk you through setting up and using the Snarky Discord Bot, powered by Llama-3.1-8B-Instruct. You can run this bot locally, in GitHub Codespaces, or using GitHub Actions.

### 📋 Prerequisites

- Python 3.11 or later
- A Discord bot token
- GitHub Personal Access Token (PAT)
- Azure AI Inference credentials

### 🔑 Obtaining Required Secrets

1. **DISCORD_TOKEN:**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and provide a name for your bot.
   - Navigate to the "Bot" section and click on "Add Bot".
   - Copy the "Token". This is your `DISCORD_TOKEN`.

2. **TARGET_USER_ID:**

   - Open Discord and go to "User Settings".
   - Under "Advanced", enable "Developer Mode".
   - Right-click on the target user and select "Copy ID". This is your `TARGET_USER_ID`.

3. **GH_PAT_TOKEN:**

   - Go to [GitHub Settings](https://github.com/settings/tokens).
   - Click on "Generate new token (classic)" and check none.
   - Copy the generated token. This is your `GH_PAT_TOKEN`.

### 💻 Local Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/slashedzer0/snarky-discord-bot.git
    cd snarky-discord-bot
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

### 🌐 GitHub Codespaces Setup

1. **Create a Codespace:**

    - Navigate to this repository homepage.
    - Click the "Code" button and select "Create codespace on main".

2. **Configure Environment Variables:**

    - In the Codespace, create a `.env` file in the root directory.
    - Add your environment variables to the `.env` file:

      ```env
      DISCORD_TOKEN=your_discord_bot_token
      TARGET_USER_ID=target_user_id
      GH_PAT_TOKEN=your_github_pat_token
      ```

3. **Run the Bot:**

    - Open a terminal in the Codespace.
    - Run the bot:

      ```sh
      python main.py
      ```

### ⚙️ GitHub Actions Setup

1. **Configure Secrets:**

    Go to your repository settings on GitHub and add the following secrets:

    - `DISCORD_TOKEN`
    - `TARGET_USER_ID`
    - `GH_PAT_TOKEN`

2. **Setup GitHub Actions Workflow:**

    The repository includes a GitHub Actions workflow file [here](https://github.com/slashedzer0/snarky-discord-bot/blob/main/.github/workflows/bot.yml). You can adjust it to your liking.

### 🐳 Development Container

The repository includes a development container configuration in `.devcontainer/devcontainer.json` for VS Code and GitHub Codespaces. This allows you to work in a consistent environment.

### ⚡ Additional Configuration

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
```
