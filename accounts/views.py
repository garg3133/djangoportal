from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Info
from .forms import UpdateForm

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile(request):
    info = Info.objects.all()
    id=0
    u=request.user.username
    for i in info:
        if i.username==u:
            id=i.id
            break
    if id==0:
        a=Info(username=u, college="IIITDMJ")
        a.save()
        id=i.id+1
        info = Info.objects.all()
    
    context = {
        'info': info[id-1]
    }
    return render(request, 'accounts/index.html', context)

def update(request):
    u=request.user.username
    info = Info.objects.get(username=u)
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            info.college = form.cleaned_data['college']
            info.save()
            return HttpResponseRedirect('../profile')
    else:
        form = UpdateForm()

    return render(request, 'accounts/update.html', {'form' : form})

def delete(request):
    u=request.user.username
    info = Info.objects.get(username=u)
    info.college = "-"
    info.save()
    return render(request, 'accounts/index.html', {'info' : info})