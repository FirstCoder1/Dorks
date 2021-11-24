from flask import jsonify
from service.firestore_service import *
from service.email_service import *


def purchase_dorks(user_email, payment_intent, name_on_card):
    user = by_email(db.transaction(), user_email)
    if user and user.get("purchased"):
        return jsonify({"error": "purchased"})
    elif user:
        user["name_on_card"] = name_on_card
        result = store_payment(db.transaction(), user_email, payment_intent, user)
        send_email("purchase_dorks", user_email, "")
        return jsonify({"result": result})
    else:
        return jsonify({"error": "form_bypass"})


def gift_dorks(user_purchasing_email, name_on_card, to_email, payment_intent, session_id):
    if to_email == user_purchasing_email:
        return jsonify({"error": "Please select a different email"})

    if user_purchasing_email and name_on_card and to_email:
        user_purchasing = by_email(db.transaction(), user_purchasing_email)
        if user_purchasing:
            print("user exists")
            gifted_to = user_purchasing.get("gifted_to")
            if gifted_to is None:
                user_purchasing["gifted_to"] = []
                gifted_to = []
            if to_email not in gifted_to:
                gifted_user = by_email(db.transaction(), to_email)
                if gifted_user and (gifted_user.get("gifted_by") or gifted_user.get("purchased")):
                    return jsonify({"error": "User %s already has an active plan" % to_email})
                else:
                    ref = users.document(document_id=user_purchasing_email)
                    set_gifted_to(db.transaction(), user_purchasing, to_email, ref)
                    gifted_name = set_gifted_by(db.transaction(), user_purchasing_email, to_email, session_id)
                    send_email("gift_dorks", to_email, gifted_name)
                    return jsonify({"result": True})

            else:
                return jsonify({"error": "You have already purchased dorks for this user"})
        # User purchasing does not exist by the email entered, so create a purchasing user
        else:
            # create a user that doesn't exist upon checkout of gift
            print("User does not exist, creating gifter")

            user, ref = create_gifter(db.transaction(), user_purchasing_email, name_on_card, payment_intent, to_email)
            set_gifted_to(db.transaction(), user, to_email, ref)
            set_gifted_by(db.transaction(), user_purchasing_email, to_email, session_id)
            return jsonify({"result": True})
    else:
        print("Form data invalid")
        return jsonify({})
