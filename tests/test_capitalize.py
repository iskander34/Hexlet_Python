# PYTHONPATH=package_name python3 tests/test_capitalize.py

from capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

print('Все тесты пройдены!')
