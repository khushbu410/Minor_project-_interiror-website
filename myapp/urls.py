from django.urls import path
from myapp import views
# from .views import login_view

urlpatterns = [
    
    path('',views.index,name='myapp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('book//<service_name>/', views.Book_view, name='book'),
    path('meetdesigner/', views.meet_designer, name='meetdesigner'),
    path('howitworks/', views.how_it_work, name='howitworks'),
    path('service/', views.services, name='services'),
    path('singleblog/', views.singleblog, name='singleblog'),
    path('contect/', views.contect, name='contect'),
    

    
        
]
