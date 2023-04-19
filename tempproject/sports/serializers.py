from rest_framework import serializers
from .models import *
class PlayerslistSerializer(serializers.ModelSerializer):
   class Meta:
       model=Playerslist
       fields='__all__'