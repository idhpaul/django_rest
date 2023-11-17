from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from tut_drf import views

urlpatterns = [
    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),

    #path('', views.api_root),
    path('', views.test,name="testUrlPatterns"),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),
    
    path('test', views.test),

    # url 제한을 시킬 수 있음(오류 방지) -> ex) 2000년 이후만 받도록 
    # /snippets/page, /snippets/pages 한번에 사용 가능
    # 일반적으로는 path("pages/", views.test), path("page/", vews.test) 두 개를 작성해야함
    #re_path(r"^pages?/$", views.test)
]

#urlpatterns = format_suffix_patterns(urlpatterns)