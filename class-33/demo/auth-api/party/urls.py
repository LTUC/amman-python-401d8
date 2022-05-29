from lib2to3.pgen2 import token
from django.urls import path
from .views import PartyListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('party-list', PartyListView.as_view(), name="party_list"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzg5ODEyOSwiaWF0IjoxNjUzODExNzI5LCJqdGkiOiI5ZDg0ZjhjMTA4MDg0YmQ0OWVmM2EwZWU0ZDYzODdjNyIsInVzZXJfaWQiOjF9.zFmsN0gMIVpLv_-ToXU0mhRj6Fj1_s8pmS61S-xCpsA",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzODEyMDI5LCJpYXQiOjE2NTM4MTE3MjksImp0aSI6ImY5NWYyNWQyZmU1YTQxMGRiODlhZWI5ZWZmOWI0ODQxIiwidXNlcl9pZCI6MX0.gbrXlS3Dkeh30BBkhpDvfevRmOiienPNY18O8SmeBVg"
# }