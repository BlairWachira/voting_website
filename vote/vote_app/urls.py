from django.urls import path
from. import views

urlpatterns = [
    path('', views.voter_choose, name='choose'),
    path('registration/', views.voter_reg, name='regestration'),
    path('identity/', views.code_identification, name='identity'),
    path('voting/', views.voting, name='voting'),
    path('vote/<int:candidate_id>/', views.cast_vote, name='cast_vote'),
    path('done/', views.done, name='done'),

]