# In iEngApp/urls.py
from django.urls import path
from . import views

app_name = 'cmmsApp'

from django.views.static import serve
from django.conf import settings
urlpatterns = [
      path("request-demo/", views.request_demo_view, name="request_demo"),
    # path("contact-thanks/", views.thanks_view, name="contact_thanks"),  # if you add a separate thanks view for demo
    path('', views.home, name='home'),


   



    path('thanks/', views.contact_thanks, name='contact_thanks'),
    
    # More URLs
     # --- NEW: consulting block form + helper ---
    path("contact/submit/", views.contact_block_submit, name="contact_submit"),
    path("contact/phone-info/", views.phone_info, name="phone_info"),
    
    path("contact/country-list/", views.country_list, name="country_list"),




     path('sitemap.xml', views.sitemap, name='sitemap'),
      

]
