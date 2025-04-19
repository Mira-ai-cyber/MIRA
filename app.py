from flask import Flask, request
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# LINEアクセストークンとユーザーID
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")

# メッセージ送信関数
def send_message(to, text):
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "to": to,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
    print("Send message response:", response.status_code, response.text)

# 毎朝8時に送るリマインダーメッセージ
def scheduled_message():
    send_message(USER_ID, "おはようございます☀️ 今日追加したい予定はありますか？✨")

# スケジューラー設定
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_message, 'cron', hour=8, minute=0)
scheduler.start()

# LINE Webhookエンドポイント
@app.route("/", methods=["POST"])
def webhook():
    body = request.json
    print("Received body:", body)

    events = body.get("events", [])
    for event in events:
        if event.get("type") == "message" and event.get("message", {}).get("type") == "text":
            user_message = event["message"]["text"]
            user_id = event["source"]["userId"]

            # 受け取ったメッセージに返信する
            reply_text = f"メッセージ受け取りました🩷: {user_message}"
            send_message(user_id, reply_text)

    return "OK", 200

# 動作確認用のGETリクエスト（ブラウザアクセス用）
@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"

if __name__ == "__main__":
    print(f"LINE_ACCESS_TOKEN: {LINE_ACCESS_TOKEN}")
    print(f"USER_ID: {USER_ID}")
    app.run(host="0.0.0.0", port=10000)
 flask import Flask, request
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# LINEアクセストークンとユーザーID
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")

# メッセージ送信関数
def send_message(to, text):
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "to": to,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
    print("Send message response:", response.status_code, response.text)

# 毎朝8時に送るリマインダーメッセージ
def scheduled_message():
    send_message(USER_ID, "おはようございます☀️ 今日追加したい予定はありますか？✨")

# スケジューラー設定
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_message, 'cron', hour=8, minute=0)
scheduler.start()

# LINE Webhookエンドポイント
@app.route("/", methods=["POST"])
def webhook():
    body = request.json
    print("Received body:", body)

    events = body.get("events", [])
    for event in events:
        if event.get("type") == "message" and event.get("message", {}).get("type") == "text":
            user_message = event["message"]["text"]
            user_id = event["source"]["userId"]

            # 受け取ったメッセージに返信する
            reply_text = f"メッセージ受け取りました🩷: {user_message}"
            send_message(user_id, reply_text)

    return "OK", 200

# 動作確認用のGETリクエスト（ブラウザアクセス用）
@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"

if __name__ == "__main__":
    print(f"LINE_ACCESS_TOKEN: {LINE_ACCESS_TOKEN}")
    print(f"USER_ID: {USER_ID}")
    app.run(host="0.0.0.0", port=10000)
 flask import Flask, request
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# LINEアクセストークンとユーザーID
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")

# メッセージ送信関数
def send_message(to, text):
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "to": to,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=body)
    print("Send message response:", response.status_code, response.text)

# 毎朝8時に送るリマインダーメッセージ
def scheduled_message():
    send_message(USER_ID, "おはようございます☀️ 今日追加したい予定はありますか？✨")

# スケジューラー設定
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_message, 'cron', hour=8, minute=0)
scheduler.start()

# LINE WebhookエンドポイントとGET確認を統合
@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Hello, world!"
    
    if request.method == "POST":
        body = request.json
        print("Received body:", body)

        events = body.get("events", [])
        for event in events:
            if event.get("type") == "message" and event.get("message", {}).get("type") == "text":
                user_message = event["message"]["text"]
                user_id = event["source"]["userId"]

                # 受け取ったメッセージに返信する
                reply_text = f"メッセージ受け取りました🩷: {user_message}"
                send_message(user_id, reply_text)

        return "OK", 200

if __name__ == "__main__":
    print(f"LINE_ACCESS_TOKEN: {LINE_ACCESS_TOKEN}")
    print(f"USER_ID: {USER_ID}")
    app.run(host="0.0.0.0", port=10000)
 flask import Flask
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# LINEアクセストークンとユーザーID
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
print(f"LINE_ACCESS_TOKEN: {LINE_ACCESS_TOKEN}")
print(f"USER_ID: {USER_ID}")
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
    print(f"LINE_ACCESS_TOKEN: {LINE_ACCESS_TOKEN}")
    print(f"USER_ID: {USER_ID}")
    send_message()  # ⭐️起動時にメッセージ送る！
    app.run(host="0.0.0.0", port=10000)
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
