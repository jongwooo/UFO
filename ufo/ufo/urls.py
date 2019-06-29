from django.contrib import admin
from django.urls import path, include
import page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    # path('signup/', page.views.signup, name='signup'),
    # path('login/', page.views.login, name='login'),
]
