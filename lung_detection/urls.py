from django.urls import path


from .views import XrayView, XrayDetail

app_name = 'api'

urlpatterns =[
    path('lung_detect/',XrayView.as_view(), name='lung-detect'),

    path('detail_view/<int:pk>', XrayDetail.as_view(), name='view_detail'),

]