import os, sys

from pathlib import Path

path = '../../media/images'
fileDirectory = os.path.dirname('C:/Users/simoc/Desktop/Blog/media/images')
print(fileDirectory)
lista=[]

for elementi in os.listdir(path):
    lista.append(elementi)


print(lista)


path = "/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)