from django.urls import path
from .views import HomeView, ArticleDetail, PostView, EditPost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('add_post/', PostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>/', EditPost.as_view(), name='update_article'),
    path('article/delete/<int:pk>/', DeletePost.as_view(), name='delete_article'),
]
