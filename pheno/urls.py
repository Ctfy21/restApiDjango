from django.urls import include, path
from rest_framework import routers

from experimentAPI.views import ExperimentAPIList, ExperimentAPIUpdate, ExperimentAPIDetailView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/experiment', ExperimentAPIList.as_view()),
    path('api/experiment/<int:pk>', ExperimentAPIUpdate.as_view()),
    path('api/experimentdetail/<int:pk>', ExperimentAPIDetailView.as_view()),
]

urlpatterns += router.urls