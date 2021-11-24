from flask import Blueprint, request, jsonify

stripe_webhooks = Blueprint('stripe_webhooks', __name__, url_prefix='/stripe/webhooks')


@stripe_webhooks.route("/", methods=["POST"])
def test(*args, **kwargs):
    print("[+] Received stripe webhook")
    print(vars(request))


