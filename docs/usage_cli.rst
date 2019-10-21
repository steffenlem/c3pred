========================================
Usage Python Package / Command Line Tool
========================================

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

To use C3Pred in a Python script
--------------------------------

Example Python script::

    from c3pred.c3pred import *
    
    # predict using sequence string
    predict_fasta("AGYLLGKINLKALAALAKKIL")
    
    # predict using sequence string
    predict_uniprot("Q86FU0")
    
    # predict using sequence string
    predict_igem("BBa_K2660000")
