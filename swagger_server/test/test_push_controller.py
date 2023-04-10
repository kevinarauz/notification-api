# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPushController(BaseTestCase):
    """PushController integration test stubs"""

    def test_add_notification(self):
        """Test case for add_notification

        Add a new notification to the store
        """
        body = Notification()
        response = self.client.open(
            '/rest/notification-api/v1.0/update',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_notifications_by_status(self):
        """Test case for find_notifications_by_status

        Finds Notifications by status
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/rest/notification-api/v1.0/notification/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
