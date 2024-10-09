.. Test Documentation master file, created by
   sphinx-quickstart on Tue Oct 8 19:07:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================
Voight-Kampff Test Documentation
==================================

Quickstart Guide
================

This project provides a Voight-Kampff test simulator that allows you to differentiate between humans and replicants.

**How to Run the Test:**

1. Ensure you have a valid `questions.json` file in the same directory as the script.
2. Run the test by executing the following command:

.. code-block:: bash

    $ python main.py

Running Tests
=============

To verify your code, you can run the unit tests using `pytest`. 

**How to Install `pytest`:**

If you haven't installed `pytest`, do so by running:

.. code-block:: bash

    $ pip install pytest

**How to Run Tests:**

To run the tests, execute the following command in the project directory:

.. code-block:: bash

    $ pytest

This command will automatically discover and run all tests located in the `tests/` directory.

API Documentation
=================

The following sections contain automatically generated API documentation for the modules in the project.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**Main Module:**

.. automodule:: ex00.main
   :members:
   :undoc-members:
   :show-inheritance:

**Logic Module:**

.. automodule:: ex00.logic
   :members:
   :undoc-members:
   :show-inheritance:

**Utilities Module:**

.. automodule:: ex00.utils
   :members:
   :undoc-members:
   :show-inheritance:

