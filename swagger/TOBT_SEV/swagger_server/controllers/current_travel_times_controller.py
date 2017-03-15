import connexion
from swagger_server.models.error import Error
from swagger_server.models.response_object import ResponseObject
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def realtime_get(start_point, end_point):
    """
    Realtime data of travel times.
    
    :param start_point: Letter label for travel start point.
    :type start_point: str
    :param end_point: Letter label for travel end point.
    :type end_point: str

    :rtype: ResponseObject
    """
    return 'do some magic!'
