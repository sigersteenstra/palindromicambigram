from datetime import datetime

ambinums = {0:0,1:1,2:2,5:5,6:9,8:8,9:6}
not_ambinums = [3,4,7]

def validate(date_text):
    try:
        datetime.strptime(date_text, '%d%m%Y')
        return True
    except ValueError:
        return False


def is_palindrome(date_text: str):
    reverse = date_text[::-1]
    if date_text == reverse:
        return True
    return False


def is_ambigram(date_text: str):
    for num in not_ambinums:
        if str(num) in date_text:
            return False
    reverse: str = date_text[::-1]
    upsreverse: str = ''
    for i in range(0, len(reverse)):
        key = int(reverse[i])
        upsreverse = upsreverse + str(ambinums.get(key))
    if date_text == upsreverse:
        return True
    return False


def concatdate(day: int, month: int, year: int):
    if day<10:
        strday = '0' + str(day)
    else:
        strday = str(day)
    if month<10:
        strmonth = '0' + str(month)
    else:
        strmonth = str(month)
    if year<10:
        stryear = '000' + str(year)
    elif year<100:
        stryear = '00' + str(year)
    elif year <1000:
        stryear = '0' + str(year)
    else:
        stryear = str(year)
    return strday + strmonth + stryear
