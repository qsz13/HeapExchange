from django.shortcuts import render
from post.models import Course, Activity, Tag


def index(request):
    if request.method == 'GET':
        return render(request, 'search/index.html')
    else:
        keyword = request.POST.get('keyword', '').lower()
        select = int(request.POST.get('select', ''))
        result = do_the_search(keyword, select)
        return render(request, 'search/result.html', {'list': result, 'select': select})


def do_the_search(keyword, select):
    if select == 3:
        tag_result = []
        for tag in Tag.objects.all():
            if keyword.lower() in tag.name.lower():
                for c in tag.course.all():
                    tag_result.append(c)
                for a in tag.activity.all():
                    tag_result.append(a)
        return tag_result
    else:
        obj_list = [[Course], [Activity], [Course, Activity]]
        result = iterate(keyword, obj_list[select])
        return result


def iterate(keyword, obj_list):
    result = []
    for obj in obj_list:
        for item in obj.objects.all():
            if keyword in item.title.lower():
                result.append(item)
    return result
