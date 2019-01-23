from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('znBpy6a2wyOpkb7wUJWMlzHVQ7hrXnJKufA5UNUWdZg6nJWXae5H+9nJ+lYaCWDDo6wWWDN48iDCPMBkzIBov1hrvlWzNqobTN9WhNvaZJZZTPtSFNGzzHJ2OdT0W82WKU2RucRDJCdHMf/+84f7MwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('87adbedee81e40a4aee8de6609e35b6b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉 ，您說什麼'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
    )

    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

    return

    if msg == ['hi', 'Hi']:
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '您想訂位，是嗎？'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

if __name__ == "__main__":
    app.run()