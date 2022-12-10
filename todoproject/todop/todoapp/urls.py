from . import views
from django.urls import path
app_name='todoapp'
urlpatterns = [

    path('index',views.index,name="index"),
    #path('detail',views.detail,name="detail"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('Listview/',views.Listview.as_view(),name='Listview'),
    path('Detail_view/<int:pk>/',views.Detail_view.as_view(),name='Detail_view'),
    path('Update_view/<int:pk>/', views.Update_view.as_view(), name='Update_view'),
    path('Delete_view/<int:pk>/', views.Delete_view.as_view(), name='Delete_view'),

]
