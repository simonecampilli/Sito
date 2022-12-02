from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
#importo query set dal database fatto in maniera automatica
#detail view riporta solo i detail di un records, così  evito di scrivere io i comandi
#create view serve per creare
#def home(request):
#return render(request, 'home.html', {}) #passo un dizionario

from .models import Post
from .forms import PostForm,FormVoti
from django.urls import reverse_lazy






class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    #ordering = ['-d'] #per ordinare in base al più recente

class ArticleDetailView(DetailView):
    model= Post
    template_name = 'article_detail.html'


class NuovoPost(CreateView):
    model = Post
    form_class = PostForm #per usare il post form creato da noi che usa bootstrap e fields non ci serve più in questo caso
    template_name = 'add_post.html'

    #fields = '__all__'
    #fields = ('title', 'body') #così ritorno una  di quello che voglio anzichè tutto



class UpdatePost(UpdateView):
    model=Post #quale modello usare
    template_name = 'update_post.html'
    fields = ['title','body']


class DeletePost(DeleteView):
    model=Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') #perchè eliminando non sa dove andare quindi serve questo che mi riporta alla home


from django.http import HttpResponse, HttpResponseRedirect


from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Choice, Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'index.html', context)



#The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.
# It returns an HttpResponse object of the given template rendered with the given context.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})




def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

class NuovoAtleta(CreateView):
    model = Choice
    form_class = FormVoti #per usare il post form creato da noi che usa bootstrap e fields non ci serve più in questo caso
    template_name = 'add_atleta.html'

    #fields = '__all__'
    #fields = ('title', 'body') #così ritorno una  di quello che voglio anzichè tutto
class UpdateAtleta(UpdateView):
    model = Choice #quale modello usare
    template_name = 'update_atleta.html'
    fields = ['choice_text','header_image']


class DeleteAtleta(DeleteView):
    model = Choice
    template_name = 'delete_atleta.html'
    success_url = reverse_lazy('home')

def top3(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    classifica = Choice.objects.order_by('-votes')[:3]
    template = loader.get_template('classifica.html')
    context = {'classifica': classifica}
    #question_id=question
    return HttpResponse(template.render(context,request))

