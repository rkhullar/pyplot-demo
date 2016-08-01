#!local/bin/python

"""
@author  :  Rajan Khullar
@created :  07/29/16
@updated :  07/31/16
"""

import csv
import urllib2
import inspect
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.dates import strpdate2num

myname = lambda: inspect.stack()[1][3]

def finalize(axis=1, legend=1, xlabel='X AXIS', ylabel='Y AXIS', title='Interesting Graph'):
    if axis == 1:
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    if legend == 1:
        plt.legend()
    plt.title(title)
    plt.show()

def test01():
    x = [1,2,3,4,5]
    y = [7,4,5,2,8]
    plt.plot(x, y, label=myname(), color='b')

def test02():
    x = [1,2,3,4,5]
    y = [7,4,5,2,8]
    plt.scatter(x, y, 10**2, label=myname(), color='r', marker='*')

def test03():
    k = [0,1,2,3,4,5,6,7,8,9]
    v = [5,3,2,7,6,5,4,8,7,6]
    plt.bar(k, v, label=myname(), color='c')

def test04():
    k = [0,1,2,3,4,5,6,7,8,9] # bins
    v = [5,3,2,7,6,5,4,8,7,6]
    plt.hist(v, k, histtype='bar', rwidth=0.8, label=myname(), color='c')

def test05():
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

def test06():
    k = ['a','b','c','d']
    v = [ 5 , 2 , 6 , 4]
    plt.pie(v, labels=k,
        colors=['r','g','b','y'],
        startangle=180,
        autopct='%1.1f%%')
        # explode
        # shadow
    #finalize(axis=0, legend=0)

def test07():
    x = []
    y = []
    with open('data/example.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=';')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
    plt.plot(x, y, label=myname(), color='k')

def test08():
    url = 'http://www.quandl.com/api/v1/datasets/EUROSTAT/CRIM_PLCE_42.csv'
    # https://theodi.org/blog/how-to-use-r-to-access-data-on-the-web
    f = urllib2.urlopen(url)
    s = f.read().strip().split('\n')[1:]
    f.close()
    date, value = np.loadtxt(s, delimiter=',', unpack=True, converters={0:strpdate2num('%Y-%m-%d')})
    plt.plot_date(date, value, '-', label=myname())
    #finalize(xlabel='DATE')

# supplot intro, rotated axis and grid
def test09():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    ax1.plot([1,2,3,4,5,6],[5,3,6,4,3,6])
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='#ff69b4', linestyle='--', linewidth=1)
    #plt.subplots_adjust(bottom=0.20)

# unix time to numpy time
def test10():
    #import time
    #print time.time() #float
    date = [1469983819.99, 1269983819.99, 1369983819.99]
    #print dt.datetime.fromtimestamp(date[0])
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)
    print date

# stock graph with gain and loss fill
def test11():
    date = []; closep = []
    with open('data/twtr-10y.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        dateconv = strpdate2num('%Y/%m/%d')
        for row in reader:
            date.append(dateconv(row['date']))
            closep.append(float(row['close']))
    date = np.array(date)
    closep = np.array(closep)


    ipo = closep[-1]

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))

    ax1.plot_date(date, closep, '-', label='price')
    ax1.plot([],[], color='g', alpha=0.5, linewidth=3, label='gain')
    ax1.plot([],[], color='r', alpha=0.5, linewidth=3, label='loss')

    ax1.fill_between(date, closep, ipo, where=closep>ipo, facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep, ipo, where=closep<ipo, facecolor='r', alpha=0.5)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.grid(True)

    plt.subplots_adjust(bottom=0.20)

# stylesheets
def test12():
    style.use('ggplot')
    print style.available
    plt.plot([1,2,3,4,5,6,7,8],[50,45,30,55,40,30,45,50],label=myname())


if __name__ == '__main__':
    #test01()
    #test02()
    #test03()
    #test04()
    #test05()
    #test06()
    #test07()
    #test08()
    #test09()
    #test10()
    #test11()
    test12()
    finalize(axis=1, legend=1)
