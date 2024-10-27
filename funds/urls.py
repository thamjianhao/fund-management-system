from django.contrib import admin
from django.urls import path, include
from funds import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # URL for Django admin interface
    path('admin/', admin.site.urls),

    # URL for listing all funds and creating new ones
    path('funds/', views.fund_list),

    # URL for retrieving, updating or deleting a specific fund by ID
    path('funds/<str:id>/', views.fund_detail),
]

# Add format suffix patterns to support different response formats (e.g., .json)
urlpatterns = format_suffix_patterns(urlpatterns)
