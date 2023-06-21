from django.urls import path
from .views import ShowroomListView,ShowroomDetailView,ShowroomCreateView,ShowroomUpdateView,ShowroomDeleteView

urlpatterns = [
    path("car/", ShowroomListView.as_view(), name="list_car"),
    path("car/<int:pk>/", ShowroomDetailView.as_view(), name="detail_car"),
    path("car/add/", ShowroomCreateView.as_view(), name="add_car"),
    path("car/<int:pk>/update/", ShowroomUpdateView.as_view(), name="update_car"),
    path("car/<int:pk>/delete/", ShowroomDeleteView.as_view(), name="delete_car"),
]