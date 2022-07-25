from django.shortcuts import render
from sign.models import Workers

# Create your views here.
def service(request):
    service = request.GET.get("service")
    userid = request.GET.get("userid")
    x = Workers.objects.filter(service=service)
    return render(request, 'services.html', {'service': service,'rows':x,'userid':userid})


