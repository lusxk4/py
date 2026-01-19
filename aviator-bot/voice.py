import speech_recognition as sr

recognizer = sr.Recognizer()

# Configurações balanceadas - sensível mas não pega muito ruído
recognizer.energy_threshold = 1000  # Balanceado (padrão é 4000)
recognizer.dynamic_energy_threshold = True
recognizer.dynamic_energy_adjustment_damping = 0.15
recognizer.dynamic_energy_ratio = 1.5
recognizer.pause_threshold = 0.8  # Tempo de pausa
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5

def listen_command():
    """
    Escuta comando de voz e retorna string lowercase.
    Retorna None se não reconheceu.
    """
    with sr.Microphone() as source:
        try:
            # Calibração rápida apenas na primeira vez
            if not hasattr(listen_command, 'calibrated'):
                print("🎤 Calibrando microfone... (fique em silêncio)")
                recognizer.adjust_for_ambient_noise(source, duration=1.5)
                listen_command.calibrated = True
                print(f"✅ Microfone pronto! (threshold: {recognizer.energy_threshold})\n")
            
            # Escuta sem timeout (fica esperando você falar)
            audio = recognizer.listen(source, phrase_time_limit=5)
            text = recognizer.recognize_google(audio, language="pt-BR")
            return text.lower()
        except sr.UnknownValueError:
            # Não entendeu o que foi dito
            return None
        except Exception as e:
            # Outro erro
            return None