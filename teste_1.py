import os
import pywhatkit
import datetime
import time
import pyautogui
import spacy



text = input("Digite a mensagem que deseja enviar: ")

def mensagem():
    nlp = spacy.load("pt_core_news_sm")
 
   
    
    doc = nlp(text)

    for entity in doc.ents:
        print(entity.text, entity.label_)

    telefone = "+5519997754060"
    mensagem = doc.text
    print(f"Mensagem a ser enviada: {mensagem}")

    # Horário para envio
    agora = datetime.datetime.now()
    agendado = agora + datetime.timedelta(minutes=2)
    hora = agendado.hour
    minuto = agendado.minute

    # Envio programado
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

mensagem()


