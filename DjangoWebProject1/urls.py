from django.contrib import admin
from django.urls import path, include


from.import view
urlpatterns = [


    path('', view.index, name="Home"),

path('admin/', admin.site.urls),
path('shop/', include('shop.urls'))
]