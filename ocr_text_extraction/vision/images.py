"""
vision.images
~~~~~~~~~~~~~


"""
import typing

from google.cloud import vision

from ocr_text_extraction import utils

ImageLabel = typing.NamedTuple(
    "ImageLabel", [("description", str), ("score", float), ("topicality", float)]
)
ImageLabels = typing.List[ImageLabel]


def detect_labels(client: typing.Any, image: typing.Any) -> ImageLabels:
    """
    Calls Google's Cloud Vision API to detect labels in the picture.
    """
    img_labels = []
    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        img_label = ImageLabel(
            description=label.description,
            score=label.score,
            topicality=label.topicality,
        )
        img_labels.append(img_label)
    return img_labels
