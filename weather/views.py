from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']         #wruting this only will render an unbound errot 
    else:
        city = ''                                 #puting this else statemets removes it

    return render(request, 'index.html',{'city' : city})


