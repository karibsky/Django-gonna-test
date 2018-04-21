from django.db import models

class Subscriber (models.Model):
	id = models.AutoField(primary_key=True)
	email = models.EmailField(verbose_name = "Адрес электронной почты")
	name = models.CharField(max_length = 50, verbose_name = "Логин")

	class Meta:
		verbose_name = 'подписчиков'
		verbose_name_plural = 'подписчики'
		
class Post(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 50, verbose_name = "Название")
	description = models.TextField(verbose_name = "Текст")
	author = models.CharField(max_length = 30, verbose_name = "Автор")
	date = models.DateField(auto_now_add=True, verbose_name = "Дата публикации")
	image = models.CharField(max_length = 255, verbose_name = "Изображение")

	class Meta:
		verbose_name = 'публикацию'
		verbose_name_plural = 'публикации'
			
		