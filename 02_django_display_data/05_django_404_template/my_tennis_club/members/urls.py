# from django.urls import path
# from . import views

# urlpatterns = [
#     path('members/', views.members, name='members')
# ]

# --------------------------------------------------

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('members/', views.members, name='members'),
#     path('members/details/<int:id>', views.details, name='details')
# ]


# --------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
