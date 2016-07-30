#!local/bin/python

"""
@author  :  Rajan Khullar
@created :  07/29/16
@updated :  07/30/16
"""

import csv
import urllib2
import inspect
import matplotlib.pyplot as plt

myname = lambda: inspect.stack()[1][3]

def finalize(axis=1, legend=1):
    if axis == 1:
        plt.xlabel('X AXIS')
        plt.ylabel('Y AXIS')
    if legend == 1:
        plt.legend()
    plt.title('Interesting Graph')
    plt.show()

def stock_quote(symbol):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1c1hgv' % symbol
    f = urllib2.urlopen(url)
    s = f.read().strip().split(',')
    f.close()
    d = {}
    d['symbol']  = s[0].replace('"','')
    d['last']    = float(s[1])
    d['date']    = s[2].replace('"','')
    d['change']  = float(s[3])
    d['high']    = float(s[4])
    d['low']     = float(s[5])
    d['vol']     = int(s[6])
    return d

def test1():
    x = [1,2,3,4,5]
    y = [7,4,5,2,8]
    plt.plot(x, y, label=myname(), color='b')

def test2():
    x = [1,2,3,4,5]
    y = [7,4,5,2,8]
    plt.scatter(x, y, 10**2, label=myname(), color='r', marker='*')

def test3():
    k = [0,1,2,3,4,5,6,7,8,9]
    v = [5,3,2,7,6,5,4,8,7,6]
    plt.bar(k, v, label=myname(), color='c')

def test4():
    k = [0,1,2,3,4,5,6,7,8,9] # bins
    v = [5,3,2,7,6,5,4,8,7,6]
    plt.hist(v, k, histtype='bar', rwidth=0.8, label=myname(), color='c')

def test5():
    k = [1,2,3,4,5]

    a = [2,3,2,3,2]
    b = [4,1,5,3,5]
    c = [1,4,2,2,3]
    d = [3,2,1,2,0]

    plt.stackplot(k, a, b, c, d, colors=['r', 'g', 'b', 'y'])
    plt.plot([],[],label='a',color='r',linewidth=5)
    plt.plot([],[],label='b',color='g',linewidth=5)
    plt.plot([],[],label='c',color='b',linewidth=5)
    plt.plot([],[],label='d',color='y',linewidth=5)

def test6():
    k = ['a','b','c','d']
    v = [ 5 , 2 , 6 , 4]
    plt.pie(v, labels=k,
        colors=['r','g','b','y'],
        startangle=180,
        autopct='%1.1f%%')
        # explode
        # shadow

def test7():
    x = []
    y = []
    with open('data/example.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=';')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
    plt.plot(x, y, label=myname(), color='k')

def test8():
    print stock_quote('GOOG')


if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()
    #test6()
    #test7()
    test8()
    #finalize(axis=1, legend=1)
