from django.urls import path
from app_name.views import to_do_view, add_to_do, delete_to_do, is_important, is_completed, delete_completed, \
    delete_all, edit, redirect_edit

urlpatterns = [
    path('', to_do_view, name='todo'),
    path('todo/', to_do_view),
    path('addtodo/', add_to_do),
    path('deletetodo/<int:todo_id>/', delete_to_do),
    path('makeimportant/<int:todo_id>/', is_important),
    path('markascompleted/<int:todo_id>/', is_completed),
    path('deletecompleted/', delete_completed),
    path('deleteall/', delete_all),
    path('redirectedit/<int:todo_id>/<todo_content>', redirect_edit, name='redirectedit'),
    path('edit/<int:todo_id>/', edit)
]