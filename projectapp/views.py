from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .helpers import send_forget_password_mail
from .models import *
from .models import Profile
import uuid
import json
import stripe
import time
import settings


@login_required(login_url='login')
def HomePage(request):
    notifications = Notification.objects.all().order_by('-timestamp')[:5]  # Fetch latest 5 notifications
    return render(request, 'index.html', {'notifications': notifications})


def SignupPage(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken.')
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is taken.')
                return redirect('signup')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()

            profile_obj = Profile.objects.create(user=user_obj)
            profile_obj.save()

            messages.success(request, 'Signup successful. You can now log in.')
            return redirect('login')

    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during signup.')

    return render(request, 'signup.html')

def LoginPage(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                messages.error(request, 'Both Username and Password are required.')
                return redirect('login')

            user_obj = User.objects.filter(username=username).first()

            if user_obj is None:
                messages.error(request, 'User not found.')
                return redirect('login')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Wrong password.')
                return redirect('login')

            login(request, user)
            return redirect('index')

    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during login.')

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Forget(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            user_obj = User.objects.filter(username=username).first()
            
            if not user_obj:
                messages.error(request, 'No user found with this username.')
                return redirect('/forget/')
            
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            
            profile_obj.forget_password_token = token
            profile_obj.save()
            
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, 'An email is sent. Please check your inbox to reset the password.')
            return redirect('/forget/')
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during password reset.')

    return render(request, 'forget.html')

def BuyTicket(request):
    return render(request, 'ticket.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Reset(request, token):
    context = {}
    try:
        profile_obj = get_object_or_404(Profile, forget_password_token=token)
        context['user_id'] = profile_obj.user.id
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if not user_id:
                messages.error(request, 'No user id found.')
                return redirect(f'/reset/{token}/')
                
            if new_password != confirm_password:
                messages.error(request, 'Both passwords should be equal.')
                return redirect(f'/reset/{token}/')
            
            user_obj = get_object_or_404(User, id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            
            # Clear the forget_password_token in the profile after password reset
            profile_obj.forget_password_token = ''
            profile_obj.save()
            
            messages.success(request, 'Your password has been reset. You can now log in with the new password.')
            return redirect('/login/')
            
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during password reset.')

    return render(request, 'reset.html', context)
def Detail1(request):
    reviews = Review.objects.all()
    return render(request, 'viewdetails1.html', {'reviews': reviews})
def Detail2(request):
    reviews = Review2.objects.all()
    return render(request, 'viewdetails2.html', {'reviews': reviews})
def Detail3(request):
    reviews = Review3.objects.all()
    return render(request, 'viewdetails3.html', {'reviews': reviews})
def Detail4(request):
    reviews = Review4.objects.all()
    return render(request, 'viewdetails4.html', {'reviews': reviews})
def Detail5(request):
    reviews = Review5.objects.all()
    return render(request, 'viewdetails5.html', {'reviews': reviews})
def Detail6(request):
    reviews = Review6.objects.all()
    return render(request, 'viewdetails6.html', {'reviews': reviews})
def Detail7(request):
    reviews = Review7.objects.all()
    return render(request, 'viewdetails7.html', {'reviews': reviews})
def Detail8(request):
    reviews = Review8.objects.all()
    return render(request, 'viewdetails8.html', {'reviews': reviews})
def Detail9(request):
    reviews = Review9.objects.all()
    return render(request, 'viewdetails9.html', {'reviews': reviews})
@login_required
def delete_account(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update':
            new_username = request.POST.get('username')
            new_email = request.POST.get('email')

            if new_username:
                request.user.username = new_username
                request.user.save()
                messages.success(request, 'Username updated successfully.')
                return render(request, 'index.html')

            if new_email:
                request.user.email = new_email
                request.user.save()
                messages.success(request, 'Email updated successfully.')
                return render(request, 'index.html')

        elif action == 'delete':
            request.user.delete()
            messages.success(request, 'Account deleted successfully.')
            return redirect('/signup/')  # Redirect to signup or login page

    return render(request, 'delete_account.html')


from django.http import JsonResponse


from django.shortcuts import render, redirect
from .models import Review

def submit_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails1/')  # Redirect to the frontend page
    
def submit_review2(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review2.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails2/')  # Redirect to the frontend page
def submit_review3(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review3.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails3/')  # Redirect to the frontend page
def submit_review4(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review4.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails4/')  # Redirect to the frontend page
def submit_review5(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review5.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails5/')  # Redirect to the frontend page
def submit_review6(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review6.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails6/')  # Redirect to the frontend page
def submit_review7(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review7.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails7/')  # Redirect to the frontend page
def submit_review8(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review8.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails8/')  # Redirect to the frontend page
def submit_review9(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review9.objects.create(rating=rating, comment=comment)
        return redirect('/viewdetails9/')  # Redirect to the frontend page
def buyticket(request):
    all2 = museums.objects.all()
    # print(all2)
    return render(request, 'ticket.html', {'mus': all2})
def muedetail(request, pk):
    item = museums.objects.get(id=pk)
    print(item,'lll')
    print(request.user,'sdd')
    mdetail = museums.objects.get(id=pk)


    user1 = Profile.objects.get(user=request.user)

    commentsall1 = comments.objects.filter(
        comment_on_mu=museums.objects.get(id=pk))

    if request.method == 'POST':
        print("########################################")

        if 'quanti' in request.POST:
            quan = int(request.POST['quanti'])

            print('hvjhv.', quan)

            print('THis is :', user1, mdetail)
            adding = ticketcart.objects.create(
                user=user1, item=mdetail, quant=quan)
            adding.save()
            return redirect(cartView)

        elif 'comm' in request.POST:
            print("######################ufg#############")
            comment = request.POST['comm']

            print('comm.', comment)

            # print('THis is :', user1, mdetail)
            adding2 = comments.objects.create(
                user=user1, comment_on_mu=mdetail, comment=comment)
            adding2.save()
            return redirect(cartView)

    return render(request, 'ticketdetail.html', {'item': item, 'commentsall1': commentsall1})
def cartView(request):
    prod_lst = ticketcart.objects.filter(
        user=Profile.objects.get(user=request.user))

    total_prod = len(prod_lst)
    # serial = 0
    lst1 = []
    total_sum = 0
    for i in prod_lst:
        x = int(i.item.price) * int(i.quant)

        prod_lst.total_p = x

        lst1.append(x)
        total_sum += x

    print(total_prod, total_sum, lst1)

    allcoup = Coupon.objects.all()
    cupname = [row.coup_name for row in allcoup]
    cupvalue = [row.multi for row in allcoup]
    print(cupname, cupvalue)

    ####################################################
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    showmess = ''
    if 'coupon1' in request.POST:
        given = request.POST['coupon1']
        print(given)
        if given in cupname:
            # print(total_sum, 'ok')
            ind = cupname.index(given)
            print(ind, 'index')
            total_sum = total_sum * (cupvalue[ind]/100)
            print(total_sum)
            diss = str(100 - cupvalue[ind])
            messages.success(
                request, f'Congratulation! You got {diss}% of disscount. Currently your total amount is {total_sum} Tk')
        else:
            #
            messages.success(request, 'Your COUPON was not right')

        # mess
        return redirect(cartView)

    if 'pay1' in request.POST:
        # if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': settings.PRODUCT_PRICE,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN +
            '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        return redirect(checkout_session.url, code=303)
        # return render(request, 'user_payment/product_page.html')

    return render(request, "cartview2.html", {"cart": prod_lst, 'total_prod': total_prod, 'total_sum': total_sum, 'lst1': lst1, 'showmess': showmess})
    
def payment_successful(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = request.user.user_id
    user_payment = UserPayment.objects.get(app_user=user_id)
    user_payment.stripe_checkout_id = checkout_session_id
    user_payment.save()
    return render(request, 'user_payment/payment_successful.html', {'customer': customer})

def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return render(request, 'user_payment/payment_cancelled.html')













