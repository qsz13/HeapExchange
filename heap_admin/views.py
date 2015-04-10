from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class StaffLoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffLoginRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)


class TempView(StaffLoginRequiredMixin, TemplateView):
    template_name = 'heap_admin/heap_admin.html'