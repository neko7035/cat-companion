import speech_recognition as sr

WAKE_WORD = "小猫"

def listen_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="zh-CN")
        print("ASR:", text)
        return text
    except:
        return None

def parse_to_event(text):
    if not text or WAKE_WORD not in text:
        return None

    cmd = text.replace(WAKE_WORD, "").strip()

    if "几点" in cmd:
        return ("time", {})
    if "摸" in cmd:
        return ("pet", {})
    if "吃" in cmd:
        return ("feed", {})
    if "玩" in cmd:
        return ("play", {})
    if "状态" in cmd:
        return ("status", {})

    return None