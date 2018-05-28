from sniffer.api import *
import os

watch_paths = ['.', 'tests/']

@file_validator
def py_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

@runnable
def execute_koans(*args):
    os.system('python3 -B tests/my_string_test.py')
