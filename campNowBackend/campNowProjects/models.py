from django.db import models

# Create your models here.
'''Add code to campNowProjects/models.py
String (VARCHAR) -  name (itemName)
Date (DATETIME) -  createdAt
Decimal (FLOAT) - rating 1.1
Integer (INTEGER) -  numNeeded//number Needed of that item //of items in the list
Boolean (BIT) - requiresBatteries  ISInWishList - the place is added to the wishlist
'''
class Item(models.Model):
    #added this next line for authentication lab9 slide 11
    #So who created this Item will only have access to manipulate it
#uncommented this in step 27. of project
#setting default=0 becsus getting error unless set
    owner = models.ForeignKey(
        'auth.User',
        related_name='items', default=1,
        on_delete=models.CASCADE)
    #Date (DATETIME) -  createdAt
    created = models.DateTimeField(auto_now_add=True)
    #String (VARCHAR) -  itemName
    name = models.CharField(max_length=200, unique=True)
    #Decimal (FLOAT) - rating 1.1   field_name = models.FloatField(**options)
    rating = models.FloatField(max_length=2)
    #Integer (INTEGER) -  numNeeded//number Needed of that item //of items in the list
    #(choices=list(zip(range(1, 6), range(1, 6)))) could do to limit the number to 1 and 5
    numNeeded = models.IntegerField()
    #Boolean (BIT) - requiresBatteries  ISInWishList - the place is added to the wishlist
    requiresBatteries = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        #could put - infront to oder descending EX: # Order by score descending
        #ordering = ('-score',)


    def __str__(self):
        return self.name

#could make size an attribute of item
    ''' SIZE_CHOIZES  = (
    ('T', 'Tiny'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    )
    size = models.CharField(max_length=1, choices=SIZE_CHOIZES) '''

#if want a user model with email and password and Date
'''class User(models.Model):
            #added this next line for authentication lab9 slide 11
            #So who created this Item will only have access to manipulate it
    owner = models.ForeignKey(
                'auth.User',
                related_name='items',
                on_delete=models.CASCADE)
                #Date (DATETIME) -  createdAt
    created = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, unique=True)

    class Meta:
                    ordering = ('created',)
                    #could put - infront to oder descending EX: # Order by score descending
                    #ordering = ('-score',)
    def __str__(self):
        return self.name'''
