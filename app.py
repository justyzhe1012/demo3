
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
            alt_text='很高興為您服務!',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://img.freepik.com/free-vector/appointment-booking-with-calendar_52683-39831.jpg?w=1060&t=st=1664539536~exp=1664540136~hmac=015fee0ab0290a580f56a56be1d7e67f0da15e64dfae70e3bc8f4aa1ea274503',
                        title='請假區',
                        text='請假/遲到都要填喔',
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
                    CarouselColumn(
                        thumbnail_image_url='https://img.freepik.com/free-vector/teacher-standing-near-blackboard-holding-stick-isolated-flat-vector-illustration-cartoon-woman-character-near-chalkboard-pointing-alphabet_74855-8600.jpg?w=1060&t=st=1664539900~exp=1664540500~hmac=c1268b5956af2a1098b42f7f53b1b32f55b57531c0f810c35068a23ac1b4b3ae',
                        title='補課區',
                        text='開放當週上課影片!',
                        actions=[
                            MessageAction(
                                label='小小提醒',
                                text='影片只會開放到當週週三23:59喔!'
                            ),
                            URIAction(
                                label='點我補課去~',
                                uri='https://youtube.com/playlist?list=PLZ0Kz0tBF3qMJ3WZlHqDQL5lACaC4IH1d'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://img.freepik.com/free-vector/organic-flat-feedback-concept_52683-62653.jpg?w=1060&t=st=1664540164~exp=1664540764~hmac=8f2ca105a46de9edd37ee1a3e872d4a51cc7d45e5a8cf48da6cbe5394d26452d',
                        title='本週回饋單',
                        text='填寫心得!',
                        actions=[
                            MessageAction(
                                label='小小提醒',
                                text='影片只會開放到當週週三23:59喔!'
                            ),
                            URIAction(
                                label='點我填寫!',
                                uri='https://forms.gle/H3mBHxHJ1imk7qtbA'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.6435-9/83154430_3293543733994427_8630956035097493504_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=4reFxnCHK8YAX8Z48Fr&_nc_ht=scontent.ftpe2-2.fna&oh=00_AT-S8oSmVVe8426yrVis__DwFqicVkPbYjYUs2ItAAGymg&oe=635A8B25',
                        title='AC課作業繳交',
                        text='請大家上傳自己的簡報!',
                        actions=[
                            MessageAction(
                                label='小小提醒',
                                text='繳交期限請參考學員手冊!'
                            ),
                            URIAction(
                                label='點我繳交!',
                                uri='https://drive.google.com/drive/folders/1cJaI75juZjzA3eQUzaxgJmXKSPCHF5gX?usp=sharing'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.6435-9/83154430_3293543733994427_8630956035097493504_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=4reFxnCHK8YAX8Z48Fr&_nc_ht=scontent.ftpe2-2.fna&oh=00_AT-S8oSmVVe8426yrVis__DwFqicVkPbYjYUs2ItAAGymg&oe=635A8B25',
                        title='Coaching修改檔作業繳交',
                        text='請大家上傳自己的簡報!',
                        actions=[
                            MessageAction(
                                label='小小提醒',
                                text='繳交期限請參考學員手冊!'
                            ),
                            URIAction(
                                label='點我繳交!',
                                uri='https://drive.google.com/drive/folders/1caa6ALoVrsyWqIFhT-YQ9hzIKobIDfkr?usp=sharing'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    elif re.match('點選下方「填寫表單」即可! 請記得附上相關證明!',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("還有其他問題的話歡迎問我!"))
    elif re.match('影片只會開放到當週週三23:59喔!',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("還有其他問題的話歡迎問我!"))
    elif re.match('繳交期限請參考學員手冊!',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage("還有其他問題的話歡迎問我!"))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage("輸入「stp」才有下一步喔😅"))



 # 主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)