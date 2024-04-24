import sys
from config import the
from test_runner import test
import re,ast,fileinput
from DATA import DATA
from load import naive
from RANGE import RANGE
from SYM import SYM
from RULES import RULES
from ascii_table import display
import random
import time
import math
from ROW import ROW
from raise_utils.interpret import ScottKnott

from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import normalize
import pandas as pd

from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt
import timeit


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
                print("Task 1: Get Distance Working: \n")
                dist()
            elif(arg=="far"):
                print("Task 2: Get Far Working: \n")
                far()
            elif(arg=="cluster"):
                tree()
                print("")
                eg_branch()
                print("")
                eg_doubletap()
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
    rows = r1.neighbors(d)
    for i, row in enumerate(rows):
        if i % 30 == 0:
            print(i+1, o(row.cells), rnd(row.dist(r1, d)))

def far():

    d = DATA(0)
    for row in csv("././data/auto93.csv"):  # Load the dataset
        d.add(row)


    a, b, C, eval = d.farapart(d.rows)
    target_distance = 0.95
    current_distance = 0
    attempts = 0
    max_attempts = 1000  # Prevent infinite loops
    total_rows = len(d.rows)
    #print(total_rows)

    while abs(current_distance - target_distance) > 0.01 and attempts < max_attempts:
        # sampled_rows = random.sample(d.rows, total_rows)  # Sample without replacement
        a, b, C, _ = d.farapart(d.rows)
        current_distance = C
        attempts += 1
        
    if attempts == max_attempts:
        print("Failed to find rows with the desired distance after maximum attempts.")
    
    print(o(a), o(b), f"distance = {round(C,4)}", f"Attempts: {attempts}",sep='\n')

def eg_branch():
    print("Task-2: ")
    d = DATA(0)
    for row in csv("././data/auto93.csv"):  # Load the dataset
        d.add(row)
    best, rest, evals = d.branch()
    print("centroid of output cluster:")
    print(o(best.mid().cells,2))
    print(evals)

def eg_doubletap():
    print("Task-3: ")
    d = DATA(0)
    for row in csv("././data/auto93.csv"):  # Load the dataset
        d.add(row)
    best1, rest, evals1 = d.branch(32)
    best2, _, evals2 = best1.branch(4)
    print(o(best2.mid().cells,2), o(rest.mid().cells,2))
    print(evals1 + evals2)

def many(t, n=None):
    if n is None:
        n = len(t)
    return [random.choice(t) for _ in range(n)]

def o(t, n=None, u=None):
        if isinstance(t, (int, float)):
            return str(round(t, n))
        if not isinstance(t, dict) and not isinstance(t, list):
            return str(t)

        u = []
        for k, v in t.items() if isinstance(t, dict) else enumerate(t):
            if str(k)[0] != "_":
                if len(t) > 0:
                    u.append(o(v, n))
                else:
                    u.append(f"${o(k, n)}: ${o(v, n)}")
        

        return u


# def tree(t=None, evals=None):
    # d = DATA(0)
    # print("Task-1: ")
    # for row in csv("././data/auto93.csv"):  # Load the dataset
    #     d.add(row)
    # t, evals = d.tree(True)
    # t.show()
    # print(evals)

def details(d):
    print(f"names\t\t {o(d.cols.names.cells)}\t D2h--")
    print(f"mid\t\t {o(d.mid().cells,2)}\t {round(d.mid().d2h(d),2)}")
    print(f"div\t\t {o(d.div().cells,2)}\t {round(d.div().d2h(d),2)}")

def stats(d):
    print(f"date: {time.strftime('%x %X')}")
    print(f"file: {the['file']}")
    print(f"repeats : 20")
    print(f"seed: {the['seed']}")
    print(f"rows: {len(d.rows)}")
    print(f"cols: {len(d.cols.names.cells)}")


def any50(d):
    random.seed(the.seed)
    rows = d.rows[:]  # Copying the list
    random.shuffle(rows)
    
    for i in range(0, 50):
        print(f"any50:\t\t {o(rows[i].cells,n=2)} \t {round(rows[i].d2h(d),2)}")
        
def evaluate_all(d):
  rows = d.rows[:]
  rows.sort(key=lambda row: row.d2h(d))
  print(f"100%:\t\t {o(rows[0].cells,n=2)} \t {round(rows[0].d2h(d),2)}")
  
def smo9(d):
  budget0 = 4
  budget = 5
  some = 0.5
  return d.smo9(budget0,budget,some)

def oo(x):
    print(o(x))
    return x

def _ranges(cols, rowss):
    t = []
    for col in cols:
        for range_ in _ranges1(col, rowss):
            t.append(range_)
    return t

