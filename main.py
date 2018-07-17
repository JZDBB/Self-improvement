import os
import argparse

import encryption

def encoding(path, keys):
    pass

def decoding(path, keys):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='face recognition demo')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--path', help='the path witch need to run', type=str)
    group.add_argument('-k', '--key', help='the key to encode or decode', type=str)
    group.add_argument('-e', '--encode', help='for encoding', action="store_true")
    parser.add_argument('-d', '--decode', help='for decoding', action="store_false")
    args = parser.parse_args()
    if args.encode:
        encoding(args.path, args.key)
    elif args.decode:
        decoding(args.path, args.key)