import os
import requests
chat_id = os.getenv('CHAT_ID')
token = os.getenv('TELEGRAM_BOT_TOKEN')

#하고싶은 것들
text = '니좀치나'
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

