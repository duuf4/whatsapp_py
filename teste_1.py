import pywhatkit
import datetime
import time
import pyautogui



telefone = "+5519997754060"
mensagem = "Olá! Teste com tempo correto de espera."
agora = datetime.datetime.now()
agendado = agora + datetime.timedelta(minutes=2)
hora = agendado.hour
minuto = agendado.minute

pywhatkit.sendwhatmsg(
    telefone,
    mensagem,
    hora,
    minuto,
    wait_time=20,
    tab_close=False,
    close_time=5
)

print(f"Mensagem agendada para {hora}:{minuto:02d}. Aguarde o envio...")
time.sleep(10)
pyautogui.press("enviar")
print("Mensagem enviada manualmente com pyautogui.")
