from rest_framework import serializers
from ProjecteDjangoAlexMarcDavid.models import Platform, Game,User

class PlatformSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Platform
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Game
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = User
        fields = '__all__'