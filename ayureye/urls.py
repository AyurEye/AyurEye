"""ayureye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import path
from django.urls import path, include
from django.contrib import admin

from django.conf.urls import url

from rest_framework.schemas import get_schema_view
from django.urls import path

from rest_framework_simplejwt import views as jwt_views
# from api.views import GoogleLogin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static 


schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Showroom API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Test description",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    # path('prediction_api/', include('prediction_api.urls')),
    path('prediction_api/', include('lung_detection.urls')),


    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('schema', schema_view),
    path('auth/', include('rest_auth.urls')),
    # path('social-login/google/', GoogleLogin.as_view(), name='google_login'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



