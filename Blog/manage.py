#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def Inserimento_dati():
    from prova.models import Choice,Question
    # CREARE LISTA IMMAGINI CARTELLA
    path = 'Immagini_da_caricare'

    lista = []

    for elementi in os.listdir(path):
        lista.append(elementi)

    print(lista)

    with open('Nomi_quadri.txt') as f:
        files = f.read()
        files = files.splitlines()
        for file in files:
            print(file)

    f.close()
    with open('Quadri_inseriti.txt') as f:
        elementi_salvati = f.read()
        elementi_salvati.splitlines()
        elementi_nuovi = []
        for file in files:
            if file not in elementi_salvati:
                elementi_nuovi.append(file)
                elemento=file
            else:
                print("elemento già presente")

    with open('Quadri_inseriti.txt', 'a') as f:
        for elementi in elementi_nuovi:
            f.write(elementi + '\n')
    domanda = Question.objects.get(pk=3)
    from django.core.files import File


    q = Question.objects.filter(question_text__startswith='Recenti')
    q= Question.objects.get(pk=q[0].id)
    count=0
    for elemento in elementi_nuovi:
        risposta=Choice(question=q, choice_text=elemento, votes=0)

        #print ("ID ---->")
        #print(risposta[0].id)
        quadro=str(lista[count])
        print(quadro)
        risposta.header_image.save(quadro, File(open('Immagini_da_caricare/'+quadro,'rb')))#rb per python 3
        count+=1










def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    Inserimento_dati()

if __name__ == '__main__':
    main()
