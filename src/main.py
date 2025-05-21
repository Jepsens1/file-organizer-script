import argparse
from filemanager import FileManager


def main():
    parser = argparse.ArgumentParser(prog='File organizer', description='Sorts files to their respective folders')
    parser.add_argument('folderpath', type=str)
    parser.add_argument('-r', '--recursive', action='store_true')
    parser.add_argument('-p', '--preview', action='store_true')

    args = parser.parse_args()
    fm = FileManager(args.folderpath, args.recursive)
    if args.preview:
        fm.sort_preview()
    else:
        fm.sort_files()


if __name__ == "__main__":
    main()
