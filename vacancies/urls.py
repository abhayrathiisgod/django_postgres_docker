from django.urls import path
from .views import JobView, HasOpening, JobViewSingle, Applyjob


urlpatterns = [
    path('jobs/', JobView.as_view()),
    path('jobs/<int:pk>/', JobViewSingle.as_view(), name='job-detail'),
    path('jobs/has-openings/', HasOpening.as_view()),
    path('apply-job/', Applyjob.as_view()),
]
