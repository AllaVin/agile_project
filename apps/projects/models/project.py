from django.db import models


class Project(models.Model):
    # name: строковое поле, макс. длина 100, должно быть уникальным
    name = models.CharField(unique=True, max_length=100)
    # description: большое текстовое поле, обязательное к заполнению
    description = models.TextField()
    # created_at: поле даты и времени, заполняется автоматически при создании
    created_at = models.DateTimeField(auto_now_add=True)

    # files- связующее поле "Многие ко многим" к ProjectFile
    file = models.ManyToManyField('ProjectFile', related_name='projects')

    # Декаратор
    @property
    def count_of_files(self):
        # Динамическое поле вычисляющее количество фа   йлов для проекта
        return len(self.file.all())


    def __str__(self):
        # Строковое отображение объекта будет его именем
        return self.name

    class Meta:
        ordering = ["name"]

