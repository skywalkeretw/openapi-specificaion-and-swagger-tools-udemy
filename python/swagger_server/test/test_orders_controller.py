# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.orders_body import OrdersBody  # noqa: E501
from swagger_server.models.orders_body1 import OrdersBody1  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_orders_delete(self):
        """Test case for orders_delete

        Delete Order
        """
        query_string = [('order_id', 56)]
        response = self.client.open(
            '/v1/orders',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_get(self):
        """Test case for orders_get

        Get Order Details
        """
        query_string = [('order_id', 56)]
        response = self.client.open(
            '/v1/orders',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_post(self):
        """Test case for orders_post

        Create Order
        """
        body = OrdersBody1()
        response = self.client.open(
            '/v1/orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_put(self):
        """Test case for orders_put

        Update Order
        """
        body = OrdersBody()
        response = self.client.open(
            '/v1/orders',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
