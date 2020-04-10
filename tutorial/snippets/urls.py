from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'snippet',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
