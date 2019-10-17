======
C3Pred
======


.. image:: https://img.shields.io/pypi/v/c3pred.svg
        :target: https://pypi.python.org/pypi/c3pred

.. image:: https://img.shields.io/travis/steffenlem/c3pred.svg
        :target: https://travis-ci.org/steffenlem/c3pred

.. image:: https://readthedocs.org/projects/c3pred/badge/?version=latest
        :target: https://c3pred.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/steffenlem/c3pred/shield.svg
     :target: https://pyup.io/repos/github/steffenlem/c3pred/
     :alt: Updates


Software project of the iGEM Team Tübingen 2019
Prediction of cargo transport potential of short peptides.


* Free software: MIT license
* Documentation: https://c3pred.readthedocs.io.




Installation
------------
.. code-block:: bash

	$ git clone https://github.com/steffenlem/c3pred.git
	$ python setup.py install
	$ c3pred



Usage
-----
The CLI - Command Line Interface

.. code-block:: bash

	Usage: c3pred [OPTIONS]

	  Console script for c3pred.

	Options:
	  -s, --sequence TEXT  If the input is a FASTA protein string, please use this flag
	  -u, --uniprot TEXT   If the input is a UniProtKB accession number, please use this flag
	  -g, --igem TEXT      If the input is a iGEM Registry ID, please use this flag
	  --help               Show this message and exit.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
