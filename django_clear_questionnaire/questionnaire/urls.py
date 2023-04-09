from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create),
    path('deleteProject', views.deleteProject),
    path('deleteSubmit', views.deleteSubmit),

    path('publishProject', views.publishProject),
    path('suspendProject', views.suspendProject),

    path('getProjects', views.getProjects),
    path('getProjectsCount', views.getProjectsCount),

    path('getQuestion', views.getQuestion),
    path('getQuestionsPublic', views.getQuestionsPublic),
    path('getQuestionsPrivate', views.getQuestionsPrivate),

    path('deleteQuestion', views.deleteQuestion),
    path('moveQuestion', views.moveQuestion),

    path('createSingleChoice', views.createSingleChoice),
    path('createMultipleChoice', views.createMultipleChoice),
    path('createCompletion', views.createCompletion),
    path('createImage', views.createImage),

    path('editSingleChoice', views.editSingleChoice),
    path('editMultipleChoice', views.editMultipleChoice),
    path('editCompletion', views.editCompletion),

    path('postQuestionnaire', views.postQuestionnaire),

    path('getAnalysis', views.getAnalysis),
    path('getSubmits', views.getSubmits),
    path('getSubmitDetail', views.getSubmitDetail),
    path('downloadData', views.downloadData),

    path('getRecommendations', views.getRecommendations),
    path('searchProjects', views.searchProjects),
    path('getHotProjects', views.getHotProjects),

]
