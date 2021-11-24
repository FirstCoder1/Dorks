from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

from_email = os.getenv('sg_from_email')
gift_template_id = "d-4158ee9a983f496cbd4bff994f818192"
purchase_template_id = "d-a7cd129a71744a30ac219698fb4a6ae9"

sg = SendGridAPIClient(os.getenv('sendgrid_api_key'))


def send_email(action, email, to_name=''):

    if action == "gift_dorks":
        send_gift_email(email, to_name)

    elif action == "purchase_dorks":
        send_purchase_email(email)


def send_gift_email(to_email, to_name):
    message = Mail(from_email=from_email, to_emails=to_email)
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'gift_receiver': to_name,
        'registration_link': 'https://hundreddorks.com',
    }
    message.template_id = gift_template_id
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        raise e
        print(e.message)


def send_purchase_email(email):
    message = Mail(from_email=from_email, to_emails=email, subject="Dorks purchased!")
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {}
    message.template_id = purchase_template_id
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        raise e
        print(e.message)

