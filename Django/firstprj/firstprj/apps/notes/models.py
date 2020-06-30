from django.db import models

STATUS_CHOICES = ( 
    ("0", "Не выполнено"), 
    ("1", "В процессе"), 
    ("2", "Выполнено"), 
) 

class Note(models.Model):
	category_note = models.CharField('Категория', max_length = 100)
	text_note = models.TextField('Текст')
	pub_date = models.DateTimeField('Дата публикации')
	status_note = models.CharField(
		'Статус', 
		max_length = 20,
		choices = STATUS_CHOICES,
		default = '1')

	def __str__(self):
		return  f'Категория: {self.category_note},Текст заметки: {self.text_note[:15]}, Статус: {self.status_note}'

	class Meta:
		verbose_name = 'Заметку'
		verbose_name_plural = 'Заметки'