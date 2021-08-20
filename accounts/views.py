
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from .models import *
from django.views.generic import View
from .forms import *

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages #import messages
from accounts.models import user_type
from django.contrib.auth import get_user_model

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
User = get_user_model()

from student_admission.settings import EMAIL_HOST_USER

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':' https://school-ui-main.herokuapp.com/',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@JDMR_ischool.com' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})



class signup_parents_student(View):
    def post(self, request):

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            form.save()

            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']

            usert = None
            user = User.objects.get(email=email)
            usert = user_type(user=user,is_parents=True)
            usert.save()

           
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')


    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup1.html', {'form': form})


def schoolsignup_details(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')

        school_details.objects.create(email=email, name=name, contact_number=contact_number)

        return HttpResponseRedirect(reverse('login'))


    else:
        
        return render(request, 'accounts/school_signup_details.html')


class signup_school(View):

    # code for superadmin only

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup1.html', {'form': form})


    def post(self, request):

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = 'jdmr.com'
            subject = 'Activate Your jdmr Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': 'JDMR',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                
            })
            user.email_user(subject, message)

            messages.success(request, ('Please Confirm your email to complete registration.'))

            return redirect('signup_school')

        else: 
            return redirect('signup_school')


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            print('1')
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            print('2')


        if user is not None and account_activation_token.check_token(user, token):
            print('3')
            user.is_active = True
            user.save()
            print('4')


            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            print('6')

            print('The confirmation link was invalid, possibly because it has already been used.')
            return redirect('home')




@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')


def student_login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)
        print(password)
        print('-----------------------jshdg sdj sdbhjdbkdnsd------------------')
        user = authenticate(username=email, password=password, school=True)

        if user is not None:
            auth.login(request, user)
            print('222222222222')
            return HttpResponseRedirect(reverse('home'))

        else:
            print('invalid creddentils')
            
            return render(request, 'accounts/login1.html')


    else:
        print('Somethings went wrong, contact us')
        return render(request, 'accounts/login1.html')
