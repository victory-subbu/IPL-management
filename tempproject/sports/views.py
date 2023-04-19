from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import viewsets





def home(request):
    emp=Playerslist.objects.all()
    print(emp)
    context={'res':emp}
    return render(request,'home1.html',context)


def search(request):
    key=request.GET.get('q')
    res=None
    try:
        res=Playerslist.objects.get(id=key)
        context={'result':res}
    except Playerslist.DoesNotExist:
        context={'result':None}
    #print(res)
    return render(request,'search.html',context)

def search1(request):
    countryname=request.GET.get('q1')
    x=Playerslist.objects.all().filter(country=countryname)
    context={'result':x}
    #print(x)
    return render(request,'search1.html',context)

def search2(request):
    teamname=request.GET.get('q2')
    x=Playerslist.objects.filter(team=teamname)
    context={'result':x}
    return render(request,'search2.html',context)

def search3(request):
    playername=request.GET.get('q3')
    #playername="virat kohli"
    x=Playerslist.objects.select_related('playerstats').get(playername=playername)
    print(x.playername,x.jerseynumber,x.country,x.team.team_name,x.playerstats.matches,x.playerstats.runs,x.playerstats.wickets)
    context={'result':x}
    return render(request,'search3.html',context)

def search4(request):
    playername=request.GET.get('q4')
    player=Playerslist.objects.get(playername=playername)
    matches=player.match.all()
    for match in matches:
        print(match.name,match.venue,match.date)
    context={'result':matches}
    return render(request,'search4.html',context)

def search5(request):
    matchname=request.GET.get('q5')
    date=request.GET.get('q6')
    players=Playerslist.objects.filter(match__name=matchname,match__date=date)
    # match=Match.objects.get(name=matchname,date=date)
    # players =PlayersList.filter(name=match.name,)
    #print(match.name,match.date)
    for player in players:
         print(player.playername, player.team.team_name)
    context={'result':players}
    return render(request,'search5.html',context)

def search6(request):
    n=request.GET.get('q7')
    n=int(n)
    top_players=PlayerStats.objects.order_by('-runs')[:n]
    for player in top_players:
        print(f"{player.player.playername} - {player.runs} runs")
    context={'result':top_players}
    return render(request,'search6.html',context)

def search7(request):
    n=request.GET.get('q8')
    n=int(n)
    top_players=PlayerStats.objects.order_by('-wickets')[:n]
    for player in top_players:
        print(f"{player.player.playername} - {player.wickets} runs")
    context={'result':top_players}
    return render(request,'search6.html',context)
def search8(request):
    playername=request.GET.get('q9')
    newmatchname=request.GET.get('q10')
    x=Playerslist.objects.get(playername=playername)
    y=IplTeamsList.objects.get(team_name=newmatchname)
    x.team=y
    #print(x.team.team_name)
    x.save()
    print(x.playername,x.team.team_name)
    context={'result':x}
    return render(request,'search8.html',context)

# def search9(request):
#      teamname=request.GET.get('q10')
#      iplobj=IplTeamsList.objects.filter(team_name=teamname)
    #  print(iplobj)
     #x=Playerslist.objects.filter(team=teamname)
  
     
        
    # y=x.objects.select_related('playerstats').order_by('-runs')
   
        






def index(request):
    return render(request,'sports.html')



@api_view(['GET'])
def checkapi(request):
    playersobject=Playerslist.objects.all()
    serializer=PlayerslistSerializer(playersobject,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postapi(request):
    serializer=PlayerslistSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateapi(request,id):
    playersobject=Playerslist.objects.get(id=id)
    serializer=PlayerslistSerializer(instance=playersobject,data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteapi(request,id):
    playersobject=Playerslist.objects.get(id=id)
    playersobject.delete()
    return Response("message is deleted")

#Generic Api class based views
class PlayerslistGet(ListAPIView):
    queryset=Playerslist.objects.all()
    serializer_class=PlayerslistSerializer


class PlayerslistCreate(CreateAPIView):
    queryset=Playerslist.objects.all()
    serializer_class=PlayerslistSerializer


#Viewset
class PlayersViewSet(viewsets.ViewSet):
    def list(self,request):
        playersobject=Playerslist.objects.all()
        serializer=PlayerslistSerializer(playersobject,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        x=pk
        if(x is not None):
            playersobject=Playerslist.objects.get(id=id)
            serializer=PlayerslistSerializer(playersobject)
            return Response(serializer.data)
        


# #SportsData.objects.all()
# #SportsData.get(id=key)
# #SportsData.objects.filter(name="virat kohli")
# #SportsData.objects.order_by(Length('name').asc())
# #SportsData.exclude('')






























def index(request):
    return render(request,'sports.html')


def add_data(request):
    if(request.method=='POST'):
        name=request.POST['name']
        price=request.POST['price']
       
        inst=Sportsdata(name=name,price=price)
        inst.save()

    else:
        pass
    sportslist=Sportsdata.objects.all()
    context={
        "sportslist":sportslist
    }
    return render(request,'adddata.html',context)



def delete_data(request,myid):
    data=Sportsdata.objects.get(id=myid)
    data.delete()
    return redirect(add_data)


def edit_data(request,myid):
    updatedata=Sportsdata.objects.get(id=myid)
    data=Sportsdata.objects.all()
    context={
        'updatedata': updatedata,'data': data
    }
    return render(request,'sports.html',context)

