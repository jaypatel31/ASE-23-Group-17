import sys
from config import the
from test_runner import test
import re,ast,fileinput
from DATA import DATA
from load import naive
from ascii_table import display
import random
import time

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

def rnd(n, ndecs=2):
    if not isinstance(n, (int, float)):
        return n
    return round(n, ndecs)

def calculate_ranges(data):
    # Transpose the list of lists to get columns
    columns = list(zip(*data))
    
    # Calculate range for each column
    ranges = [(min(col), max(col)) for col in columns]
    
    ranges_string = ",".join([f"({max_val},{min_val})" for max_val, min_val in ranges])
    
    return "[" + ranges_string + "]"

def calculate_column_averages(data):
    num_columns = len(data[0])  # Assuming all inner lists have the same length
    num_rows = len(data)

    # Initialize sums for each column
    column_sums = [0] * num_columns

    # Iterate over each row and update column sums
    for row in data:
        for i in range(num_columns):
            if(len(row)>0): column_sums[i] += row[i]

    # Calculate averages for each column
    column_averages = [round(sum_column / num_rows,2) for sum_column in column_sums]

    return column_averages

def gate20(d=None, stats=None, bests=None, stat=None, best=None):
    print("#best, mid")
    print_statements = [{"st":"1. top6","data":[]},{"st":"2. top50","data":[]},{"st":"3. most","data":[]},{"st":"4. rand","data":[]},{"st":"5. mid","data":[]},{"st":"6. top","data":[]}]
    for i in range(20):
        random.seed(20*i)
        d = DATA(0)
        for row in csv(the["file"]):
            d.add(row)
        stats, bests = d.gate(4, 16, 0.5,print_statements,i)
        stat, best = stats[-1], bests[-1]
        print(rnd(best.d2h(d)), rnd(stat.d2h(d)))
    for statement in print_statements:
        # print(statement)
        for idx, dataset in enumerate(statement['data']):
            print(f"{statement['st']}:")
            print(dataset)

            # For Average
            # if(statement['st'] != "3. most"):
            #     averages = calculate_column_averages(dataset)
            #     print(f"{statement['st']} Average:")
            #     print(averages)
            # else:
            #     print(f"{statement['st']}:")
            #     print(dataset)
        # return

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
            elif(arg=="load"):
                print("Task 1:\n\n")
                display()
                print("Task 2:")
                naive()
            elif(arg=="gate20"):
                gate20()
            elif(arg=="dist"):
                dist()
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
            
def o(t, n=None):
    return "{" + ", ".join(map(str, t)) + "}"
            
def dist():
    d = DATA(0)
    for row in csv("././data/auto93.csv"): 
        d.add(row)
    
    
    r1 = d.rows[0]
    # print(r1.cells)
    rows = r1.neighbors(d)
    for i, row in enumerate(rows):
        if i % 30 == 0:
            print(i+1, o(row.cells), rnd(row.dist(r1, d)))

if __name__ == '__main__':
    main()