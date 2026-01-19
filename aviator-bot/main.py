from aviator import bet_manual, bet_auto, cashout, open_history, toggle_auto_cashout
from voice import listen_command
import threading
import re

DEFAULT_BET_VALUES = {1: 5.0, 2: 10.0}
NUM_WORDS = {
    "um": 1, "dois": 2, "três": 3, "tres": 3, "quatro": 4,
    "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10
}

def word_to_number(word):
    return NUM_WORDS.get(word.lower())

def parse_command(text):
    if not text:
        return None
    text = text.lower().strip()

    # HISTÓRICO
    if "histórico" in text or "historico" in text:
        return ("history",)

    # SAQUE
    if re.search(r"\b(sa(c|que|car)|sacar)\b", text):
        nums = re.findall(r"\d+", text)
        if nums:
            return ("cashout", int(nums[0]))
        for word in text.split():
            n = word_to_number(word)
            if n:
                return ("cashout", n)
        return None

    # DESLIGAR SAQUE AUTOMÁTICO
    if re.search(r"\b(remover|desligar|tirar|desativar)\b", text) and \
       re.search(r"\b(saque|auto)\b", text):
        nums = re.findall(r"\d+", text)
        if nums:
            return ("disable_auto_cashout", int(nums[0]))
        for word in text.split():
            n = word_to_number(word)
            if n:
                return ("disable_auto_cashout", n)
        return None

    # APOSTA AUTOMÁTICA
    if ("aposta" in text or "apostar" in text) and "auto" in text:
        nums = re.findall(r"\d+[.,]?\d*", text)
        if len(nums) >= 3:
            bet = int(nums[0])
            value = float(nums[1].replace(",", "."))
            auto = float(nums[2].replace(",", "."))
            return ("bet_auto", bet, value, auto)
        return None

    # APOSTA MANUAL
    if "aposta" in text or "apostar" in text:
        bet_num = None
        nums = re.findall(r"\d+", text)
        if nums:
            bet_num = int(nums[0])
        else:
            for word in text.split():
                n = word_to_number(word)
                if n:
                    bet_num = n
                    break

        # valor em reais (opcional)
        value = None
        match_val = re.search(r"(\d+[.,]?\d*)\s*(reais?|r\$)", text)
        if match_val:
            value = float(match_val.group(1).replace(",", "."))

        if bet_num is not None:
            if value is None:
                return ("bet_manual", bet_num, None, False)
            else:
                return ("bet_manual", bet_num, value, True)

    return None

def execute_command(cmd):
    if not cmd:
        return
    if cmd[0] == "history":
        open_history()
    elif cmd[0] == "bet_manual":
        _, bet, value, use_value = cmd
        bet_manual(bet, value, use_value)
    elif cmd[0] == "bet_auto":
        _, bet, value, auto = cmd
        bet_auto(bet, value, auto)
    elif cmd[0] == "cashout":
        _, bet = cmd
        cashout(bet)
    elif cmd[0] == "disable_auto_cashout":
        _, bet = cmd
        toggle_auto_cashout(bet)

print("\n🎮 AVIATOR BOT ULTRA-RÁPIDO ATIVO\n")
print("📢 EXEMPLOS DE COMANDOS:")
print("aposta 1")
print("aposta 2")
print("apostar no 1")
print("apostar no 2")
print("aposta 1 10 reais")
print("aposta 1 10 auto 2")
print("saque 1")
print("tirar saque automático 1")
print("abrir histórico\n")

try:
    while True:
        spoken = listen_command()
        if not spoken:
            continue
        print(f"🗣️ Você disse: {spoken}")

        cmd = parse_command(spoken)
        if not cmd:
            print("❌ Comando não reconhecido\n")
            continue

        threading.Thread(target=execute_command, args=(cmd,), daemon=True).start()

except KeyboardInterrupt:
    print("\n🛑 Bot finalizado manualmente.")
