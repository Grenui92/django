# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=250)
    born_date = models.CharField(max_length=20, blank=True, null=True)
    born_location = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        managed = False
        db_table = 'authors'


class Quotes(models.Model):
    quote_id = models.AutoField(primary_key=True)
    tags = ArrayField(models.TextField(), blank=True, null=True)  # This field type is a guess.
    author = models.ForeignKey(Authors, models.DO_NOTHING, db_column='author', blank=True, null=True)
    quote = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotes'
