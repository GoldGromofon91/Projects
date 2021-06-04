from django.contrib.auth import get_user_model
from django.db import models

#Модель опросов
class Poll(models.Model):
    title = models.CharField('title', max_length=128, blank=True)
    description = models.CharField('description', max_length=256, blank=True)
    started_at = models.DateTimeField('start', auto_now_add=True)
    finished_at = models.DateTimeField('finish', auto_now=True)
    visible = models.BooleanField('visible', default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'poll'

#Модель вопросов
class Question(models.Model):
    STATUS_TYPE_1 = 'T'
    STATUS_TYPE_2 = 'CO'
    STATUS_TYPE_3 = 'CM'

    STATUS_CHOICES = (
        (STATUS_TYPE_1, 'text_type'),
        (STATUS_TYPE_2, 'choice_one_type'),
        (STATUS_TYPE_3, 'choice_many_type'),
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="poll_to_question")
    title = models.CharField('title', max_length=128, blank=True)
    text = models.TextField('text', blank=True)
    type = models.CharField('status', max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'question'

#Модель вариантов вопроса
class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_to_questionchoice')
    title = models.CharField(max_length=128, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'questionchoice'

#Модель анонимного участника
class Participant(models.Model):
    participant = models.PositiveIntegerField(unique=True)

#Модель ответов
class Answer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_to_answer', null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='participant_to_answer',
                                    null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll_to_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_to_answer')
    choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, related_name="questionchoice_to_answer",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(blank=False, null=True)

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return self.choice.title
