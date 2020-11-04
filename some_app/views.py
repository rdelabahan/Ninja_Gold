from django.shortcuts import render, redirect
from time import localtime, strftime

locations = {
    'farm': (10,20),
    'cave': (5,10),
    'house': (2, 5),
    'casino': (-50,50)
}

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0;
    if not 'log' in request.session:
        request.session['log'] = [];
    return render(request,'index.html')

import random
def process_money(request):
    gold_num = random.randint(locations[request.POST['location']][0],locations[request.POST['location']][1]);
    request.session['gold'] += gold_num;
    request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    if gold_num < 0:
            value = 'negative'
            message = f"Entered a casino and lost {(gold_num * -1)} golds... Ouch.. {request.session['time']}";
            request.session['log'].insert(0,(message,value));
    elif gold_num >= 0:
            value = 'positive';
            message = f"Earned {gold_num} golds from the {request.POST['location']}! {request.session['time']}";
            request.session['log'].insert(0,(message,value));
    return redirect('/')
    # if 'farm' in request.POST:
    #     print(request.session['log']);
    #     request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    #     sum1 = round(random.random() * 10 + 10);
    #     request.session['gold'] += sum1
    #     message = f"Earned {sum1} golds from the farm! {request.session['time']}";
    #     request.session['log'].insert(0,(message,'positive'));
    # if 'cave' in request.POST:
    #     request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    #     sum2 = round(random.random() * 5 + 5);
    #     request.session['gold'] += sum2;
    #     message = f"Earned {sum2} golds from the cave! {request.session['time']}";
    #     request.session['log'].insert(0,(message,'positive'))
    # if 'house' in request.POST:
    #     request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    #     sum3 = round(random.random() * 3 + 2);
    #     request.session['gold'] += sum3;
    #     message = f"Earned {sum3} golds from the house! {request.session['time']}";
    #     request.session['log'].insert(0,(message,'positive'));
    # if 'casino' in request.POST:
    #     request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    #     sum4 = round(random.random() * 100 - 50);
    #     request.session['gold'] += sum4;
    #     if sum4 < 0:
    #         request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    #         value = 'negative'
    #         message = f"Entered a casino and lost {(sum4 * -1)} golds... Ouch.. {request.session['time']}";
    #         request.session['log'].insert(0,(message,value));
    #     elif sum4 >= 0:
    #         request.session['time'] = strftime("%Y-%m-%d %I:%M %p", localtime());
    #         value = 'positive'
    #         message = f"Earned {sum4} golds from the casino! {request.session['time']}";
    #         request.session['log'].insert(0,(message,value));

def reset(request):
    request.session.clear();
    return redirect('/')
# Create your views here.
