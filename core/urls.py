"""core URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from courses import views as c
from persons import views as p
from schedule import views as s

router = routers.DefaultRouter()
router.register(r"c", c.CourseViewSet)
router.register(r"t", p.TeacherViewSet)
router.register(r"s", p.StudentViewSet)
router.register(r"g", p.GroupViewSet)
router.register(r"ic", s.IndividualClassViewSet, basename="individual")
router.register(r"ig", s.GroupClassViewSet, basename="group")

urlpatterns = [
    path('admin/', admin.site.urls),
	path("api/", include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
