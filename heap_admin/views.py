from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse_lazy



from django.views.generic import TemplateView, CreateView
from announcement.models import Announcement


class StaffLoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffLoginRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)


class TempView(StaffLoginRequiredMixin, TemplateView):
    template_name = 'heap_admin/heap_admin.html'


class AnnouncementCreateView(CreateView):

    template_name = 'heap_admin/heap_admin_announcement_create.html'

    model = Announcement

    fields = ['title', 'body']

    success_url = reverse_lazy('index')
