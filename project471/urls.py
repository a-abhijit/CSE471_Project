"""museum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views
app_name = 'app1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.HomePage,name='index'),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('ticket/',views.BuyTicket,name='ticket'),
    path('gallery/',views.Gallery,name='gallery'),
    path('forget/',views.Forget,name='forget'),
    path('reset/',views.Reset,name='reset'),
    path('viewdetails1/',views.Detail1,name='detail1'),
    path('viewdetails2/',views.Detail2,name='detail2'),
    path('viewdetails3/',views.Detail3,name='detail3'),
    path('viewdetails4/',views.Detail4,name='detail4'),
    path('viewdetails5/',views.Detail5,name='detail5'),
    path('viewdetails6/',views.Detail6,name='detail6'),
    path('viewdetails7/',views.Detail7,name='detail7'),
    path('viewdetails8/',views.Detail8,name='detail8'),
    path('viewdetails9/',views.Detail9,name='detail9'),
    path('delete_account/',views.delete_account,name='delete_account'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('submit_review2/', views.submit_review2, name='submit_review2'),
    path('submit_review3/', views.submit_review3, name='submit_review3'),
    path('submit_review4/', views.submit_review4, name='submit_review4'),
    path('submit_review5/', views.submit_review5, name='submit_review5'),
    path('submit_review6/', views.submit_review6, name='submit_review6'),
    path('submit_review7/', views.submit_review7, name='submit_review7'),
    path('submit_review8/', views.submit_review8, name='submit_review8'),
    path('submit_review9/', views.submit_review9, name='submit_review9'),
    

]
