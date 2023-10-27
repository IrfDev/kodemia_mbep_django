# [Lookup fields or QuerySe Field lookup](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#id4):

Are the specific syntax to filter entities inside a query eg


This:

```python
Entry.objects.get(id__exact=14)
Entry.objects.get(id__exact=None)
```

Is the equivalent to this: 


```SQL
SELECT ... WHERE id = 14;
SELECT ... WHERE id IS NULL;
```
