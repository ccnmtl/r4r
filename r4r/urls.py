from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from django_cas_ng import views as cas_views
from r4r.main import views
from rest_framework import routers

admin.autodiscover()


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'team', views.TeamViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cas/login', cas_views.LoginView.as_view(),
         name='cas_ng_login'),
    path('cas/logout', cas_views.LogoutView.as_view(),
         name='cas_ng_logout'),
    path('_impersonate/', include('impersonate.urls')),
    path('stats/', TemplateView.as_view(template_name='stats.html')),
    path('smoketest/', include('smoketest.urls')),
    path('uploads/<str:path>',
         serve, {'document_root': settings.MEDIA_ROOT}),
    path('sentry-debug/', trigger_error),
    re_path('', views.BaseView.as_view())
]


if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()
