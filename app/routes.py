from app import app
from flask import render_template


@app.route('/')
@app.route('/usage')
def usage():
    usages = [
        {'api_format': '/api/hash-match/captcha', 'method': 'GET',
         'Warning': 'Default 4 Characters.',
         'description': 'Get a CAPTCHA code and a matching hash code in Response.content.CAPTCHA'
                        ' and Response.content.Hash-Code field. Then you can use'
                        ' /api/hash-match/captcha/<string:hash_code> to get captcha code by hash code.'},
        {'api_format': '/api/hash-match/captcha/<string:hash_code>', 'method': 'GET',
         'Warning': 'Default 4 Characters.',
         'description': 'Get a CAPTCHA image in HTTP.content and its code in Response.headers.CAPTCHA field'
                        ' through your hash code which already given in /api/hash-match/captcha.'},
        {'api_format': '/api/captcha/hash-code/<int:seconds>', 'method': 'DELETE',
         'Warning': 'Delete captcha-hash matching record.',
         'description': 'Delete expired captcha-hash matching record by seconds you given.'},
        {'api_format': '/api/captcha', 'method': 'GET',
         'Warning': 'Generate 5 character in an image.',
         'description': 'Get a CAPTCHA image in HTTP.content and its code in Response.headers.CAPTCHA field.'},
        {'api_format': '/api/captcha/<string:captcha_code>', 'method': 'GET',
         'Warning': 'At Most 4 Characters!',
         'description': 'Get a CAPTCHA image based on string you given in Get method.'},
        {'api_format': '/api/captcha', 'method': 'POST',
         'Warning': 'At Most 4 Characters!',
         'description': 'Get a CAPTCHA image based on string you given in Post method.'}
    ]

    return render_template('frontPage.html', usage_infos=usages)
