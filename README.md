# Official cumbot for Discord
Bot that fetches videos from Pornhub in Python

## Setup



### Create an app

Go to https://discordapp.com/developers/applications/me and create a new app. On your app detail page, save the Client ID. You will need it later to authorize your bot for your server.

### Create a bot account for your app

After creating app, on the app details page, scroll down to the section named bot, and create a bot user. Save the token, you will need it later to run the bot.

### Authorize the bot for your server

Visit the URL https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot but replace XXXX with your app client ID. Choose the server you want to add it to and select authorize.

### Add your custom bot token
Go to : https://discordapp.com/developers/applications/me

Get your bot token in Settings / Bot and copy it to clipboard

Change config.SUCCBOTTOKEN in succbot.py (line 51) to your bot token
## Usage

### Commands 
```
!search "keyword" : searches keyword in Pornhub and returns the first 5 results
!square 2 : returns number given in parameter squared
!random : returns random sentence
```


## License
MIT license