
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
    if re.match('stp' ,message):
        carousel_template_message = TemplateSendMessage(
            alt_text='我是幹部我驕傲!',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.freepik.com/free-vector/young-businesswoman-showing-thumb-up-sign-cartoon-illustration_12898746.htm#query=manager%20cartoon&position=5&from_view=search',
                        title='我是PM!',
                        text='PM雲端連結',
                        actions=[
                            MessageAction(
                                label='累了可以點我',
                                text='送你一句話:「天空其實一直晴朗，只要你別一直盯著烏雲不放!」'
                            ),
                            URIAction(
                                label='連結在這邊',
                                uri='https://drive.google.com/drive/folders/12c89seGYtcDb8mmk6a-6eliXO8hbKFwQ?usp=sharing7'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.freepik.com/free-vector/young-businesswoman-holding-tablet-thumb-up-cartoon-illustration_12898721.htm#query=businesswoman%20cartoon&position=1&from_view=search',
                        title='我是學程部!',
                        text='學程部雲端連結',
                        actions=[
                            MessageAction(
                                label='累了可以點我',
                                text='送你一句話:「只要你願意為自己努力，世界會給你驚喜!」'
                            ),
                            URIAction(
                                label='連結在這邊',
                                uri='https://drive.google.com/drive/folders/1-7rmw-R14mJFdrKnD1dpy_hvtTTGqJbG?usp=sharing'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.freepik.com/free-vector/young-businesswoman-holding-smartphone-show-ok-sign-cartoon-illustration_12898719.htm#query=businesswoman%20cartoon&position=2&from_view=search',
                        title='我是課程部!',
                        text='課程部雲端連結',
                        actions=[
                            MessageAction(
                                label='累了可以點我',
                                text='送你一句話:「生命總有挫折，但那不是盡頭，只是在提醒你該堅持，還是該轉變!」'
                            ),
                            URIAction(
                                label='連結在這邊',
                                uri='https://drive.google.com/drive/folders/1-A3MQVjy4EOxGh4Ikz4hGKuh7zU-ugsE?usp=sharing'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.freepik.com/free-vector/young-businesswoman-holding-tablet-cartoon-illustration_12898722.htm#query=businesswoman%20cartoon&position=11&from_view=search',
                        title='我是品牌部!',
                        text='品牌部雲端連結',
                        actions=[
                            MessageAction(
                                label='累了可以點我',
                                text='送你一句話:「有一種溫柔溫暖的人，即使不知道方法，仍會努力想讓別人幸福!」'
                            ),
                            URIAction(
                                label='連結在這邊',
                                uri='https://drive.google.com/drive/folders/1RJm3tqbAMfLisgeaTq8qoHFVdUU708CR?usp=sharing'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.freepik.com/free-vector/man-relaxing-office-break-from-work_10780108.htm#query=time%20management%20catroon&position=3&from_view=search&track=ais',
                        title='總時程表',
                        text='時間照過來!',
                        actions=[
                            URIAction(
                                label='看時程表!',
                                uri='https://docs.google.com/spreadsheets/d/1KXePCMR5KiKNJe6mzjcFDUih60wwhzm_3v2Ack9YbGU/edit?usp=sharing'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.freepik.com/free-vector/office-table-top-view-business-flat-web-infographic-concept-staff-around-table-report-analytics-working-tablet-laptop-empty-background-brainstorm-report-planning-creative-people-collection_11467584.htm#query=meeting%20cartoon&position=3&from_view=search',
                        title='開會去!',
                        text='來開會囉~',
                        actions=[
                            URIAction(
                                label='連結在這邊',
                                uri='https://meet.google.com/den-yyxq-htq'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    elif re.match('送你一句話:「天空其實一直晴朗，只要你別一直盯著烏雲不放!」',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("加油啦!"))
    elif re.match('送你一句話:「只要你願意為自己努力，世界會給你驚喜!」',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("加油啦!"))
    elif re.match('送你一句話:「生命總有挫折，但那不是盡頭，只是在提醒你該堅持，還是該轉變!」',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("加油啦!"))
    elif re.match('送你一句話:「有一種溫柔溫暖的人，即使不知道方法，仍會努力想讓別人幸福!」送你一句話:「有一種溫柔溫暖的人，即使不知道方法，仍會努力想讓別人幸福!」',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("加油啦!"))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage("有何貴幹呢? 請按1~"))



 # 主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)