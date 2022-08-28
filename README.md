# Foks

## Description

![Hello Foks](./statics/foks.png)

This project was created to develop a bot using the Discord API in Python. The main purpose of developing this project is to learn methods such as constructors, scraping and scripting in python. Its name is FOKS.

## Table of Content

* [Technologies](#)
* [Prerequisites](#)
* [Setup](#)
* [Available Commands](#available-commands)
  * [Clear](#)
  * [Kick](#)
  * [Ban](#)
  * [Unban](#)
  * [Mute](#)
  * [Status](#)
  * [Load](#)
  * [Unload](#)
  * [Reload](#)
  * [Curr](#)
  * [Rand](#)
* [To Do](#)
* [Project Status](#)
* [Contact](#)
* [Lİcense](#)

## Technologies
Technologies used in the development of this project:
  - python        - v3.9.5
  - discord       - v2.0.0
  - os            
  - math          
  - random
  - dotenv        - v0.20.0
  - forex_python  - v1.8

## Prerequisites

- You have to create a new project through the [Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) and get the API KEY.

- On this portal, you will define your bot and manage various permissions. Then add the bot to the server.

## Setup

Download the Discord library to your local.
```python
pip install discord.py
```

Activate the bot by running bot.py file.
```python
python bot.py
```

Now on discord, you can use commands with the "!" prefix.

## Available Commands

### Clear
  The line number you want to delete should be written with the clear command. If the number of lines is not written, the last line will be deleted by default. This command can be used by admin users. 
  ```cmd
    !clear <line is one by default>
  ```
  For example: Delete the last 5 lines.
  ```cmd
    !clear 5
  ```

### Kick

  Write down the username you want to kick and the reason for kicking. So kick the user from the server. If you don't write the reason for kicking the user, "Pepega" will be assigned by default. This command can be used by admin users. 

  ```cmd
    !kick @<account name> <reason is "Pepega" by default>
  ```

  For example:
  ```cmd
    !kick @TestUser violated community rules
  ```

### Ban

  Its usage is the same as the kick command. Write the command with the name of the user you want to ban and the reason for banning. Thus, the user is completely banned from the server. If you do not write the ban reason of the user, "Pepega" will be assigned by default. This command can be used by admin users. 

  ```cmd
    !ban @<account name> <reason is "Pepega" by default>
  ```

  For example:
  ```cmd
    !ban @TestUser violated community rules
  ```

### Unban

  In order to unban the banned user, the full name of the user must be written with the command. This command can be used by admin users. 

  ```cmd
    !unban @<account name with discriminator(#...)>
  ```

  For example:
  ```cmd
    !unban @TestUser#03014
  ```

### Mute

  If you want to mute the user, you can use this command. You can do this by typing the username along with the command. This command can be used by admin users. 

  ```cmd
    !mute @<account name>
  ```

  For example:
  ```cmd
    !mute @TestUser
  ```

### Status

  If you want to change the activity status in discord, you can use this command. Current activities are game, listening, watching, streaming. Only the streaming activity takes an extra url parameter. All users can use this command.

  ```cmd
    !status <activity> <state>
  ```

  For example:
  ```cmd
    !status game Minecraft

    !status listening Ceza

    !status watching Movie

    !status streaming <url> Come to stream
  ```

### Load

  You can use it whenever you want to organize commands, events and some states in a single class. You can use this command to add a new category.

  ```cmd
    !load <category>
  ```

  For example:
  ```cmd
    !load games
  ```

### Unload

  You can use this command to delete the existing category.

  ```cmd
    !unload <category>
  ```

  For example:
  ```cmd
    !unload games
  ```

### Reload

  It is used to reload the screen after making changes to the schematic screen so that you can see the changes again.

  ```cmd
    !reload <category>
  ```

  For example:
  ```cmd
    !reload games
  ```

### Curr

  It is the command that shows the current dollar or euro rate of the Turkish lira. The information is obtained using [forex-python](https://pypi.org/project/forex-python/).

  ```cmd
    !curr <from-to-currency> <amount is 1 by default>
  ```

  For example: 5 USD how many TRY
  ```cmd
    !curr USD-TRY 5
  ```

### Rand

  You can use it to generate random numbers in the range you specify. With the command, write the number between which numbers you want, leaving a space between them.

  ```cmd
    !rand <minimum> <maximum>
  ```

  For example:
  ```cmd
    !rand 10 100
  ```

## To Do

- Automatic deletion of slang or profanity texts and banning the user.

- Commands such as playing or stopping videos by integrating the Discord API with Youtube.

- Music play, pause, volume up and down commands by integrating Discord API with Spotify.

## Project Status

- Although the project is finished in terms of functionality, it is open to development. I couldn't continue development because the main focus was on other projects.

## Contact

Created by [@Abdullah Böğrek](https://tr.linkedin.com/in/abdullah-s-bogrek) - feel free to contact me!

Mail: asbogrek@gmail.com

## License

This project is open source and available under the [MIT](https://opensource.org/licenses/MIT).