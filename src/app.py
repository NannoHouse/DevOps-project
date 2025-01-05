import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def random_number():
    rand_num = random.randint(1, 1000)

    return f"Random Number: {rand_num}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
