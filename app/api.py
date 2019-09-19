from app import app, db
from flask import jsonify
from flask import request, make_response
from func_pack import create_captcha_by_code, create_captcha_by_identifiers,\
    create_random_hash, generate_random_captcha_code, get_passed_utc_date_by_seconds
from werkzeug.http import HTTP_STATUS_CODES
from io import BytesIO
from app.models import CaptchaMatching


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


# generate a hashcode and a captcha
@app.route('/api/hash-match/captcha', methods=['GET'])
def generate_captcha_by_hash():
    hash_code = create_random_hash()
    captcha_code = generate_random_captcha_code()
    response = make_response()
    matching = CaptchaMatching(hash_code=hash_code, captcha_code=captcha_code)
    # insert into sqlite
    db.session.add(matching)
    db.session.commit()
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.headers['CAPTCHA'] = captcha_code
    response.headers['Hash-Code'] = hash_code
    response = 'Captcha Code and Hash Code are in the response headers.'
    return response


# generate a captcha based on hash code you've given already in GET method
@app.route('/api/captcha/hash-code/<string:hash_code>', methods=['GET'])
def generate_captcha_by_given_hash_code_in_get(hash_code):
    captcha_hash_match = CaptchaMatching.query.filter(CaptchaMatching.hash_code == hash_code).first_or_404().to_dict()
    captcha_code = captcha_hash_match['captcha_code']
    captcha_image = create_captcha_by_code(captcha_code)
    # image saved in buffer
    buffer = BytesIO()
    captcha_image.save(buffer, 'jpeg')
    buf_str = buffer.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    response.headers['CAPTCHA'] = captcha_code
    return response


# delete old hash_code and captcha_code matching
@app.route('/api/captcha/hash-code/<int:seconds>', methods=['DELETE'])
def delete_expired_captcha_code(seconds):
    passed_time = get_passed_utc_date_by_seconds(seconds)
    matching_list = list()
    for matching in CaptchaMatching.query.filter(CaptchaMatching.timestamp < passed_time).all():
        matching_list.append(matching.to_dict())
        db.session.delete(matching)
    db.session.commit()
    return jsonify(matching_list)


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
