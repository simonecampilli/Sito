import os, sys

#CREARE LISTA IMMAGINI CARTELLA
path = '../Immagini_da_caricare'


lista=[]

for elementi in os.listdir("C:/Users/simoc/Desktop/Blog/Immagini_da_caricare/"):
    abs_path = os.path.abspath(elementi)
    print(abs_path)
    print("wewe")
    lista.append(elementi)


#print(lista)


with open('../Nomi_quadri.txt') as f:
    files=f.read()
    files=files.splitlines()
    for file in files:
        print(file)
f.close()
with open('../Quadri_inseriti.txt') as f:
    elementi_salvati = f.read()
    elementi_salvati.splitlines()
    elementi_nuovi=[]
    for file in files:
        if file not in elementi_salvati:
            elementi_nuovi.append(file)
        else:
            print("elemento già presente")



with open('../Quadri_inseriti.txt','a') as f:
    for elementi in elementi_nuovi:
        f.write(elementi+'\n')