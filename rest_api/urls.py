from django.urls import path, include
from rest_framework import routers
from rest_api.views import *

routers=routers.DefaultRouter()
routers.register('Student',StudentViewSet,'Student')
routers.register('ParentDetails',ParentDetailsViewSet,'ParentDetails')
routers.register('ContactDetails',ContactDetailsViewSet,'ContactDetails')
routers.register('AdditionalDetails',AdditionalDetailsViewSet,'AdditionalDetails')
routers.register('Documents',DocumentsViewSet,'Documents')

urlpatterns = [
    path('', include(routers.urls)),

]
