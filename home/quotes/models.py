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
    fullname = models.CharField(max_length=255)
    born_date = models.DateField()
    born_location = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.fullname

    class Meta:
        managed = False
        db_table = 'authors'


class Quotes(models.Model):
    quote_id = models.AutoField(primary_key=True)
    tags = ArrayField(models.TextField(max_length=255))
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, db_column='author')
    quote = models.TextField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'quotes'
