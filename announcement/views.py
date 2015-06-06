from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from announcement.models import Announcement


class AnnouncementView(View):
    template_name="announcement/announcement.html"


    def get(self, request):

        announcement_list = reversed(Announcement.objects.all())

        return render(request, self.template_name,{"announcement_list":announcement_list})