# Generated by Django 3.2.20 on 2023-07-03 15:56

from django.db import migrations, models
import django.db.models.deletion
import solid_backend.utils.drf_spectacular_extensions


class Migration(migrations.Migration):

    dependencies = [
        ('wabe_content', '0008_alter_word_tree_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Titel')),
                ('graphic', solid_backend.utils.drf_spectacular_extensions.MDTextField(blank=True, max_length=500, null=True, verbose_name='Graphie')),
                ('lexem', solid_backend.utils.drf_spectacular_extensions.MDTextField(blank=True, max_length=500, null=True, verbose_name='Lexem')),
                ('etymology', solid_backend.utils.drf_spectacular_extensions.MDTextField(blank=True, max_length=500, null=True, verbose_name='Etymologie')),
                ('semantics', solid_backend.utils.drf_spectacular_extensions.MDTextField(blank=True, max_length=500, null=True, verbose_name='Semantik')),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='general_information', to='wabe_content.word', verbose_name='Wort')),
            ],
            options={
                'verbose_name': 'Allgemein',
                'verbose_name_plural': 'Allgemein',
            },
        ),
    ]