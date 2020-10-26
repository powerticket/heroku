from django.urls import path

from .views import writing_views, comment_views

app_name = 'board'
urlpatterns = [
    # writing_views
    path('', writing_views.index, name='index'),
    path('create/', writing_views.create, name='create'),
    path('<int:board_pk>/', writing_views.detail, name='detail'),
    path('<int:board_pk>/update/', writing_views.update, name='update'),
    path('<int:board_pk>/delete/', writing_views.delete, name='delete'),

    # comment_views
    path('<int:board_pk>/comment/create', comment_views.create, name='comment_create'),
    # path('<int:board_pk>/comment/<int:comment_pk>/delete/', comment_views.comment_delete, name='comment_delete'),

]
