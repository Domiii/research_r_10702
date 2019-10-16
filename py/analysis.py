from os import listdir
from os.path import isfile, join

import re

import pandas as pd


def analyze(folderName):
  fnames = [(f, re.search(r'_W(\d+)(?:-(\d+))?', f)) for f in listdir(folderName) if isfile(join(folderName, f))]
  files = [
    {
      'week': int(weekMatch.group(1)) + (weekMatch.group(2) and int(weekMatch.group(2)) * 0.1 or 0),
      'name': fname,
      'path': join(folderName, fname),
      'df': pd.read_csv(join(folderName, fname))
    } for fname, weekMatch in fnames
  ]
  files.sort(key=lambda f: f['week'])
  
  # print([f['df'].head() for f in files])
  # print([f['week'] for f in files])

  for f in files:
    week = f['week']
    df = f['df']
    print()
    print(f'W{week}')
    for col in df.columns:
      print('  ', col)
