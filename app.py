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
import re  # ファイル上に1回だけ追加！

@app.route("/", methods=["POST"])
def webhook():
    body = request.json
    print("Received body:", body)

    events = body.get("events", [])
    for event in events:
        if event.get("type") == "message" and event.get("message", {}).get("type") == "text":
            user_message = event["message"]["text"]
            user_id = event["source"]["userId"]

            # スケジュールっぽいメッセージか確認してパース
            match = re.search(r"(\\d{1,2})時.*?(.*)", user_message)
            if match:
                hour = int(match.group(1))
                task = match.group(2).strip()

                # スケジューラーにリマインダーを登録
                scheduler.add_job(
                    send_message,
                    'cron',
                    args=[user_id, f"🔔リマインダー: {task} の時間です！"],
                    hour=hour,
                    minute=0
                )
                send_message(user_id, f"✅ {hour}時に「{task}」のリマインダーを登録しました！")
            else:
                # 通常返信
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
