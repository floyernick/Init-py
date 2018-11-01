from typing import Dict

import cerberus

schemas = {
    "notes_get": {
        "note_id": {
            "required": True,
            "type": "string",
            "min": 36,
            "max": 36
        }
    },
    "notes_create": {
        "note_title": {
            "required": True,
            "type": "string",
            "min": 1,
            "max": 50
        },
        "note_data": {
            "required": True,
            "type": "string",
            "min": 1
        }
    },
    "notes_update": {
        "note_id": {
            "required": True,
            "type": "string",
            "min": 36,
            "max": 36
        },
        "note_title": {
            "required": True,
            "type": "string",
            "min": 1,
            "max": 50
        },
        "note_data": {
            "required": True,
            "type": "string",
            "min": 1
        }
    },
    "notes_delete": {
        "note_id": {
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
