from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),  # Já existe, para enquetes
    path("", include("polls.urls")),  # Novo: faz a página inicial redirecionar para a URL de enquetes
]
