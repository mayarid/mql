import yaml
import os, sys, re

def yaml_parser(file):
  with open(file, 'r') as stream:
    try:
      data = yaml.load(stream)
      return data

    except yaml.YAMLError as exc:
      print(exc)

def load_grammer(file_name):
  abs_path = os.path.dirname(os.path.realpath(__file__))
  grammer = "{}/grammers/{}".format(abs_path,file_name)
  return yaml_parser(grammer)

def after(l, start):
  s = start[:]
  x = l[:]
  s.reverse()
  x.reverse()
  count = 0
  while len(x) > 0 and s[0] != x[0]:
    count += 1
    del x[0]
  if len(x) == 0:
    return -1
  del s[0]
  while len(x) > 0 and len(s) > 0:
    if s[0] == x[0]:
      del s[0]
    del x[0]
  if len(s) > 0:
    return -1
  return count

def load_reserved_data(path_file = None):
  result = None
  if path_file :
    result = yaml_parser(grammer)
  return result

def load_tokens_data(path_file = None):
  result = None
  if path_file :
    result = yaml_parser(grammer)
  return result
