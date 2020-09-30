# Generated by Django 3.1.1 on 2020-09-30 07:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('status', models.PositiveIntegerField(choices=[(0, 'В работе (назначена)'), (1, 'Закрыто'), (2, 'Создано (запланирована)')], default=2, verbose_name='Статус')),
                ('assigned', models.ManyToManyField(blank=True, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Назначено')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]