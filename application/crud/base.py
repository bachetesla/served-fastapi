"""
This is base for CRUD files
"""
from pydantic import BaseModel
from sqlalchemy.orm import Session


class CRUDBase:
    """
    This is base for CRUD
    """
    model = None
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(self, schema: BaseModel) -> model:
        """
        Create -> Make the object
        :return:
        """
        raise NotImplementedError()

    def read(self, identifier, quantity) -> model:
        """
        Read the object
        SELECT from model where identifier = quantity !
        :param quantity: the amount
        :param identifier: the identifier or the field to search
        :return:
        """
        raise NotImplementedError()

    def update(self, schema: BaseModel, identifier, quantity) -> model:
        """
        Update the object
        :param schema: the data which updates
        :param identifier: the identifier or the field to search
        :param quantity: the amount
        :return:
        """
        raise NotImplementedError()

    def delete(self, identifier, quantity) -> bool:
        """
        Delete the object
        :param quantity: the amount
        :param identifier: the identifier or the field to search
        :return:
        """
        raise NotImplementedError()
