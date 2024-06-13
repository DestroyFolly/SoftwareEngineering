from __future__ import annotations

from flask import Blueprint
from flask import Response
from flask import request
from flask import redirect
from flask import render_template
from flask import make_response
from flask import url_for

from Gym.dto import GymResponse
from Gym.repository import GymRepository
from Gym.service import GymService
from sql.bd import GymDB
from sql.bd import SessionMaker


gym_page = Blueprint("gym_page", __name__)


class GymHandler:
    def __init__(self) -> None:
        self.session_maker = SessionMaker("pyproject.toml")
        self.table = GymDB
        self.repo = GymRepository(self.table, self.session_maker)
        self.service = GymService(self.repo)


    @staticmethod
    @gym_page.route('/getgymbyid/<id>', methods=['GET'])
    def get_gym_by_id(id: int) -> Response:
        result = GymHandler().get_service().getgymbyid(id)
        return GymResponse(result).get_response()

    @staticmethod
    @gym_page.route('/gyms_page', methods=['GET', 'POST'])
    def gyms_page() -> Response:
        result = GymHandler().get_service().getlistofgyms()
        print(result[1])
        return render_template('gym_list.html', data = result)

    @staticmethod
    @gym_page.route('/getlistofgyms/<adr>', methods=['GET'])
    def get_list_of_gyms(adr: str) -> Response:
        result = GymHandler().get_service().getlistofgyms(adr)
        return GymResponse(result).get_response()

    def get_service(self) -> GymService:
        return self.service


