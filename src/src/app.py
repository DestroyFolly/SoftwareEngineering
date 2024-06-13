from __future__ import annotations

from flask import Flask
from flask import request, redirect, url_for, render_template

import logging

from Exercise.handler import exercise_page
from Gym.handler import gym_page
from Muscles.handler import muscle_page
from Position.handler import position_page
from Train.handler import train_page
from Trainer.handler import trainer_page
from User.handler import user_page
from flask import render_template

app = Flask(__name__)
app.register_blueprint(user_page)
app.register_blueprint(train_page)
app.register_blueprint(trainer_page)
app.register_blueprint(exercise_page)
app.register_blueprint(position_page)
app.register_blueprint(gym_page)
app.register_blueprint(muscle_page)


@app.route("/")
def index():
    if request.method == 'POST' and 'register_button' in request.form:
        return redirect(url_for('register'))
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
    print('sss')
