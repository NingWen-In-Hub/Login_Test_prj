from django.urls import path
from . import views

app_name = 'login_test_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile_create/', views.ProfileCreateView.as_view(), name="profile_create"),
    path('profile_edit/<int:pk>/', views.ProfileEditView.as_view(), name="profile_edit"),
    path('user_list', views.UserListView.as_view()),
    path('user_listA', views.UserListAView.as_view()),
    path('user_listB', views.UserListBView.as_view()),
    path('test403/', views.MyView403, name='403'),
    path('test500/', views.MyView500, name='500'),

]
