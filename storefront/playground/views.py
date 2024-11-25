from django.shortcuts import render
from django.db import transaction, connection
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Order, OrderItem, Product
from tags.models import TaggedItem

def say_hello(request):
    with connection.cursor() as cursor:
        cursor.callproc('')

    return render(request, 'hello.html', {'name': 'Mosh'})
