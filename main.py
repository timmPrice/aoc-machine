import requests 

def readCookie():
    env = open('./.env', 'r')
    line = env.readlines() 
    the_cookie = line[0].strip()
    return the_cookie 

def makeUrl(year, day, isInput):
    if isInput:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
    else: 
        url = f"https://adventofcode.com/{year}/day/{day}"
    return url

def getFile(cookie, url):
    headers = {"Cookie": f"session={cookie}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("successfully retrieved file")
    else:
        print(f"Error: {response.status_code}")
        return

    return response

def saveFile(response, year, day):
    puzzle_info = f"~/repos/advent-of-code/{year}/day{day}/input.txt"
    puzzle_input = f"~/repos/advent-of-code/{year}/day{day}/input.txt"

def main():
    cookie = readCookie()
    url = makeUrl(2024, 1, True)  
    getFile(cookie, url)

if __name__ == "__main__":
    main()
