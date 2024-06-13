from __future__ import annotations

from flask import Blueprint
from flask import Response

from Muscles.dto import MuscleResponse
from Muscles.repository import MusclesRepository
from Muscles.service import MuscleService
from sql.bd import MusclesDB
from sql.bd import SessionMaker


muscle_page = Blueprint("muscle_page", __name__)


class MuscleHandler:
    def __init__(self) -> None:
        self.session_maker = SessionMaker("pyproject.toml")
        self.table = MusclesDB
        self.repo = MusclesRepository(self.table, self.session_maker)
        self.service = MuscleService(self.repo)
    

    @staticmethod
    @muscle_page.route('/getmusclebyid/<id>', methods=['GET'])
    def get_muscle_by_id(id: int) -> Response:
        result = MuscleHandler().get_service().getmusclebyid(id)
        return MuscleResponse(result).get_response()

    @staticmethod
    @muscle_page.route('/getlistofmuscles/<mgroup>', methods=['GET'])
    def get_list_of_muscles(mgroup: str) -> Response:
        result = MuscleHandler().get_service().getlistofmuscles(mgroup)
        return MuscleResponse(result).get_response()


    def get_service(self) -> MuscleService:
        return self.service


