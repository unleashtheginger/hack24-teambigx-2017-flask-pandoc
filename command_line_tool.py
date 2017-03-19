import argparse
import os 
import sys
from FlaskPandoc import ConvertPandoc

IGNORED_DIRECTORIES = ['files_external']

OUTPUT_DIRECTORY = "/tmp/"

def transform_input_path(filepath):
    output_filepath = filepath
    return output_filepath

def calculate_ignored(to_ignore, root):
    ignored = []
    for directory in to_ignore:
        ignored.append(root+directory)
    return ignored

def walk_directories(top):
    to_ignore = calculate_ignored(IGNORED_DIRECTORIES, top)
    list_of_files = []

    for root, dirs, files in os.walk(top, topdown=True):
        for name in files:
            if root not in to_ignore:
                path = os.path.join(root, name)
                list_of_files.append(path)

    return list_of_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input", help="Input")
    parser.add_argument("-o","--output", help="Output")
    parser.add_argument("-v","--verbosity", help="Verbosity",
                        action="store_true")


    args = parser.parse_args()

    if args.verbosity:
        verbosity_level = 1
    else:
        verbosity_level = 0

    print args.input
    list_of_files = walk_directories(args.input)

    for in_file in list_of_files:
        output_file = transform_input_path(in_file)
        print output_file
        #pandoc = ConvertPandoc.ConvertPandoc(in_file, output_file)

