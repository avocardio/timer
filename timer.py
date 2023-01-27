import time
import sys
import os
import argparse

# File for making an importable function, that when called, ie. when in the new
# file executed with an arg -t, will copy the contents of the file to a new file
# wrapped around a time function.

def timer():

    def get_args():
        parser = argparse.ArgumentParser(description='Read a file with time tracking')
        parser.add_argument('-t', '--timeit', action='store_true', help='Time the file')
        args = parser.parse_args()
        return args

    def get_current_file():
        return sys.argv[0]

    def read_file(file):
        with open(file, 'r') as f:
            lines = f.readlines()
            lines = [line for line in lines if not line.startswith('timer()')] # Not today recursion!
            lines = [line for line in lines if not line.startswith('from timer import timer')]
        return lines

    def time_file(file):
        lines = read_file(file)
        with open('time_' + file, 'w') as f:
            f.write('import time \n')
            f.write('start = time.time() \n')
            for line in lines:
                f.write(line)
            f.write('\nend = time.time()')
            f.write('\nprint("Total time:",round(end - start,5))')

    def execute_file(file):
        os.system('python3 ' + file)

    def delete_file(file):
        os.remove(file)

    if get_args().timeit:
        time_file(get_current_file())
        execute_file('time_' + get_current_file())
        delete_file('time_' + get_current_file())
        sys.exit(0)