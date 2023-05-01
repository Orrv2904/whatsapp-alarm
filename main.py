import os
from twilio.rest import Client
import time
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Credenciales de Twilio
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Número de teléfono de destino (incluyendo el prefijo del país)
to_number = os.getenv('TO_NUMBER')

# Mensaje a enviar
message = client.messages.create(
    to=to_number,
    from_=os.getenv('TWILIO_PHONE_NUMBER'),
    body='¡Hola! Esta es tu alarma programada en Python. ¡Es hora de despertar!')

# Realizar la llamada
call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to=to_number,
    from_=os.getenv('TWILIO_PHONE_NUMBER')
)

# Esperar 30 segundos antes de finalizar el script
time.sleep(30)
