import cowsay as cow
import sys


if len(sys.argv) == 2:
    cow.cow("heloo" + ' " ' + sys.argv[1])
