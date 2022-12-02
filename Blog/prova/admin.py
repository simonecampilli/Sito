from django.contrib import admin
from .models import Post

# Register your models here.
from .models import Question # in questo modo posso modificare da Admin le domande
from .models import Choice
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Choice)
