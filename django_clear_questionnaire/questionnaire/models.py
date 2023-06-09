import time

from django.db import models
from user.models import USER


# Create your models here.
class PROJECT(models.Model):
    user = models.ForeignKey(USER, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300, blank=False)
    desc = models.CharField(max_length=900, blank=False, default="感谢参与调查！")
    state = models.IntegerField(default=0)  # 0未发布 1发布中 2已删除
    created_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    submits = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + ' ' + self.title


class QUESTION(models.Model):
    project = models.ForeignKey(PROJECT, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    required = models.BooleanField(blank=False, default=False)
    type = models.IntegerField(blank=False)
    desc = models.CharField(max_length=900)
    random = models.BooleanField(blank=False, default=False)
    serial_number = models.IntegerField(default=0)
    state = models.IntegerField(default=1)  # 0删除 1正常


class SUBMIT(models.Model):
    project = models.ForeignKey(PROJECT, on_delete=models.DO_NOTHING)
    submit_time = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    os = models.CharField(max_length=1000)
    duration = models.IntegerField()
    state = models.IntegerField(default=1)  # 0删除 1正常

    def to_dict(self):
        """重写model_to_dict()方法转字典"""
        from datetime import datetime

        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            value = f.value_from_object(self)
            if isinstance(value, datetime):
                value = time.mktime(value.timetuple())
            elif isinstance(f, models.FileField):
                value = value.url if value else None
            data[f.name] = value
        return data


class ANSWER(models.Model):
    submit = models.ForeignKey(SUBMIT, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(QUESTION, on_delete=models.DO_NOTHING)
    type = models.IntegerField(blank=False)
    is_null = models.BooleanField(blank=False, default=0)


class Q_NOTE(models.Model):
    question = models.ForeignKey(QUESTION, on_delete=models.DO_NOTHING)
    title = models.TextField(blank=False)


class Q_COMPLETION(models.Model):
    question = models.ForeignKey(QUESTION, on_delete=models.DO_NOTHING)
    regex = models.CharField(max_length=200)


class Q_CHOICE(models.Model):
    question = models.ForeignKey(QUESTION, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300, blank=False)
    index = models.IntegerField(blank=False, default=0)


class Q_TABLE(models.Model):
    question = models.ForeignKey(QUESTION, on_delete=models.DO_NOTHING)
    field = models.CharField(max_length=300, blank=False)
    field_type = models.IntegerField()
    serial_number = models.IntegerField()
    cell_type = models.IntegerField()


class Q_TABLE_OPTIONS(models.Model):
    field = models.ForeignKey(Q_TABLE, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300, blank=False)


class Q_IMAGE(models.Model):
    question = models.ForeignKey(QUESTION, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    size = models.IntegerField(null=True)


class A_IMAGE(models.Model):
    answer = models.ForeignKey(ANSWER, on_delete=models.DO_NOTHING)
    url = models.ImageField(upload_to='images')


class A_TABLE(models.Model):
    answer = models.ForeignKey(ANSWER, on_delete=models.DO_NOTHING)
    row_field = models.ForeignKey(Q_TABLE, related_name='row', on_delete=models.DO_NOTHING)
    column_field = models.ForeignKey(Q_TABLE, related_name='column', on_delete=models.DO_NOTHING)
    serial_number = models.IntegerField()
    content = models.TextField(blank=False)


class A_CHOICE(models.Model):
    answer = models.ForeignKey(ANSWER, on_delete=models.DO_NOTHING)
    option = models.ForeignKey(Q_CHOICE, on_delete=models.DO_NOTHING)


class A_COMPLETION(models.Model):
    answer = models.ForeignKey(ANSWER, on_delete=models.DO_NOTHING)
    completion = models.ForeignKey(Q_COMPLETION, on_delete=models.DO_NOTHING)
    content = models.TextField(blank=False)
