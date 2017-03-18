import os
import subprocess
import sys

class ConvertPandoc():
    def __init__(self, input_file, output_file, force=False):
        if not os.path.isfile(input_file):
            print "Input File not found"
            sys.exit(1)
        elif os.path.isfile(output_file) and not force:
            print "Output file already exists"
            sys.exit(1)
        elif input_file == output_file:
            print "Input file and output file are the same"
            sys.exit(1)

        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        subprocess.call("touch ~/tmp/test", shell=True)


if __name__ == '__main__':
    a = ConvertPandoc("README.md", "foo2")
    a.convert() 
