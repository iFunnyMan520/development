from models.test_db import User, db, app
from flask import Response, render_template, request
import random

Random = int(random.random()*10000)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/phone/', methods=['get'])
def phone():
    return render_template('phone.html')


@app.route('/phone/confirm', methods=['post'])
def confirm():
    resp = Response(status=200, response=render_template('confirm_code.html'))
    phone_number = request.form.get('phone')
    if not phone_number:
        return render_template('phone.html', message="Wrong phone number. Try it again")
    else:
        resp.set_cookie('phone', phone_number)
        your_phone = db.session.query(User).filter_by(phone=phone_number).first()
        if not your_phone:
            user1 = User(phone=phone_number, code=Random)
            db.session.add(user1)
            db.session.commit()
            return resp
        else:
            your_phone.code = Random
            db.session.add(your_phone)
            db.session.commit()
            return resp


@app.route('/phone/confirm/enter', methods=['post'])
def enter():

    conf = request.form.get('confirm')
    your_phone = db.session.query(User).filter_by(phone=request.cookies.get('phone')).first()
    if your_phone.code == conf:
        return 'OK'
    else:
        return render_template('phone.html', message="Wrong confirm code. Try it again")


if __name__ == "__main__":
    app.run(debug=True)
