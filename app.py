from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/fahrenheit/<celsius>')
def to_fahrenheit(celsius=""):
    try:
        fahrenheit = celsius_to_fahrenheit(float(celsius))
        return f"{celsius} degrees celsius =  {fahrenheit} degrees fahrenheit"
    except ValueError:
        return ""


if __name__ == '__main__':
    app.run()
