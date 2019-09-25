import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import keys

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "mail": keys.mail,
    "pass": keys.passwd
}

serialize = "mail={0}&pass={1}".format(keys.mail, keys.passwd)

# action
url_login = "https://vis-its.com/users/login"
res = session.post(url_login, data=serialize)
res.raise_for_status()  # エラーならここで例外を発生させる

url_qr = "https://vis-its.com/student/place_qr"

res = session.get(url_qr)

print(res.text)
