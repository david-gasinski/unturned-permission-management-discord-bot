# Discord bot for managing permissions in unturned servers

Usage
```
> $perms add [steamid] [permissions]
    You can add multiple permissions to one steamid. 
	Example:  "?perms add 0778312777312736 god demi hecate"
    This will add God, Demi and Hecate to the steamid 0778312777312736.

> $perms remove [steamid] [permissions]
    You can remove multiple permissions from a steamid. 
	Example:  "?perms remove 0778312777312736 god demi hecate"
    This will remove God, Demi, Hecate from the steamid 0778312777312736

> $perms view [steamid]
    Allows you to view the permissions of a given steamid. 
	Example:  "?perms view 0778312777312736"

> $perms check [steamid] [permission]
    Allows you to check if a steamid has a given permission. This only works for one permission at a time. 
	Example:  "?perms check 0778312777312736 hecate"
```


## Installation
1. Clone the repo
```bash
git clone https://github.com/david-gasinski/rocket-permission-management-unturned-discord-bot.git
```

2. Create a virtual python environment
```bash
python3 -m venv venv
```

3. Install dependencies
```bash
pip install flask-restful
pip install python-dotenv
pip install elementpath
pip install -U discord.py

```

## Setup 
1. Fill in the neccessary information in the **.env** file
```.env
#Filepath to the permission.config.xml file
PERMISSIONS=""
# Fiscord bot token
TOKEN=""
# ID of the channel you want to use for permission management. This is for security so commands aren't ran by non moderators.
COMMAND_CHANNEL_ID=
# URL for rocket web permissions
URL=""
# DIR for backup (the one containing the permissions and kits file)
DIR=""
# DIR to backup to 
MOVEDIR=""
# Where to place logs (leave blank for current dir)
LOG_DIR=""
```

## Running the program
1. Run **bot.py** to start the discord bot
```bash
python3 bot.py
```

2. Run **app.py** (in the root dir) to start the XML editing server
```bash
flask run
```

3. Run **./file_serving/app.py** and open it to all non-local IPs (DO NOT RUN THIS ON YOUR HOME PC. ONLY RUN IT ON A DEDICATED SERVER)
```bash
cd ./file_serving
flask run --host=0.0.0.0
```

# License
This software is provided under the MIT License
Copyright 2023 David Gasinski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.