======================================
Usage Python Package/Command-line tool
======================================

The CLI - Command Line Interface
--------------------------------


.. code-block:: bash

	Usage: c3pred [OPTIONS]

	  Console script for c3pred.

	Options:
	  -s, --sequence TEXT  If the input is a FASTA protein string, please use this flag
	  -u, --uniprot TEXT   If the input is a UniProtKB accession number, please use this flag
	  -g, --igem TEXT      If the input is a iGEM Registry ID, please use this flag
	  --help               Show this message and exit.

How to use C3Pred in a Python script
--------------------------------

Example Python script::

    from c3pred.c3pred import *
    
    # predict using sequence string
    example_1 = predict_fasta("AGYLLGKINLKALAALAKKIL")
    
    # predict using sequence string
    example_2 = predict_uniprot("Q86FU0")
    
    # predict using sequence string
    example_3 = predict_igem("BBa_K2660000")

The functions **predict_fasta()**, :**predict_uniprot()**, **predict_igem()** return a "Results" object:

**Results object**:

:sequence: str - sequence string
:activity: float - activity score
:activity_class: str - classification for activity ("low/none"/"medium"/"high")
:description: str - description of the sequence (if available for Uniprot ID, iGEM ID)
:error: boolean - describes whether the prediction was successful
:error_type: str - if an error occured, the error message is stored here


