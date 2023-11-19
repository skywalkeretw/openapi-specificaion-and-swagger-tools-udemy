import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.orders_body import OrdersBody  # noqa: E501
from swagger_server.models.orders_body1 import OrdersBody1  # noqa: E501
from swagger_server import util


def orders_delete(order_id):  # noqa: E501
    """Delete Order

    Delete order details from EazyShop # noqa: E501

    :param order_id: 
    :type order_id: int

    :rtype: None
    """
    return 'do some magic!'


def orders_get(order_id):  # noqa: E501
    """Get Order Details

    Get order details from EazyShop # noqa: E501

    :param order_id: 
    :type order_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def orders_post(body=None):  # noqa: E501
    """Create Order

    Post order details to EazyShop for processing and shipping  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = OrdersBody1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def orders_put(body=None):  # noqa: E501
    """Update Order

    Update order details to EazyShop for processing and shipping  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = OrdersBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
