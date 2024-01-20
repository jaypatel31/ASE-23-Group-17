import sys
from config import the
from test_runner import test
import re,ast,fileinput
from DATA import DATA

def help():
    print("OPTIONS:")
    print("  -c --cohen    small effect size               = .35")
    print("  -f --file     csv data file name              = ././data/auto93.csv")
    print("  -h --help     show help                       = false")
    print("  -k --k        low class frequency kludge      = 1")
    print("  -m --m        low attribute frequency kludge  = 2")
    print("  -s --seed     random number seed              = 31210")
    print("  -t --todo     todo an action command          = todo")
    sys.exit(0)

def get_option_(arg):
    if arg == "-c" or arg == "--cohen":
        return "cohen"
    elif arg == "-f" or arg == "--file":
        return "file"
    elif arg == "-h" or arg == "--help":
        help()
        return False
    elif arg == "-s" or arg == "--seed":
        return "seed"
    elif arg == "-t" or arg == "--todo":
        # test()
        return "todo"
    else:
        print("Unknown option, please run -h (or) --help for more details.")
        return False




def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]

def dstats():
    # Load Data
    data = DATA(0)
    for row in csv(the["file"]): 
        data.add(row)


    print(data.stats())
    


    sys.exit(0)

def main():
    args = sys.argv[1:]
    # print("args",args)
    next_value = False
    option_details = ''
    for arg in args:
        if option_details == "todo":
            if(arg=="stats"): dstats()
            else: test(arg)
            option_details = ""
            next_value = False
            continue
        if next_value == True:
            the[option_details] = arg
            next_value = False
            continue
        option_details = get_option_(arg)
        if option_details != False:
            next_value = True
            continue
        else:
            sys.exit(0)

    # print(the)

if __name__ == '__main__':
    main()        

