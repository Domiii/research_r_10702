## Steps taken

1. Build a basic Google Web App, using clang (in `gs/` folder)
   * Can list specific files on website
1. Decided to use python + Google Drive API instead
1. Setup Python Project in VSCode
   * Setup python venv https://realpython.com/python-virtual-environments-a-primer/
      * (set `python.pythonPath` in VSCode)
   * Fix [python paths in `.env`](https://github.com/Microsoft/vscode-python/issues/3840#issuecomment-463789294) in VSCode
   * Setup `pylint` + `.pylintrc` in VSCode
      * Enable `jedi` in VSCode (seems to be stabler for now?)
   * Setup Python debugger (can do this in VSCode debugger UI now; shortcut: F5 or CTRL+F5)