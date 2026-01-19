import pyautogui
import coordinates as c

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.02  # ultra-rápido

def click(pos):
    pyautogui.click(pos)

def clear_and_type(value, pos):
    pyautogui.click(pos)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(str(value), interval=0.01)

# ===== HISTÓRICO =====
def open_history():
    click(c.OPEN_HISTORY)

# ===== APOSTAS =====
def bet_manual(bet, value=None, use_value=True):
    if bet == 1:
        if use_value and value is not None:
            clear_and_type(value, c.BET1_VALUE_INPUT)
        click(c.BET1_BET_BUTTON)
    elif bet == 2:
        if use_value and value is not None:
            clear_and_type(value, c.BET2_VALUE_INPUT)
        click(c.BET2_BET_BUTTON)

def bet_auto(bet, value, auto_cashout):
    if bet == 1:
        click(c.BET1_AUTO_TAB)
        click(c.BET1_AUTO_TOGGLE)
        clear_and_type(auto_cashout, c.BET1_AUTO_INPUT)
        clear_and_type(value, c.BET1_VALUE_INPUT)
        click(c.BET1_BET_BUTTON)
    elif bet == 2:
        click(c.BET2_AUTO_TAB)
        click(c.BET2_AUTO_TOGGLE)
        clear_and_type(auto_cashout, c.BET2_AUTO_INPUT)
        clear_and_type(value, c.BET2_VALUE_INPUT)
        click(c.BET2_BET_BUTTON)

def cashout(bet):
    if bet == 1:
        click(c.BET1_BET_BUTTON)
    elif bet == 2:
        click(c.BET2_BET_BUTTON)

def toggle_auto_cashout(bet):
    if bet == 1:
        click(c.BET1_AUTO_TOGGLE)
    elif bet == 2:
        click(c.BET2_AUTO_TOGGLE)
