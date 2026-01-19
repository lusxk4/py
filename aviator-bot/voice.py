import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def start_listening(callback_function):
    """
    callback_function(text) será chamado sempre que uma frase for reconhecida
    """
    def internal_callback(recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            text = text.lower().strip()
            if text:
                callback_function(text)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"❌ Erro de serviço: {e}")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.1)
    stop_listening = recognizer.listen_in_background(microphone, internal_callback, phrase_time_limit=2)
    return stop_listening
