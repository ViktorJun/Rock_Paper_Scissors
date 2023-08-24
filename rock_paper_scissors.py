from pyrogram import filters, Client
from pyrogram.errors import MessageEmpty
from time import sleep

api_id = your_api_id
api_hash = "your_api_hash"

app = Client("my_acc", api_id, api_hash)

# rock paper scissors
@app.on_message(filters.command("start rps", prefixes=""))
def start_kmn(_, msg):
    sleep(0.5)
    msg.reply_text('3')
    sleep(0.5)
    msg.reply_text('2')
    sleep(0.5)
    msg.reply_text('1')
    msg.reply_text('First player')
    @app.on_message(
        filters.command(['rock', 'scissors', 'paper'], prefixes="") & filters.me & filters.chat(msg.chat.id))
    def stone(_, msg):
        msg.delete(msg)
        global text, name1
        name1 = msg.from_user.first_name
        text = msg.text.split()
        text = text[0].lower()
        msg.reply_text('Second player')
        @app.on_message(filters.command(['rock', 'scissors', 'paper'], prefixes="") & filters.chat(msg.chat.id))
        def stone1(_, msg):
            msg.delete(msg)
            global text, name1
            name2 = msg.from_user.first_name
            text1 = msg.text.split()
            text1 = text1[0].lower()
            if text == "rock" and text1 == 'scissors':
                msg.reply_text(f'{name1} won')
            elif text == "rock" and text1 == 'paper':
                msg.reply_text(f'{name2} won')
            elif text == "scissors" and text1 == 'rock':
                msg.reply_text(f'{name2} won')
            elif text == "scissors" and text1 == 'paper':
                msg.reply_text(f'{name1} won')
            elif text == "paper" and text1 == 'rock':
                msg.reply_text(f'{name1} won')
            elif text == "paper" and text1 == 'scissors':
                msg.reply_text(f'{name2} won')
            else:
                msg.reply_text('Draw')
            msg.reply_text(f'{name1}: {text}\n{name2}: {text1}')


app.run()