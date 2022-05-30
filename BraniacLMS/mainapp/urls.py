from django.urls import path
<<<<<<< HEAD
=======

>>>>>>> master
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
<<<<<<< HEAD
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
]
=======
    path("", views.MainPageView.as_view()),
    path("news/", views.NewsPageView.as_view()),
    path("courses/", views.CoursesPageView.as_view()),
    path("contacts/", views.ContactsPageView.as_view()),
    path("doc_site/", views.DocSitePageView.as_view()),
    path("login/", views.LoginPageView.as_view()),
]
>>>>>>> master
