# sample-django

## djangoインストール
python -m pip install Djangoe

python -m django --version
$3.2

## プロジェクトの作成(git clone時点で生成済み)
django-admin startproject mysite

### gitリポジトリの直下をプロジェクトとするので階層を移動
mv mysite/manage.py .
mv mysite/mysite/* mysite
rmdir .\mysite\mysite\ 

## 開発用サーバ
python manage.py runserver

### ポート指定
python manage.py runserver 8080

### 他の指定方法
https://docs.djangoproject.com/ja/3.2/ref/django-admin/#django-admin-runserver


## アプリケーションの作成(git clone時点で生成済み)
python manage.py startapp polls
