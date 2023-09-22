#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : file.py
# Time       : 2023/3/7 15:51
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：上传文件
"""
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from web import models

from web.utils.bootstrap import BootStrapForm, BootStrapModelForm


# def upload_file(request):
#     """ 上传文件 """
#     if request.method == "GET":
#         return render(request, "upload_file.html")
#
#     # 读取文件
#     file_object = request.FILES.get('avatar')
#
#     # 将上传的文件写入到内存中
#     f = open(file_object.name, mode='wb')
#     for chunk in file_object.chunks():
#         f.write(chunk)
#
#     f.close()
#
#     return HttpResponse("success")
#
#
# class UploadForm(BootStrapForm):
#     bootstrap_exclude_fields = ['img']
#
#     name = forms.CharField(label='机器人名称')
#     price = forms.CharField(label='价格')
#     num = forms.IntegerField(label="销售数量")
#     img = forms.FileField(label="形状")


# def upload_form(request):
#     """ 以form形式混合上传文件和数据 """
#     title = "Form上传"
#     if request.method == "GET":
#         form = UploadForm()
#         return render(request, 'upload_form.html', {"form": form, "title": title})
#
#     form = UploadForm(data=request.POST, files=request.FILES)
#     if form.is_valid():
#         # 1.读取图片内容， 写入到文件夹中并获取文件的路径
#         img_objects = form.cleaned_data.get("img")
#         # media_path = os.path.join(settings.MEDIA_ROOT, img_objects.name)    # 绝对路径
#         media_path = os.path.join('media', img_objects.name)    # 相对路径
#         f = open(media_path, mode="wb")
#         for chunk in img_objects.chunks():
#             f.write(chunk)
#         f.close()
#
#         # 2.将图片文件路径写入到数据库中
#         models.Bot.objects.create(
#             name=form.cleaned_data["name"],
#             price=form.cleaned_data["price"],
#             num=form.cleaned_data['num'],
#             img=media_path
#         )
#         return HttpResponse("...")
#     return render(request, 'upload_form.html', {"form": form, "title": title})


# class UploadModelForm(BootStrapModelForm):
#     bootstrap_exclude_fields = ['img']
#
#     class Meta:
#         model = models.Flowers
#         fields = "__all__"

#
# def upload_model_form(request):
#     """ ModelForm上传混合文件和数据 """
#     title = "ModelForm上传文件"
#     if request.method == "GET":
#         form = UploadModelForm()
#         return render(request, "upload_model_form.html", {'form': form, "title": title})
#
#     form = UploadModelForm(data=request.POST, files=request.FILES)
#     if form.is_valid():
#         # 对于文件会自动保存，并把 字段+上传路径写入到数据库
#         form.save()
#         return HttpResponse("success")
#     return render(request, 'upload_model_form.html', {"form": form, 'title': title})
