"""backend_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users.views import userAPIView as usersPath
from projects.views import projectAPIView as projectsPath
from websites.views import websiteAPIView as websitesPath
from phases.views import phaseAPIView as phasesPath
from project_image.views import projectImagesAPIView as projectImagesPath
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('users', usersPath.as_view(), name='users'),
    path('users/<int:id>', usersPath.as_view(), name='users_id'),
]

urlpatterns += [
    path('projects', projectsPath.as_view()),
    path('projects/<int:id>', projectsPath.as_view()),
]

urlpatterns += [
    path('websites', websitesPath.as_view()),
    path('websites/<int:id>', websitesPath.as_view()),
]

urlpatterns += [
    path('phases', phasesPath.as_view()),
    path('phases/<int:id>', phasesPath.as_view()),
]

urlpatterns += [
    path('project_images', projectImagesPath.as_view()),
    path('project_images/<int:id>', projectImagesPath.as_view()),
]
