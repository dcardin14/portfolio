from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog = models.TextField()
    date = models.DateField()
    writer = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.title

class WriterIdentifier(models.Model):
    everybodys = Blog.objects.all()
    daniels = everybodys.filter(writer = 'Daniel')
    stefans = everybodys.filter(writer = 'Stefan')
    

