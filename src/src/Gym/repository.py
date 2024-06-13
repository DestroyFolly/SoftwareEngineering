from __future__ import annotations

from sql.bd import SessionMaker


class GymRepository:
    def __init__(self, table: type, session_maker: SessionMaker) -> None:
        self.table = table
        self.session = session_maker

    def getgymbyid(self, id: int) -> None:
        with self.session as session:
            return session.query(self.table).get(id)

    def getlistofgyms(self) -> None:
        with self.session as session:
            return session.query(self.table).all()


