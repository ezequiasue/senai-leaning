from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']  # Ordena os projetos por data de criação, do mais recente ao mais antigo.
        verbose_name = "Project"  # Nome do modelo no singular.
        verbose_name_plural = "Projects"  # Nome do modelo no plural.
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']  # Ordena categorias por nome, em ordem alfabética.
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    class Meta:
        ordering = ['level']  # Ordena prioridades pelo nível, do menor para o maior.
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"
    
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # Ordena tarefas pela data de criação, do mais recente ao mais antigo.
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Ordena comentários pela data de criação.
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']  # Ordena anexos pela data de upload.
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"
    
    def __str__(self):
        return f'Attachment for {self.task.title}'


class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    remind_at = models.DateTimeField()

    class Meta:
        ordering = ['remind_at']  # Ordena lembretes pela data do lembrete.
        verbose_name = "Reminder"
        verbose_name_plural = "Reminders"
    
    def __str__(self):
        return f'Reminder for {self.task.title}'
