from django.contrib import admin
from .models import Project, Category, Priority, Task, Comment, Attachment, Reminder

# Registrando os modelos no painel administrativo
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(Reminder)
