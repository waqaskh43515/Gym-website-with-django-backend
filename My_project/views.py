from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms
from videos.models import Videos
from news.models import News
from contactenquiry.models import Contactenquiry
from django.core.paginator import Paginator


def homepage(request):
    all_data = Videos.objects.all()
    all_data1 = News.objects.all()


    paginator = Paginator(all_data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    totalpages = page_obj.paginator.num_pages




    # if request.method == 'GET':
    #     st = request.GET.get('servicename')
    #     if st != None:
    #         all_data = Videos.objects.filter(Name__icontains=st)
    return render(request,'index.html',{'data':page_obj,'data1':all_data1,'lastpage':totalpages,'totalpageslist':[n+1 for n in range(totalpages)]})


def saveEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en = Contactenquiry(Name=name,Email=email,Phone=phone,Message=message)
        en.save()
    return render(request,'about.html')


def detail_page(request,newname):

    data = News.objects.get(new_name=newname)
    return render(request,'news_detail.html',{'data':data})



def aboutus(request):
    return render(request,'about.html')



def Classes(request):
    return render(request,'Classes.html') 


def Passdata(request):
    return HttpResponse(request)




def examsheet(request):
        num1 = eval(request.POST.get('num1'))
        num2 = eval(request.POST.get('num2'))
        num3 = eval(request.POST.get('num3'))
        num4 = eval(request.POST.get('num4'))
        num5 = eval(request.POST.get('num5'))
        Total = num1 + num2 + num3 + num4 + num5
        Percentage = (Total/500)*100
        if Percentage >= 80:
            Dev = 'A+'
        elif Percentage >= 70:
            Dev = 'A'
        elif Percentage >= 60:
            Dev = 'B'
        elif Percentage >= 50:
            Dev = 'C'
        elif Percentage >= 40:
            Dev = 'D'
        else:
            Dev = 'F'
        result = {'Total':Total,'Percentage':Percentage,'Dev':Dev}  
        print(result)  
        return render(request,'examsheet.html',result)



def evenodd(request):
    result = ''
    try:
        if request.POST.get('num1') == "":
            return render(request,'evenodd.html',{'error':True})
            
        num1 = eval(request.POST.get('num1'))
        result =  num1%2
        if result == 0:
            result = 'even'
        else:
            result = 'odd'    
    except: 
        result = 'invalidddddddd operationnnnnnn'

    return render(request,'evenodd.html',{'result':result})


def calculator(request):
    result = ''
    uf = userforms()

    try:
        num1 = eval(request.POST.get('num1'))
        num2 = eval(request.POST.get('num2'))
        opr = request.POST.get('operation')
        if opr == '+':
            result = num1 + num2
        elif opr == '-':
            result = num1 - num2
        elif opr == '*':
            result = num1 * num2
        elif opr == '/':
            result = num1 / num2
    except:
        result='invalidddddddd operationnnnnnn'  
    print(result)    
                     
    return render(request,'calculatore.html',{'result':result,'form':uf})

def blog(request):
    uf = userforms()
    data = {"form":uf}
    try:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        data = {"form":uf,"name":name,"phone":phone,"email":email,"message":message}
        # url = "/about-us/?value={}".format(name)
        # return HttpResponseRedirect(url)
    except:
        print("Error Found")
    return render(request,'blog.html',data) 