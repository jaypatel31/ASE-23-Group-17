import sys
from config import the
from test_runner import test
import re,ast,fileinput
from DATA import DATA
from COLS import COLS
from ROW import ROW

def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]

def load():
    global data1,data2

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
           obj.cols = COLS(ROW(head))
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
   
           

def learn(data, row, my, kl=None):
    my['n'] += 1

   #  print(row.cells)
    
    kl = row.cells[data.cols.klass.at]
   #  print(kl)
    
    if my['n'] > 10:
        my['tries'] += 1
        my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0

   #  my['datas'][kl] = my['datas'].get(kl, DATA(0).add(data.cols.names.cells))
    if kl not in my['datas']:
       my['datas'][kl] = DATA(0)
       my['datas'][kl].add(data.cols.names.cells)
    
   #  print(my['datas'][kl])
   
    my['datas'][kl].add(row)


def test_one_row():
   global data1,data2
   # Sample row to test which it likes the most
   row = ROW([1,87,78,27,32,34.6,0.101,22,"negative"]) 
   liked1 = row.likes(data1) #('negative', 7.970983172335202e-20)

   soyabean_row = ['july', 'normal', 'gt-norm', 'norm', 'yes', 'same-lst-yr', 'scattered', 'severe', 'none', '80-89', 'abnorm', 'abnorm', 'absent', 'dna', 'dna', 'absent', 'absent', 'absent', 'abnorm', 'yes', 'above-sec-nde', 'dna', 'present', 'firm-and-dry', 'absent', 'none', 'absent', 'norm', 'dna', 'norm', 'absent', 'absent', 'norm', 'absent', 'norm','diaporthe-stem-canker']
   row = ROW(soyabean_row) 
   liked2 = row.likes(data2) #('diaporthe-stem-canker', 1.9239137836110653e-06)

def bayes():
   wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
   
   data = DATA(0)
   n = 0

   for row in csv("././data/diabetes.csv"):
      if n==0:
         data.cols = COLS(ROW(row))
         n = n+1
      else:
         learn(data,ROW(row),wme)
          
   print(wme['acc'] / wme['tries']*100)

def soyabean_bayes():
   for k in range(4):
    for m in range(4):
       the.k = k
       the.m = m
       wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
   
       data = DATA(0)
       n = 0

       for row in csv("././data/soybean.csv"):
         if n==0:
            data.cols = COLS(ROW(row))
            n = n+1
         else:
            learn(data,ROW(row),wme)
    #    print(k,m,wme['acc'] / wme['tries']*100)
       print(f"{k:<10}{m:<10}{format(wme['acc'] / wme['tries']*100, '.2f')}%")

def naive():
   print("\nLoading of files completed\n")
   load()

   test_one_row()

   print("Accuracy for diabetes.csv:")
   bayes()

   print("\nAccuracies for soybean.csv with different k and m values:")
   print("-" * 52)
   print(f"{'k':<10}{'m':<10}{'Accuracy'}")
   print("-" * 52)
   
   soyabean_bayes()

data1 = {}
data2 = {}   
if __name__ == '__main__':
   
   naive()
   