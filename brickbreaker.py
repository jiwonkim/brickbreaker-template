from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import url_for


application = Flask(__name__)


@application.route('/')
def brickbreaker():
    # TODO: fetch top 5 high scores
    return render_template(
        'brickbreaker.html',
        high_scores=[],
    )


@application.route('/save_score', methods=['POST'])
def save_score():
    # TODO:
    # 1. fetch user and score from request
    # 2. save user and score
    # 3. return top 5 high scores
    return jsonify({})


if __name__ == "__main__":
    application.run(host='0.0.0.0')
