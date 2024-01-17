import pyautogui as py
import time
import pandas as pd

py.PAUSE = 2

# ABRIR O CHROME
py.press('win')
py.write('chrome')
py.press('enter')
time.sleep(10)


# ENTRAR NO SITE
py.click(x=681, y=432)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
py.write(link)
py.press('enter')
time.sleep(10)


# FAZER LOGIN
py.press('tab')
py.write('pietro.rosolia.2704@gmail.com')
py.press('tab')
py.write('Rosolia2704')
py.press('enter')
time.sleep(10)


# LER TABELA PRODUTOS
arquivo = 'C:\\Users\\Pietro Rosolia\\Desktop\\VScode\\Cursos\\PYTHON\\Jornada_HashTag\\PowerUp\\produtos.csv'
tabela = pd.read_csv(arquivo)


# FAZER O CADASTRO DOS PRODUTOS
for linha in tabela.index:
  
  py.click(x=428, y=291)
  py.write(str(tabela['codigo'].iloc[linha]))
  py.press('tab')

  py.write(str(tabela['marca'].iloc[linha]))
  py.press('tab')

  py.write(str(tabela['tipo'].iloc[linha]))
  py.press('tab')

  py.write(str(tabela['categoria'].iloc[linha]))
  py.press('tab')

  py.write(str(tabela['preco_unitario'].iloc[linha]))
  py.press('tab')

  py.write(str(tabela['custo'].iloc[linha]))
  py.press('tab')

  obs = tabela['obs'].iloc[linha]
  if not pd.isna(obs):
    py.write(obs)

  py.press('tab')
  py.press('enter')

  py.scroll(5000)