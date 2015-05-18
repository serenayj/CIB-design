import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.db.models import Q
from django.contrib.auth import models

#this is a form which might turn to index
def index123(request):    
    return render(request, 'index.html')

#def registration(request):


def loginajax(request):
    if request.method == "POST":
        form = AdvertForm(request.POST)

        message = 'something wrong!'
        if(form.is_valid()):
            print(request.POST['title'])
            message = request.POST['title']

        return HttpResponse(json.dumps({'message': message}))

    return render_to_response('contact/advert.html',
            {'form':AdvertForm()}, RequestContext(request))

   
'''
    if request.user.is_authenticated():
        request.session['currUserId'] = request.user.id
        message_ids   = request.REQUEST.getlist('messages')
        dialogs = []
        if (len(message_ids) != 0): 
            dialogs.append("message_table") # TODO: what is message table?
        return render(request, 'dashboard/index.html', Context({"dialogs": dialogs,'USERNAME': request.user.username}))
    # anonymous user
    else:
        request.session['currUserId'] = -1  #set -1 for anonymous user.
        request.session['currForumId'] = -1
        return render(request, 'dashboard/index.html', Context({'USERNAME': ''}))
    return redirect('/login')   # this may never be triggered.
'''