"""adwiti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp.views import *
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    # path('get_slides/<project_id>', get_slides, name="get_slides"),

    # NEW URLS
    path('home/', home, name="home"),
    path('favicon.ico', RedirectView.as_view(
         url='/static/images/favicons/favicon.ico')),
    path('about/', about, name="about"),
    path('pricing/', pricing, name="pricing"),
    path('hiw/', hiw, name="hiw"),
    path('signup/', signup, name="signup"),
    path('logout/', log_out, name="logout"),
    path('login/', log_in, name="login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('adwiti/<user>/<project_name>/', adwiti, name="adwiti"),
    path('projectStartAjax/', projectStartAjax, name="projectStartAjax"),
    path('addSlideAjax/', addSlideAjax, name="addSlideAjax"),
    path('addImgAjax/', addImgAjax, name="addImgAjax"),
    path('account/', my_account, name="my_account"),
    path('update_info/', update_info, name="update_info"),
    path('change_password/', change_password, name="change_password"),
    path('addPPTAjax/', addPPTAjax, name="addPPTAjax"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
