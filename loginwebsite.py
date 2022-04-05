import requests

s = requests.session()

playload = {

    'contact' :'01724805028',
    'password': '1711911042',

}

respose = s.post("https://lms.10minuteschool.com/api/v4/auth/login", data=playload)
r = s.get("https://10minuteschool.com/study")
print(r.content)