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

