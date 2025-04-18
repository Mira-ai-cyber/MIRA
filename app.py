from flask import Flask
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# LINEアクセストークンとユーザーID
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
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

# 毎朝8時に送信するスケジュール設定
scheduler = BackgroundScheduler()
scheduler.add_job(send_message, 'cron', hour=8, minute=0)  # 毎朝8時に実行
scheduler.start()

@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"

if __name__ == "__main__":
    send_message()  # 
    app.run(host="0.0.0.0", port=10000)
def send_message():
    print("Sending message now...")  # ⭐️関数が呼ばれたチェック
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
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
    print(f"LINE API response: {response.status_code}, {response.text}")  # ⭐️送った結果を出す
