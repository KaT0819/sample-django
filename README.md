# sample-django

# djangoインストール
```
python -m pip install Djangoe

python -m django --version
$3.2
```

# DB作成
```
python manage.py migrate
```


#
# 
# 開発用サーバ
```
python manage.py runserver
```

## ポート指定
```
python manage.py runserver 8080
```

## 他の指定方法
https://docs.djangoproject.com/ja/3.2/ref/django-admin/#django-admin-runserver


# 対話シェル
```
python manage.py shell
```



# プロジェクトの作成(git clone時点で生成済み)
```
django-admin startproject mysite
```

## gitリポジトリの直下をプロジェクトとするので階層を移動
```
mv mysite/manage.py .
mv mysite/mysite/* mysite
rmdir .\mysite\mysite\ 
```

# アプリケーションの作成(git clone時点で生成済み)
```
python manage.py startapp polls
```

# マイグレーション
## マイグレーションファイルの作成
```
python manage.py makemigrations polls
```

## マイグレーションのSQL出力
```
python manage.py sqlmigrate polls 0001
```

# 管理ユーザー作成
```
python manage.py createsuperuser
```

``` shell
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```
