import json
from typing import Callable, List
from urllib.request import urlopen

from .rules import Rules

__all__ = ["extract_metadata"]


def extract_metadata(url: str) -> dict:
    from bs4 import BeautifulSoup

    metadata = {"request": {"url": url}, "summary": {}}
    response = urlopen(url)

    if response.status != 200:
        raise Exception(f"Invalid response status {response.status!r}")

    if url != response.geturl():
        metadata["request"]["redirects"] = response.geturl

    soup = BeautifulSoup(response.read(), "html5lib")

    for group in Rules:
        ruleset = Rules[group]
        processors: List[Callable] = ruleset.get("processors", [])

        for rule in ruleset["rules"]:
            if group in metadata["summary"]:
                break

            lookup, handler = rule
            match = soup.select_one(lookup)
            value = None

            if match:
                value = handler(match)

                for processor in processors:
                    value = processor(value)

            if value:
                metadata["summary"][group] = value

    for schema_node in soup.select('script[type="application/ld+json"]'):
        schema = json.loads(schema_node.get_text())

        if "author" in schema:
            metadata["summary"].update(
                {
                    "author": schema["author"]["name"]
                    if hasattr(schema["author"], "name")
                    else schema["author"]
                }
            )

        if "publisher" in schema:
            metadata["summary"].update(
                {
                    "publisher": schema["publisher"]["name"]
                    if hasattr(schema["publisher"], "name")
                    else schema["publisher"]
                }
            )

        if "datePublished" in schema:
            metadata["summary"].update({"date": schema["datePublished"]})

        if "image" in schema and "image" not in metadata["summary"]:
            if isinstance(schema["image"], list):
                metadata["summary"]["image"] = schema["image"][0]
            else:
                metadata["summary"]["image"] = schema["image"]

    return metadata
