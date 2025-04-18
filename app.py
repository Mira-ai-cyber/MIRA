from flask import Flask
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# LINEアクセストークン（Renderの環境変数に入れておく）
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
# ユーザーのLINE ID（あとで取得して環境変数に入れる！）
USER_ID = os.getenv("USER_ID")

def send_message():
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": "おはようございます☀️ 今日追加したい予定はありますか？✨"
            }
        ]
    }
    requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)

scheduler = BackgroundScheduler()
scheduler.add_job(send_message, 'cron', hour=8, minute=0)  # 毎朝8時に実行
scheduler.start()

@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()

import os
import requests

def send_message():
    headers = {
        "Authorization": f"Bearer {os.getenv('LINE_ACCESS_TOKEN')}",
        "Content-Type": "application/json"
    }
    body = {
        "to": os.getenv('USER_ID'),  # あとで自分のLINE User IDを設定するよ！
        "messages": [
            {
                "type": "text",
                "text": "おはようございます☀️ 今日追加したい予定はありますか？✨"
            }
        ]
    }
    requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
