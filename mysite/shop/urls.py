from django.urls import path,include
from shop import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackerStatus'),
    path('search/',views.search,name='Search'),
    path('products/<int:myid>',views.productview,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout'),
]
