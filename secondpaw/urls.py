from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from accounts import urls as accounts_urls
from products import urls as products_urls
from cart import urls as cart_urls
from search import urls as search_urls
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
