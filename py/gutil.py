'''
Google utilities
'''

from os import path
from drive import getOrCreateService

def exportFileCsv(folder, file, override = False):
  fileId = file['id']
  fileName = path.splitext(file['name'].replace(' ', '_'))[0]
  targetFileName = f'{folder}/{fileName}.csv'
  targetMimeType = 'text/csv'

  return exportFile(fileId, targetFileName, targetMimeType, override)

def exportFile(fileId, targetFileName, targetMimeType, override = False):
  if not override and path.exists(targetFileName):
    # no need to do it again
    return

  service = getOrCreateService()

  data = service.files().export(fileId=fileId, mimeType=targetMimeType).execute()

  with open(targetFileName, 'wb') as f:
    f.write(data)


# search files: https://developers.google.com/drive/api/v2/search-files
# mime types: https://developers.google.com/drive/api/v3/mime-types
def getFilesInFolder(folderId, mimeType = None):
  service = getOrCreateService()

  q = f'\'{folderId}\' in parents'
  if mimeType:
    q += f' AND mimeType="{mimeType}"'
  results = service.files().list(
    fields="nextPageToken, files(id, name)",
    q=q
  ).execute()
  return results.get('files', [])

def getFileNames(folderId):
  service = getOrCreateService()
  files = getFilesInFolder(folderId)
  return [f['name'] for f in files]