from django.contrib import admin

# Register your models here.

from .models import Notification
admin.site.register(Notification)

from .models import Review
admin.site.register(Review)

from .models import Review2
admin.site.register(Review2)

from .models import Review3
admin.site.register(Review3)

from .models import Review4
admin.site.register(Review4)

from .models import Review5
admin.site.register(Review5)

from .models import Review6
admin.site.register(Review6)

from .models import Review7
admin.site.register(Review7)

from .models import Review8
admin.site.register(Review8)

from .models import Review9
admin.site.register(Review9)

from .models import museums, ticketcart, UserPayment, comments, Coupon

admin.site.register(museums)
admin.site.register(ticketcart)
admin.site.register(UserPayment)
admin.site.register(comments)
admin.site.register(Coupon)




