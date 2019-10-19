# -*- coding: utf-8 -*-
import pickle
import re

import numpy as np
import warnings
import os

from .results import Results

from .parsing import get_registry_info, parse_uniprot


def do_padding(seq, window_size=10):
    if len(seq) >= window_size:
        return seq
    else:
        while len(seq) < window_size:
            current_length = len(seq)
            if current_length % 2 == 0:
                seq = "X" + seq
            else:
                seq = seq + "X"
        return seq


def blomap_extra_encode(amino_sequence):
    blomap_physicochemical = {
        'A': [-0.57, 0.39, -0.96, -0.61, -0.69, 1, 71, 6.0, 0.806, 0.0, 10.0],
        'R': [-0.40, -0.83, -0.61, 1.26, -0.28, 4, 156, 10.8, 0.000, 52.0, 32.6],
        'N': [-0.70, -0.63, -1.47, 1.02, 1.06, 3, 114, 5.4, 0.448, 3.4, 20.4],
        'D': [-1.62, -0.52, -0.67, 1.02, 1.47, 3, 115, 3.0, 0.417, 49.7, 18.3],
        'C': [0.07, 2.04, 0.65, -1.13, -0.39, 2, 103, 5.0, 0.721, 1.5, 3.8],
        'Q': [-0.05, -1.50, -0.67, 0.49, 0.21, 4, 128, 5.7, 0.430, 3.5, 24.7],
        'E': [-0.64, -1.59, -0.39, 0.69, 1.04, 4, 129, 3.2, 0.458, 49.9, 15.8],
        'G': [-0.90, 0.87, -0.36, 1.08, 1.95, 0, 57, 6.0, 0.770, 0.0, 7.6],
        'H': [0.73, -0.67, -0.42, 1.13, 0.99, 3, 137, 7.6, 0.548, 51.6, 12.3],
        'I': [0.59, 0.79, 1.44, -1.90, -0.93, 3, 113, 6.0, 1.000, 0.2, 7.0],
        'L': [0.65, 0.84, 1.25, -0.99, -1.90, 3, 113, 6.0, 0.918, 0.1, 7.7],
        'K': [-0.64, -1.19, -0.65, 0.68, -0.13, 4, 128, 9.7, 0.263, 49.5, 34.3],
        'M': [0.76, 0.05, 0.06, -0.62, -1.59, 4, 131, 5.7, 0.811, 1.4, 7.2],
        'F': [1.87, 1.04, 1.28, -0.61, -0.16, 3, 147, 5.5, 0.951, 0.4, 8.1],
        'P': [-1.82, -0.63, 0.32, 0.03, 0.68, 1, 97, 6.3, 0.678, 1.6, 12.8],
        'S': [-0.39, -0.27, -1.51, -0.25, 0.31, 2, 87, 5.7, 0.601, 1.7, 12.9],
        'T': [-0.04, -0.30, -0.82, -1.02, -0.04, 2, 101, 5.6, 0.634, 1.6, 15.1],
        'W': [1.38, 1.69, 1.91, 1.07, -0.05, 3, 186, 5.9, 0.854, 2.1, 10.3],
        'Y': [1.75, 0.11, 0.65, 0.21, -0.41, 3, 163, 5.7, 0.714, 1.6, 18.3],
        'V': [-0.02, 0.30, 0.97, -1.55, -1.16, 2, 99, 6.0, 0.923, 0.1, 7.2],
        'X': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # unknown amino acids
        'Z': [-0.345, -1.545, -0.53, 0.59, 0.625, 4.0, 128.5, 4.45, 0.444, 26.7, 20.25],  # Glutamic acid or Glutamine,
        'U': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Selenocysteine
        'O': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Pyrrolysine
        'B': [-1.16, -0.575, -1.07, 1.02, 1.265, 3.0, 114.5, 4.2, 0.4325, 26.55, 19.35],  # Aspartic acid or Asparagine
        'J': [0.62, 0.815, 1.345, -1.445, -1.415, 3.0, 113.0, 6.0, 0.959, 0.15, 7.35]  # Leucine or Isoleucine
    }

    translated_sequence = list()
    for amino_acid in amino_sequence:
        if amino_acid in ['J', 'B', 'O', 'U', 'Z']:
            warnings.warn("non-standard amino acid in seqeunce", Warning)
        translated_sequence.extend(blomap_physicochemical[amino_acid.upper()])
    return translated_sequence


def make_prediction(input_sequence):
    WD = os.path.dirname(__file__)
    regr = pickle.load(open(f'{WD}/data/cpp_predictor.sav', 'rb'))
    input_sequence = input_sequence.upper()
    window_size = 14
    if len(input_sequence) > window_size:
        pred_kmer_values = []
        for kmer in [input_sequence[i:i + window_size] for i in range(len(input_sequence) - (window_size - 1))]:
            pred_kmer_values.append(regr.predict(np.asarray([blomap_extra_encode(kmer)]))[0])
        return 2 ** np.mean(np.asarray(pred_kmer_values))

    else:
        seq_paddded = do_padding(input_sequence, window_size=window_size)
        return 2 ** regr.predict(np.asarray([blomap_extra_encode(seq_paddded)]))[0]


def get_activity_class(activity):
    medium_border = 40.1550  # 50 percentile
    high_border = 80.0838  # 75 percentile
    if activity >= high_border:
        return "high"
    elif activity >= medium_border:
        return "medium"
    else:
        return "low/none"


def predict_fasta(sequence):
    if re.match("^[a-zA-Z]*$", sequence):
        if len(sequence) <= 40:
            if len(sequence) >= 4:
                activity = make_prediction(sequence)
                activity_class = get_activity_class(activity)
                return Results(error=False, error_type=None, description="", sequence=sequence, activity=activity,
                               activity_class=activity_class)
            else:
                return Results(error=True, error_type="sequence is too short", description="",
                               sequence=sequence, activity=None)
        else:
            return Results(error=True, error_type="sequence is too long", description="",
                           sequence=sequence, activity=None)
    else:
        return Results(error=True, error_type="Sequence string contains non-valid characters", description="",
                       sequence=sequence, activity=None)


def predict_uniprot(uniprot):
    unip_info = parse_uniprot(uniprot)
    if unip_info.error:
        return unip_info
    else:
        activity = make_prediction(unip_info.sequence)
        unip_info.activity = activity
        activity_class = get_activity_class(activity)
        unip_info.activity_class = activity_class
        return unip_info


def predict_igem(igem):
    reg_info = get_registry_info(igem)
    if reg_info.error:
        return reg_info
    else:
        activity = make_prediction(reg_info.sequence)
        reg_info.activity = activity
        activity_class = get_activity_class(activity)
        reg_info.activity_class = activity_class
        return reg_info
