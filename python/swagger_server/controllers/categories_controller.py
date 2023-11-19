import connexion
import six

from swagger_server.models.category import Category  # noqa: E501
from swagger_server import util


def categories_category_id_get(category_id):  # noqa: E501
    """Return category details

    Returns the category details from EazyShop # noqa: E501

    :param category_id: 
    :type category_id: int

    :rtype: Category
    """
    return 'do some magic!'


def categories_get(category_id=None):  # noqa: E501
    """List all catgories

    Returns the list of categories supported by EazyShop # noqa: E501

    :param category_id: 
    :type category_id: int

    :rtype: List[Category]
    """
    return 'do some magic!'
