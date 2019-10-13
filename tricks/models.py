from django.db import models
from django.forms import ModelForm

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    syntax = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CodeTrick(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    code = models.TextField(max_length=5000)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CodeTrickCreateForm(ModelForm):
    class Meta:
        model = CodeTrick
        fields = ['title', 'description', 'code', 'language']