# -*- coding:utf-8 -*-

def dbpediasent(filename, maxind = None):
    fobj = open(filename)
    fobj.readline()
    for ind, line in enumerate(fobj):
        if maxind and ind >= maxind:
            break
        line = line.strip().decode('utf-8')
        line = line.split('> "')[-1].split('"@fr')[0]
        if not line:
            continue
        yield line

def printsents(filename, indastr, maxind = None):
    ind = [int(i) for i in indastr.split(' ')]
    for i, s in enumerate(dbpediasent(filename, maxind)):
        if i in ind:
            print s
            print
