from django.db import models


class Cody(models.Model):
    title = models.CharField(max_length=30, verbose_name='Должность')
    department = models.CharField(max_length=50, verbose_name='Отдел')

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО сотрудника')
    birth_date = models.DateField(verbose_name='Дата рождения')
    job_title = models.CharField(max_length=50, verbose_name='Должность сотрудника')
    salary = models.IntegerField(verbose_name='Зарплата')
    cody = models.ForeignKey(Cody, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

