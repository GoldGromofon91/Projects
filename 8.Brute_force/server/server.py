import json
from flask import Flask, Response, request

app = Flask(__name__)

statistic = {
    'attemp': 0,
    'success': 0
}


@app.route("/")
def hello():
    return f'Attack Statistic!<br>stats={statistic}'


@app.route("/auth",methods=['POST'])
def auth():
    statistic['attemp'] +=1
    data = request.json
    usr_login = data['login']
    usr_pswd = data['password']

    with open('../user.json') as users:
        example_users = json.load(users)

    if usr_login in example_users and example_users[usr_login] == usr_pswd:
        status_code=200
        statistic['success'] +=1
    else:
        status_code=401

    return Response(status=status_code)


if __name__=="__main__":
    app.run()
