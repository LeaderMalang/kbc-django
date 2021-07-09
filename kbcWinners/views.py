from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .forms import ContactForm,WinnerForm
from  .models import Winner


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def index(request):
    if request.method == 'POST':
        form = WinnerForm(request.POST)
        if form.is_valid():
            mobile_num=form.data['mobile_number']
            lottery_num=form.data['lottery_number']
            winner=Winner.objects.get(mobile_number=mobile_num,lottery_number=lottery_num)
            print(winner)
            context={"winner":winner}
            return render(request, 'winner.html',context)
    form=WinnerForm()
    context={'form':form}

    return render(request, 'home.html',context)
