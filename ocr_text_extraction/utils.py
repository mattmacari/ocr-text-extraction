import csv
import io
import pathlib
import typing

from google.cloud import vision
from prettytable import PrettyTable

CLIENT = None


def read_file(path: pathlib.Path) -> bytes:
    """
    Function to read in an image file and return the bytes

    :param path: File path
    """
    with io.open(path, "rb") as file:
        content = file.read()
    return content


def get_client():
    """
    Fetches a vision client
    """
    global CLIENT
    if CLIENT is None:
        CLIENT = vision.ImageAnnotatorClient()
    return CLIENT


def print_tabular_data(data: typing.List, field_names: typing.List):
    """
    Prints results as tabular data
    """
    tbl = PrettyTable()
    tbl.field_names = field_names
    for row in data:
        tbl.add_row(list(row))
    return tbl


def output_results(
    output_path: pathlib.Path, data: typing.List, field_names: typing.List
):
    """
    Outputs data to csv file.

    :param output_path: path to write to
    :param data: data to write
    :param field_names: field names to write
    """
    with open(output_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(field_names)
        writer.writerows(data)
