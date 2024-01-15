import sys
from config import the
from test_runner import test

def help():
    print("OPTIONS:")
    print("  -c --cohen    small effect size               = .35")
    print("  -f --file     csv data file name              = ../data/auto93.csv")
    print("  -h --help     show help                       = false")
    print("  -k --k        low class frequency kludge      = 1")
    print("  -m --m        low attribute frequency kludge  = 2")
    print("  -s --seed     random number seed              = 31210")
    print("  -t --test     test the Classes                = test")
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
    elif arg == "-t" or arg == "--test":
        test()
        return "test"
    else:
        print("Unknown option, please run -h (or) --help for more details.")
        return False

def main():
    args = sys.argv[1:]
    next_value = False
    option_details = ''
    for arg in args:
        if option_details == "test":
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
    print(the)
        
main()
