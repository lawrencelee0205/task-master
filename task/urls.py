from django.urls import path
from task import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<uuid:pk>/', views.task_detail),
    path('class_tasks/', views.TaskList.as_view()),
    path('class_tasks/<uuid:pk>/', views.TaskDetail.as_view()),
    path('mixins_tasks/', views.TaskMixinList.as_view()),
    path('mixins_tasks/<uuid:pk>/', views.TaskMixinDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)