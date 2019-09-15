from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/phone/', methods=['post', 'get'])
def phone():

    message = request.form.get('phone')
    return render_template('phone.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
