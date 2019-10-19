# -*- coding: utf-8 -*-

"""Console script for c3pred."""

import sys
import click
import warnings

from .c3pred import make_prediction, predict_fasta, predict_uniprot, predict_igem


@click.command()
@click.option('-s', '--sequence',  # prompt='sequence string',
              help='If the input is a FASTA protein string, please use this flag',
              required=False)
@click.option('-u', '--uniprot',  # prompt='UniProtKB accession number',
              help="If the input is a UniProtKB accession number, please use this flag",
              required=False)
@click.option('-g', '--igem',  # prompt='iGEM Registry ID',
              help="If the input is a iGEM Registry ID, please use this flag",
              required=False)
def main(sequence, uniprot, igem):
    """Console script for c3pred."""
    if not sequence and not uniprot and not igem:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

    if sequence:
        results = predict_fasta(sequence)
    elif uniprot:
        results = predict_uniprot(uniprot)
        print('UniprotID:\t' + uniprot)
    elif igem:
        results = predict_igem(igem)
        print('Registy ID:\t' + igem)

    if results.error:
        warnings.warn(results.error_type, Warning)
    else:
        print('Description:\t' + results.description)
        print('Sequence:\t' + results.sequence)
        print('Activity:\t' + str(results.activity))
        print('Activity class:\t' + results.activity_class)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
