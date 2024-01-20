import sys
from config import the
from test_runner import test
import re,ast,fileinput
from DATA import DATA
from ROW import likes
def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]

def load():
    # Load Data
    data1 = {}
    data2 = {}
   
    head=None
    for row in csv("././data/diabetes.csv"): 
       head = row
       break
       
    n=0
    for row in csv("././data/diabetes.csv"): 
        if n==0:
           n+=1
           continue
        if(row[-1] in data1):
           data1[row[-1]].add(row)
        else:
           obj = DATA(0)
           obj.add(head)
           obj.add(row)
           data1[row[-1]] = obj

    
    for row in csv("././data/soybean.csv"): 
       head = row
       break

    n=0
    for row in csv("././data/soybean.csv"): 
        if n==0:
           n+=1
           continue
        if(row[-1] in data2):
           data2[row[-1]].add(row)
        else:
           obj = DATA(0)
           obj.add(head)
           data2[row[-1]] = obj
           obj.add(row)
           

def learn(data, row, my, kl):
    my['n'] += 1
    kl = row.cells[data.cols.klass.at]

    if my['n'] > 10:
        my['tries'] += 1
        my['acc'] += 1 if kl == likes(row, my['datas']) else 0

    my['datas'][kl] = my['datas'].get(kl, DATA({data.cols.names}))
    my['datas'][kl].add(row)



if __name__ == '__main__':
   load()