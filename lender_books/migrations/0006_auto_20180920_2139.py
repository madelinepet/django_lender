# Generated by Django 2.1.1 on 2018-09-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lender_books', '0005_book_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='last_borrowed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]