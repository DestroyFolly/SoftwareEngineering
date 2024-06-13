from __future__ import annotations

from flask import Blueprint
from flask import Response
from flask import request
from flask import redirect
from flask import render_template
from flask import make_response
from flask import url_for

from sql.bd import SessionMaker
from sql.bd import TrainerDB
from Trainer.dto import TrainerResponse
from Trainer.repository import TrainerRepository
from Trainer.service import TrainerService


trainer_page = Blueprint("trainer_page", __name__)


class TrainerHandler:
    def __init__(self) -> None:
        self.session_maker = SessionMaker("pyproject.toml")
        self.table = TrainerDB
        self.repo = TrainerRepository(self.table, self.session_maker)
        self.service = TrainerService(self.repo)

    @staticmethod
    @trainer_page.route('/deletetrainerbyid/<id>', methods=['GET'])
    def delete(id: int) -> Response:
        result = TrainerHandler().get_service().deletetrainerbyid(id)
        return TrainerResponse(result).get_response()



    @trainer_page.route('/trainers_page', methods=['GET', 'POST'])
    def trainers_page() -> Response:
        result = TrainerHandler().get_service().gettrainers()
        return render_template('trainers_list.html', data = result)

    @trainer_page.route('/listoftrainers', methods=['GET', 'POST'])
    def trainers_page_admin() -> Response:
        result = TrainerHandler().get_service().gettrainers()
        return render_template('trainers_list_admin.html', data=result)

    @staticmethod
    @trainer_page.route('/gettrainerbyid/<id>', methods=['GET'])
    def get_trainer_by_id(id: int) -> Response:
        result = TrainerHandler().get_service().gettrainerbyid(id)
        return render_template('trainers_list.html', data = result)

    @staticmethod
    @trainer_page.route('/gettrainerbyemail/', methods=['GET'])
    def get_trainer_by_email() -> Response:
        result = TrainerHandler().get_service().gettrainers()
        return TrainerResponse(result).get_response()

    def get_service(self) -> TrainerService:
        return self.service
