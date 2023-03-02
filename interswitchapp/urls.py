from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


route = DefaultRouter()

route.register('',views.PaymentValidation,basename='payment_validation')

urlpatterns = [ 
    # path('',)
] + route.urls