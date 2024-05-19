# Discord Bot for Role Management

This Python script utilizes the `discord` library to create a Discord bot capable of managing roles based on reactions to specific messages. The bot allows users to subscribe and unsubscribe from notifications using reactions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/v1lmok/ReactionBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ReactionBot
   ```

3. Install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the bot, you need to configure the `Consts` class in the source-code files:

- `TOKEN`: Your Discord bot token.
- `ADD_CHANNEL_ID`: The ID of the channel where users can subscribe.
- `REMOVE_CHANNEL_ID`: The ID of the channel where users can unsubscribe.
- `LOGS_CHANNEL_ID`: The ID of the channel where bot logs will be sent.
- `ROLE_ID`: The ID of the role to be assigned/removed.
- `REACTION_ADD`: The emoji reaction for subscribing.
- `REACTION_REMOVE`: The emoji reaction for unsubscribing.

## Usage

Run the bot using the following command:

```bash
python reaction.py
python redirect.py
```

Once the bot is running, users can react to specific messages in the `ADD_CHANNEL_ID` and `REMOVE_CHANNEL_ID` channels to subscribe or unsubscribe from notifications.

## Features

- Automatic role assignment/removal based on reactions.
- Logging of user actions in the specified logs channel.
- Error handling for missing channels or roles.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
