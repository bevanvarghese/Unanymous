from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    published_on = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # CASCADE: if a Q is deleted, all its choices are deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
