


# Best-Translator-&-Animation-Client-Bot

Send Animation messages and translate texts from other languages via your account in telegram whith telegram client bot.

## Getting Started

(Download or Copy) main.py and save it in a directory... example directory: /path/to/file/main.py

### Prerequisites

You Need to Install python3 + and set your python env-variables...
(if you check the add to path in installation it will be fixed after re-start)

```
Python 3.5 or newer Versions
```

### Installing

Run this Commands Throw CMD(WINDOWS) or Terminal(LINUX):
if your command dont work choose other command...(commands are seprated by or)
(You should be connected to Internet network Connection to download and Install this Packages)

```
pip install asyncio
pip install python-telegram-bot
pip install telethon 
pip install google trans
```
or
```
py -m pip install asyncio
py -m pip install python-telegram-bot
py -m pip install telethon 
py -m pip install google trans
```


### Setup

You should get api from telegram web site by following steps:
1-
Goto https://my.telegram.org/
Login to your Telegram account with the phone number of the developer account to use.
Click under API Development tools.<br/>
A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!
Copy and Save your API-id and API-hash

2-
Now  go to t.me/userinfobot and start the bot...
you'll get a message like this:
```
Id: 401165773
First: ฅli
Lang: en
```
copy you Id Number and save it...

3- We should edit the source code... open the file whithe a text Editor(Recommended to Use ATOM, Pycharm, VSCODE, SUBLIME)
You Can find class Bot in line 13:
```
class Bot:
    api_id = 0 
    api_hash = ""    
    admin = 0  
    translator =  Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
```
change api-id to your saved api-id(integer format)   [got to step 1]
change api-hash to your saved api-hash(string format)   [got to step 1]
change admin to your saved Id from t.me/userinfobot(integer format)    [got to step 2]

Example:
```
class Bot:
    api_id = 122246935
    api_hash = "0efadaw22611667esfsfbbf2b5f65de39e2awb11b" 
    admin = 401165773  
    translator =  Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
```
Now Save the code By Ctrl+S...

4 - Now If you're in Filtered telegram location, you should connect to VPN, DNS to Bypass filtering...

5 - Run this Commands Throw CMD(WINDOWS) or Terminal(LINUX):
if your command dont work choose other command...(commands are seprated by or)
(  /path/to/file/main.py is my example file location... you should put your file location instead  )

```
python /path/to/file/main.py
```
or
```
py /path/to/file/main.py
```
### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Version

Version 1.0.1

## Authors

* **Ali Sadafi** - *Initial work* - [GitHUB](https://github.com/alisadafi83)



## Cost


Lets Pray for me and Star the project and follow me instead paying...