def _ranges1(col, rowss):
    out, nrows = {}, 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in rows:
            x = row.cells[col.at]
            if x != "?":
                bin_ = col.bin(x)
                out[bin_] = out.get(bin_, RANGE(col.at, col.txt, x))
                out[bin_].add(x, y)
    
    out = list(out.values())
    out.sort(key=lambda a: a.x['lo'])
    return out if isinstance(col, SYM) else _mergeds(out, nrows / the.bins)

def _mergeds(ranges, tooFew):
    t = []
    i = 0
    while i < len(ranges):
        a = ranges[i]
        if i < len(ranges) - 1:
            both = a.merged(ranges[i + 1], tooFew)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1
    if len(t) < len(ranges):
        return _mergeds(t, tooFew)
    for i in range(1, len(t)):
        t[i].x['lo'] = t[i - 1].x['hi']
    t[0].x['lo'] = -math.inf
    t[-1].x['hi'] = math.inf
    return t

def bins(d):
    best, rest, evals = d.branch()
    like = best.rows
    hate = random.sample(rest.rows, 3 * len(like))
    t = []

    def score(range_obj):
        return range_obj.score("LIKE", len(like), len(hate))

    for col in d.cols.x:
        print("")
        for range_obj in _ranges1(col, {"LIKE": like, "HATE": hate}):
            print(range_obj)
            t.append(range_obj)

    t.sort(key=lambda x: score(x), reverse=True)
    max_score = score(t[0])
    print("\n#scores:\n")
    for v in t[:the.Beam]:
        if score(v) > max_score * 0.1:
            print(round(score(v),2), v)
    print({"LIKE": len(like), "HATE": len(hate)})

def eg_rules(d):
    for xxx in range(1, 2):
        # best, rest = d:branch()
        best0, rest, evals1 = d.branch(the.d)
        best, _, evals2 = best0.branch(the.D)
        print(evals1 + evals2 + the.D - 1)
        LIKE = best.rows
        random.sample(rest.rows, 3 * len(LIKE))
        HATE = random.sample(rest.rows, 3 * len(LIKE))
        rowss = {"LIKE": LIKE, "HATE": HATE}
        print("score", "\t\t\t" ,"mid selected", "\t\t\t\t\t", "rules")
        print("_____", "\t" ,"__________________________________________________", "\t", "__________________")
        print("")
        for rule in RULES(_ranges(d.cols.x, rowss), "LIKE", rowss).sorted:
            result = d.clone(rule.selects(rest.rows))
            if len(result.rows) > 0:
                result.rows.sort(key=lambda a: a.d2h(d))
                print(round(rule.scored,2), "\t" ,o(result.mid().cells), "\t", rule.show())

def kmeans_20(d):
    bests = []
    for i in range(1):
        rows = d.rows[:]
        
        # Only for health Dataset
        for row in rows:
            # in row.cells[7] if absolute_error make it 0, sqaured_error make it 1  else 
            if(row.cells[7]=="absolute_error"):
                row.cells[7] = 0
            elif(row.cells[7]=="squared_error"):
                row.cells[7] = 1
            else:
                row.cells[7] = 2
        
        X = np.array([np.array(row.cells) for row in d.rows[1:]])

        # Elbow Method
        # wcss = []
        # for i in range(1, 21):
        #     kmeans = KMeans(n_clusters=i, max_iter=300, n_init=10, random_state=0)
        #     kmeans.fit(X)  # X is your data
        #     wcss.append(kmeans.inertia_)

        # plt.plot(range(1, 21), wcss)
        # plt.title('Elbow Method')
        # plt.xlabel('Number of clusters')
        # plt.ylabel('WCSS')
        # plt.show()

        kmeans = KMeans(n_clusters = 3, n_init = 100).fit(X)

        predections = kmeans.predict(X)
        clusters = {}
        for i in range(len(predections)):
            if predections[i] not in clusters:
                d_new = DATA(0)
                d_new.add(d.cols.names.cells)
                clusters[predections[i]] = d_new
            clusters[predections[i]].add(X[i])


        def calculate_mid_d2h(cluster):
            mid_value = cluster.mid()  # Assuming mid() returns the midpoint of the cluster
            d2h_value = mid_value.d2h(cluster)  # Assuming d2h() calculates a distance metric
            return d2h_value
        

        # Sort clusters based on the mid().d2h() value
        sorted_clusters = list(clusters.values())

        # Sort clusters based on the mid().d2h() value
        sorted_clusters.sort(key=calculate_mid_d2h)

        sorted_clusters[0].rows.sort(key=lambda row: row.d2h(d))
        bests.append(sorted_clusters[0].rows[0].d2h(d))
        # print(sorted_clusters[0].rows[0].d2h(d))

    return bests

