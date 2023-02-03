from . import views
from django.urls import path
from .views import post_vehicle_view


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
#    path("admin2", views.admin.as_view(), name="admin2"),
#    path("admin/vehicles/post", admin.vehicles.post.as_view(), name="admin_post"),    # noqa
    path('delete/<post_id>', views.delete_post, name='delete'),
    path('post_vehicle_view/', post_vehicle_view, name='post_vehicle_view'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_vehicle', views.PostVehicle.as_view(), name='post_vehicle'),

    #   path('edit_post/<post_id>',
    #        views.add_edit_post, name='add_edit_post'),
    #   path('delete_post/<post_id>',
    #         views.delete_post, name='delete_post'),
    #   path("search_vehicle", views.search_car, name="search_vehicle"),
    #   path('<slug:slug>/', views.search_vehicle,
    #         name='search_vehicle'),  # link to vehicle in search
]
