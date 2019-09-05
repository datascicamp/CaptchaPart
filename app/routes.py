from app import app
from flask import render_template


@app.route('/')
@app.route('/usage')
def usage():
    usages = [
        {'api_format': '/api/captcha', 'method': 'GET',
         'Warning': 'Generate 5 character in an image.',
         'description': 'Get a CAPTCHA image in HTTP.content and its code in HTTP.headers.CAPTCHA field.'},
        {'api_format': '/api/captcha/<string:captcha_code>', 'method': 'GET',
         'Warning': 'At Most 4 Characters!',
         'description': 'Get a CAPTCHA image based on string you given in Get method.'},
        {'api_format': '/api/captcha', 'method': 'POST',
         'Warning': 'At Most 4 Characters!',
         'description': 'Get a CAPTCHA image based on string you given in Post method.'}
    ]

    return render_template('frontPage.html', usage_infos=usages)
