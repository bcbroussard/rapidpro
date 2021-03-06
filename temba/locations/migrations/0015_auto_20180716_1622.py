# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-16 16:22
from __future__ import unicode_literals

import mptt.fields

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("orgs", "0045_initial"), ("locations", "0014_initial")]

    operations = [
        migrations.AddField(
            model_name="boundaryalias",
            name="org",
            field=models.ForeignKey(
                help_text="The org that owns this alias", on_delete=django.db.models.deletion.PROTECT, to="orgs.Org"
            ),
        ),
        migrations.AddField(
            model_name="adminboundary",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                help_text="The parent to this political boundary if any",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="children",
                to="locations.AdminBoundary",
            ),
        ),
    ]
