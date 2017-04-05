# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.response_object import ResponseObject
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCurrentTTController(BaseTestCase):
    """ CurrentTTController integration test stubs """

    def test_realtime_get(self):
        """
        Test case for realtime_get

        Realtime data of travel times.
        """
        query_string = [('start_point', 'start_point_example'),
                        ('end_point', 'end_point_example')]
        response = self.client.open('/v0/realtime',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
