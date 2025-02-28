from src import readCookie, getPuzzle
import argparse

def main():
    cookie = readCookie()
    parser = argparse.ArgumentParser(
        prog='aoc',
        description='gather aoc puzzle info and input',
        epilog='that gone do it'
    )

    parser.add_argument("-g", "--get", nargs=2, metavar=("YEAR", "DAY"), type=int,
                        help = "Get puzzle input for a given year and day"
                       )

    args = parser.parse_args()

    if args.get:
        year, day = args.get
        getPuzzle(year, day, cookie)

if __name__ == "__main__":
    main()
