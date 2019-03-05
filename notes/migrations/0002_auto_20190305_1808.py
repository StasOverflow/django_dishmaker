# Generated by Django 2.1.5 on 2019-03-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='noteitem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='noteitem',
            name='note',
        ),
        migrations.RemoveField(
            model_name='note',
            name='description',
        ),
        migrations.DeleteModel(
            name='NoteItem',
        ),
        migrations.AddField(
            model_name='noteditem',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noted_item', to='notes.Note'),
        ),
    ]