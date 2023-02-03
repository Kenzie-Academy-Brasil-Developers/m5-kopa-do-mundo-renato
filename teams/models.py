from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(blank=True,null=True ,default=0)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(blank=True, null=True)


# {
#     "name": "brasil",
#     "titles": 5,
#     "top_scorer": "neymar",
#     "fifa_code": 123,
#     "first_cup": "1990-03-03"
# }

