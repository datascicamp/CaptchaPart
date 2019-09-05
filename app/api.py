from app import app
from flask import jsonify
from flask import request, make_response
from func_pack import create_captcha_by_code, create_captcha_by_identifiers
from werkzeug.http import HTTP_STATUS_CODES
from io import BytesIO


# generate a captcha based on code you given
@app.route('/api/captcha', methods=['POST'])
def generate_captcha_by_code():
    captcha_code = request.form.get('captcha_code')
    captcha_image = create_captcha_by_code(captcha_code)
    # image saved in buffer
    buffer = BytesIO()
    captcha_image.save(buffer, 'jpeg')
    buf_str = buffer.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # save image in session field
    return response


# generate a captcha based on code you given in GET method
@app.route('/api/captcha/<string:captcha_code>', methods=['GET'])
def generate_captcha_by_code_in_get(captcha_code):
    captcha_image = create_captcha_by_code(captcha_code)
    # image saved in buffer
    buffer = BytesIO()
    captcha_image.save(buffer, 'jpeg')
    buf_str = buffer.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    response.headers['CAPTCHA'] = captcha_code
    # save image in session field
    return response


# generate a captcha with random identifier
@app.route('/api/captcha', methods=['GET'])
def generate_captcha_by_identifier():
    captcha_image, captcha_code = create_captcha_by_identifiers()
    # image saved in buffer
    buffer = BytesIO()
    captcha_image.save(buffer, 'jpeg')
    buf_str = buffer.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    response.headers['CAPTCHA'] = captcha_code
    # save image in session field
    return response


# bad requests holder
def bad_request(message):
    return error_response(400, message)


# error response
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response
