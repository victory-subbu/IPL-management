from django.db import models

# Create your models here.
class Sportsdata(models.Model):
     name=models.CharField(max_length=100)
     price=models.IntegerField()


class Match(models.Model):
    name=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.name



class IplTeamsList(models.Model):
    team_name=models.CharField(max_length=100,primary_key=True)


class Playerslist(models.Model):
    playername=models.CharField(max_length=100)
    jerseynumber=models.IntegerField()
    country=models.CharField(max_length=100)
    team=models.ForeignKey(IplTeamsList,on_delete=models.CASCADE)
    match=models.ManyToManyField('Match',related_name='player')

class PlayerStats(models.Model):
    player=models.OneToOneField(Playerslist,on_delete=models.CASCADE)
    matches=models.IntegerField()
    runs=models.IntegerField()
    wickets=models.IntegerField()
   


    
    





    