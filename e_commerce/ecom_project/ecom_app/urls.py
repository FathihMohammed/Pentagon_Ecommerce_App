from django.urls import path
from .import views
app_name='ecom_app'
urlpatterns=[
    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='all_product_cat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodetails,name='prodetails'),
]