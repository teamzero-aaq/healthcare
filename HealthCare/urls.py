"""Scholar_Help URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path

from . import views

# from Scholar_Help.views import home, login, register

urlpatterns = [

    path('login/', views.login),
    path('test/', views.testingdd),
    path('admin/', views.admin),
    path('verifyuser', views.verifyuser),
    path('patient_dashboard/', views.patient_dashboard),
    path('games/', views.play_games),
    path('patient_profile/', views.patient_profile),
    path('savepatient_profile', views.savepatient_profile),
    path('patient_viewevent/', views.patient_viewevent),
    path('meditation/', views.meditation),
    path('wishlist/', views.wishlist),
    path('addwishlist', views.addwishlist),
    path('removewishlist', views.removewishlist),
    path('addpatientpost', views.addpatientpost),
    path('doctor_contact', views.doctor_contact),
    path('stress_analysis', views.stress_analysis),
    path('stress_analysis_submit', views.stress_analysis_submit),

    path('ask_ques/', views.ask_ques),
    path('addpatques', views.addpatques),
    path('viewpatientdetails', views.viewpatientdetails),
    url(r'^viewpatienttest/(?P<pk>\d+)$', views.viewpatienttest),
    url(r'^posts/(?P<pk>\d+)$', views.viewpostdetails),
    url(r'^chatwithdoc/(?P<pk>\d+)$', views.chatwithdoc),

    url(r'^question/(?P<pk>\d+)$', views.viewquestiondetail),
    path('addchat', views.addchat),
    path('testing/', views.testing),

    path('doctor_dashboard/', views.doctor_dashboard),
    path('adddocpost', views.adddocpost),
    url(r'^answer/(?P<pk>\d+)$', views.viewdocans),
    url(r'^doc_profile/(?P<pk>\d+)$', views.viewdocprofile),

    path('docgiveans', views.docgiveans),
    path('add_event', views.add_event),
    path('add_event_db', views.add_event_db),
    path('doctor_profile/', views.doctor_profile),
    path('doctortips/', views.doctor_tips),
    path('patient_signup', views.patient_signup),
    path('doctor_signup', views.doctor_signup),
    path('user_add', views.user_add),
    path('', views.login),
]
