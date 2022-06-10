import os
import io


allFileName = ''
dir_path = r'directoryPath'   #PATH
for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path, file)
    if os.path.isfile(cur_path):
        with io.open(cur_path, 'r', encoding='utf-8', newline='\n',  errors='ignore') as f:
            if 'Term' in f.read():    #Term to search
                x = cur_path.split('Split from absolute path\\') #Split from absolute path
                allFileName += x[1]+'\n'
print(allFileName)
