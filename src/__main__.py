import argparse

from src.pysource import get_callable, print_source


def main():
    parser = argparse.ArgumentParser(description='Read Python source.')
    parser.add_argument("-m", "--module", required=True, dest='module',
                        help='module(.submodule).name')
    parser.add_argument("-p", "--pager", action='store_true', dest='use_pager',
                        help='page output (like Unix more command)')
    args = parser.parse_args()

    func = get_callable(args.module)
    print_source(func, pager=args.use_pager)


if __name__ == '__main__':
    main()
