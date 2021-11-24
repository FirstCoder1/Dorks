import os 

blueprints_dir = os.path.join(os.getcwd(), "blueprints")
secret_key = 'secret_key_here'  # use uuid
test_items = {
    "prod_KPTfhGKhu1mctX": 1999,
    "prod_KPTceB84KmgLqr": 19999
}
live_items = {
    "prod_K0INzx1cIiWe52": 19999,
    "prod_JxiVwtfMGpkAlq": 1999
}


class Config(object):
    DEBUG = True
    TESTING = True
