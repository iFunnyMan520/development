from models.test_db import session, User, Flask, render_template, request
import random

app = Flask(__name__)
Random = int(random.random()*10000)


@app.route('/phone/', methods=['post', 'get'])
def phone():

    return render_template('phone.html')


@app.route('/phone/confirm', methods=['post', 'get'])
def confirm():
    phone_number = request.form.get('phone')
    your_phone = session.query(User).filter_by(phone=phone_number).first()
    if not your_phone:
        user1 = User(phone=phone_number, code=Random)
        session.add(user1)
        session.commit()
    return render_template('confirm_code.html')


@app.route('/phone/confirm/enter', methods=['post', 'get'])
def enter():
    conf = request.form.get('confirm')
    phone_number = request.form.get('phone')
    your_phone = session.query(User).filter_by(phone=phone_number).first()
    #if your_phone.code == conf:
        #return 'OK'
    #else:
        #return your_phone.code
    return phone_number


if __name__ == "__main__":
    app.run(debug=True)
