bytesinsert
===========

Description
-----------

A library allows to insert one piece of code into another piece of code
secretly, without changing line numbers.

The current version supports only **Python 3.6**. Also it allows to
insert only functions without arguments.

Usage
-----

A library has a useful function ``insert_code``, which inserts which
takes the original code, the code to insert and line number for
insertion. The simplest example of usage from the ``examples``
directory:

.. code:: python

    from bytesinsert import insert_code


    def hello():
        print("1")
        print("3")


    def new_code():
        print("2")


    code_orig = hello.__code__
    code_to_insert = new_code.__code__
    success, result = insert_code(code_orig, code_to_insert, 6)
    if success:
        exec(result)

The resulting output will be:

::

    1
    2
    3

The ``insert_code`` function inserted code from the function
``new_code`` into the function ``hello`` by updating its bytecode.

Install
-------

This library can be easily installed with pip:

``pip install bytesinsert``
