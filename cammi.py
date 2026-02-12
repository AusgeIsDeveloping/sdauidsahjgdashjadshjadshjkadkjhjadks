import cv2
import requests
import traceback

# >>> HIER DEIN DISCORD WEBHOOK EINTRAGEN <<<
WEBHOOK_URL = "https://discord.com/api/webhooks/1469709535022420152/Fvmuq_82nWlMjj_KSV7mf-QnucQX7JyagCncSNPRnO56_-ywOdwI3hO7YcXJ7rTtapya"

def send_to_discord(message):
    data = {
        "content": message
    }
    requests.post(WEBHOOK_URL, json=data)

def check_cameras(max_devices=10):
    working_cameras = []

    for index in range(max_devices):
        cap = cv2.VideoCapture(index)
        if cap is not None and cap.isOpened():
            working_cameras.append(f"Kamera Index {index} funktioniert")
            cap.release()

    return working_cameras

try:
    cams = check_cameras()

    if cams:
        message = "**Funktionierende Kameras:**\n" + "\n".join(cams)
    else:
        message = "Keine funktionierenden Kameras gefunden."

    send_to_discord(message)

except Exception as e:
    error_message = f"❌ Fehler beim Prüfen der Kameras:\n```\n{traceback.format_exc()}\n```"
    send_to_discord(error_message)
