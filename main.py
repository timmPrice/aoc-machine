from src.curl import * 

def main():
    cookie = readCookie()
    getPuzzle(2024, 1, cookie)

if __name__ == "__main__":
    main()

