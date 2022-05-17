import pyautogui, time
from faker import Faker
fake = Faker()

#Primer Formulario
pyautogui.click(613,478)      
pyautogui.press('tab')
pyautogui.press('tab')
with open("catchphrase.txt") as f:
    first = f.readlines()[0].rstrip()
pyautogui.typewrite(first)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press(['enter', 'enter'])
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(fake.email())
pyautogui.press('tab')
pyautogui.press('enter')

#Cambio de Formulario
time.sleep(3)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

#Segundo Formulario
pyautogui.click(618,520)      
pyautogui.press('tab')
pyautogui.press('tab')
with open("catchphrase.txt") as f:
    first = f.readlines()[1].rstrip()
pyautogui.typewrite(first)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('down', presses=12)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(fake.email())
pyautogui.press('tab')
pyautogui.press('enter')
