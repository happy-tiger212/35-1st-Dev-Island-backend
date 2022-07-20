from django.urls import path

from products.views import DetailView

urlpatterns = [
    path('/detail/<product_id>', DetailView.as_view())
]