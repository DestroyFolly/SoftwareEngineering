from __future__ import annotations

from flask import Blueprint
from flask import Response
from flask import request
from flask import redirect
from flask import render_template
from flask import make_response
from flask import url_for

from sql.bd import SessionMaker
from sql.bd import TrainDB
from Train.dto import TrainRequest
from Train.dto import TrainResponse
from Train.repository import TrainRepository
from Train.service import TrainService


train_page = Blueprint("train_page", __name__)


class TrainHandler:
    def __init__(self) -> None:
        self.session_maker = SessionMaker("pyproject.toml")
        self.table = TrainDB
        self.repo = TrainRepository(self.table, self.session_maker)
        self.service = TrainService(self.repo)

    @staticmethod
    @train_page.route('/add_train', methods=['GET'])
    def addtrain_get() -> Response:
        return make_response(render_template("add_train.html"))

    @staticmethod
    @train_page.route('/add_train', methods=['POST'])
    def addtrain_post() -> Response:
        title = request.form['title']
        dates = request.form['dates']
        times = request.form['times']
        trainer_id = int(request.form['trainer_id'])
        gym_id = int(request.form['gym_id'])
        print(dates)
        result = TrainHandler().get_service().addtrain(title, times, dates, trainer_id, gym_id)

        res = TrainResponse(result)
        if res.error == 1:
            return make_response(render_template("add_train_error.html"))
        else:
            return redirect(url_for('user_page.admin_get'))

    @staticmethod
    @train_page.route('/gettrainbyid/<id>', methods=['GET'])
    def get_train_by_id(id: int) -> Response:
        result = TrainHandler().get_service().gettrainbyid(id)
        return TrainResponse(result).get_response()

    @staticmethod
    @train_page.route('/getlistoftrains/<date>', methods=['GET'])
    def get_list_of_trains(date: str) -> Response:
        result = TrainHandler().get_service().getlistoftrains(date)
        return TrainResponse(result).get_response()


    @staticmethod
    @train_page.route('/delete_train', methods=['GET'])
    def deletetrain_get() -> Response:
        return make_response(render_template("delete_train.html"))

    @staticmethod
    @train_page.route('/delete_train', methods=['POST'])
    def deletetrain_post() -> Response:
        id = request.form['id']
        TrainHandler().get_service().deletetrain(id)
        return redirect(url_for('user_page.admin_get'))

    @staticmethod
    @train_page.route('/trains_page', methods=['GET', 'POST'])
    def trains_page() -> Response:
        result = TrainHandler().get_service().getlistoftrains()
        print(result[1])
        return render_template('all_trains.html', data=result)

    @staticmethod
    @train_page.route('/change_train', methods=['GET'])
    def change_train_get() -> Response:
        result = TrainHandler().get_service().getlistoftrains()
        return make_response(render_template("change_train.html", data=result))

    @staticmethod
    @train_page.route('/change_train', methods=['POST'])
    def change_train_post() -> Response:
        id = int(request.form['id'])
        title = request.form['title']
        dates = request.form['dates']
        times = request.form['times']
        trainer_id = int(request.form['trainer_id'])
        gym_id = int(request.form['gym_id'])
        print(dates)
        result = TrainHandler().get_service().changetrain(id, title, times, dates, trainer_id, gym_id)

        if result == '-':
            return make_response(render_template("add_train_error.html"))
        else:
            return redirect(url_for('user_page.admin_get'))



    def get_service(self) -> TrainService:
        return self.service
