
from django.conf import settings
from django.urls import include, path
from rest_framework import routers


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('Gepeat_rest.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=  [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