def dbscan_20(d):
    # Process the data
    bests = []
    start_eps = 50
    end_eps = 100
    for i in range(1):
        rows = d.rows[:]

        # Only for health Dataset
        for row in rows:
            # Map row.cells[7] to numeric values based on your conditions
            if row.cells[7] == "absolute_error":
                row.cells[7] = 0
            elif row.cells[7] == "squared_error":
                row.cells[7] = 1
            else:
                row.cells[7] = 2
        
        # Extract the feature vectors
        X = np.array([np.array(row.cells) for row in d.rows[1:]])

        # neighbors = NearestNeighbors(n_neighbors=22)
        # neighbors_fit = neighbors.fit(X)
        # distances, indices = neighbors_fit.kneighbors(X)
        # eps_value = 100 + 3.0 * i

        eps_value = start_eps + (end_eps - start_eps) * (i / 20)

        # # Perform DBSCAN clustering
        dbs = DBSCAN(eps=eps_value, min_samples=44).fit(X)

        # distances = np.sort(distances, axis=0)
        # distances = distances[:,1]
        # plt.plot(distances)
        # plt.show()
        
        # Retrieve cluster labels and core sample indices
        labels = dbs.labels_


        #Organize clusters into dictionaries
        clusters = {}
        for i, label in enumerate(labels):
            if label == -1:
                continue
            if label not in clusters:
                d_new = DATA(0)  # Assuming DATA(0) is a placeholder for a new dataset
                d_new.add(d.cols.names.cells)
                clusters[label] = d_new
            clusters[label].add(X[i])

        print(len(clusters))
        

        def calculate_mid_d2h(cluster):
            mid_value = cluster.mid()  # Assuming mid() returns the midpoint of the cluster
            d2h_value = mid_value.d2h(cluster)  # Assuming d2h() calculates a distance metric
            return d2h_value
        

        # Sort clusters based on the mid().d2h() value
        sorted_clusters = list(clusters.values())
        sorted_clusters.sort(key=calculate_mid_d2h)
        sorted_clusters[0].rows.sort(key=lambda row: row.d2h(d))
        bests.append(sorted_clusters[0].rows[1].d2h(d))

    return bests

def rrp_20(d,elem):
    bests = []
    for i in range(1):
        best, rest, evals = d.branch(elem)
        rows = best.rows[:]
        rows.sort(key=lambda row: row.d2h(d))
        bests.append(rows[0].d2h(d))
    return bests

def run_smo_20(d,elem):
    stats = []
    bests_all = []
    budget0 = 4
    budget = elem
    some = 0.5
    for i in range(1):
        random.seed(20*i)
        stats, bests = d.smo9(budget0, budget, some)
        stat, best = stats[-1], bests[-1]
        bests_all.append(best.d2h(d))
        # print(rnd(best.d2h(d)), rnd(stat.d2h(d)))
    return bests_all

def plot_running_times():
    algorithm_names = ['SMO9', 'SMO24', 'SMO32', 'SMO64', 'RRP9', 'RRP24', 'RRP32', 'RRP64', 'KMeans', 'DBSCAN']
    running_times = [0.08864763975143433, 0.3944209575653076, 0.5034198522567749, 0.9677125453948975, 0.04634635448455811, 0.044590091705322264, 0.045543551445007324, 0.044534814357757566, 19.19049354791641, 0.06285688877105713]

    # divide running times by 20
    running_times = [time / 20 for time in running_times]

    # in print keep int value limited to three decimal point
    def prt(x):
        return round(x,3)
    

    plt.bar(algorithm_names, running_times, color=['blue', 'green', 'red'])  # Adjust colors as needed
    plt.title('Running Times of Different Algorithms on DTLZ Dataset')
    plt.xlabel('Algorithms')
    plt.ylabel('Running Time (seconds)')
    plt.show()
    running_times = [prt(x) for x in running_times]
    print(running_times)


def randN(d, n):
    random.seed(the.seed)
    randArr = []
    for i in range(20):
        rows = d.rows[:]  # Copying the list
        random.shuffle(rows)
        rowsN = random.sample(rows,n)
        rowsN.sort(key=lambda row: row.d2h(d))
        randArr.append(round(rowsN[0].d2h(d),2))
    return randArr

