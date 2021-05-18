import json

from news.models import Blog


with open('post_data.json') as f:
    posts_json = json.load(f)

for p in posts_json:
    post = Blog(title=p['title'], text=p['text'], author_id=p['user_id'])
    post.save()

