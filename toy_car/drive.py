import argparse


def main():

    parser = argparse.ArgumentParser(prog="drive")
    parser.add_argument('file', help='The input file for the robot. This file need to be placed on the root directory')

    args = parser.parse_args()

    file = open(args.file, 'r')
    lines = file.readlines()

    for i, line in enumerate(lines):
        print("Line {0}: {1}".format(i, line.strip()))

    file.close()

    print("Finish reading the file")


if __name__ == "__main__":

    print("Should not access this file this way")