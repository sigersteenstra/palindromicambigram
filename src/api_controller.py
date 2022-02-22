import json
from datetime import datetime, timedelta, date

from flask import Blueprint, Response, request
import logging
from src.logic import validate, is_palindrome, is_ambigram, concatdate

is_palindromeambigram_v1 = Blueprint('is_palindromeambigram_endpoint', __name__)
get_palindromeambigram_v1 = Blueprint('get_palindromeambigram_endpoint', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@is_palindromeambigram_v1.route("/ispalam", defaults={'path':''}, methods=['GET'])
@is_palindromeambigram_v1.route("/ispalam/<path:path>", methods=['GET'])
def is_palindromeambigram(path: str):
    if not validate(path):
        return Response(), 400
    if is_palindrome(path) and is_ambigram(path):
        return Response("{} is a palindromic ambigram.".format(path)), 200
    return Response("{} is not a palindromic ambigram.".format(path)), 200

@get_palindromeambigram_v1.route("/getpalams", methods=['GET'])
def get_palindromeambigram():
    from_date: str = request.args.get('from', '01010000')
    to_date: str = request.args.get('to', '31129999')
    if not validate(from_date) or not validate(to_date):
        return Response(), 400
    dates: list = []
    dt_from_date = datetime.strptime(from_date, '%d%m%Y')
    dt_to_date = datetime.strptime(to_date, '%d%m%Y')
    delta = timedelta(days=1)
    iter_date = dt_from_date
    while iter_date <= dt_to_date:
        iter_str: str = concatdate(iter_date.day, iter_date.month, iter_date.year)
        if is_palindrome(iter_str) and is_ambigram(iter_str):
            dates.append(iter_str)
        iter_date += delta
    print(json.dumps(dates))
    return Response(json.dumps(dates), content_type='application/json'), 200
