from django.conf.urls import url
from exam import views
urlpatterns =[
url("test",views.showtest),
url("result",views.showResult),
url("^$",views.showland),
]
