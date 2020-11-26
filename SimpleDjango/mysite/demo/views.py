from django.shortcuts import render
from demo import models

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("http://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"myapi":api})  #{}为传给html的参数
    
def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("http://api.github.com/users"+user)
        username = json.loads(user_request.content)
        return render(request, 'user.html', {'username':username})
        
    else:
        notfound = "请在搜索框中输入你要查询的用户..."
        return render(request,'user.html',{'notfound':notfound})
        
def ani(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        models.Animal.objects.create(first_name=first,last_name=last)
    all = models.Animal.objects.all()
    return render(request, 'animal.html', {'animal':all})