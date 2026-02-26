"""Minimal AWS Lambda project example."""

from __future__ import annotations


def lambda_handler(event: dict | None, context) -> dict:
    """Return a small greeting payload.

    Expected event format:
    {
        "name": "Ada"
    }
    """
    event = event or {}
    name = event.get("name", "World")

    return {
        "statusCode": 200,
        "body": {
            "message": f"Hello, {name}!",
            "project": "short-lambda-project",
        },
    }
