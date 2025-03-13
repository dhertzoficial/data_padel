from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Data atual
data_atual = datetime.now()

# 2. Quantidade de dias para frente
qtde_dias = 40

# 3. Calculando a data futura
data_futura = data_atual + timedelta(days=qtde_dias)

# 4. Formatação da data futura
data_futura_formatada = data_futura.strftime("%A, %d %b")

# Exibindo as variáveis
print(f"Data Alvo: {data_futura_formatada.upper()}")

# 1. Informações do e-mail
remetente = "danihertz@gmail.com"
destinatario = "daniucs@gmail.com"
senha_aplicativo = "zmqc pqtm obsw bspi"
assunto = f"Data Alvo: {data_futura_formatada.upper()}"
corpo_email = f"Data Alvo: {data_futura_formatada.upper()}"

# 2. Configuração do servidor SMTP do Gmail
servidor_smtp = "smtp.gmail.com"
porta_smtp = 587

# 3. Criando a mensagem do e-mail
mensagem = MIMEMultipart()
mensagem["From"] = remetente
mensagem["To"] = destinatario
mensagem["Subject"] = assunto
mensagem.attach(MIMEText(corpo_email, "plain"))

# 4. Enviando o e-mail
try:
    # Conectar ao servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()  # Ativar criptografia TLS
    servidor.login(remetente, senha_aplicativo)  # Login com seu e-mail e senha de aplicativo

    # Enviar o e-mail
    texto_email = mensagem.as_string()
    servidor.sendmail(remetente, destinatario, texto_email)
    print("E-mail enviado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    servidor.quit()  # Fechar a conexão com o servidor
