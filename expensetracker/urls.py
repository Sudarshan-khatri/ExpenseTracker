"""
URL configuration for expensetracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views import View
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#TOkem for jwt authentication 
from registerandlogin.viewset.viewsets import RegisterViewset,LoginViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework import routers,permissions
from management.router.routers import expenseIncome_router



router=routers.DefaultRouter()
router.registry.extend(expenseIncome_router.registry) 


#swagger documetation:
schema_view=get_schema_view(
    openapi.Info(
        title="ExpenseTracker API",
        default_version='v1',
        description="API for ExpenseTracker",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="Khatrisudarshan360@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('auth/register',RegisterViewset.as_view(),name="Register"),
    path('auth/login',LoginViewset.as_view(),name="Register"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
