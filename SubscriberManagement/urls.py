from django.urls import path
from .views import SubscriberView, SubscriberViewById, getSubscribersByFilter

urlpatterns = [
    path('subscriber', SubscriberView.as_view()),
    path('subscriber/filter', getSubscribersByFilter),
    path('subscriber/<str:id>', SubscriberViewById.as_view()),
]