from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("treadmills/", hello.views.treadmills, name="treadmills"),
    path("protien_shakes/", hello.views.protien_shakes, name="protien_shakes"),
    path("ellipticals/", hello.views.ellipticals, name="ellipticals"),
    path("healthy_snacks/", hello.views.healthy_snacks, name="healthy_snacks"),
    path("ankle_weights/", hello.views.ankle_weights, name="ankle_weights"),
    path("admin/", admin.site.urls),
]
