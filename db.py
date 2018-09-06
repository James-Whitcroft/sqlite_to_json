#!/usr/bin/env python3
import sqlite3 as s_
import json as j_
import os
r_={}
d_={}
s__=[115,101,108,101,99,116,32,110,97,109,101,32,102,114,111,109,32,115,113,108,105,116,101,95,109,97,115,116,101,114,32,119,104,101,114,101,32,116,121,112,101,61,39,116,97,98,108,101,39]
pr__=[112,114,97,103,109,97,32,116,97,98,108,101,95,105,110,102,111]
pd__=[32, 112, 111, 116, 101, 110, 116, 105, 97, 108, 32, 100, 97, 116, 97, 98, 97, 115, 101, 115, 10]
f__=[70, 111, 117, 110, 100, 32]
dr__=[100, 105, 114, 32, 47, 115, 32, 42, 46, 115, 113, 108, 105, 116, 101]
sl__=[115, 101, 108, 101, 99, 116, 32]
fr__=[32, 102, 114, 111, 109, 32]
di__=[68, 105, 114, 101, 99, 116, 111, 114, 121]
def gdb_():
  os.chdir('c:')
  os.chdir('/')
  p = os.popen(''.join([chr(x) for x in dr__]), 'r')
  for x in p:
    if ''.join([chr(x) for x in di__]) in x:
      d_[x[x.find('of')+3:]]=[]
      c_ = x[x.find('of')+3:]
    elif 'AM' in x or 'PM' in x:
      d_[c_].append(x.split()[-1])
      
def gt_(c):
  global s__
  c_ = c.execute(''.join([chr(x) for x in s__]))
  for x in c_:
    r_[str(x[0])] = {}
  return
  
def gc_(c,t):
  c_ = c.execute(''.join([chr(x) for x in pr__])+"(\'"+t+"\')")
  for x in c_:
    r_[t][str(x[1])] = {}
  return
  
def gcd_(c, cc, t):
  c_ = c.execute(''.join([chr(x) for x in sl__])+cc+''.join([chr(x) for x in fr__])+t)
  r_[t][cc] = []
  for x in c_:
    try:
      r_[t][cc].append(str(x[0]))
    except Exception as err:
      r_[t][cc].append('')
  return

def d():
  if os.name == 'nt':
    t = input("To >> ")
    gdb_()
    print(''.join([chr(x) for x in f__])+str(len(d_.keys()))+''.join([chr(x) for x in pd__]))
    for x in d_:
      print(x)
      for y in d_[x]:
        print('+++ '+ y)
      print('\n')
      print('+'*len(x))
    ff_ = open(t, 'w')
    ff_.write(j_.dumps(d_))
    ff_.close()
  return
  
def m():
  # d()
  i = input("From >> ")
  q = input("To >> ")
  try:
    c_=s_.connect(i)
    c_.text_factory = lambda x: str(x, 'latin1')
  except Exception as err:
    print(str(err))
    return
  c__=c_.cursor()
  gt_(c__)
  for y in r_:
    gc_(c__, y)
  for z in r_:
    for z_ in r_[z]:
      gcd_(c__, z_, z)
  f_ = open(q, 'w')
  f_.write(j_.dumps(r_))
  f_.close()

m()
