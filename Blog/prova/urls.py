from django.urls import path
from . import views

from .views import HomeView,ArticleDetailView,NuovoPost,UpdatePost, DeletePost, detail, index, NuovoAtleta, UpdateAtleta, DeleteAtleta


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),  #per la homepage ''
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),    #in questo modo mi crea le pagine con article/pk (primary key). quindi sarà article/1 article/2 ecc
    path('add_post/', NuovoPost.as_view(), name="nuovo_post"),
    path('update_post/<int:pk>',UpdatePost.as_view(), name="update_post"),
    path('delete_post/<int:pk>', DeletePost.as_view(), name="delete_post"),

    path('index/', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),  #
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('classifica/<int:question_id>', views.top3, name='classifica'),
    path('add_atleta/', NuovoAtleta.as_view(), name="nuovo_atleta"),
    path('update_atleta/<int:pk>',UpdateAtleta.as_view(), name="update_atleta"),
    path('delete_atleta/<int:pk>', DeleteAtleta.as_view(), name="delete_atleta"),
]
