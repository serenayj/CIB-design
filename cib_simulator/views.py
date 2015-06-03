import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.db.models import Q
from django.contrib.auth import models
from forms import UserForm
from django.contrib import auth
from sampleapp.models import User

from django.views.decorators.csrf import ensure_csrf_cookie

#from django.db.models import User
"""from django.contrib.auth import AuthenticationForm"""

#this is a form which might turn to index
def index123(request):    
    return render(request, 'index.html')

#def registration(request):

#def reg(request):
    #return render(request,'reg.html')

#def registration and create record into database, works(save to database successfully) but no return anything
def create(request):
    form = UserForm(request.POST) 
    if form.is_valid():
        new_user = form.save()
        return render(request, 'index.html')
        #return HttpResponseRedirect('/index/' + str(new_user.pk))
    else:
        form = UserForm()
        return render(request, 'create_user.html', {'form': form})

#simple user login and save session 
def login(request):
    return render(request,'login.html')

def login_view(request):
    userid= request.POST.get('userid', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(userid=userid, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render_to_response('/index',RequestContext(request,{'userid': userid}))
    else:
        # Redirect to registration page.
        print "redirecting to registration"
        return HttpResponseRedirect("/create")

#def shareboards(request):


#def chathistory(request):


#def queries(request):

        #m = User.objects.get(userid=request.POST['userid'])
        """if m.password == request.POST['password']:
        request.session['userid'] = m.id
        return HttpResponseRedirect('/index/')
        else m.password=request.POST.get('password')
        request.session['userid'] = m.id
        return HttpResponseRedirect('/index/')
    except User.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")


        form = UserForm()
        book_formset = BookFormset(instance=Author())

        if request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                book_formset = BookFormset(request.POST, instance=author)
                if book_formset.is_valid():
                    book_formset.save()
                    return redirect('/index/')

                    return render_to_response('newuser.html',{
                        'form': form, 'formset': book_formset
                        },context_instance=RequestContext(request))  
q = request.GET.get( 'userid' )
if q is not None:            
    results = User.objects.filter( 
        NewRecord = request.get("userid","username","password","email")
        NewRecord.save()
        return render_to_response( 'results.html', { 'results': results, }, 
         context_instance = RequestContext( request ) )

def login(request):
    return render(request,'login.html')
    if request.user.is_authenticated():
        request.session['userid'] = request.user.id
        return HttpResponseRedirect('/index/')

        if request.method == 'POST':                                                                                                            
            request.session.set_test_cookie()                                                                                                   
            login_form = AuthenticationForm(request, request.POST)                                                                              
            if login_form.is_valid():                                                                                                           
                if request.is_ajax:                                                                                                             
                    user = django_login(request, login_form.get_user())
                    u.id = request.session.get["userid"]                                                                        
                    if user is not None:                                                                                                        
                        #return HttpResponse(request.REQUEST.get('next', '/'))
                        return render_to_response('index.html', u.id, context_instance=RequestContext(request))   
                        return HttpResponseForbidden() # catch invalid ajax and all non ajax  
                        # if not valid users, return registration form                                                      
                    else:                                                                                                                                   
                        return login_form;
                        #login_form = AuthenticationForm()                                                                                                                                        
                        #c = Context({                                                                                                                           
                          next': request.REQUEST.get('next'),                                                                                                
                          'login_form': login_form,                                                                                                                         
                          'request':request,                                                                                                                  
                          })                                                                                                                                      
return render_to_response('login.html', c, context_instance=RequestContext(request))

def registraion(request):
    if request.method == "POST":
        content = login_form = AuthenticationForm(request, request.POST)
        newRecord = request.get("userid","username","password","email")
        from models import User:
        newRecord.save()
        return render_to_response('index.html', context_instance=RequestContext(request)


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
                """