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
    if is_input:
        url = f"~/repos/aoc/{year}/day{day}/input.txt"  
    else:
        url = f"~/repos/aoc/{year}/day{day}/puzzle.txt"
    
    url = os.path.expanduser(url)
    directory = os.path.dirname(url)

    if not os.path.expanduser(url):
        print(f"Error: Directory {directory} does not exist.")
        os.makedirs(directory, exist_ok=True)
    try: 
       open(url, "w").write(response.text)
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

def main():
    cookie = readCookie()
    url = makeUrl(2024, 1, True)  
    response = getFile(cookie, url)
    save_file(response, 2024, 1, True)

if __name__ == "__main__":
    main()
