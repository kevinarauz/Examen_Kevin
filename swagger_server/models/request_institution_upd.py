# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestInstitutionUpd(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, description: str=None, address: str=None, updated_user: str=None):  # noqa: E501
        """RequestInstitutionUpd - a model defined in Swagger

        :param id: The id of this RequestInstitutionUpd.  # noqa: E501
        :type id: int
        :param name: The name of this RequestInstitutionUpd.  # noqa: E501
        :type name: str
        :param description: The description of this RequestInstitutionUpd.  # noqa: E501
        :type description: str
        :param address: The address of this RequestInstitutionUpd.  # noqa: E501
        :type address: str
        :param updated_user: The updated_user of this RequestInstitutionUpd.  # noqa: E501
        :type updated_user: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'description': str,
            'address': str,
            'updated_user': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'address': 'address',
            'updated_user': 'updatedUser'
        }
        self._id = id
        self._name = name
        self._description = description
        self._address = address
        self._updated_user = updated_user

    @classmethod
    def from_dict(cls, dikt) -> 'RequestInstitutionUpd':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestInstitutionUpd of this RequestInstitutionUpd.  # noqa: E501
        :rtype: RequestInstitutionUpd
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this RequestInstitutionUpd.


        :return: The id of this RequestInstitutionUpd.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this RequestInstitutionUpd.


        :param id: The id of this RequestInstitutionUpd.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this RequestInstitutionUpd.


        :return: The name of this RequestInstitutionUpd.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this RequestInstitutionUpd.


        :param name: The name of this RequestInstitutionUpd.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this RequestInstitutionUpd.


        :return: The description of this RequestInstitutionUpd.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this RequestInstitutionUpd.


        :param description: The description of this RequestInstitutionUpd.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def address(self) -> str:
        """Gets the address of this RequestInstitutionUpd.


        :return: The address of this RequestInstitutionUpd.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this RequestInstitutionUpd.


        :param address: The address of this RequestInstitutionUpd.
        :type address: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def updated_user(self) -> str:
        """Gets the updated_user of this RequestInstitutionUpd.


        :return: The updated_user of this RequestInstitutionUpd.
        :rtype: str
        """
        return self._updated_user

    @updated_user.setter
    def updated_user(self, updated_user: str):
        """Sets the updated_user of this RequestInstitutionUpd.


        :param updated_user: The updated_user of this RequestInstitutionUpd.
        :type updated_user: str
        """
        if updated_user is None:
            raise ValueError("Invalid value for `updated_user`, must not be `None`")  # noqa: E501

        self._updated_user = updated_user
