# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("tests", "0002_uuid_models")]

    operations = [
        migrations.CreateModel(
            name="OfficialTagTranslation",
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
                "verbose_name": "official tag Translation",
                "db_table": "tests_officialtag_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="UUIDTagTranslation",
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
                "verbose_name": "uuid tag Translation",
                "db_table": "tests_uuidtag_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
        ),
        migrations.RemoveField(model_name="officialtag", name="name"),
        migrations.RemoveField(model_name="uuidtag", name="name"),
        migrations.AddField(
            model_name="uuidtagtranslation",
            name="master",
            field=models.ForeignKey(
                null=True,
                editable=False,
                related_name="translations",
                to="tests.UUIDTag",
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AddField(
            model_name="officialtagtranslation",
            name="master",
            field=models.ForeignKey(
                null=True,
                editable=False,
                related_name="translations",
                to="tests.OfficialTag",
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="uuidtagtranslation",
            unique_together=set([("language_code", "master")]),
        ),
        migrations.AlterUniqueTogether(
            name="officialtagtranslation",
            unique_together=set([("language_code", "master")]),
        ),
    ]
