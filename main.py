from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/phone/', methods=['post', 'get'])
def phone():

    return render_template('phone.html')


@app.route('/phone/confirm_code', methods=['post', 'get'])
def confirm():

    phone_number = request.form.get('phone')

    if phone_number:
        return render_template('confirm_code.html')
    else:
        return 'Error'


@app.route('/phone/confirm_code/confirming', methods=['post', 'get'])
def confirming():

    confirm_code = request.form.get('confirm')

    if confirm_code:
        return 'Ok'
    else:
        return 'Error'


if __name__ == "__main__":
    app.run(debug=True)
