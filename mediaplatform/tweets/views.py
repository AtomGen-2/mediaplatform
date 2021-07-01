from django.shortcuts import render;
from django.http import HttpResponse, Http404, JsonResponse;
from .models import Tweet;
import random;
from .forms import TweetForm;

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context = {}, status= 200)

def tweet_create_view(request, *args, **kwargs):
    # TweetForm class can be initialised with data or not
    # if there is data being sent by the POST method, then it is sent to that form, ptherwise blank form
    # if the form is valid, then it will save the form, if form is invalid, then the page is rendered   
    tweet_form=TweetForm( request.POST or None )
    context = { 'tweet_form' : tweet_form }
    if tweet_form.is_valid():
        obj = tweet_form.save(commit = False)
        obj.save()
        tweet_form = TweetForm()
        return render(request, 'pages/home.html', context, status = 200)
    return render(request, 'components/forms.html', context, status= 200)  

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content": x.content, "likes": random.randint(0,500)} for x in qs]
    data = { 
        "isUser" : False, 
        "response" : tweets_list, 
    }
    return JsonResponse(data)

def tweet_detail_view(result, tweet_id, *args, **kwargs):
    data = {
        "id" : tweet_id,
    }
    status = 200
    try: 
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except: 
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
