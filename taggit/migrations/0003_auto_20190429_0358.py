# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("taggit", "0002_auto_20150616_2121")]

    operations = [
        migrations.CreateModel(
            name="TagTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        primary_key=True,
                        serialize=False,
                        auto_created=True,
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        verbose_name="Language", max_length=15, db_index=True
                    ),
                ),
                ("name", models.CharField(verbose_name="Name", max_length=100)),
            ],
            options={
                "verbose_name": "Tag Translation",
                "db_table": "taggit_tag_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
        ),
        migrations.RemoveField(model_name="tag", name="name"),
        migrations.AddField(
            model_name="tagtranslation",
            name="master",
            field=models.ForeignKey(
                null=True,
                editable=False,
                related_name="translations",
                to="taggit.Tag",
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="tagtranslation", unique_together=set([("language_code", "master")])
        ),
    ]
