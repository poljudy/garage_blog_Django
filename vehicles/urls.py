from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
#    path('post_vehicle/<slug:slug>', views.PostDetail.as_view(), name='post_vehicle'),
#   path('edit_post/<post_id>',
#        views.add_edit_post, name='add_edit_post'),
#   path('delete_post/<post_id>',
#         views.delete_post, name='delete_post'),
#   path("search_vehicle", views.search_car, name="search_vehicle"),
#   path('<slug:slug>/', views.search_vehicle,
#         name='search_vehicle'),  # link to vehicle in search
]