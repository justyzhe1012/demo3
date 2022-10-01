
 # 載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)
 # 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Lz3DQQxDHAndFnJJdQko+TlzV2ylapoCUgp12mtaCeRlTfJieBKwUEl57v3E5ZTVnCiVxs/HWhqk7t8SDG1q+giRdcul9RBeN2AutidC2j0gbOSnNtR2H3b2EcQWXjy2LZWYz7p0SoLlEFHNLz11egdB04t89/1O/w1cDnyilFU=')
 # 必須放上自己的Channel Secret
handler = WebhookHandler('1994241049acb267fc341cbbadefdbca')
line_bot_api.push_message('Ub08a25b46cc48ec5f4be8ef499820a4f', TextSendMessage(text='打入「1」開始'))

 # 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
     # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 # get request body as text body = request.get_data(as_text=True) app.logger.info("Request body: " + body) # handle webhook body try:     handler.handle(body, signature) except InvalidSignatureError:     abort(400) return 'OK'
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


 # get request body as text body = request.get_data(as_text=True) app.logger.info("Request body: " + body) # handle webhook body try:     handler.handle(body, signature) except InvalidSignatureError:     abort(400) return 'OK'
 # 訊息傳遞區塊
 # 基本上程式編輯都在這個function
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('1',message):
        image_carousel_template_message = TemplateSendMessage(
            alt_text='我是幹部我驕傲',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/wpM584d.jpg',
                        actions=[
                            MessageAction(
                                label='小小提醒',
                                text='點選下方「填寫表單」即可! 請記得附上相關證明!'
                            ),
                            URIAction(
                                label='點我填寫!',
                                uri='https://forms.gle/nEZBdNT3p1QYXZdE7'
                            )
                        ]
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/W7nI6fg.jpg',
                        action=PostbackAction(
                            label='LineBot聊天機器人',
                            display_text='台灣最廣泛使用的通訊軟體',
                            data='action=興趣不能當飯吃，但總比吃飯當興趣好'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))


 # 主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)