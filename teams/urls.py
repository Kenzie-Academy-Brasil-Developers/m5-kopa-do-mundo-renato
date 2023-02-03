from django.urls import path
from .views import TeamView, DetailedTeamView

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:team_id>/',DetailedTeamView.as_view() )
]