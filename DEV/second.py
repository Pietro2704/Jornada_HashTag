import flet as ft

def main(pagina):
  
  def entrar_popup(evento):
    pagina.dialog = popUp
    popUp.open = True
    pagina.update()
    
  def iniciar_chat(evento):
    popUp.open = False
    pagina.remove(btn_init)
    msg = f"{nome_user.value} entrou no chat"
    pagina.pubsub.send_all(msg)
    pagina.add(campo_mensagens)
    pagina.add(chat)
    pagina.update()
    
  def enviar_mensagem(evento):
    usuario = nome_user.value
    mensagem = f"{usuario}: {label_mensagem.value}"
    pagina.pubsub.send_all(mensagem)
    label_mensagem.value = ""
    pagina.update()
    
  def passar_tunel(info):
    chat.controls.append(ft.Text(info))
    pagina.update()
    
  
  
  # Parte inicial
  title = ft.Text("HashZaps")
  pagina.add(title)
  btn_init = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)
  pagina.add(btn_init)
  
  # PopUp
  nome_user = ft.TextField(label="Escreva seu nome", on_submit=iniciar_chat)
  popUp = ft.AlertDialog(
    open = False,
    modal = True,
    title = ft.Text("Bem vindo ao Zapis Zapis"),
    content = nome_user,
    actions = [
      ft.ElevatedButton("Entrar", on_click=iniciar_chat)
      ]
  )
  
  # Chat
  chat = ft.Column()
  label_mensagem = ft.TextField(label="Escreva algo aqui:", on_submit=enviar_mensagem)
  btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
  campo_mensagens = ft.Row([
    label_mensagem, btn_enviar
  ])
  
  # Criar um Túnel
  pagina.pubsub.subscribe(passar_tunel)
  
  
  
  
  pagina.update()
  
ft.app(main, view=ft.WEB_BROWSER)