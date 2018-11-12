#!/usr/bin/env python3

import sqlite3 as sql3
import json
import os

return_dict={}
data_dict={}



def gather_dbs():
  os.chdir('c:')
  os.chdir('/')
  potentials = os.popen('dir /s *.sqlite', 'r')
  for potential in potentials:
  
    if 'Directory' in potential:
      data_dict[potential[potential.find('of') + 3:]] = []
      key = potential[potential.find('of') + 3:]
      
    elif 'AM' in potential or 'PM' in potential:
      data_dict[key].append(potential.split()[-1])
      
def get_tables(cursor):
  cursor = cursor.execute("select name from sqlite_master where type='table'")
  for x in cursor:
    return_dict[str(x[0])] = {}
  return
  
def get_columns(cursor, table_name):
  c_ = cursor.execute('pragma table_info (\'' + table_name + "\')")
  for x in c_:
    return_dict[table_name][str(x[1])] = {}
  return
  
def run_query(cursor, search_term, table_name):
  c_ = cursor.execute('select ' + search_term + ' from ' + table_name)
  return_dict[table_name][search_term] = []
  for x in c_:
    try:
      return_dict[table_name][search_term].append(str(x[0]))
    except Exception as err:
      return_dict[table_name][search_term].append('')
  return

def discover_dbs():
  if os.name == 'nt':
    write_to = input("To >> ")
    gather_dbs()
    print('Found ' +str(len(data_dict.keys())) + ' potential databases\n')
    for x in data_dict:
      print(x)
      for y in data_dict[x]:
        print('+++ '+ y)
      print('\n')
      print('+'*len(x))
    ff_ = open(write_to, 'w')
    ff_.write(json.dumps(data_dict))
    ff_.close()
  return
  
def main():
  # discover_dbs()
  user_in = input("From >> ")
  user_out = input("To >> ")
  
  try:
    c_ = sql3.connect(user_in)
    c_.text_factory = lambda x: str(x, 'latin1')
  except Exception as err:
    print(str(err))
    return
  
  cursor = c_.cursor()
  get_tables(cursor)
  
  for y in return_dict:
    get_columns(cursor, y)
    
  for z in return_dict:
    for z_ in return_dict[z]:
      run_query(cursor, z_, z)
      
  f_ = open(user_out, 'w')
  f_.write(json.dumps(return_dict))
  f_.close()

main()
