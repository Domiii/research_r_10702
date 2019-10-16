from __future__ import print_function

import os
from os import path

from gutil import getFilesInFolder, exportFileCsv
# from drive import getOrCreateService
from analysis import analyze

csvFolder = f'{path.dirname(__file__)}/_files'

# TODO: setup virtualenv - https://towardsdatascience.com/all-you-need-to-know-about-python-virtual-environments-9b4aae690f97

def exportFiles(files):
  # create folder, if it does not exist yet
  if not path.exists(csvFolder):
    os.mkdir(csvFolder)

  # export files
  if not files:
    print('No files found.')
  else:
    print('Files:')
    for f in files:
      print(u'{0} ({1})'.format(f['name'], f['id']))
      exportFileCsv(csvFolder, f)

def main():
  # service = getOrCreateService()

  if not path.exists(csvFolder):
    # Query files from drive
    # https://drive.google.com/drive/u/0/folders/16SQCIy97DRDsRAhpKBilbMh8hlazQAhZ
    driveFolderId = '16SQCIy97DRDsRAhpKBilbMh8hlazQAhZ'
    files = getFilesInFolder(driveFolderId, mimeType='application/vnd.google-apps.spreadsheet')

    # export files
    exportFiles(files)

  # do the analysis
  analyze(csvFolder)


if __name__ == '__main__':
  main()
