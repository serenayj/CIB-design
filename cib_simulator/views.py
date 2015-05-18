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
    if request.method == 'POST':                                                                                                            
        request.session.set_test_cookie()                                                                                                   
        login_form = AuthenticationForm(request, request.POST)                                                                              
        if login_form.is_valid():                                                                                                           
            if request.is_ajax:                                                                                                             
                user = django_login(request, login_form.get_user())                                                                         
                if user is not None:                                                                                                        
                    return HttpResponse(request.REQUEST.get('next', '/'))   
        return HttpResponseForbidden() # catch invalid ajax and all non ajax  
        # if not valid users, return registration form                                                      
    else:                                                                                                                                   
        return login_form;
        #login_form = AuthenticationForm()                                                                                                                                        
    #c = Context({                                                                                                                           
        """'next': request.REQUEST.get('next'),                                                                                                
        'login_form': login_form,                                                                                                                         
        'request':request,                                                                                                                  
    })                                                                                                                                      
    return render_to_response('login.html', c, context_instance=RequestContext(request))"""

def registraion(request):
    if request.method == "POST":
        content = login_form = AuthenticationForm(request, request.POST)
        newRecord = ({
            Userid= request.POST.get("Userid")
            username= request.POST.get("username")
            Password = request.POST.get("Password")
            E-mail = request.POST.get("Email")
        })
        class User(models.Model):
            newRecord.save()
            return render_to_response('index.html', context_instance=RequestContext(request))


def shareboards(request):


def chathistory(request):


def queries(request):


   
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