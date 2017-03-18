import os
import subprocess
import sys

class ConvertPandoc():
    def __init__(self, input_file, output_file, force=False):
        if not os.path.isfile(input_file):
            print "Input File not found"
            return False
        elif os.path.isfile(output_file) and not force:
            print "Output file already exists"
            return False
        elif input_file == output_file:
            print "Input file and output file are the same"
            return False

        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        command = "pandoc -s " + self.input_file +  " -o " + self.output_file
        print command
        subprocess.call(command, shell=True)
        return True

if __name__ == '__main__':
    a = ConvertPandoc("README.md", "foo2.docx")
    a.convert() 
