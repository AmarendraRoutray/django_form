from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *
from django.http import HttpResponse




def create_topic(request):
    
    ETFO = TopicForm()
    d={'ETFO':ETFO}
    
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['TopicName']
            
            TO = Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            
            return HttpResponse('Topic created Successfully!!!!')
        else:
            return HttpResponse('Invalid Entry')

    return render(request,'create_topic.html',d)





def create_webpage(request):
    EWFO = WebpageForm()
    d = {'EWFO':EWFO}
    if request.method=='POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            tn = WFDO.cleaned_data['TopicName']
            TO = Topic.objects.get(topic_name=tn)
            
            nm = WFDO.cleaned_data['Name']
            em = WFDO.cleaned_data['Email']
            ur = WFDO.cleaned_data['Url']
            
            WO = Webpage.objects.get_or_create(topic_name=TO, name=nm,email=em,url=ur)[0]
            WO.save()
            
            QLWO = Webpage.objects.all()
            d = {'webpage':QLWO}
            
            return render(request,'display_webpage.html',d)
        else:
            return HttpResponse('Invalid Input')
    
    return render(request,'create_webpage.html',d)





def create_AccessRecord(request):
    EAFO = AccessRecordForm()
    d = {'EAFO':EAFO}
    
    if request.method == 'POST':
        AFDO = AccessRecordForm(request.POST)
        if AFDO.is_valid():
            nm = AFDO.cleaned_data['Name']
            WO = Webpage.objects.get(pk=nm)
            
            au = AFDO.cleaned_data['Author']
            dt = AFDO.cleaned_data['Date']
            
            AO = AccessRecord.objects.get_or_create(name=WO,author=au,date=dt)[0]
            AO.save()
            
            QLAO = AccessRecord.objects.all()
            d = {'accessrecord':QLAO}
            
            return render(request,'display_accessrecord.html',d)
        else:
            return HttpResponse('Invalid Input')
    
    return render(request,'create_AccessRecord.html',d)