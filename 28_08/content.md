# [Django tpl](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#block)

# Adding templates:
1. Add all the directories to the settings.py
   1. ````python
      TEMPLATES = [
          {
              ...
              "DIRS": [os.path.join(BASE_DIR, ".")],
              ...
          },
      ]
   ````
2. Adding template.html to the app directory
   1. You can extend from base or do a base from scratch
   2. If you're adding a child component, you'll need to declare a block
   3. ````django
        {% extends "base.html" %} {% block normal_content %}

      <dl class="text-white text-lg font-mono">
        {% for koder in koders %}

        <dd class="ml-2 text-sm">name: {{koder.name}}</dd>
        <dd class="ml-2 text-sm mb-3">id: {{koder.id}}</dd>
        {% endfor %}
      </dl>
      {% endblock %}

   ````
3. Adding view to views.py with the render method, passing component
````python
def VIEW_FUNCTION(req, *PARAMS):
    return render(req, "NAME_OF_YOUR_TEMPLATE.html", context={"params": *params})
````
4. Adding the url to the urlPatterns list
````python 
urlpatterns = [
  ...
  path("SOME_PATH/<str:SOME_INT_PARAM>/<str:SOME_STRING_PARAM>", VIEW_FUNCTION),
  ...
]
````

# [Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)

Models are the DB classes we define.

These Models, are based on an ORM where you can create each class with an specific syntax. No matter which DB system you're using




You can import them directly from models, or if you saved it in another app, you can import it with `YOUR_APP.YOUR_MODEL`.


Remember that each Model is a class with some predefined methods.

Some notes:
- The objects key includes a set of functions to interact with the DB
- When you're creating a new instance on the database you need to call the `.save()` method in your Model class to persist the change
- Inheritance and all the class features are available as each Model is a regular Python Class

## [Field types](https://docs.djangoproject.com/en/4.2/topics/db/models/#field-types):

You can import them from `models.DEFINED_TYPE` where you can find different pre-defined types that you can use. 

Please noticed that each field type is a function that take some required arguments.

