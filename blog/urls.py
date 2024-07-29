from django.urls import path
from .views import home, single, login_view, logout_view, register_view


urlpatterns  = [
    path('', view=home.as_view(), name='home_page'),
    path('blog/<int:pk>/', view=single.as_view(), name='blog_page'),
    path('login/', view=login_view.as_view(), name='login'),
    path('logout/', view=logout_view.as_view(), name='logout'),
    path('register/', view=register_view.as_view(), name='register'),
]
