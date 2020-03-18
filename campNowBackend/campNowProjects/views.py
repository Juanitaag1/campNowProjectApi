from django.shortcuts import render
from campNowProjects.models import Item
from campNowProjects.serializers import ItemSerializer
from rest_framework import generics
#from rest_framework.response import Response
#from rest_framework.reverse import reverse
#added next 4 linesin step 32 to persist a user who makes a request
from django.contrib.auth.models import User
from campNowProjects.serializers import UserSerializer
from rest_framework import permissions
from campNowProjects.permissions import IsOwnerOrReadOnly

#added next 4 linesin step 32 to persist a user who makes a request
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

#added next 4 linesin step 32 to persist a user who makes a request
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'



# Create your views here.
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #In Step 36 add to configure permission
    #policies for the class-based views related to campNowProjects

permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    #from step 35 We will override the perform_create method to populate the
    #owner before a new Game instance is persisted in the database.
def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To Set the owner to the user received in the request
        serializer.save(owner=self.request.user)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #name = 'dog-detail'
    #from step 37 add to configure permission
    #policies for the class-based views related to campNowProjects
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly)

#step 37d
'''class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly) '''

#Step 36
'''class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
   permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )'''


    #from step 35
'''class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To Set the owner to the user received in the request
        serializer.save(owner=self.request.user)'''
