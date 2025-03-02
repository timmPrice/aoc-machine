## Advent - Of - Code Machine ~ CLI TOOL
### Usage - aoc command
- [ ] {-h, --help} provides a list of available commands
- [x]  {-g, --get} uses aoc website cookie to retrieve puzzle input and puzzle instructions
    - [x]  parses puzzle instructions to make them more readable
- [ ] submit puzzle solutions throught the terminal - Coming Soon!
- [ ] choose puzzle download locations - Coming soon - For now make a `~/repos/aoc` directory... or it will make one for you (if you already have one it should still work fine although this isn't throughly tested) 

### Instructions
- run the setup script provided
- in the .env file that was created... paste *just* the cookie and only the cookie... Make sure there are no spaces or \n end characters in the line.
- test the aoc command that was symlinked into your path... better path finding is coming soon so you may have to adjust where it is linked to or what which paths are in your $PATH

#### To get your accounts website cookie
- log in to [advent of code](https://adventofcode.com/)
- inspect the page, refresh on the network tab, inspect any of the returned network request and view the cookie value in the cookie tab of the network page
