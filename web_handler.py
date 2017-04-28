from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        return 'handle progress'
    else:
        return 'Hello world!'


if __name__ == '__main__':
    app.debug = True
    app.run()
