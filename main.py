from flask import Flask, request
from bot_logic import handle_message
import telegram

TOKEN = "7703253666:AAF2hshsoLhUh_YoyQURMoTGVjVXPL4ruYY"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    handle_message(update, bot)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
