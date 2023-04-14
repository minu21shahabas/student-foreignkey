from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('add',views.add,name='add'),
   path('add_course',views.add_course,name='add_course'),
   path('stud',views.stud,name='stud'),
   path('addstud',views.addstud,name='addstud'),
   path('show',views.show,name='show'),
   path('editpage/<int:id>',views.editpage,name='editpage'),
   path('editstudent/<int:id>',views.editstudent,name='editstudent'),
   path('delete/<int:id>',views.delete,name='delete')

]
