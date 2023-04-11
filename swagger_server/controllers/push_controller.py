import connexion
import six

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server import util


def add_notification(body):  # noqa: E501
    """Add a new notification to the store

    Add a new notification to the store # noqa: E501

    :param body: Create a new notification in the store
    :type body: dict | bytes

    :rtype: Notification
    """
    if connexion.request.is_json:
        body = Notification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'Se agrego la notificacion!'


def find_notifications_by_status(status=None):  # noqa: E501
    """Finds Notifications by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Notification]
    """
    return 'El estado de la notificacion es: '+ status;
