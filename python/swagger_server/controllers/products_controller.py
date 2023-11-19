import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def products_get(category_id=None):  # noqa: E501
    """List all products

    Returns the list of products supported by EazyShop  # noqa: E501

    :param category_id: 
    :type category_id: int

    :rtype: List[Product]
    """
    return 'do some magic!'


def products_product_id_get(product_id):  # noqa: E501
    """Return product details

    Returns the product details from  EazyShop  # noqa: E501

    :param product_id: 
    :type product_id: int

    :rtype: Product
    """
    return 'do some magic!'
