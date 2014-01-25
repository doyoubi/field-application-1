from django.conf.urls import url, patterns

from field_application.meeting_room.views import display_table
from field_application.meeting_room.views import display_listing 
from field_application.meeting_room.views import ApplyMeetingRoomView
from field_application.meeting_room.views import get_detail
from field_application.meeting_room.views import manage, ModifyView

urlpatterns = patterns(
    '',
    url(r'^apply/$', ApplyMeetingRoomView.as_view(), name='apply'),
    url(r'^table/$', display_table, name='table'),
    url(r'^list/$', display_listing, name='listing'),
    url(r'^manage/$', manage, name='manage'),
    url(r'^get_detail/$', get_detail, name='get_detail'),
    url(r'^modify/$', ModifyView.as_view(), name='modify'),
 )
