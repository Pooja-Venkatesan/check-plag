from django.urls import path
from . import views

print(views)  # Print the value of the `views` variable

urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    # path('report/', views.ViewPDF.as_view(), name="report"),
    path('report/', views.report, name='report'),
    path('compare/', views.fileCompare,name='compare'), 
    path('test/', views.test,name='Test'),
    path('filetest/', views.filetest,name='filetest'),
    path('twofiletest1/', views.twofiletest1,name='twofiletest1'),
    path('twofilecompare1/', views.twofilecompare1,name='twofilecompare1'),
   
]
