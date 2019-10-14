from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
from os import path
from gutil import getFilesInFolder, exportFileCsv
from drive import getOrCreateService

csvFolder = f'{path.dirname(__file__)}/_files'

# TODO: setup virtualenv - https://towardsdatascience.com/all-you-need-to-know-about-python-virtual-environments-9b4aae690f97

def main():
  service = getOrCreateService()

  # Query files from drive
  # https://drive.google.com/drive/u/0/folders/16SQCIy97DRDsRAhpKBilbMh8hlazQAhZ
  driveFolderId = '16SQCIy97DRDsRAhpKBilbMh8hlazQAhZ'
  files = getFilesInFolder(driveFolderId, mimeType = 'application/vnd.google-apps.spreadsheet')

  # create folder, if it does not exist yet
  os.mkdir(csvFolder)

  if not files:
    print('No files found.')
  else:
    print('Files:')
    for f in files:
      print(u'{0} ({1})'.format(f['name'], f['id']))
      exportFileCsv(csvFolder, f)


if __name__ == '__main__':
  main()
