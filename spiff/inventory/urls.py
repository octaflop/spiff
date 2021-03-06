from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('spiff.inventory',
  url(r'^add$', 'views.addResource', name='add'),
  url(r'^(?P<id>[0-9]+)/qr.png$', 'views.qrCode', name='qr'),
  url(r'^(?P<id>[0-9]+)/qr-(?P<size>[0-9]+).png$', 'views.qrCode', name='qr'),
  url(r'^(?P<id>[0-9]+)/meta$', 'views.addMeta', name='meta'),
  url(r'^deleteMeta/(?P<id>[0-9]+)$', 'views.deleteMeta', name='deleteMeta'),
  url(r'^(?P<id>[0-9]+)/meta/(?P<name>.+)$', 'views.addMeta', name='meta'),
  url(r'^(?P<id>[0-9]+)/train$', 'views.train', name='train'),
  url(r'^(?P<id>[0-9]+)/certify$', 'views.certify', name='certify'),
  url(r'^(?P<certID>[0-9]+)/uncertify$', 'views.uncertify', name='uncertify'),
  url(r'^(?P<id>[0-9]+)/promote$', 'views.promoteTraining', name='promote'),
)

urlpatterns += views.InventoryView.as_url()
