# -*- coding: utf-8 -*-
"""Mirroshnikov_ZBPI212

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUDQAcH9Udo0LNHf6jyOoR6iXU17245R
"""

def fact(x):
  if x == 0:
    return 1
  else:
    return x * fact(x - 1)

def filter_even(li):
  return list(filter(lambda x: (x % 2 == 0), li))

def square(li):
  return list(map(lambda x: x*x, li))

def bin_search(li, element):
    start = 0
    end= len(li)-1
    middle= int(end/2)
    while li[middle] != element and start < end:
        if element > li[middle]:
            start = middle+1
        else:
            end= middle-1
        middle= int((start+end)/2)
    if element == li[middle]:
      return middle
    else: 
      return -1 


def is_palindrome(string):
    string="".join(c for c in string if c.isalpha())
    string = string.casefold()
    if str(string) == "".join(reversed(string)) :
      return "YES"
    else:
      return "NO"

def pluse(x,y):
  return x+y

def minuse(x,y):
  return x-y

def multip(x,y):
  return  x*y

def remains(x,y):
  return  x%y

def degree(x,y):
  return x**y

def unit(x,y):
  return x // y

ex = {
    '+': pluse,
    '-': minuse,
    '*': multip,
    '%': remains,
    '**': degree,
    '//': unit,
    }

def calculate(path2file):
  done = ""
  zap = ""
  with open(path2file,'r') as finp:
          for st in finp:
            list = st.split()
            done = done + zap + str(ex[list[0]](int(list[1]),int(list[2])))
            zap =","           
  return done

def substring_slice(path2file_1,path2file_2):
  res = ''

  # read lines from file_1
  with open(path2file_1, 'r') as f:
    lines_1 = f.readlines()

  # iterate over lines from file_2
  with open(path2file_2, 'r') as f:
    for i, line in enumerate(f):
      # read two integers from line
      a, b = map(int, line.split())
      # slice lines_1
      res += lines_1[i][a:b + 1] + ' '
  
  return res[:-1]

# test substring_slice
# read test_output_file_2.txt as a string
#s = ''
#with open('test_output_file_2.txt', 'r') as f:
#  s = f.read()

#assert substring_slice('test_import_file_2_1.txt','test_import_file_2_2.txt') == s

import json

periodic_table = json.load(open('periodic_table.json'))

# unmerge text by uppercase
def unmerge(txt):
  res = []
  for i in range(len(txt)):
    if txt[i].isupper():
      j = i
      while j + 1 < len(txt) and txt[j + 1].islower():   
        j += 1
      res.append(txt[i:j + 1])
      i = j
  return res

def decode_ch(string_of_elements):
  res = ''
  for element in unmerge(string_of_elements):
    res += periodic_table[element]
  return res

from statistics import mean
class Student:
    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def greeting(self):
        return 'Hello, I am Student'

    def mean_grade(self):
        return mean(self.grades)

    def is_otlichnik(self):
        return 'YES' if self.mean_grade() >= 4.5 else 'NO'

    def __add__(self, other):
        return self.name + ' is friends with ' + other.name

    def __str__(self):
        return self.fullname

    
class MyError(Exception):
  def __init__(self, msg):
    self.msg = msg

