import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('WEB_SERVER_SECRET_KEY') or 'abcdef020301abc8c86f'


    # Identifiers when generating CAPTCHA
    identifiers = 'ABCDEFGHIJKLMNPQRSTUVWXYZ12345789'
