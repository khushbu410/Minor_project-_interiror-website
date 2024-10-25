from django.urls import path
from myapp import views
# from .views import login_view

urlpatterns = [
    
    path('',views.index,name='myapp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('book/', views.Book_view, name='book'),
    path('meetdesigner/', views.meet_designer, name='meetdesigner'),
    path('howitworks/', views.how_it_work, name='howitworks'),
    path('service/', views.services, name='services'),
    path('singleblog/', views.singleblog, name='singleblog'),
    path('contect/', views.contect, name='contect'),
    path('vastu_check/', views.vastu_check, name='vastu_check'), 
    path('vastu-info/', views.vastu_info, name='vastu_info'), 
    # path('vastu_result/', views.vastu_check, name='vastu_result'),

        
]
