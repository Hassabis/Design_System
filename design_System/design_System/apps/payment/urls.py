from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'payment/',views.PaymentStatusView.as_view())
]