from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^redirect_to_user_home$', views.user_home),
    url(r'^add_book$', views.add_book),
    url(r'^display_book/(?P<book_id>\d+)$', views.details_book),
    url(r'^update_book/(?P<book_id>\d+)$', views.update_book),
    url(r'^post_update/(?P<book_id>\d+)$', views.post_update),

]
