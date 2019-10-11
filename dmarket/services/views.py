from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
##### User API #####
@login_required
def index(request):
    return HttpResponse("Hello {}, world. Distributed Market.".format(request.user.id))
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def login(request):
#     context = {}
#     context['status'] = True
#     context['error_code'] = 0
#     context['message'] = 'User login API'

#     return render(request, 'general_status.json', context, 
#         content_type='application/json')

##### Machine API #####
@login_required
def submit_machine(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Submit machine API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')
@login_required
def remove_machine(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Remove machine API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')
@login_required
def list_machines(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'List machine API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

##### Job API #####
@login_required
def submit_job(request):
    job = Job()
    job.root_path = request.GET['root_path']
    job.core_num = int(request.GET['core_num'])
    job.user = User.objects.get(id=request.user.id)
    job.status = 'new'
    job.save()
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = "job {} create successfully, all jobs:{}".format(job.job_id, Job.objects.all())

    return render(request, 'general_status.json', context, 
        content_type='application/json')
@login_required
def cancel_job(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Cancel job API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')
@login_required
def get_result(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Get result API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')
@login_required
def get_log(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Get log API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

##### Credit API #####
@login_required
def get_credit(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Get credit API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')
