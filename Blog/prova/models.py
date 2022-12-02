from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)

    author = models.ForeignKey(User, on_delete=models.CASCADE) #serve per eliminare tutti i post di un utente quando eliminato
    #body= models.TextField()
    body= RichTextField(blank=True, null=True)
    #paragrafo = models.CharField(max_length=255, default='Click link sotto per leggere i post')

    def __str__(self):
        return self.title + ' | ' + str(self.author) #ritorno il titolo e l'autore concatenati


    def get_absolute_url(self): #mi serve per il form--> default di django
        #return reverse('article_detail', args=(str(self.id)))   #ogni cosa creato con i modelli hanno un ID o primary key è la stessa roba e quindi gliela passo
        return reverse('home', ) #così torno direttamente alla home



import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  #questo mi serve perchè così se uso question.objects.all() mi fa uscire la domanda
        #anizchè <QuerySet [<Question: Question object (1)>]>
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") #in questo modo posso avere quadri senza immagine senza avere problemi
    def __str__(self):  #questo mi serve perchè così se uso question.objects.all() mi fa uscire la domanda
        #anizchè <QuerySet [<Question: Question object (1)>]>
        return self.choice_text
    def get_absolute_url(self): #mi serve per il form--> default di django
        #return reverse('article_detail', args=(str(self.id)))   #ogni cosa creato con i modelli hanno un ID o primary key è la stessa roba e quindi gliela passo
        return reverse('home', )

