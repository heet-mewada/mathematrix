#imports
import random
import sympy
import matplotlib as mpl
import appdirs
import tinydb

grade = input("What grade do you wish to tackle?")

match grade:
    case "1st":
        print("executing 1st grade")
        #subprocess.run(["python", "src/modules/grade/1stgrade.py"])
    case _:
        print("invalid")
