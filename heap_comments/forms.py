from django import forms
from django.utils.translation import ugettext_lazy as _
from django_comments.forms import CommentDetailsForm, CommentForm




class CommentFormWithOutEmail(CommentForm):
    def __init__(self,*args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["email"].required = False