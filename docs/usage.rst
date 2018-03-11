=====
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



* Free software: MIT license
* Documentation: https://vm-cpf-validator.readthedocs.io.

