# Generated by Django 4.1.7 on 2023-05-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Accounts", "0007_remove_appuser_number_appuser_degree_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DoctorRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doctor_name", models.CharField(max_length=50)),
                ("doctor_email", models.EmailField(max_length=254)),
                ("doctor_gouvernerat", models.CharField(max_length=50)),
                ("doctor_city", models.CharField(max_length=50)),
                (
                    "doctor_genre",
                    models.CharField(
                        choices=[("Homme", "Homme"), ("Femme", "Femme")],
                        default="Homme",
                        max_length=20,
                    ),
                ),
                ("doctor_age", models.IntegerField()),
                ("doctor_password", models.CharField(max_length=50)),
                (
                    "doctor_degree_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="pics/requests/{id}/degree image/",
                    ),
                ),
                (
                    "profil_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="pics/requests/{id}/profil image/",
                    ),
                ),
                ("request_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="appuser",
            name="degree",
            field=models.ImageField(
                blank=True, null=True, upload_to="pics/users/{id}/degree image/"
            ),
        ),
        migrations.AlterField(
            model_name="appuser",
            name="profil_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="pics/users/<django.db.models.fields.AutoField>/profil image/",
            ),
        ),
    ]
