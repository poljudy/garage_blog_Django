from . import views
from django.urls import path
from .views import (
    post_vehicle_view,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostList,
    PostDetail,
    PostLike,
    post_vehicle,
    delete_post,
    addVehicle,
    post_vehicle_view
)


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('delete/<post_id>', delete_post, name='delete'),
    path('post_vehicle/', post_vehicle, name='post_vehicle'),
    path('add_vehicle/', addVehicle, name='add_vehicle'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post_vehicle_view/', post_vehicle_view, name='post_vehicle_view'),  # noqa
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
    #   Future menu items may be as follows
    #   path("search_vehicle", views.search_vehicle, name="search_vehicle"),
    #   path('<slug:slug>/', views.search_vehicle,
    #         name='search_vehicle'),  # link to vehicle in search
]
