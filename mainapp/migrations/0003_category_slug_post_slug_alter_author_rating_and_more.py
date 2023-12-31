# Generated by Django 4.2.5 on 2023-09-21 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_alter_comment_post_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='mainapp.post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to='mainapp.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='mainapp.PostCategory', to='mainapp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('St', 'Статья'), ('Nv', 'Новость')], default='Nv', max_length=2, verbose_name='Тип поста'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.post', verbose_name='Пост'),
        ),
    ]
