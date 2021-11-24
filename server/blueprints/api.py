from flask import Flask, Blueprint, request, jsonify, make_response, send_file
from google.cloud import firestore
from service.firestore_service import *
from service.email_service import *
from service.payment_service import *
from dotenv import load_dotenv
from config import test_items, live_items
from pathlib import Path
import os
import stripe


load_dotenv(dotenv_path=Path(r"/Users/tmatembo/Desktop/Dorks/Dorks/server/.env"))

stripe.api_key = os.getenv('stripe_test_secret')

api = Blueprint('api', __name__, url_prefix='/api')

db = firestore.Client()


def get_amount(item):
    name = item["name"]
    if name == "dorks_annual":
        return 19999
    elif name == "dorks_monthly":
        return 1999


@api.route("/session", methods=["GET"])

def session(*args, **kwargs):
    try:
        session_data = get_session_data(db.transaction(), request.cookies.get('session_id'))
        resp = jsonify(session_data)
        resp.set_cookie('session_id', session_data['session_id'])
        print(
            resp.get_json()
        )
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
        return jsonify({})


@api.route("/store/myself_form", methods=["POST"])
def myself_form(*args, **kwargs):
    print("yes")
    try:
        form_data = request.get_json()
        if form_data:
            email = form_data["email"]
            # obj_by_email = by_email(cursor, conn, email)
            obj_by_email = by_email(db.transaction(), email)
            if obj_by_email and (obj_by_email.get("purchased") or obj_by_email.get("gifted_by")):
                return jsonify({"error": "purchased"})
            else:
                result = store_purchase_form(db.transaction(), form_data, request.cookies.get('session_id'))
                if result:
                    return jsonify({"success": True})
        return jsonify({})
    except Exception as e:
        raise e
        return jsonify({})


@api.route('/store/gift_form', methods=["POST"])
def gift_form():
    try:
        form_data = request.get_json()
        to_email, to_name, to_message = form_data.get("to_email"), form_data.get("to_name"), form_data.get("to_message")
        if to_email and to_name and to_message:
            store_gift_form_session(db.transaction(), to_email, to_name, to_message, request.cookies.get("session_id"))
            obj_by_email = by_email(db.transaction(), to_email)
            if obj_by_email and (obj_by_email.get("gifted_by") or obj_by_email.get("purchased")):
                return jsonify({"error": "gifted"})
            else:
                result = store_purchase_form(db.transaction(), form_data, request.cookies.get('session_id'))
                if result:
                    return jsonify({"result": True})
        else:
            return jsonify({"error": "email_not_provided"})
    except Exception as e:
        # raise e
        return jsonify({})


@api.route('/create/payment', methods=["POST"])
def create_payment():
    try:
        print("creating stripe payment")
        data = request.get_json()
        amount = get_amount(data["item"])
        payment_intent = stripe.PaymentIntent.create(amount=amount, currency='usd')
        return jsonify({'secret': payment_intent.client_secret})
        #return jsonify({"secret": payment_intent["client_secret"]})
    except Exception as e:
        # raise e
        return jsonify({})


@api.route('/check/purchased', methods=["POST"])
def check_purchased():
    try:
        data = request.get_json()
        email = data.get("email")
        user = by_email(db.transaction(), email)
        result = False
        if user and user.get("purchased"):
            result = True
        return jsonify({"result": result})
    except:
        return jsonify({})


@api.route('/payment/successful', methods=["POST"])
def successful_payment():
    print('yes?')
    try:
        data = request.get_json()
        payment_intent = data["paymentIntent"]
        session_data = get_session_data(db.transaction(), request.cookies.get('session_id'))
        action = data.get("action")
        name_on_card = data.get("name_on_card")
        print(action)
        if action == "purchase_dorks":
            print(session_data.get("email"))
            pp = purchase_dorks(data.get("email"), payment_intent, name_on_card)
            print("pp: ")
            print(pp.json)
            return pp
        elif action == "gift_dorks":
            print(data)
            email, name_on_card = data.get("email"), data.get("name_on_card")
            to_email = session_data.get("to_email").lower()
            piop = gift_dorks(email, name_on_card, to_email, payment_intent, request.cookies.get('session_id'))
            print(piop)
            return piop
        else:
            return jsonify({})

        # first_name = session_data.get('first_name')
        # last_name = session_data.get('last_name')
        # email = session_data.get("email")
        # user = by_email(db.transaction(), email)
        # if user:
        #     if user.get("purchased"):
        #         return jsonify({"error": "purchased"})
        #     else:
        #         result = store_payment(db.transaction(), email, payment_intent)
        #         send_email("gift_dorks", email, "Grandpa Joe")
        #         return jsonify({"result": result})
        # return jsonify({})
    except Exception as e:
        print(e)
        raise e
        return jsonify({})


@api.route('/template/<filename>')
def purchase_email_template(filename):
    purchase_template = os.path.join(os.getcwd(), 'email_templates', filename)
    return send_file(purchase_template)