if __name__ == '__main__': 
    # main()
    d = DATA(0)
    for i in range(11):
        j=0
        for row in csv(f"././data/health{i}.csv"): 
            if j==0 and i!=0:
                j += 1
                continue
            d.add(row)

    print(len(d.rows))
    
    algo = []
    time_all = []

    bestrand9 = randN(d,9)
    bestrand24 = randN(d,24)
    bestrand32 = randN(d,32)
    bestrand64 = randN(d,64)

    # plot_running_times()

    # SMO
    # start_time = time.time()
    # bests_smo9 = run_smo_20(d,5)
    # end_time = time.time()
    # algo.append("SMO9")
    # time_all.append(end_time-start_time)

    # start_time = time.time()
    # bests_smo24 = run_smo_20(d,24)
    # end_time = time.time()
    # algo.append("SMO24")
    # time_all.append(end_time-start_time)

    # start_time = time.time()
    # bests_smo32 = run_smo_20(d,32)
    # end_time = time.time()
    # algo.append("SMO32")
    # time_all.append(end_time-start_time)

    # start_time = time.time()
    # bests_smo64 = run_smo_20(d,64)
    # end_time = time.time()
    # algo.append("SMO64")
    # time_all.append(end_time-start_time)

    # # print("SMO DONE")

    # # #RRP
    # start_time = time.time()
    # bests_rrp9 = rrp_20(d,9)
    # end_time = time.time()
    # algo.append("RRP9")
    # time_all.append(end_time-start_time)

    # start_time = time.time()
    # bests_rrp24 = rrp_20(d,28)
    # end_time = time.time()
    # algo.append("RRP24")
    # time_all.append(end_time-start_time)

    # start_time = time.time()
    # bests_rrp32 = rrp_20(d,36)
    # end_time = time.time()
    # algo.append("RRP32")
    # time_all.append(end_time-start_time)

    # start_time = time.time()
    # bests_rrp64 = rrp_20(d,68)
    # end_time = time.time()
    # algo.append("RRP64")
    # time_all.append(end_time-start_time)

    # # print('RRP DONE')
        
    # # # KMeans
    # start_time = time.time()
    # best_kmean = kmeans_20(d)
    # end_time = time.time()
    # algo.append("KMeans")
    # time_all.append(end_time-start_time)

        
    # # DBSCAN
    # start_time = time.time()
    # best_dbscan = dbscan_20(d)
    # end_time = time.time()
    # algo.append("DBSCAN")
    # time_all.append(end_time-start_time)

    # print(algo)
    # print(time_all)

    

    # sk = ScottKnott({
    #               'smo9': bests_smo9,
    #                 'smo24': bests_smo24,
    #                 'smo32': bests_smo32,
    #                 'smo64': bests_smo64,
    #               'rrp9': bests_rrp9,
    #                 'rrp24': bests_rrp24,
    #                 'rrp32': bests_rrp32,
    #                 'rrp64': bests_rrp64,
    #               'kmeans': best_kmean,
    #               'dbscan': best_dbscan
    #             })
    # sk.pprint() 

    sk = ScottKnott({
                  'rand9': bestrand9,
                    'rand24': bestrand24,
                    'rand32': bestrand32,
                    'rand64': bestrand64
                })
    sk.pprint() 



    # best,worst,mean = dbscan(d)
    # print("DBSCAN-Best: ",best.mid().d2h(best))
    # print("DBSCAN-Worst: ",worst.mid().d2h(worst))
    # print("DBSCAN-Mean: ",mean)
        
    # best,worst,mean = kmeans(d)
    # print("Kmeans-Best: ",best.mid().d2h(best))
    # print("Kmeans-Worst: ",worst.mid().d2h(worst))
    # print("Kmeans-Mean: ",mean)
    
    # d3 = DATA(0)
    # for row in csv("././data/health0.csv"): 
    #     d3.add(row)
    # # eg_rules(d)
    # # print("TASK-1:")
    # # print("\n")
    # # stats(d)
    # # print("#")
    # # details(d)
    # # print("#")
    # d2 = DATA(0)
    # # print()
    # d2.add(d.cols.names.cells)
    
    # bestrrp,_,__ = d3.branch(32)
    # print("Number of Rows in cluster",len(bestrrp.rows))
    # print("RRP-26: ",bestrrp.mid().d2h(d3))
    # print("#")
    # any50(d)
    # print("#")
    # evaluate_all(d)


# def algorithm_1(input_size):
#     # Implement algorithm 1
#     start_time = time.time()
#     # Run algorithm 1 with given input size
#     # Example: some_function(input_size)
#     time.sleep(0.1)  # Simulating computation time
#     end_time = time.time()
#     return end_time - start_time

# def algorithm_2(input_size):
#     # Implement algorithm 2
#     start_time = time.time()
#     # Run algorithm 2 with given input size
#     # Example: another_function(input_size)
#     time.sleep(0.2)  # Simulating computation time
#     end_time = time.time()
#     return end_time - start_time



# if __name__ == "__main__":
#     # Input size (assuming it's constant)
#     input_size = 100

#     # List of algorithms to compare
#     algorithms = [algorithm_1, algorithm_2]

#     # Plot the running times of the algorithms
#     plot_running_times(algorithms, input_size)
