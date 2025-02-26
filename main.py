import requests 
import os

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

def save_file(response, year, day, is_input):
    home = os.path.expanduser("~")

    print(home)
    if is_input:
        url = f"{home}/repos/aoc/{year}/day{day}/input.txt"  
    else:
        url = f"{home}/repos/aoc/{year}/day{day}/puzzle.txt"
   
    directory = os.path.dirname(url)

    if not os.path.exists(directory):
        print(f"{directory} does not exist. making directory")
        os.makedirs(directory, exist_ok=True)

    try: 
        with open(url, "w") as f:
            f.write(response.text)
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

# retrieves the puzzle and the input for the given day
def getPuzzle(year, day, cookie): 
    input_url = makeUrl(year, day, True)
    puzzle_url = makeUrl(year, day, False)

    input_reposnse = getFile(cookie, input_url) 
    save_file(input_reposnse, year, day, True)
    
    puzzle_reposnse = getFile(cookie, puzzle_url) 
    save_file(puzzle_reposnse, year, day, False)

def main():
    cookie = readCookie()
    getPuzzle(2024, 1, cookie)

if __name__ == "__main__":
    main()
