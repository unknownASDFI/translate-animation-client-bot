


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

6-
Now it Need Your phone Number... You Shoud Put it with this Fomat:
```
+Country-Code Phone Number
```
For Example This is For Iranian Users:
```
+989123456789
```
Telegram Will Send You Five-Digits as Code and you should put it...
If you have tow-step-Verfiacation You Should Enter Your Second Password... It wont show you the password in Terminal(or CMD)...

7-
Congratulation! You're Logged in Successfully!


### Connection Test

Send this text as Message in Telegram

```
ping
```
if It get Editted to:
```
pong
```
it shows that you're Connected Successfully!

### Animations Intro

As it Knowned... Animations are frames of actions that build effects or story...

### Text Animations
In Texts We Can Animate Our Text Messages...

Effects:

1-Normal Effect:
you can send Message with this format:
```
normal
this is your
text messages...
it Can be in any formats and contain digits,emojis and etc
and be more than one or tow line
```
Example:
```
normal
Hello
```
the text will be Eddited in This Way:

H    ---    He   ---   Hel   ---   Hell   ---   Hell   ---   Hello

2-Type Effect:
you can send Message with this format:
```
type
this is your
text messages...
it Can be in any formats and contain digits,emojis and etc
and be more than one or tow line
```
Example:
```
type
Hello
```
the text will be Eddited in This Way:

H|    ---    He|   ---   Hel|   ---   Hell|   ---   Hello|   --- Hello 

### Emoji Animations

you can build animations by Emojis:)
you can get animation names by sending thos message:
```
animation help
```
and you can get animation names...
your emoji animation message should be in this format:

```
animation_name counts_of_replay
```
example:

```
moon 10
```

## Version

Version 1.0.1

## Authors

* **Ali Sadafi** - *Initial work* - [GitHUB](https://github.com/alisadafi83)

## Used Libraries
* **Telethon** - *V 1.14.0* - [GitHUB](https://github.com/LonamiWebs/Telethon) - [Documentation](https://docs.telethon.dev/en/latest/)
* **GoogleTrans** - *V 3.0.0* - [Documentation](https://py-googletrans.readthedocs.io/en/latest/)

## Cost


Lets Pray for me and Star the project and follow me instead paying...


