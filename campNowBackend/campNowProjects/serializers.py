from rest_framework import serializers
from campNowProjects.models import Item
#Make sure to import the models you need in project
 #will nave to import the campNowProjects.views
 #might import the import games.views
 #next line from step 29 in project for authentication
 #used with UserSerializer and UserItemSerializer fx
from django.contrib.auth.models import User



class ItemSerializer(serializers.ModelSerializer):
      # We just want to display the owner username (read-only) step 30
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ('id',
                  'name',
                  'created',
                  'rating',
                  'numNeeded',
                  'requiresBatteries',
                  'owner')

#added for authentiacation step 29
#only include the fields that you want
class UserItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = Item
            fields = (
                'id',
                'name')
#added for authentiacation step 29
class UserSerializer(serializers.ModelSerializer):
    items = UserItemSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'pk',
            'username',
            'items')



'''class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name') '''


'''class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'games') '''
