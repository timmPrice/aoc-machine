from src import readCookie, getPuzzle, parse_puzzle
import argparse

def main():
    cookie = readCookie()
    parser = argparse.ArgumentParser(
        prog='aoc',
        description='gather aoc puzzle info and input',
        epilog='------------'
    )

if __name__ == "__main__":
    main()
