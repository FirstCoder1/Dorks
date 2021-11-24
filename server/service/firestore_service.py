from google.cloud import firestore
from uuid import uuid4
db = firestore.Client()
sessions = db.collection('sessions')
users = db.collection('users')


@firestore.transactional
def by_email(transaction, email):
    print('here')
    doc_ref = users.document(document_id=email)
    document = doc_ref.get(transaction=transaction)
    print(document.exists)
    if document.exists:
        return document.to_dict()
    return {}


@firestore.transactional
def create_gifter(transaction, user_purchasing_email, name_on_card, payment_intent, to_email):
    print("Create Gifter")
    doc_ref = users.document(document_id=user_purchasing_email)
    session = {}
    session['user_purchasing'] = user_purchasing_email
    session['name_on_card'] = name_on_card
    session['payment_intent'] = payment_intent
    session['to_email'] = to_email
    return session, doc_ref


@firestore.transactional
def set_gifted_to(transaction, user_purchasing, to_email, ref):
    print("user purchasing", user_purchasing)
    if "gifted_to" not in user_purchasing.keys():
        user_purchasing["gifted_to"] = []
    user_purchasing["gifted_to"].append(to_email)
    transaction.set(ref, user_purchasing)


@firestore.transactional
def set_gifted_by(transaction, user_purchasing_email, to_email, session_id):
    print("user gifted:", to_email)
    ref = users.document(document_id=to_email)
    ses_ref = sessions.document(document_id=session_id)
    gifted = ses_ref.get(transaction=transaction).to_dict()
    user = ref.get(transaction=transaction)
    if user.exists:
        user = {}
    else:
        user = user.to_dict()
    print(gifted)
    user['name'] = gifted['to_name']
    user['email'] = gifted['to_email']
    user['message'] = gifted['to_message']
    user["gifted_by"] = user_purchasing_email
    transaction.set(ref, user)
    transaction.set(ses_ref, gifted)
    return user['name']


@firestore.transactional
def store_gift_form_session(transaction, to_email, to_name, to_message, session_id):
    doc_ref = sessions.document(document_id=session_id)
    document = doc_ref.get(transaction=transaction)
    if document.exists:
        obj = document.to_dict()
        obj["to_name"] = to_name
        obj["to_email"] = to_email
        obj["to_message"] = to_message
        obj["form_active"] = 1
        transaction.set(doc_ref, obj)
    else:
        obj = {}
        obj["to_name"] = to_name
        obj["to_email"] = to_email
        obj["to_message"] = to_message
        obj["form_active"] = 1
        transaction.set(doc_ref, obj)


@firestore.transactional
def store_payment(transaction, email, payment_object, user_obj):
    doc_ref = users.document(document_id=email)
    user_obj["purchased"] = True
    if user_obj.get("payments"):
        user_obj["payments"].append(payment_object)
    else:
        user_obj["payments"] = [payment_object]
    transaction.set(doc_ref, user_obj)
    return True


@firestore.transactional
def store_purchase_form(transaction, form_data, session_id):
    print(form_data)
    if "to_email" in form_data:
        doc_ref = users.document(document_id=form_data["to_email"])
        form_data['name'] = form_data['to_name']
        del form_data['to_name']
        form_data['email'] = form_data['to_email']
        del form_data['to_email']
        del form_data['to_message']
        form_data["form_active"] = 1
        document = doc_ref.get(transaction=transaction)
        if document.exists:
            transaction.update(doc_ref, form_data)
        else:
            transaction.set(doc_ref, form_data)
        store_session_data(db.transaction(), session_id, form_data)
        return True
    else:
        doc_ref = users.document(document_id=form_data["email"])
        document = doc_ref.get(transaction=transaction)
        form_data["form_active"] = 0
        if document.exists:
            transaction.update(doc_ref, form_data)
        else:
            transaction.set(doc_ref, form_data)
        store_session_data(db.transaction(), session_id, form_data)
        return True


@firestore.transactional
def get_session_data(transaction, session_id):
    """ Looks up (or creates) the session with the given session_id.
        Creates a random session_id if none is provided. Increments
        the number of views in this session. Updates are done in a
        transaction to make sure no saved increments are overwritten.
    """
    if session_id is None:
        session_id = str(uuid4())   # Random, unique identifier
    doc_ref = sessions.document(document_id=session_id)
    doc = doc_ref.get(transaction=transaction)
    if doc.exists:
        session = doc.to_dict()
        print("[+] Session found: ", session)
    else:
        print("[+] Creating new session")
        session = {}
        transaction.set(doc_ref, session)
    session['session_id'] = session_id
    print(session)
    return session


@firestore.transactional
def store_session_data(transaction, session_id, data):
    doc_ref = sessions.document(document_id=session_id)
    doc = doc_ref.get(transaction=transaction)
    if doc.exists:
        transaction.update(doc_ref, data)
    else:
        transaction.set(doc_ref, data)

