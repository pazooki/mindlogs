from activities.models import ActivityModel
from activities.serializers import ActivitySerializer
from rest_framework import generics


class ActivityList(generics.ListCreateAPIView):
    queryset = ActivityModel.objects.all()
    serializer_class = ActivitySerializer


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityModel.objects.all()
    serializer_class = ActivitySerializer

# from django.shortcuts import render
# from django.utils.timezone import now
# from models import *
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def activity(request):
#
#     user = request.user
#
#     def add(form):
#         if form.is_valid():
#             material = form.save(commit=False)
#             material.mind = user
#             material.save()
#         else:
#             context.update(errors=form.errors)
#
#     def search(search_query):
#         top_activity = user.activitymodel_set.filter(info=search_query, archived=None).order_by('-created')
#         top_archived_activity = user.activitymodel_set.filter(info=search_query).exclude(archived=None).order_by('-archived')
#         return top_activity, top_archived_activity
#
#     def get():
#         top_activity = user.activitymodel_set.filter(archived=None).order_by('-created')
#         top_archived_activity = user.activitymodel_set.exclude(archived=None).order_by('-archived')
#         return top_activity, top_archived_activity
#
#     def archive(id):
#         user.activitymodel_set.filter(id=id).update(archived=now())
#
#     def delete(id):
#         user.activitymodel_set.filter(id=id).delete()
#
#     actions = {'search': search, 'add': add, 'archive': archive, 'delete': delete, 'get': get}
#     context = {}
#
#     if request.method == 'POST':
#         form = ActivityForm(request.POST, request.FILES)
#         if 'add' in form.data:
#             actions.get('add')(form)
#         if 'archive' in form.data:
#             actions.get('archive')(form.data.get('archive'))
#         if 'delete' in form.data:
#             actions.get('delete')(form.data.get('delete'))
#         top_activity, top_archived_activity = actions.get('get')()
#     elif request.method == 'GET':
#         if 'search' in request.GET and request.GET.get('search'):
#             top_activity, top_archived_activity = actions.get('search')(request.GET.get('search'))
#         else:
#             top_activity, top_archived_activity = actions.get('get')()
#         context.update(activity_form=ActivityForm())
#
#     context.update(top_activity=top_activity, top_archived_activity=top_archived_activity, user=user)
#     return render(request, 'activities/activities.html', context)