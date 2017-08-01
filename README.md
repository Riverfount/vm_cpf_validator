# CPF Validator

[![Build Status](https://travis-ci.org/Riverfount/vm_cpf_validator.svg?branch=master)](https://travis-ci.org/Riverfount/vm_cpf_validator)
[![Updates](https://pyup.io/repos/github/Riverfount/vm_cpf_validator/shield.svg)](https://pyup.io/repos/github/Riverfount/vm_cpf_validator/)
[![Python 3](https://pyup.io/repos/github/Riverfount/vm_cpf_validator/python-3-shield.svg)](https://pyup.io/repos/github/Riverfount/vm_cpf_validator/)
[![Coverage Status](https://coveralls.io/repos/github/Riverfount/vm_cpf_validator/badge.svg?branch=master)](https://coveralls.io/github/Riverfount/vm_cpf_validator?branch=master)
[![Code Health](https://landscape.io/github/Riverfount/vm_cpf_validator/master/landscape.svg?style=flat)](https://landscape.io/github/Riverfount/vm_cpf_validator/master)


This package contains four modules three to validate a Brazilian CPF and one tor format in correct form the Brazilian
 CPF. Each of modules can be used separately.
 
## Install

`pip install vm-cpf-validator`

## Usage

`from vm_cpf_validator import cpf_is_digits, cpf_has_correct_length, cpf_is_valid, format_cpf`

After import the package, follow the instructions for each functions above:

### 1. cpf_is_digits

This first module receives the Brazilian CPF and returns True if it contains only digits or False if not.

The syntax to use this module is:

```
if cpf_is_digits(value):
    print('The only contains digits')
else:
    print('The value do not contains only digits, please type it only digits')
```


### 2. cpf_has_correct_length

This second module receives the Brazilian CPF and returns True if the length of CPF is 11 or False if not.

The syntax to use this module is:

```
if cpf_has_correct_length(value):
    print('The contains 11 digits')
else:
    print('The value do not contains 11 digits, please type it a correct length of digits')
```


### 3. cpf_is_valid

This third module receives the Brazilian CPF and returns True if the CPF is valid or False if not valid.

The syntax to use this module is:

```
if cpf_is_valid(value):
    print('The CPF is valid')
else:
    print('The CPF is not valid, please type it a valid CPF')
```

### 4. format_cpf

This fourth module recives the Brazilian CPF numbers like 12345678911 and returns a valid format like 123.456.789-11.
 
 The syntax to use this module is:
 
 ```
 >>> print(format_cpf('12345678977'))
 123.456.789-11
 ```
