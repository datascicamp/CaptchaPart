from app import app
from flask import jsonify


@app.route('/')
@app.route('/usage')
def usage():
    usage = [
        {'api_format': '/api/captcha', 'method': 'GET', 'description': 'Get a CAPTCHA image in HTTP.content and its code in HTTP.headers.CAPTCHA field.'},
        {'api_format': '/api/captcha', 'method': 'POST', 'description': 'Get a CAPTCHA image based on string you given.'}
    ]

    return jsonify(usage)
