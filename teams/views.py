from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.request import Request
from teams.models import Team
from django.forms.models import model_to_dict
from .validations import InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError, world_cup_happened, verify_titles, is_title_negative


class TeamView(APIView):
    def post(self, request: Request) -> Response:

        try:
            world_cup_happened(request.data['first_cup'])
        except InvalidYearCupError as error:
            return Response({"error": error.message},
                            status.HTTP_400_BAD_REQUEST)
        
        try:
            is_title_negative(request.data['titles'])
        except NegativeTitlesError  as error:
            return Response({"error": error.message},
                            status.HTTP_400_BAD_REQUEST)   

        try:
            verify_titles(request.data['titles'], request.data['first_cup'])
        except ImpossibleTitlesError as error:
            return Response({"error": error.message},status.HTTP_400_BAD_REQUEST )

        team_data = request.data

        team = Team.objects.create(**team_data)

        return Response(model_to_dict(team), status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            t = model_to_dict(team)

            teams_list.append(t)
        return Response(teams_list, status.HTTP_200_OK)


class DetailedTeamView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
           team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)
    

    def patch(self, request: Request, team_id:int) -> Response:
        try:
           team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        for key, value in request.data.items():
            setattr(team, key, value)
        
        team.save()
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)
    

    def delete(self, request: Request, team_id:int) -> Response:
        try:
           team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


