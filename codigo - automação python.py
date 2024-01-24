#passo a passo do projeto

#1-Entrar no sistema da empresa (https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazhwVzlPaHdORWVvSElMRHByTEd6QUFZcmlyQXxBQ3Jtc0tsZl96em4yRHpTWi1pcGJuWFZTZGY2YTN6dWtXU0M3UU9Cc1hMT241ZGxkMlEwQkYxbmVoblZpMnh5NDJkNk5QRFNUNGJqMWNyMkRBbFlONHdkc3BlOFhHc3JyMkN1RFlfekhjMU1jc195YW9OVWlHdw&q=https%3A%2F%2Fdlp.hashtagtreinamentos.com%2Fpython%2Fintensivao%2Flogin&v=A5vqqXR8csk)

# pyautogui - rpa- automação bot
#pip install pyautogui - no terminal

import pyautogui
import time
import pandas

# clicar -> pyautogui.click
#escrever -> pyautogui.write
#presssionar -> pyautogui.
#rolar pag -> pyautogui.scroll
#pyautogui.press("win")- aperta o windows
pyautogui.PAUSE = 1
#aperta o win
pyautogui.press("win")
#digita o nome do progrsama(opera)
pyautogui.write("opera")
#aperta enter 
pyautogui.press("enter")

#digitar link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
#apertar enter 
pyautogui.press("enter")

#espera 3 segundos 
time.sleep(3)

#2-Fazer login

pyautogui.click(x=772, y=399)
pyautogui.write("gabriel.vaz.franco@gmail.com")
pyautogui.click(x=878, y=511)
pyautogui.write("franco032")
pyautogui.click(x=962, y=578)

time.sleep(1)
#3-importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    #4-Cadastrar um produto
    pyautogui.click(x=860, y=279)
    #cod
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write( str (tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write( str (tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write( str (tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
         pyautogui.write(obs)

  

    #enviar produto
    pyautogui.press("enter")
    pyautogui.scroll(500000)




#5-repetir ate acabar a base de dados

