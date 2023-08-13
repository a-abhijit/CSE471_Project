from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE )
# class Profile(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     forget_password_token = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username
from django.db import models
from django.contrib.auth.models import User

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.rating}"



class Notification(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# models.py


class Review(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
class Review2(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
    
class Review3(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
class Review4(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
class Review5(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
class Review6(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
class Review7(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
    
class Review8(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
class Review9(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"
    
class museums(models.Model):
    name = models.CharField(max_length= 100)
    des = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    img = models.ImageField(upload_to = 'static/img/')

    def __str__(self):
        return self.name
class ticketcart(models.Model):    
    user = models.ForeignKey(Profile, on_delete= models.CASCADE)
    item = models.ForeignKey(museums, on_delete= models.CASCADE)
    total_p = models.IntegerField(default=1)
    quant = models.IntegerField(default=1)
    pur= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.CharField(max_length=255, blank= True, null= True)

    def __str__(self):
        return f'Bought {self.quant} tickets of {self.item}'
class comments(models.Model):    
    user = models.ForeignKey(Profile, on_delete= models.CASCADE)
    comment_on_mu = models.ForeignKey(museums, on_delete= models.CASCADE)
    comment = models.CharField(max_length= 500, blank = True, null = True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented {self.when}'
class UserPayment(models.Model):
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
class Coupon(models.Model):    
    coup_name = models.CharField(max_length= 100)
    multi = models.IntegerField(default=1)

    def __str__(self):
        return f'This {self.coup_name} will reduce amount to {self.multi}'


