from typing import Dict

import cerberus

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


async def validate(kind: str, document: Dict) -> bool:
    v = cerberus.Validator()
    return v.validate(document, schemas[kind])
