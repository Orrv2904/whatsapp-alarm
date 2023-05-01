# WhatsApp Alarm

WhatsApp Alarm is a Python script that uses the Twilio API to send a message and make a WhatsApp call at a scheduled time. With this script, you can set up a custom alarm on your mobile phone using WhatsApp as a notification platform.

To use WhatsApp Alarm, you'll need to have a Twilio account and a verified WhatsApp phone number in your account. You'll also need to install the Twilio Python library and configure your authentication credentials in the configuration file.

Once you've set everything up correctly, simply run the script and you'll receive a message and a WhatsApp call at the scheduled time. With this tool, you'll never forget an important appointment or work meeting again.

# Twilio WhatsApp Alarm

This project demonstrates how to send a WhatsApp message as an alarm using the Twilio API in Python.

## Prerequisites

A Twilio account
A verified WhatsApp phone number in your Twilio account (follow the instructions in the Twilio console)
Installation
Clone or download this repository.

Install the required Python packages using pip.

Copy code
pip install -r requirements.txt
Rename .env.example to .env and replace the placeholders with your Twilio account details.

```
TWILIO_ACCOUNT_SID=<your_account_sid>
TWILIO_AUTH_TOKEN=<your_auth_token>
TWILIO_WHATSAPP_NUMBER=<your_whatsapp_number>
```
Usage
Run the following command in the terminal to send a WhatsApp message as an alarm:

```python main.py```

Note
If you are using a free Twilio account, you can only send messages to verified phone numbers. Verify your phone number in the Twilio console or upgrade your account to send messages to unverified numbers.
This project is for educational purposes only. Use it at your own risk.
