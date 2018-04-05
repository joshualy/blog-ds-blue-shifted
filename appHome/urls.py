from django.conf.urls import url
from appHome import views

app_name = "appHome"
urlpatterns=[
            # url(r'^index/',views.index,name='index'),
            url(r'^seattle_data/',views.myseattle,name='myseattle'),
            url(r'^blog/',views.main_blog,name='main_blog'),
            url(r'^logistic_regression/',views.logistic_regression,
                                    name='logistic_regression'),
            url(r'^linear_regression/',views.linear_regression,
                                    name='linear_regression'),
            url(r'^pseudospectral/',views.pseudospectral,
                                    name='pseudospectral'),
            url(r'^pseudospectral_blog1/',views.pseudospectral_blog1,
                                    name='pseudospectral_blog1'),
            url(r'^evaluation_metrics1/',views.evaluation_metrics1,
                                    name='evaluation_metrics1'),
            url(r'^introduction/',views.introduction,
                                    name='introduction'),
]
