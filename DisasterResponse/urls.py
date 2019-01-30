"""DisasterResponse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as authViews


from operations import views as operationViews
from accountsapp import views as accountsViews


urlpatterns = [
    path('', operationViews.home, name='home'),
    path('operations/create/', operationViews.createOperation, name='create_operations'),
    path('signup/volunteer/', accountsViews.volunteer_signup, name='volunteer_signup'),
    path('signup/organization/', accountsViews.organization_signup, name='organization_signup'),
    path('login/', authViews.LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
