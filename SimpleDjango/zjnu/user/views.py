from django.shortcuts import render
from user import models as umodels, forms as uforms 
from runTg import forms as rforms, models as rmodels

# login page
def login(request):
    # before login
    form = uforms.UserForm()
    if request.method == 'GET':
        return render(request, 'login.html', {"form":form})
    # after login
    elif request.method == 'POST':
        user_id = request.POST['id']
        user_passwd = request.POST['passwd']
        # id is exist
        if len(umodels.User.objects.filter(id=user_id)) is 0:
            return render(request, 'login.html', {"form":form})
        # passwd is valid
        if umodels.User.objects.filter(id=user_id)[0].passwd != user_passwd:
            return render(request, 'login.html', {"form":form})
        # store the login user info
        request.session['id'] = user_id

        return render(request, './index.html')
    else:
        pass

# logout
def logout(request):
    request.session['id'] = ''
    return render(request, './login.html')

# user center page
def userpage(request):
    if 'id' not in request.session or request.session['id'] == '':
        return render(request, './login.html')
    user_id = request.session['id']
    cancelRecord_id = request.GET.get("cancelRecord_id", False)
    cancelJoinRecord_id = request.GET.get("cancelJoinRecord_id", False)
    if cancelRecord_id != False and not cancelJoinRecord_id:
        # delete the runrecord and the runjoinrecord related with the runrecord
        return cancelrecord(request,user_id,cancelRecord_id)
    elif not cancelRecord_id and cancelJoinRecord_id != False:
        # delete the runjoinrecord and update the isfull if isfull == True
        return canceljoinrecord(request,user_id,cancelJoinRecord_id)
    else:
        # show the page
        return showuserpage(request,user_id)
    
def showuserpage(request, user_id):
    runRecords = rmodels.RunRecord.objects.filter(user_id = user_id)
    runRecordsId = [r.runRecord_id_id for r in rmodels.RunJoinRecord.objects.filter(user_id = user_id)]
    runJoinRecords = [rmodels.RunRecord.objects.filter(id=i)[0] for i in runRecordsId]
    for r in runRecords:
        # add a attribute join_sum
        r.join_sum = len(rmodels.RunJoinRecord.objects.filter(runRecord_id=r.id))
    for r in runJoinRecords:
        # add a attribute join_sum
        r.join_sum = len(rmodels.RunJoinRecord.objects.filter(runRecord_id=r.id))
    return render(request, 'userpage.html', {"runRecords":runRecords,"runJoinRecords":runJoinRecords})
        
# cancel run record (both run record and its attaching run join record)
def cancelrecord(request, user_id, cancelRecord_id):
    rmodels.RunRecord.objects.filter(id=cancelRecord_id).delete()
    rmodels.RunJoinRecord.objects.filter(runRecord_id=cancelRecord_id).delete()
    return showuserpage(request,user_id)
    
# cancel run join record (if the full record turns to infull after this action, then set isfull to False)
def canceljoinrecord(request, user_id, cancelJoinRecord_id):
    rmodels.RunJoinRecord.objects.filter(runRecord_id=cancelJoinRecord_id).filter(user_id=user_id).delete()
    runRecord = rmodels.RunRecord.objects.filter(id=cancelJoinRecord_id)
    if runRecord[0].isfull == True:
        rmodels.RunRecord.objects.filter(id=cancelJoinRecord_id).update(isfull=False)
    return showuserpage(request,user_id)
