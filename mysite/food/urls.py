from django.urls import path
from . import views

urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name='index'),
    # /food/pk
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    # add items
    path('add', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:id>', views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>', views.delete_item, name='delete_item'),

]
