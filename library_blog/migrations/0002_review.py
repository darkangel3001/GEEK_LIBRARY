# Generated by Django 5.1.4 on 2024-12-12 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('text_review', models.TextField(verbose_name='напишите отзыв о книге')),
                ('stars', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], default='⭐', max_length=100, verbose_name='поставьте оценку')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='library_blog.bookmodel')),
            ],
        ),
    ]
