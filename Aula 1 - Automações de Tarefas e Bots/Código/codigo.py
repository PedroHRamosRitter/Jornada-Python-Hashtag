# bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time


#pyautogui.click -> Click do mouse
#pyautogui.write -> Escrever texto
#pyautogui.press -> Pressionar somente uma tecla
#pyautogui.hotkey -> Pressionar um atalho como por exemplo crtl + c

pyautogui.PAUSE = 0.7
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "pythonimpressionador@gmail.com"
senha = "escolha sua senha"

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
#abriria o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3) # pyautogui hashtag

# Passo 2: Fazeer login
# clicar no campo de email
pyautogui.click(x=716, y=374)
pyautogui.write(email)
pyautogui.press("tab") # passar para o outro campo
pyautogui.write(senha)
pyautogui.click(x=939, y=533)
# outra alternativa
#pyautogui.press("tab") # passar para o botão
#pyautogui.press("enter")
time.sleep(2)

# Passo 3: Abrir base de dados (importar o arquivo)
#pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=700, y=259)
    # Código do produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo

    # Marca do produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo do produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write("tipo")
    pyautogui.press("tab")

    # Categoria do produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço unitário do produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #Custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # Botão enviar formulário do produto cadastrado
    pyautogui.press("tab")
    pyautogui.press("enter") # clicou no enviar
    #pyautogui.click(x=869, y=921)
    # voltar para inicio da tela
    pyautogui.scroll(5000)


# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# NaN = Not a Number = Valor Vazio

