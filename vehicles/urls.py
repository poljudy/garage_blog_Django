from . import views
from django.urls import path
from .views import (
    post_vehicle_view,
    PostCreateView,
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
#    path("admin2", views.admin.as_view(), name="admin2"),
#    path("admin/vehicles/post", admin.vehicles.post.as_view(), name="admin_post"),    # noqa
    path('delete/<post_id>', delete_post, name='delete'),
    path('post_vehicle/', post_vehicle, name='post_vehicle'),
    path('add_vehicle/', addVehicle, name='add_vehicle'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post_vehicle_view/', post_vehicle_view, name='post_vehicle_view'),  # noqa
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),


    #   path('edit_post/<post_id>',
    #        views.add_edit_post, name='add_edit_post'),
    #   path('delete_post/<post_id>',
    #         views.delete_post, name='delete_post'),
    #   path("search_vehicle", views.search_car, name="search_vehicle"),
    #   path('<slug:slug>/', views.search_vehicle,
    #         name='search_vehicle'),  # link to vehicle in search
]
