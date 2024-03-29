from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('feed', views.homePage, name='feed'),
    path('new-question', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('reply', views.replyPage, name='reply'),
    path('', views.index, name='index'),
]
