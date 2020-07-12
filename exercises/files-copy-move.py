import shutil

# Copying file
print('Moving file Hello.txt to output-files')
shutil.copy('/Users/lucasmonteiroi/Documents/hello.txt', '/Users/lucasmonteiroi/git-repo/python-course/output-files/hello.txt')
print('File moved')

# Use shutil.move to move file
# Rename will renaming file
# You can move with a new name too
