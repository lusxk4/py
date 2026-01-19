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

    # ---------- HISTÓRICO ----------
    if "histórico" in text or "historico" in text:
        return ("history",)

    # ---------- DESLIGAR SAQUE AUTOMÁTICO ----------
    # DEVE VIR ANTES DE "SAQUE" para não confundir!
    if ("remover" in text or "desligar" in text or "tirar" in text) and ("auto" in text or "alto" in text or "automático" in text or "automatico" in text):
        # Procura especificamente "aposta X" ou final da frase
        if "aposta 2" in text or text.endswith(" 2") or text.endswith("dois") or " 2 " in text:
            return ("disable_auto_cashout", 2)
        if "aposta 1" in text or text.endswith(" 1") or text.endswith("um") or " 1 " in text:
            return ("disable_auto_cashout", 1)
        # Se não especificou, assume aposta 1
        return ("disable_auto_cashout", 1)

    # ---------- SAQUE ----------
    if "sac" in text or "sacar" in text or "saque" in text or "cash" in text:
        # Procura número da aposta - PRIORIZA 2
        if "2" in text or "dois" in text or " 2" in text:
            return ("cashout", 2)
        if "1" in text or "um" in text or " 1" in text:
            return ("cashout", 1)
        return None

    # ---------- APOSTA ----------
    if "aposta" in text or "apostar" in text:
        # Identifica qual aposta (1 ou 2) - PRIORIZA 2 ANTES DE 1
        bet_num = None
        if "aposta 2" in text or " 2 " in text or text.endswith(" 2") or "dois" in text:
            bet_num = 2
        elif "aposta 1" in text or " 1 " in text or text.endswith(" 1") or "um" in text:
            bet_num = 1
        
        if bet_num is None:
            return None
        
        # Procura TODOS os valores (números que não são 1 ou 2)
        # Regex melhorado para pegar números isolados
        nums = re.findall(r"\b(\d+(?:[.,]\d+)?)\b", text)
        values = []
        for n in nums:
            n_clean = n.replace(",", ".")
            n_float = float(n_clean)
            if n_float not in [1.0, 2.0]:
                values.append(n_float)
        
        # Debug: mostra números encontrados
        if values:
            print(f"  🔢 Números encontrados: {values}")
        
        # Verifica se tem "auto" ou "alto" para aposta automática
        if "auto" in text or "alto" in text:
            if len(values) >= 2:
                # Primeiro valor = aposta, Segundo = auto cashout
                return ("bet_auto", bet_num, values[0], values[1])
            elif len(values) == 1:
                # Só tem um valor = aposta, usa padrão 2.0 para auto
                return ("bet_auto", bet_num, values[0], 2.0)
            else:
                # Sem valores, usa padrões
                return ("bet_auto", bet_num, DEFAULT_BET_VALUES.get(bet_num, 5.0), 2.0)
        
        # Aposta manual
        if len(values) >= 1:
            return ("bet_manual", bet_num, values[0], True)
        else:
            # Sem valor especificado, usa padrão
            return ("bet_manual", bet_num, DEFAULT_BET_VALUES.get(bet_num, 5.0), False)

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
print("✅ 5 reais aposta 1")
print("✅ 5 reais na aposta 2")
print("✅ 10 reais aposta 2 auto 3")
print("✅ aposta 1")
print("✅ aposta 2")
print("✅ sacar 1")
print("✅ tirar saque automático 1")
print("✅ abrir histórico\n")

try:
    while True:
        print("🎤 Ouvindo...", end="\r")  # Indicador visual
        spoken = listen_command()
        if not spoken:
            continue
        
        print(" " * 50, end="\r")  # Limpa linha
        print(f"🗣️  Você disse: {spoken}")

        cmd = parse_command(spoken)
        if not cmd:
            print("❌ Comando não reconhecido\n")
            continue
        
        # Debug detalhado
        if cmd[0] == "bet_manual":
            print(f"✅ Aposta {cmd[1]} | Valor: R$ {cmd[2]:.2f} | Alterar: {cmd[3]}")
        elif cmd[0] == "bet_auto":
            print(f"✅ Aposta AUTO {cmd[1]} | Valor: R$ {cmd[2]:.2f} | Cashout: {cmd[3]:.1f}x")
        elif cmd[0] == "cashout":
            print(f"✅ SAQUE aposta {cmd[1]}")
        elif cmd[0] == "history":
            print(f"✅ Abrir histórico")
        elif cmd[0] == "disable_auto_cashout":
            print(f"✅ Desligar auto cashout {cmd[1]}")
        else:
            print(f"✅ Comando: {cmd}")

        # Executa sem travar o reconhecimento
        threading.Thread(target=execute_command, args=(cmd,), daemon=True).start()

except KeyboardInterrupt:
    print("\n🛑 Bot finalizado manualmente.")