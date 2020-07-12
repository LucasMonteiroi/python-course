import os, shutil, send2trash as trash

# Get current path
print('Current directory: %s' % (str(os.getcwd())))

# Removing directory
# This will throw exception because the folder is not empty
# os.rmdir('/Users/lucasmonteiroi/Documents/hello') 

# print('Removing folder hello_backup')
# This will remove permanently the folder
# shutil.rmtree('/Users/lucasmonteiroi/Documents/hello_backup') 
print('Sending to trash the following file: => /Users/lucasmonteiroi/Documents/hello_backup/hello.txt ')
trash.send2trash('/Users/lucasmonteiroi/Documents/hello_backup/hello.txt')