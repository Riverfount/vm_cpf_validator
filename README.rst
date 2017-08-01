CPF Validator
=============

.. image:: https://travis-ci.org/Riverfount/vm_cpf_validator.svg?branch=master
    :target: https://travis-ci.org/Riverfount/vm_cpf_validator

.. image:: https://pyup.io/repos/github/Riverfount/vm_cpf_validator/shield.svg
     :target: https://pyup.io/repos/github/Riverfount/vm_cpf_validator/
     :alt: Updates

.. image:: https://pyup.io/repos/github/Riverfount/vm_cpf_validator/python-3-shield.svg
     :target: https://pyup.io/repos/github/Riverfount/vm_cpf_validator/
     :alt: Python 3

.. image:: https://coveralls.io/repos/github/Riverfount/vm_cpf_validator/badge.svg?branch=master
     :target: https://coveralls.io/github/Riverfount/vm_cpf_validator?branch=master
     :alt: Coverage


.. image:: https://landscape.io/github/Riverfount/vm_cpf_validator/master/landscape.svg?style=flat
   :target: https://landscape.io/github/Riverfount/vm_cpf_validator/master
   :alt: Code Health


This package contains four modules three to validate a Brazilian CPF and one to format in correct form the Brazilian
 CPF. Each of modules can be used separately.

Install
=======

::

   pip install vm-cpf-validator

Usage
=====

::

   from vm_cpf_validator import cpf_is_digits, cpf_has_correct_length, cpf_is_valid, format_cpf

After import the package, follow the instructions for each function below:

1. cpf\_is\_digits
------------------

This first module receives the Brazilian CPF and returns True if it
contains only digits or False if not.

The syntax to use this function is:

::

    if cpf_is_digits(value):
        print('The only contains digits')
    else:
        print('The value do not contains only digits, please type it only digits')

2. cpf\_has\_correct\_length
----------------------------

This second module receives the Brazilian CPF and returns True if the
length of CPF is 11 or False if not.

The syntax to use this function is:

::

    if cpf_has_correct_length(value):
        print('The contains 11 digits')
    else:
        print('The value do not contains 11 digits, please type it a correct length of digits')

3. cpf\_is\_valid
-----------------

This third module receives the Brazilian CPF and returns True if the CPF
is valid or False if not valid.

The syntax to use this function is:

::

    if cpf_is_valid(value):
        print('The CPF is valid')
    else:
        print('The CPF is not valid, please type it a valid CPF')

4. format\_cpf:
---------------

This fourth module receives the Brazilian CPF numbers as 12345678911 and returns the valid format as 123.456.789-11.

The syntax to use this function is:

::

  >>>print(format_cpf('12345678911'))
  123.456.789-11
