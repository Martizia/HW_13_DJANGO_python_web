import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")
django.setup()

from quotes.models import Author, Quote, Tag # noqa
from .connect import connection


db = connection.get_database('hw9')
authors_collection = db['authors']
quotes_collection = db['quotes']

authors_data = authors_collection.find({})

for author in authors_data:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes_data = quotes_collection.find({})

for quote in quotes_data:
    tags = list()
    for t in quote['tags']:
        tag = t['name']
        tt, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(tt)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author_from_mongo = authors_collection.find_one({'_id': quote['author']})
        author_in_pg = Author.objects.get(fullname=author_from_mongo['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=author_in_pg
        )
        for t in tags:
            q.tags.add(t)
