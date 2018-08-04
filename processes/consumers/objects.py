# System level imports
from pendulum import DateTime, Date

# Miyagi imports
from miyagi import TypedMany

# Installation-specific imports
from ..users import User

# Process-specific imports
from .types import ContactTypes, Brands, PrivacyFlags


class Consumer:
    _json_api = True

    creation_datetime: DateTime
    creation_user: User
    update_datetime: DateTime
    update_user: User

    name: str
    surname: str
    birth: Date

    class Contacts(TypedMany):
        _json_api = True
        typ: ContactTypes
        value: str

    class Privacy(TypedMany):
        _json_api = True
        typ: Brands

        class Consents(TypedMany):
            _json_api = True
            typ: PrivacyFlags
            value: bool
