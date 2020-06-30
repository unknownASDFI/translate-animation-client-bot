import logging, time, random
from telethon.sync import TelegramClient
from telethon import events
from googletrans import Translator








class Bot:
    api_id = 0 # your api id in
    api_hash = ""    # your api hash
    admin = 0  #chat_id int
    translator =  Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
    




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client = TelegramClient("pro", Bot.api_id, Bot.api_hash)
@client.on(events.NewMessage)
async def main(event):

    user_id = event.from_id
    if(user_id == Bot.admin):
        text = event.raw_text
        if(text in ["ping","Ping"]):
            await client.edit_message(event.chat_id, event.message, "✅PONG✅")
            time.sleep(3)
            await client.delete_messages(event.chat_id, [event.message])
            return
        if(text[0] in ["translate", "ترجمه"]):
            if(len(text) == 1):
                if(event.is_reply):
                    replied = await event.get_reply_message()

                    lang = Bot.translator.detect(replied.raw_text).lang
                    if(lang != "fa"):
                        text = Bot.translator.translate(replied.raw_text, dest = "fa").text
                        await client.edit_message(event.chat_id, event.message, text)
                    else:
                        text = Bot.translator.translate(replied.raw_text, dest = "en").text
                        await client.edit_message(event.chat_id, event.message, text)
                return
            if(len(text) == 3 and text[1] == "to"):
                if(text[1] == "to"):
                    lang = text[2]

                    if(lang not in ["fa","english","persian","en"]):
                        await client.edit_message(event.chat_id, event.message, "❌Language Not Found❌")
                        time.sleep(1.5)
                        await client.delete_messages(event.chat_id, [event.message])
                        return
                    if(event.is_reply):
                        replied = await event.get_reply_message()



                        text = Bot.translator.translate(replied.raw_text, dest = lang).text
                        await client.edit_message(event.chat_id, event.message, text)


                    return
            if(len(text) > 3 and text[1] == "to"):
                text = event.raw_text.split("\n")
                t = text[0].split()
                lang = t[2]

                if(lang not in ["fa","english","persian","en"]):
                    await client.edit_message(event.chat_id, event.message, "❌Language Not Found❌")
                    time.sleep(1.5)
                    await client.delete_messages(event.chat_id, [event.message])
                    return
                message = ""
                for line in text[1:]:
                    message += Bot.translator.translate(line, dest = lang).text + "\n"
                await client.edit_message(event.chat_id, event.message, message)
        elif(text == "translate help"):
            new_text = "Available Languages:\n\nen,fa\n\nhttps://github.com/AliSadafi83/translate-client-bot"
            await client.edit_message(event.chat_id, event.message, new_text)
            return
        else:
            pass
        if(text == "animation help"):
            message = """
            Animations:
            1- Texts:
            type
            normal
            2-Emojis:
            moon
            sky
            time
            earth
            count
            colorheart
            heartbreak
            love
            angry
            sad
            happy
            dumb
            volcano
            city
            3-Bio:

            https://github.com/AliSadafi83/translate-client-bot
            """
            await client.edit_message(event.chat_id, event.message, message)
        test = event.raw_text.split()
        text = event.raw_text.split()
        test = event.raw_text.split()

        text = event.raw_text.split("\n")
        if(text[0] == "type"):

            message = event.message
            mess = ""
            frames = []
            for i in range(1,len(text)):
                for j in range(len(text[i])):
                    mess += text[i][j]
                    if(i == len(text) - 1 and j == len(text[i]) - 1):
                        pess = mess[:]
                    else:

                        tt = random.randint(0,4)
                        if(tt in [1,2,3,4]):

                            pess = mess[:] + "|"
                        else:
                            pess = mess[:]
                    frames += [pess]
                mess += "\n"
            for frame in frames:
                try:
                    await client.edit_message(event.chat_id, message, frame)
                except:
                    pass


                    time.sleep(.125)
        elif(text[0] == "normal"):


            message = event.message
            mess = ""
            for i in range(1,len(text)):
                for j in range(len(text[i])):
                    mess += text[i][j]
                    try:
                        await client.edit_message(event.chat_id, message, mess)
                        time.sleep(.125)
                    except:
                        pass
                mess += "\n"
            t = 0
        elif(test[0] == "sky"):

            gify = "☀️🌤⛅️🌥☁️🌩⛈🌧🌨🌧"

            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.125)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "moon"):

            gify = "🌕🌖🌗🌘🌑🌒🌓🌔🌕"
            message =event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.125)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "time"):

            message = event.message

            gify = "🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧"
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.125)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "earth"):

            gify = "🌎🌍🌏"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.125)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "count"):

            gify = "0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(1)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "colorheart"):

            gify = "❤️🧡💛💚💙💜🖤"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "heartbrake"):

            gify = "❤️💔"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "love"):

            gify = "💕💞💓💗💖💝"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "angry"):

            gify = "😤😠😡🤬"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "sad"):

            gify = "😁😄😃😀🙂🙃😕🙁☹️😔😞😣😖😫😢😭😞"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "happy"):

            gify = "😃😄😁😆😂🤣"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "dumb"):

            gify = "😛😝😜🤪"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "volcano"):

            gify = "⛰🏔🌋"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        elif(test[0] == "city"):

            gify = "🌆🌇🏙🌇🌆🌃"
            message = event.message
            for j in range(int(test[1])):
                for i in gify:
                    try:
                        await client.edit_message(event.chat_id, message, i)
                        time.sleep(.5)
                    except:
                        pass
            await client.delete_messages(event.chat_id, [event.message])
        else:
            pass
client.start()
client.run_until_disconnected()
