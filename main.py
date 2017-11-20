from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form
            action="/"
            method="post">
            Rotate by:
            <input
                type="text"
                name="rot"
                value="0" />
            <textarea name="text">%s</textarea>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
'''

@app.route("/", methods=['GET'])
def index():
    return form % ''

@app.route("/", methods=['POST'])
def encrypt():
    # Save the variables for passed in form parameters
    rot=int(request.form['rot'])
    text=request.form['text']

    # log those variables for debugging
    app.logger.info('%d rot', rot)
    app.logger.info('%s text',text)

    # return the encrypted string using variables
    return form % rotate_string(text,rot)

app.run()