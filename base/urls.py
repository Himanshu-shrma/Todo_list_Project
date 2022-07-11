from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasklist,name='home'),
    path('edittask/<int:task_id>/',views.edit_task,name='edit-task'),
    path('showtask/<int:task_id>/',views.show_task,name='show-task'),
    path('addtask/',views.add_task,name='add-task'),
    path('deletetask/<int:task_id>',views.delete_task,name='delete-task'),
    path('updatetask/<int:task_id>',views.update_task,name='update-task')
]