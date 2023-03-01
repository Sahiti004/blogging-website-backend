import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('date_posted', models.DateField(default=datetime.datetime(2023, 2, 23, 3, 35, 58, 379449, tzinfo=utc))),
                ('category', models.CharField(choices=[('Web-dev', 'Web-dev'), ('Machine Learning', 'Machine Learning')], default='Web-dev', max_length=160, null=True)),
            ],
        ),
    ]
