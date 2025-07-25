from django.urls import path
from temp.views import contact_student, success_page



urlpatterns = [
    path('', contact_student, name='home'),
    path("success/", success_page, name='success')
]