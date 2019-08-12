from typing import Dict, Any

import cerberus


class ValidationError(Exception):
    pass


schemas = {
    "notes_get": {
        "id": {
            "required": True,
            "type": "string",
            "min": 36,
            "max": 36
        }
    },
    "notes_create": {
        "title": {
            "required": True,
            "type": "string",
            "min": 1,
            "max": 50
        },
        "data": {
            "required": True,
            "type": "string",
            "min": 1
        }
    },
    "notes_update": {
        "id": {
            "required": True,
            "type": "string",
            "min": 36,
            "max": 36
        },
        "title": {
            "required": False,
            "type": "string",
            "min": 1,
            "max": 50
        },
        "data": {
            "required": False,
            "type": "string",
            "min": 1
        }
    },
    "notes_delete": {
        "id": {
            "required": True,
            "type": "string",
            "min": 36,
            "max": 36
        }
    }
}


def validate(kind: str, document: Dict[str, Any]) -> None:
    v = cerberus.Validator()
    if not v.validate(document, schemas[kind]):
        raise ValidationError
