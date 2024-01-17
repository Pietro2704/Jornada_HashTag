# importa biblioteca frontEnd
import flet as ft

# função main
def main(pagina):
  
  # Funçao botão inicial
  def iniciarChat(evento):
    pagina.dialog = popUp 
    popUp.open = True 
    pagina.update() 
    
    
    
  # Função do botão no PopUp
  def entrar(evento): 
    popUp.open = False # Fecha PopUp
    pagina.remove(btn_init) # Remove botão inicial
    texto = f"{nome_user.value} entrou no chat"
    chat.controls.append(texto)
    
    # Colocar campos do chat em linha
    campo_mensagens = ft.Row([
      labelMsg,
      btnMsg
    ])
    
    pagina.add(campo_mensagens)
    pagina.add(chat)
    pagina.update()
    
    
    
  # Função do chat
  def enviarMensagem(evento):
    texto_labelMsg = f"{nome_user.value}: {labelMsg.value}"
    chat.controls.append(ft.Text(texto_labelMsg))
    labelMsg.value = ""
    pagina.update()
    
  
  
  
  
  
  
  
  
  # Cria título
  txt = ft.Text("Aoooba!!")
  
  # Criar um chat
  chat = ft.Column()
  
  # Pegar nome do usuario do PopUp
  nome_user = ft.TextField(
    label="Escreva seu nome:"
  )
  
  # Campos do chat
  labelMsg = ft.TextField(label="Escreva sua mensagem:")
  btnMsg = ft.ElevatedButton("Enviar", on_click=enviarMensagem)
  
  # Criar PopUp
  popUp = ft.AlertDialog(
    open=False, 
    modal=True, 
    title=ft.Text("Bem vindo ao Zapis Zapis"),
    content=nome_user,
    actions=[
      ft.ElevatedButton("Entrar", on_click=entrar)
      ]
    )
  
  pagina.add(txt)
  btn_init = ft.ElevatedButton("Iniciar chat", on_click=iniciarChat)
  pagina.add(btn_init)
  
  
  
  
  
ft.app(main)