from django.conf.urls import url


urlpatterns = [
    url(r'^login$', 'accounts.views.persona_login', name='persona_login'),
]
