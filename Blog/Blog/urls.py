"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#per immagini
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('prova.urls')),
    path('registration/',include('django.contrib.auth.urls')), #login fa parte in auomatico degli urls già preimpostati di django
                  #django fa in automatica il login e gestisce lui. questo deve #essere primo. django.contribut.auth serve per il login e logout ma fa tutto lui già preimpostato urls ecc
    path('registration/',include('members.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
