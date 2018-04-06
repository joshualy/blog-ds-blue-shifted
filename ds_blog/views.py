from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

image_list = [('penn_waterfall1.jpg','Waterfall'),
    ('penn_fallcolors1_cropped.jpg','Fall Colors'),
    ('maine1.jpg','Maine'),
    ('nz_flower.jpg','NZ Flower'),
    ('nz_beach1.jpg','NZ Beach 1'),
    ('nz_beach2.jpg','NZ Beach 2'),
    ('nz_beach3.jpg','NZ Beach 3'),
    ('nz4.jpg','NZ 4'),
    ('nz5.jpg','NZ 5'),
    ('nz6.jpg','NZ 6'),
    ]

def penn(request):
    context_dic = {'imgs': image_list}
    return render(request,'ds_blog/penn.html',context_dic)

def index(request):
    return render(request,'ds_blog/index.html')


def myseattle(request):
    return render(request,'ds_blog/notebooks/seattle_bicycle/seattle_bicycle_data.html')

def logistic_regression(request):
    context_dic = {'imgs': image_list}
    return render(request,'ds_blog/logisticRegression.html',context_dic)


def linear_regression(request):
    context_dic = {'imgs': image_list}
    return render(request,'ds_blog/linearRegression.html',context_dic)

def pseudospectral(request):
    context_dic = {'imgs': image_list}
    return render(request,'ds_blog/notebooks/pseudospectral_continuation/pseudospectral_example.html',context_dic)

def pseudospectral_blog1(request):
    context_dic = {'imgs': image_list}
    return render(request,'ds_blog/pseudospectral_blog1.html')

def evaluation_metrics1(request):
    context_dic = {'imgs': image_list}
    return render(request,'ds_blog/EvaluationMetrics1.html',context_dic)

def introduction(request):
    # context_dic = {'imgs': image_list}
    return render(request,'ds_blog/introduction.html')#,context_dic)

def list(request):
    return render(request,'ds_blog/bloglist.html')
