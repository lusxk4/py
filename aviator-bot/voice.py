import speech_recognition as sr

recognizer = sr.Recognizer()

# Configurações otimizadas para máxima sensibilidade
recognizer.energy_threshold = 300  # MUITO mais sensível (padrão é 4000)
recognizer.dynamic_energy_threshold = True
recognizer.dynamic_energy_adjustment_damping = 0.15
recognizer.dynamic_energy_ratio = 1.5
recognizer.pause_threshold = 0.5  # Menos pausa necessária
recognizer.phrase_threshold = 0.1
recognizer.non_speaking_duration = 0.3

def listen_command():
    """
    Escuta comando de voz e retorna string lowercase.
    Retorna None se não reconheceu.
    """
    with sr.Microphone() as source:
        try:
            # Calibração rápida apenas na primeira vez
            if not hasattr(listen_command, 'calibrated'):
                print("🎤 Calibrando microfone...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                listen_command.calibrated = True
                print("✅ Microfone pronto!\n")
            
            # Escuta com timeout curto
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
            text = recognizer.recognize_google(audio, language="pt-BR")
            return text.lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except Exception:
            return None