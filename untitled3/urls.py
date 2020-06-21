
from django.conf.urls import url
from django.contrib import admin


from app01 import views
from app02 import views as views2
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login2/', views.login2),
    url(r'^login/', views.login),
    url(r'^book/', views.book),
    url(r'^book/', views.book),
    url(r'^addbook/', views.addbook),
    url(r'^deletebook/', views.deletebook),
    url(r'^editbook/', views.editbook),
    url(r'^author/', views.author),
    url(r'^addauthor/', views.addauthor),
    url(r'^deleteauthor/', views.deleteauthor),
    url(r'^editauthor/', views.editauthor),
    url(r'^logout/', views.logout),
    url(r'^registe/', views.registe),
    url(r'^ajax/', views2.ajax),
    url(r'^ajaxadd/', views2.ajaxadd),
    url(r'^ajaxmany/', views2.ajaxmany),
    url(r'^pc-geetest/register/', views.get_geetest),
    url(r'^fileup/', views2.fileup),
    url(r'^blogregiste/', views2.registe),


]
