import logging

import click

import ocr_text_extraction.utils as utils
from ocr_text_extraction import client
from ocr_text_extraction.vision import detect_labels, generate_image, parse_document

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@click.command(name="label-image")
@click.option("-f", "--file-path", type=click.Path(), required=True)
@click.option("-o", "--output", type=click.Path(), required=False)
@click.option("-v", "--verbose", required=False, is_flag=True)
def label_image(file_path, output=None, verbose=False):
    """
    Command to label an image
    """
    if verbose:
        click.echo(f"Generating image labels for {file_path}")
    img = generate_image(path=file_path)
    labels = detect_labels(client=client, image=img)
    header = ["Label", "Score", "Topicality"]
    if verbose:
        click.echo("Label Results")
        tbl = utils.print_tabular_data(data=labels, field_names=header)
        click.echo(tbl)
    if output is not None:
        # write out output as csv
        utils.output_results(output_path=output, data=labels, field_names=header)


@click.command(name="parse-document")
@click.option("-f", "--file-path", type=click.Path(), required=True)
@click.option("-o", "--output", type=click.Path(), required=False)
@click.option("-v", "--verbose", required=False, is_flag=True)
def parse_text_documemt(file_path, output=None, verbose=False):
    """
    Command to parse text from a document.
    """
    if verbose:
        click.echo(f"Generating text data for document {file_path}")
    img = generate_image(path=file_path)
    text_data = parse_document(client=client, image=img)
    if verbose:
        click.echo("Document results")
        for line in text_data.split_text:
            click.echo(line)
    if output is not None:
        with open(output, "w") as f:
            f.write(text_data.raw_text)


# Configure commands
cli.add_command(label_image)
cli.add_command(parse_text_documemt)


if __name__ == "__main__":
    cli()
