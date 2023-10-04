from django.urls import path, include

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('news/', ShowAllNews.as_view(), name='show_all_news'),
    path('articles/', ShowAllArticles.as_view(), name='show_all_articles'),
    path('news/create/', CreateNews.as_view(), name='create_news'),
    path('articles/create/', CreateArticles.as_view(), name='create_articles'),
    path('news/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('news/update/<slug:slug>/', UpdatePost.as_view(), name='update_post'),
    path('news/delete/<slug:slug>/', DeletePost.as_view(), name='delete_post'),
    path('accounts/', include('allauth.urls')),
    path('get_author/', get_author, name='upgrade'),
    # path('login/', LoginUser.as_view(), name='login_page'),
    # path('register/', RegisterUser.as_view(), name='register_page'),
    # path('logout/', LogoutUser.as_view(), name='logout_page'),
]
