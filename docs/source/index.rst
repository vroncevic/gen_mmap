Create Mmap project skeleton
----------------------------

**gen_mmap** is tool for creating Mmap project skeleton.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

|gen_mmap python checker| |gen_mmap python package| |github issues| |documentation status| |github contributors|

.. |gen_mmap python checker| image:: https://github.com/vroncevic/gen_mmap/actions/workflows/gen_mmap_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_mmap/actions/workflows/gen_mmap_python_checker.yml

.. |gen_mmap python package| image:: https://github.com/vroncevic/gen_mmap/actions/workflows/gen_mmap_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_mmap/actions/workflows/gen_mmap_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_mmap.svg
   :target: https://github.com/vroncevic/gen_mmap/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_mmap.svg
   :target: https://github.com/vroncevic/gen_mmap/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-mmap/badge/?version=latest
   :target: https://gen-mmap.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

🚀 Installation
---------------

|gen_mmap python3 build|

.. |gen_mmap python3 build| image:: https://github.com/vroncevic/gen_mmap/actions/workflows/gen_mmap_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_mmap/actions/workflows/gen_mmap_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_mmap/releases

To install **gen_mmap** type the following

.. code-block:: bash

    tar xvzf gen_mmap-x.y.z.tar.gz
    cd gen_mmap-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_mmap-*-py3-none-any.whl
    rm -f get-pip.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install gen_mmap

📦 Dependencies
---------------

**gen_mmap** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-----------------

**gen_mmap** is based on OOP.

Tool structure

.. code-block:: bash

    gen_mmap/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_mmap_command_definition.py
         │   │   ├── gen_mmap_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_mmap.cfg
         │   │   ├── gen_mmap.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 44 files

✨ Features
-----------

* Automatically scaffolds C/C++ memory map (mmap) projects.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

📊 Code coverage
----------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
--------

Install package

.. code-block:: bash

    pip3 install gen_mmap

Prepare main entry point by downloading `main.py` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_mmap/main/main.py

Running tool for creating new Mmap project skeleton

.. code-block:: bash

    python3 main.py create --name mytool --type base --output ./demo/

📚 Docs
-------

More documentation and info at

* `gen_mmap.readthedocs.io <https://gen-mmap.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
---------------

`Contributing to gen_mmap <https://github.com/vroncevic/gen_mmap/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
-------------------------

Copyright (C) 2025 - 2026 by `vroncevic.github.io/gen_mmap <https://vroncevic.github.io/gen_mmap>`_

**gen_mmap** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.
