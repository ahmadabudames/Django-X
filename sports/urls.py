from django.urls import path
from django.urls.resolvers import URLPattern

from .views import *

urlpatterns=[
     path('', sportsListView.as_view(), name= 'sports_list'),
     path('<int:pk>/', sportsDetailView.as_view(), name= 'sports_detail'),
     path('create/', sportsCreateView.as_view(), name= 'sports_create'),
     path('<int:pk>/update/', sportsUpdateView.as_view(), name= 'sports_update'),
     path('<int:pk>/delete/', sportsDeleteView.as_view(), name= 'sports_delete'),

]