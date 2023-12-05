from django.shortcuts import render
import json
import urllib . request


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']         #wruting this only will render an unbound errot 
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=591cb835a391ac630779528aeb2dc035').read()
        json_data = json.loads(res)                    # current data stored in this data variable
        data = {                                       # making it a dictionary
            'country_code': str (json_data['sys']['country']),
             "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            'temp' : str(json_data['main']['temp']) + 'k' ,  
            'pressure': str (json_data['main']['pressure']),                                           #all data converted to a dictionary
            'humidity': str (json_data['main']['humidity']),            
        }
    else:
        city = ''      
        data = {}                           #puting this else statemets removes it

    return render(request, 'index.html',{'city': city,  'data': data})


