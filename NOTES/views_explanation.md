### how to create new application and add a function based view under it?

- `django-admin startapp <app-name>` 
- OR `python manage.py startapp <app-name>`
- when you create new application you get `views.py` file auto-created under application
- we write django function based views like following - 
```python
from django.shortcuts import HttpResponse, render

def view_name(request):
    return render(request, "subapp/welcome.html")
```


### what is django working directory?
### what is django project root?
- wherever you have `manage.py` file



### names of django generic views

- 127.0.0.1:8080/students (ListView)

- 127.0.0.1:8080/students/1 (DetailView)

- `from django.views.generic`
	- DetailView
	- ListView

- `from django.views.generic.edit`
	- CreateView
	- UpdateView
	- DeleteView



#### reverse vs reverse_lazy

- `from django.shortcuts import reverse`



- `from django.utils import reverse_lazy`

This function can do URL reversal before URLConf is loaded.
This function can be used to avoid `circular imports` issue.