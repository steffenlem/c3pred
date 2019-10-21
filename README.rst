==========================================================
C3Pred - Cell-penetrating peptide activity prediction tool
==========================================================


.. image:: https://img.shields.io/pypi/v/c3pred.svg
        :target: https://pypi.python.org/pypi/c3pred


.. image:: https://readthedocs.org/projects/c3pred/badge/?version=latest
        :target: https://c3pred.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



Software project of the iGEM Team Tübingen 2019


C3Pred is an easy-to-use software tool, to predict the transport effectivity of cell-penetrating peptides (CPP).  CPPs are short 4-30 amino acids long peptides, which possess the ability to transport different cargo over the cell membrane. These cargos include proteins, nanobodies, DNA molecules, and small molecule drugs. In recent years, numerous promising clinical and pre-clinical trials have been launched, with CPPs as a carrier for pharmacologically active small molecules. C3Pred allows scientists to make design choices for their CPP-utilizing system based on quantitative transport activity scores.

C3Pred accepts three possible input formats for protein data:

* FASTA-formatted sequences
* UniProtKB Accession Number
* iGEM Part ID
C3Pred automatically fetches and parses the information about the given identifiers using the UniProt website REST API or using the iGEM Registry API, respectively.

C3Pred was released as:

* Web application with an intuitive browser-based graphical user interface (https://github.com/igemsoftware2019/Tuebingen_c3pred_webapp)
* Python package / Command-line tool (https://github.com/igemsoftware2019/Tuebingen_c3pred)




Installation and Usage
----------------------

Documentation: https://c3pred.readthedocs.io.


License
-------

Free software: MIT license


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
