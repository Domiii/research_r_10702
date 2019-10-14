import { iterToArray } from './util';

function listFileNames(folderId) {
  const folder = DriveApp.getFolderById(folderId);
  const files = iterToArray(folder.getFiles());
  return files.map(f => f.getName());
}

export function doGet() {
  // https://drive.google.com/drive/u/0/folders/16SQCIy97DRDsRAhpKBilbMh8hlazQAhZ
  const files = listFileNames('16SQCIy97DRDsRAhpKBilbMh8hlazQAhZ');
  const html = `\
hi!
<pre>${files.join('\n')}</pre>
`;

  return HtmlService.createHtmlOutput(html);
}