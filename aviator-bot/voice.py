# voice.py
import speech_recognition as sr
import time

recognizer = sr.Recognizer()

def listen_command(timeout=2, phrase_time_limit=3):
    """
    Escuta comando de voz.
    Junta fragmentos curtos em uma única frase para não cortar a fala.
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("🎙️ Ouvindo comando...")

        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio, language="pt-BR")
            text = text.lower().strip()
            if text:
                return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            print("❌ Não entendi")
            return None
        except sr.RequestError as e:
            print(f"❌ Erro de serviço: {e}")
            return None
    return None
