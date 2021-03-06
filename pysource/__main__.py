import argparse

from pysource.pysource import get_object, print_source


def main():
    parser = argparse.ArgumentParser(description='Read Python source.')
    parser.add_argument("-m", "--module", required=True, dest='module',
                        help='module(.submodule).name')
    parser.add_argument("-p", "--pager", action='store_true', dest='use_pager',
                        help='page output (like Unix more command)')
    args = parser.parse_args()

    obj = get_object(args.module)
    print_source(obj, pager=args.use_pager)


if __name__ == '__main__':
    main()
