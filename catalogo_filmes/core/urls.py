from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiretorViewSet, FilmeViewSet

# Roteador automático do DRF
router = DefaultRouter()
router.register(r'diretores', DiretorViewSet)
router.register(r'filmes', FilmeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]