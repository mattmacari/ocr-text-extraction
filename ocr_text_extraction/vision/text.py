"""
ocr_text_extraction.vision.text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module that calls Google's Cloud Vision API for handwriting extraction.
"""
from google.cloud import vision
import typing

ParsedDocument = typing.NamedTuple(
    "ParsedDocument", [("raw_text", str), ("split_text", typing.List[str])]
)


def detect_document(client: typing.Any, image: typing.Any):
    """
    Detects text data in a document.
    """
    response = client.document_text_detection(image=image)
    return response.full_text_annotation.text


def parse_document(client: typing.Any, image: typing.Any) -> ParsedDocument:
    """
    Detects the data within the document, and then returns a list representing the document.
    """
    text = detect_document(client=client, image=image)
    return ParsedDocument(raw_text=text, split_text=text.split("\n"))
