from django.urls import path
import measurement.views 

urlpatterns = [
    path("sensors/", measurement.views.SensorView.as_view()),
    path("sensors/<int:pk>/", measurement.views.SensorViewDetailView.as_view()),
    path("measurements/", measurement.views.MeasurementView.as_view())
]
