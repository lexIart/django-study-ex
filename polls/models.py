from django.db import models
"""Эта часть кода указывает Джанго на то, чтобы он:
    Создал структуру базы данных (create table) для application
    Создать Python API для доступа к данным объектов Question and Choice."""

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Текстовое поле вопроса
    pub_date = models.DateTimeField('date published')  # Поле даты (публикации)
    # В поле pub_date использован необязательный аргумент для определения отображаемого названия поля
    # Если этот аргумент не указан, джанго будет использовать "машинное" название (pub_date)
    def __str__(self):
        return self.question_text
# Каждое поле представлено экземпляром класса Field - текст, дата. Так мы указываем какие типы данных хранят поля
#
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Связь между моделями реализована с помощью FK, указывающим на то что
    # каждый choice связан с одним объектом question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Осталось подключить приложение в installed_apps
