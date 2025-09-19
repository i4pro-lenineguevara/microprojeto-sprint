import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def enviar_email_aviso(email, nome, data_ferias):
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        print("❌ Variável de ambiente SENDGRID_API_KEY não definida.")
        return False
    mensagem = Mail(
        from_email='noreply@empresa.com',
        to_emails=email,
        subject='Aviso: Suas férias estão próximas!',
        html_content=f"""
        <p>Olá, {nome}!</p>
        <p>Este é um lembrete de que suas férias começam em 5 dias, na data marcada: <b>{data_ferias}</b>.</p>
        <p>Bom descanso!</p>
        <p><i>Mensagem automática - não responda.</i></p>
        """
    )
    try:
        sg = SendGridAPIClient(api_key)
        sg.send(mensagem)
        print(f"✉️ E-mail enviado para {nome} <{email}>")
        return True
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail para {nome} <{email}>: {e}")
        return False
