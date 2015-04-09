from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

__author__ = 'danielqiu'




class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(View):
    template_name_before = "index_before_login.html"
    template_name_after = "index_after_login.html"


    def get(self, request):
        user = request.user

        if not user.is_authenticated():
            return render(request, self.template_name_before)
        else:
            return render(request, self.template_name_after)

        # leading_project = None
        # involved_project = None
        # try:
        #     leading_project = user.student.leading_project.all()
        #     involved_project = user.student.involved_project.all()
        # except:
        #     pass
        #
        # return render(request, self.template_name,
        #               {"leading_project": leading_project, "involved_project": involved_project})