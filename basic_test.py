import requests
from func_pack import get_passed_utc_date_by_seconds

if __name__ == '__main__':
    # requests.delete('http://127.0.0.1:5000/api/captcha/hash-code/60')
    result = '2019-09-19 06:44:01.990498' < get_passed_utc_date_by_seconds(600)
    print(get_passed_utc_date_by_seconds(600))
    print(result)
    pass
