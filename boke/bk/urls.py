from django.conf.urls import url
import bk.views
urlpatterns = [
    url(r'^muban',bk.views.muban,name='muban'),
    url(r'^aa/(?P<aa_id>[0-9]+)/$',bk.views.wz1,name='wz1'),
    url(r'^zj/(?P<aa_id>[0-9]+)/$',bk.views.zj,name='zj'),
    url(r'^zj/xg/$',bk.views.xg,name='xg'),
    url(r'^zc/$',bk.views.zc,name='zc'),
    url(r'^zccg/$',bk.views.zccg),
    url(r'^dl',bk.views.dl,name='dl'),
    url(r'^lll',bk.views.dl,name='lll'),
    url(r'^zjm',bk.views.zjm,name='zjm'),
    url(r'^zt/(?P<aa_id>[0-9]+)/$',bk.views.zt,name='zt'),
    url(r'^dt/(?P<aa_id>[0-9]+)/$',bk.views.dt,name='dt'),
    url(r'^read/(?P<aa_id>[0-9]+)',bk.views.read),
    url(r'^yh/(?P<aa_id>[0-9]+)/$', bk.views.yh,name='yh'),
    url(r'^yhxg/$', bk.views.yhxg, name='yhxg'),
    url(r'^yyyh/$',bk.views.yyyh,name='yyyh'),


]
