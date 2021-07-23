from django.shortcuts import render
from .models import Winner
# Create your views here.

from django.http import HttpResponse

from .forms import ContactForm,WinnerForm
from  .models import Winner

from django.shortcuts import redirect

def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')

def about_view(request):
    return  render(request,'KBC/about.html')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'KBC/contact.html', context)


def index(request):
    allWinners=Winner.objects.all()
    if request.method == 'POST':
        form = WinnerForm(request.POST)
        if form.is_valid():
            mobile_num=form.data['mobile_number']
            lottery_num=form.data['lottery_number']
            winner=Winner.objects.get(mobile_number=mobile_num,lottery_number=lottery_num)
            print(winner)
            context={"winner":winner}
            return render(request, 'KBC/winner.html',context)
    form=WinnerForm()
    context={'form':form,"allWinners":allWinners}

    return render(request, 'KBC/index.html',context)
