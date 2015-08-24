from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choice

# Create your views here.
def index(request):
    l_q_l= Question.objects.order_by('-pub_date')[:5]
    
    return render(request,'polls/index.html',{'latest_question_list': l_q_l,})


def detail(request,question_id):  
    question = get_object_or_404(Question, pk=question_id) 

    return render(request,'polls/details.html',{'question':question})

def results(request,question_id):  
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request,question_id):  
    
    return HttpResponse("You are voting on question %s" % question_id)


