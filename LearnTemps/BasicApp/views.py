from django.shortcuts import render


# Create your views here.
def index(request):
    cont_dic={"text":"hello world","number":100}
    return render(request, 'BasicApp/index.html',cont_dic)


def other(request):
    return render(request, 'BasicApp/other.html')


def rel_url_temps(request):
    return render(request, 'BasicApp/rel_url_temps.html')

