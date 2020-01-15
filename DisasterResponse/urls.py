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
from django.conf import settings
from django.conf.urls.static import static


from operations import views as operationViews
from accountsapp import views as accountsViews


urlpatterns = [
    path('', operationViews.home, name='home'),
    path('unauthorized/<profileType>/', operationViews.unauthorized, name='unauthorized'),
    path('operation/create/', operationViews.createOperation, name='create_operations'),
    path('operation/change/', operationViews.changeOperation, name='change_operations'),
    path('operation/view/', operationViews.viewOperations, name='view_operations'),
    path('volunteer/enroll/', operationViews.enrollVolunteers, name='enroll_volunteers'),
    path('profile/<username>/', accountsViews.viewProfile, name='profile'),
    path('profile/<username>/updateinfo/', accountsViews.editProfile, name='update_info'),
    # path('organization/profile/<username>', accountsViews.viewOrganizations, name='organization_profile'),
    # path('organization/profile/<username>/updateinfo/', accountsViews.editOrganizationInfo, name='update_organization_info'),
    path('organization/<username>/volunteers/',accountsViews.viewVolunteer,name='volunteer_organization'),
    path('signup/volunteer/', accountsViews.volunteer_signup, name='volunteer_signup'),
    path('signup/organization/', accountsViews.organization_signup, name='organization_signup'),
    path('login/', authViews.LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)