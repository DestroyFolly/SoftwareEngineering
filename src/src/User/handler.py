from __future__ import annotations

import logging

from flask import Blueprint
from flask import Response
from flask import request
from flask import redirect
from flask import render_template
from flask import make_response
from flask import url_for

from Train.repository import TrainRepository
from sql.bd import SessionMaker, TrainDB, UserDB, tuDB
from User.dto import UserRequest
from User.dto import UserResponse
from User.repository import UserRepository
from User.service import UserService
from conn.tu_repository import TURepository
from Train.handler import TrainHandler
from Trainer.handler import TrainerHandler
from Gym.handler import GymHandler
from Position.handler import PositionHandler



user_page = Blueprint("user_page", __name__)


class UserHandler:
    def __init__(self) -> None:
        self.session_maker = SessionMaker("pyproject.toml")
        self.table = UserDB
        self.tu_table = tuDB
        self.train_table = TrainDB
        self.repo = UserRepository(self.table, self.session_maker)
        self.tu_repo = TURepository(self.tu_table, self.session_maker)
        self.train_repo = TrainRepository(self.train_table, self.session_maker)
        self.service = UserService(self.repo, self.tu_repo, self.train_repo)

    @staticmethod
    @user_page.route('/', methods=['GET'])
    def main_page() -> Response | str:
        return make_response(render_template("main.html"))

    @staticmethod
    @user_page.route('/login', methods=['GET'])
    def login_get() -> Response:
        return make_response(render_template("login.html"))

    @staticmethod
    @user_page.route('/login', methods=['POST'])
    def login_post() -> Response:
        email = request.form['email']
        password = request.form['password']
        result = UserHandler().get_service().login(password, email)
        res = UserResponse(result)
        print(res)
        if res.error == 1:
            print("error")
            return make_response(render_template("login_error.html"))
        else:
            user = (res.data.get_json())
            if user['role'] == "u":
                return redirect(url_for('user_page.page_get', id=user['id']))
            elif user['role'] == "a":
                return redirect(url_for('user_page.admin_get', id=user['id']))
            elif user['role'] == "t":
                return redirect(url_for('user_page.trainer_get', id=user['id']))

            return make_response(render_template("login.html"))

    @staticmethod
    @user_page.route('/admin', methods=['GET'])
    def admin_get() -> Response:
        return make_response(render_template("admin_page.html"))

    @staticmethod
    @user_page.route('/trainer/<id>', methods=['GET'])
    def trainer_get(id: int) -> Response:
        print(id)
        return make_response(render_template("trainer_page.html"))

    @staticmethod
    @user_page.route('/trainer/<id>', methods=['POST'])
    def trainer_post(id: int) -> Response:
        user = UserHandler().get_service().getuserbyid(id)
        # print(user.phone)
        trainer = TrainerHandler().get_service().gettrainerbyphone(user.phone)
        print(trainer.first_name)
        gym = GymHandler().get_service().getgymbyid(trainer.gym_id)
        position = PositionHandler().get_service().getpositionid(trainer.position_id)
        result = [trainer.first_name, trainer.surname, str(trainer.number), gym.adress, position.title]
        return render_template("trainer_info.html", data = result)

    @staticmethod
    @user_page.route('/add_user', methods=['GET'])
    def add_user_get() -> Response:
        return make_response(render_template("add_user.html"))

    @staticmethod
    @user_page.route('/add_user', methods=['POST'])
    def add_user_post() -> Response:
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['firstname']
        surname = request.form['lastname']
        phone = int(request.form['phone'])
        gender = request.form['gender']
        role = request.form['role']
        # print(email, password, name, surname, phone, gender)
        result = UserHandler().get_service().register(phone, email, first_name, surname, password, role, gender)
        # if role == 't':
        #     trainer = TrainerHandler().get_service().addtrainer(first_name, surname, gender, phone,1, 1)
        res = UserResponse(result)
        if res.error == 1:
            return make_response(render_template("add_user_error.html"))
        else:
            return redirect(url_for('user_page.admin_get'))


    @staticmethod
    @user_page.route('/page/<id>', methods=[ 'GET'])
    def page_get(id: int) -> Response:
        print(id)
        return render_template("user_page.html")

    @staticmethod
    @user_page.route('/page/<id>', methods=['POST'])
    def page_post(id: int) -> Response:
        if 'my_trains' in request.form:
            result = UserHandler().get_service().getusertrains(id)
            return render_template('trains_list.html', data = result)
        elif 'choose_train' in request.form:
            return redirect(url_for('user_page.choose_train_get', id = id))
        elif 'exit' in request.form:
            return render_template('main.html')


    @staticmethod
    @user_page.route('/register', methods=['GET'])
    def register_get() -> Response:
        return make_response(render_template("register.html"))

    @staticmethod
    @user_page.route('/register', methods=['POST'])
    def register_post() -> Response:
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['firstname']
        surname = request.form['lastname']
        phone = int(request.form['phone'])
        gender = request.form['gender']
        # print(email, password, name, surname, phone, gender)
        result = UserHandler().get_service().register(phone, email, first_name, surname, password, 'u', gender)

        res = UserResponse(result)
        if res.error == 1:
            return make_response(render_template("register_error.html"))
        else:
            user = (res.data.get_json())
            return redirect(url_for('user_page.page_get', id=user['id']))





    @staticmethod
    @user_page.route('/deleteuserbyid/<id>', methods=['DELETE'])
    def delete(user_id: int) -> Response:
        result = UserHandler().get_service().deleteuserbyid(user_id)
        return UserResponse(result).get_response()

    @staticmethod
    @user_page.route('/getuserbyid/<id>', methods=['GET'])
    def getuserbyid(id: int) -> Response:
        logging.basicConfig(level=logging.DEBUG, filename="../py_log.log",
                            format='%(levelname)s (%(asctime)s): %(message)s'
                                   '(Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S', filemode="w")
        logging.info("User handler getuserbyid")
        result = UserHandler().get_service().getuserbyid(id)
        return UserResponse(result).get_response()

    @staticmethod
    @user_page.route('/getuserbyemail/<email>', methods=['GET'])
    def get_user_by_email(email: str) -> Response:
        result = UserHandler().get_service().getuserbyemail(email)
        return UserResponse(result).get_response()

    @staticmethod
    @user_page.route('/choose_train/<id>', methods=['GET'])
    def choose_train_get(id: int) -> Response:
        result = TrainHandler().get_service().getlistoftrains()
        print(id)
        return render_template('all_trains_choose.html', data=result)

    @staticmethod
    @user_page.route('/choose_train/<id>', methods=['POST'])
    def choose_train_post(id: int) -> Response:
        train_id = int(request.form['train_id'])
        train = TrainHandler().get_service().gettrainbyid(train_id)
        if train == '-':
            return redirect(url_for('user_page.choose_error_get', id=id))
        user_id = id
        UserHandler().get_service().addconn(user_id, train_id)
        result = UserHandler().get_service().getusertrains(user_id)
        return render_template('trains_list.html', data=result)

    @staticmethod
    @user_page.route('/choose_error/<id>', methods=['GET'])
    def choose_error_get(id: int) -> Response:
        print(id)
        return render_template('choose_error.html')

    @staticmethod
    @user_page.route('/choose_error/<id>', methods=['POST'])
    def choose_error_post(id: int) -> Response:
        return redirect(url_for('user_page.page_get', id=id))

    @staticmethod
    @user_page.route('/research', methods=['GET', 'POST'])
    def research() -> Response:
        for i in range (2000, 5001):
            UserHandler().get_service().register(123, str(i), 'Name', 'Surname', 'Password', 'u', 'm')


    def get_service(self) -> UserService:
        return self.service
