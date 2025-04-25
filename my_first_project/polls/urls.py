from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),  # Página inicial das perguntas
    path("<int:question_id>/", views.detail, name="detail"),  # Detalhes da pergunta
    path("<int:question_id>/results/", views.results, name="results"),  # Resultados da pergunta
    path("<int:question_id>/vote/", views.vote, name="vote"),  # Votação da pergunta
]
