# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.category import Category  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCategoriesController(BaseTestCase):
    """CategoriesController integration test stubs"""

    def test_categories_category_id_get(self):
        """Test case for categories_category_id_get

        Return category details
        """
        response = self.client.open(
            '/v1/categories/{categoryId}'.format(category_id=1000),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_categories_get(self):
        """Test case for categories_get

        List all catgories
        """
        query_string = [('category_id', 1000)]
        response = self.client.open(
            '/v1/categories',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
