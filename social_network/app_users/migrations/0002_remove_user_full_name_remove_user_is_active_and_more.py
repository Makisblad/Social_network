# Generated by Django 4.1.1 on 2022-10-06 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.AddField(
            model_name="user",
            name="birth_date",
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(default=None, max_length=30, verbose_name="Имя"),
        ),
        migrations.AddField(
            model_name="user",
            name="friends",
            field=models.ManyToManyField(
                blank=True, related_name="user_friends", to="app_users.user"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="info",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(default=None, max_length=30, verbose_name="Фамилия"),
        ),
        migrations.AddField(
            model_name="user",
            name="partner",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_partner",
                to="app_users.user",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="photo",
            field=models.ImageField(blank=True, upload_to="photo/%Y/%M/%D/"),
        ),
        migrations.AddField(
            model_name="user",
            name="slug",
            field=models.SlugField(default=None, unique=True, verbose_name="Url"),
        ),
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.CharField(
                choices=[
                    ("в активном поиске", "в активном поиске"),
                    ("без отношений", "без отношений"),
                    ("в отношениях с", "в отношениях с"),
                    ("в браке с", "в браке с"),
                    ("все сложно", "все сложно"),
                ],
                default="без отношений",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=40, unique=True, verbose_name="e-mail"),
        ),
    ]
