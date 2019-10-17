# -*- coding: utf-8 -*-

"""Console script for c3pred."""
import os
import sys
import click
import pickle
from.c3pred import predict_sequence

WD = os.path.dirname(__file__)

@click.command()
@click.option('-s', '--sequence', prompt='protein sequence',
              help='protein string in one-letter code', required=True)
def main(sequence):
    """Console script for c3pred."""
    regressor = pickle.load(open(f'{WD}/data/cpp_predictor.sav', 'rb'))
    activity = predict_sequence(sequence, regressor)
    print(activity)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
