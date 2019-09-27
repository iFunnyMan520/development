from models.test_db import session, User, Flask, render_template, request
from flask import Response
import random

app = Flask(__name__)
Random = int(random.random()*10000)


@app.route('/phone/', methods=['post', 'get'])
def phone():

    return render_template('phone.html')


@app.route('/phone/confirm', methods=['post', 'get'])
def confirm():
    resp = Response(status=200, response=render_template('confirm_code.html'))
    if request.method == 'POST':
        phone_number = request.form.get('phone')
        if not phone_number:
            return 'You didn`t enter your phone number. Try it again'
        else:
            resp.set_cookie('phone', phone_number)
            your_phone = session.query(User).filter_by(phone=phone_number).first()
            if not your_phone:
                user1 = User(phone=phone_number, code=Random)
                session.add(user1)
                session.commit()
            else:
                your_phone.code = Random
                session.add(your_phone)
                session.commit()
            return resp
    else:
        return 'Go to the first page and enter your phone number'


@app.route('/phone/confirm/enter', methods=['post', 'get'])
def enter():
    if request.method == 'POST':
        conf = request.form.get('confirm')
        your_phone = session.query(User).filter_by(phone=request.cookies.get('phone')).first()
        if your_phone.code == conf:
            return 'OK'
        else:
            return Response(status=200, response=b'Try again')
    else:
        return 'Go to the first page and enter your phone number'


if __name__ == "__main__":
    app.run(debug=True)
