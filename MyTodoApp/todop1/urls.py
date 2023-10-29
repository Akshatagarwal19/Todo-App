from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_page),
    path('list',views.list),
    path('task',views.task),
    path('delete/<int:id>', views.delete)
]
