#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import boto3
import os

def s3_upload():
   s3 = boto3.resource('s3')
   bucket = s3.Bucket('camdataraspi')
# linuxコマンドでjpgファイルを取得
   cmd = 'find /home/pi/YO/movie -type f -name "*.mp4"'
   file_names = (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')
# 配列化
   array_files = file_names.split()
#ファイルをアップロード
   for item in array_files:
       s3_filename = item.split('/home/pi/YO/movie/')[1]
       bucket.upload_file(item, s3_filename)
