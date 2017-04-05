import connexion
from swagger_server.models.error import Error
from swagger_server.models.response_object import ResponseObject
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def historical_get(start_point, end_point, start_datetime, end_datetime):
    """
    Historical data of travel times.
    
    :param start_point: Letter label for travel start point.
    :type start_point: str
    :param end_point: Letter label for travel end point.
    :type end_point: str
    :param start_datetime: Datetime for start of aggregation period.
    :type start_datetime: str
    :param end_datetime: Datetime for start of aggregation period.
    :type end_datetime: str

    :rtype: List[ResponseObject]
    """
    start_datetimeT = deserialize_date(start_datetime)
    end_datetimeT = deserialize_date(end_datetime)
    #test object returns
    t = "2014-01-02T14:35:00-05"
    a = ResponseObject(0,0,t,t,"_".join([start_point,end_point]))
    b = ResponseObject(1,1,t,t,"_".join([start_point,end_point]))
    c = ResponseObject(2,2,t,t,"_".join([start_point,end_point]))
    lst = [a,b,c]
    return lst#'do some magic!'
