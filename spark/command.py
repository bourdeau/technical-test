import click
from typing import List
from spark.processor import ImageProcessor


@click.command()
@click.option('-p', '--paths', help='Comma-separated URLs or file paths')
@click.option('-o', '--operation', help='Operation to perform on the data')
def images_processing(paths: str, operation: str):
    """
    Note: I was thinking about Click and not Typer, but it doesn't make much diffrence
    """
    if operation not in {"APPEND", "COMBINE", "SUM"}:
        raise ValueError(f"Invalid operation: {operation}")

    path_list = paths.split(',') if paths else []

    if not path_list:
        raise ValueError("--paths doesn't contain any paths")

    # The Processor handles the operations
    result = ImageProcessor.run(path_list, operation)
    
    click.echo(result)
