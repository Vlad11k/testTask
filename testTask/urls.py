from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from clients.views import ClientViewSet
from clients.views import ClientAPIList, ClientAPIRetrieve, ClientAPIProfile
from employees.views import EmployeeViewSet

router = DefaultRouter()
router.register(r"employee", EmployeeViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/client/', ClientAPIList.as_view()),
    path('api/v1/client/<int:pk>/', ClientAPIRetrieve.as_view()),
    path('api/v1/client/profile', ClientAPIProfile.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
