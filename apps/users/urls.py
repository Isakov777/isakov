from django.urls import path
from apps.users.views import UserCreateView
urlpatterns = [
    path('signup', UserCreateView.as_view(), name='signup'),
    # path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('delete/<int:pk>/', UserdeleteView.as_view(), name='user_delete')
]