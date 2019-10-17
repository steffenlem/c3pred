# -*- coding: utf-8 -*-

"""Console script for c3pred."""
import os
import sys
import click

WD = os.path.dirname(__file__)

@click.command()
def main(args=None):
    """Console script for c3pred."""
    click.echo("Replace this message by putting your code into "
               "c3pred.cli.main")

    with open (f'{WD}/models/heidiklim.txt', 'r') as f: contents = f.readlines()
    print(contents)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
