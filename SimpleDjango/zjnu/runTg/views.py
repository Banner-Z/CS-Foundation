from django.shortcuts import render
from django.db import connection
from runTg import models as rmodels, forms as rforms
from user import models as umodels, views as uviews
import datetime

# show the runTg main page
def show(request):
    # login first
    if 'id' not in request.session or request.session['id'] == '':
        return render(request, './login.html')
    # get the empty form
    form = rforms.RunRecordForm()
    records = rmodels.RunRecord.objects.filter(isfull=False)

    # judge if the join num is greater than the total num
    cursor = connection.cursor()
    for r in records:
        # add a attribute join_sum
        r.join_sum = len(rmodels.RunJoinRecord.objects.filter(runRecord_id=r.id))
    return render(request, 'runTg.html', {"records":records, "form": form})

# add a run record
def insert(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        form = rforms.RunRecordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # get the login user id
            user_id = request.session['id']
            data["user_id_id"] = user_id
            rmodels.RunRecord.objects.create(**data)
        else:
            print('Invalid')
    return show(request)
    
# add a join record
def join(request):
    cursor = connection.cursor()
    # get login user id and the run record id
    user_id = request.session['id']
    run_id = request.GET.get("run_id",False)
    
    # forbid the re-join
    if len(rmodels.RunJoinRecord.objects.filter(user_id_id=user_id).filter(runRecord_id_id=run_id)) > 0:
        return show(request)
    
    # add a join record
    rmodels.RunJoinRecord.objects.create(runRecord_id_id=run_id, user_id_id=user_id)
    
    # get the join sum
    join_sum = len(rmodels.RunJoinRecord.objects.filter(runRecord_id=run_id))
    # get the run sum
    run_sum = rmodels.RunRecord.objects.filter(id=run_id)[0].num
    
    # set isfull to True id join sum == run_sum
    if run_sum <= join_sum:
        rmodels.RunRecord.objects.filter(id=run_id).update(isfull=True)
    return show(request)
