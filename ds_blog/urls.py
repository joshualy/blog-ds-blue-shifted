from django.conf.urls import url
from ds_blog import views

app_name = "ds_blog"
urlpatterns=[
            # url(r'^index/',views.index,name='index'),
            url(r'^seattle_data/',views.myseattle,name='myseattle'),
            url(r'^list/',views.list,name='list'),
            url(r'^logistic_regression/',views.logistic_regression,
                                    name='logistic_regression'),
            url(r'^linear_regression/',views.linear_regression,
                                    name='linear_regression'),
            url(r'^pseudospectral/',views.pseudospectral,
                                    name='pseudospectral'),
            url(r'^pseudospectral-functions/',views.pseudospectral_blog1,
                                    name='pseudospectral_blog1'),
            url(r'^evaluation-metrics-regression/',views.evaluation_metrics1,
                                    name='evaluation_metrics1'),
            url(r'^introduction/',views.introduction,
                                    name='introduction'),
]
