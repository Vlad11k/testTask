from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from clients.views import ClientAPIList, ClientAPIRetrieve, ClientAPIProfile
from employees.views import EmployeeAPIList, EmployeeAPIRetrieve, EmployeeAPIProfile
from tasks.views import TaskAPIList, TaskAPIUpdate, TaskAPIEnd

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    path('api/v1/client/', ClientAPIList.as_view()),
    path('api/v1/client/<int:pk>/', ClientAPIRetrieve.as_view()),
    path('api/v1/client/profile', ClientAPIProfile.as_view()),

    path('api/v1/employee/', EmployeeAPIList.as_view()),
    path('api/v1/employee/<int:pk>/', EmployeeAPIRetrieve.as_view()),
    path('api/v1/employee/profile', EmployeeAPIProfile.as_view()),

    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/task/<int:pk>/end/', TaskAPIEnd.as_view()),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
