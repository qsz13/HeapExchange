from .models import Course
from haystack import indexes


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    user = indexes.CharField(model_attr='initiator')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Course

    def index_query(self, using=None):
        return self.get_model().objects.all()
