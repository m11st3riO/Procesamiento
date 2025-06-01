import sys
from src.Tarea_1 import tarea_1


def main(options):
    if options[1] == "tarea_1":
        tarea_1()
    else:
        print("Please give a frequency. Example: python main.py act_2 2")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")
