import pyautogui
import time
import coordinates as c

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.02  # ultra-rápido

def click(pos):
    pyautogui.click(pos)

def clear_and_type(value, pos):
    print(f"  📝 Digitando: {value}")
    pyautogui.click(pos)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(str(value), interval=0.005)  # mais rápido

# ===== HISTÓRICO =====
def open_history():
    print("  📊 Abrindo histórico")
    click(c.OPEN_HISTORY)

# ===== APOSTA MANUAL =====
def bet_manual(bet, value=None, use_value=True):
    print(f"  🎯 bet_manual chamado: bet={bet}, value={value}, use_value={use_value}")
    
    if bet == 1:
        if use_value and value is not None:
            clear_and_type(value, c.BET1_VALUE_INPUT)
        else:
            print(f"  ⚠️ Não alterando valor (use_value={use_value}, value={value})")
        click(c.BET1_BET_BUTTON)
        print("  ✅ Aposta 1 realizada")
        
    elif bet == 2:
        if use_value and value is not None:
            clear_and_type(value, c.BET2_VALUE_INPUT)
        else:
            print(f"  ⚠️ Não alterando valor (use_value={use_value}, value={value})")
        click(c.BET2_BET_BUTTON)
        print("  ✅ Aposta 2 realizada")

# ===== APOSTA AUTOMÁTICA =====
def bet_auto(bet, value, auto_cashout):
    print(f"  🤖 bet_auto chamado: bet={bet}, value={value}, auto_cashout={auto_cashout}")
    
    if bet == 1:
        click(c.BET1_AUTO_TAB)
        time.sleep(0.1)
        click(c.BET1_AUTO_TOGGLE)
        time.sleep(0.1)
        clear_and_type(auto_cashout, c.BET1_AUTO_INPUT)
        time.sleep(0.05)
        clear_and_type(value, c.BET1_VALUE_INPUT)
        time.sleep(0.05)
        click(c.BET1_BET_BUTTON)
        print("  ✅ Aposta automática 1 configurada")
        
    elif bet == 2:
        click(c.BET2_AUTO_TAB)
        time.sleep(0.1)
        click(c.BET2_AUTO_TOGGLE)
        time.sleep(0.1)
        clear_and_type(auto_cashout, c.BET2_AUTO_INPUT)
        time.sleep(0.05)
        clear_and_type(value, c.BET2_VALUE_INPUT)
        time.sleep(0.05)
        click(c.BET2_BET_BUTTON)
        print("  ✅ Aposta automática 2 configurada")

# ===== SAQUE =====
def cashout(bet):
    print(f"  💰 Sacando aposta {bet}")
    if bet == 1:
        click(c.BET1_BET_BUTTON)
    elif bet == 2:
        click(c.BET2_BET_BUTTON)

# ===== DESLIGAR SAQUE AUTOMÁTICO =====
def toggle_auto_cashout(bet):
    print(f"  🔄 Desligando saque automático {bet}")
    if bet == 1:
        click(c.BET1_AUTO_TOGGLE)
    elif bet == 2:
        click(c.BET2_AUTO_TOGGLE)