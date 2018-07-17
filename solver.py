#!python3
# Author: Ibb Marsh
# Created: 2018-07-17

import sys

class WSSolver:
    def __init__ (self, argv):
        print("The letters are {}".format(','.join(list(argv[1]))))

    def run (self):
        pass


if __name__ == '__main__':
    wss = WSSolver(sys.argv)
    wss.run()
