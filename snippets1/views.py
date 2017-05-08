from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets1.models import Snippet,Snippet2,Snippet3,Snippet4,Snippet5,Snippet6,Snippet7,Snippet8,Snippet9,Snippet10
from snippets1.serializers import SnippetSerializer,SnippetSerializer2,SnippetSerializer3
from snippets1.Oauth.serverside_outh1 import Oauth
import json
from datetime import datetime,timedelta
from django.shortcuts import render
from snippets1.notification_backend.Mock_Queues import post_request
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
import re
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        d1 = datetime.now()
        # snippets = Snippet.objects.filter(date__gte=d1-timedelta(seconds=300))
        # snippets = Snippet.objects.all()
        snippets=None
        if re.search('snippets1',request.path)!=None:
            snippets = Snippet.objects.filter(date__gte=d1-timedelta(seconds=60))
        elif re.search('snippets2',request.path)!=None:
            snippets = Snippet2.objects.all()
        elif re.search('snippets3',request.path)!=None:
            snippets = Snippet3.objects.all()
        elif re.search('snippets4',request.path)!=None:
            snippets = Snippet4.objects.all()
        elif re.search('snippets5',request.path)!=None:
            snippets = Snippet5.objects.all()
        elif re.search('snippets6',request.path)!=None:
            snippets = Snippet6.objects.all()
        elif re.search('snippets7',request.path)!=None:
            snippets = Snippet7.objects.all()
        elif re.search('snippets8',request.path)!=None:
            snippets = Snippet8.objects.all()
        elif re.search('snippets9',request.path)!=None:
            snippets = Snippet9.objects.all()
        elif re.search('snippets10',request.path)!=None:
            snippets = Snippet10.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        resp = JSONResponse(serializer.data)
        resp['Access-Control-Allow-Origin'] = '*'
        return resp
    elif request.method == 'POST':
        print("request",request.body)
        print("request-type",type(request.body))
        data = json.loads(request.body.decode('ISO-8859-1'))
        #data = json.loads((request.body.encode('utf-8')).decode('utf-8'))
        # data1 = {'ids':data['id'],'airdate':data['AirDateTime'],'end_airdate':data['EndAirDateTime']}
        data1 = {'resource':data['resource'],'operation':data['operation'],'ref':data['ref'],'airdate':data['start'],'end_airdate':data['end'],'content':data['content'],'source':data['source']}
        # data = JSONParser().parse(request)
        #data = {"ids": 4331814238,"airdate" : '2017-02-09T06:30:00Z',"end_airdate" : '2017-02-09T07:00:00Z'}
        print("data:",data)
        serializer=''
        x = re.search("snippets([\d]+)",request.path)
        if re.search('snippets1',request.path)!=None:
            serializer = SnippetSerializer(data=data1)
            serializer.set_snippetmodel("Snippet")
            if serializer.is_valid():
                print("valid:",True)
                serializer.save()
                return JSONResponse(serializer.data, status=200)
        elif re.search('snippets2',request.path)!=None:
            #serializer = SnippetSerializer2(data=data1)
            return HttpResponse(status=200)
        elif x!=None:
            serializer = SnippetSerializer(data=data1)
            serializer.set_snippetmodel("Snippet"+x.group(1))
            if serializer.is_valid():
                print("valid:",True)
                serializer.save()
                return JSONResponse(serializer.data, status=200)
        # serializer = SnippetSerializer(data=data1)
        #if serializer.is_valid():
        #    print("valid:",True)
        #    serializer.save()
        #    return JSONResponse(serializer.data, status=200)
        #return JSONResponse(serializer.errors, status=400)
        return HttpResponse(status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    snippet=''
    # try:
    #    snippet = Snippet.objects.get(pk=pk)
    #except Snippet.DoesNotExist:
    #    return HttpResponse(status=404)
    try:
        if re.search('snippets1',request.path)!=None:
            snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    try:
        if re.search('snippets1',request.path)!=None:
            snippet = Snippet.objects.get(pk=pk)
    except Snippet2.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def snippet_200(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # print("Body:",request.path)
        return HttpResponse(status=int(request.path.split('/')[-1]))
    if request.method == 'POST':
        # print("Body:",request.body)
        return HttpResponse(status=int(request.path.split('/')[-1]))

@xframe_options_deny
@csrf_exempt
def notification_input(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        # return HttpResponse(status=200)
        if post_request()==True:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

@csrf_exempt
def snippet_oauth(request):
    if request.method == 'GET':
        if request.method == 'GET':
            d1 = datetime.now()
            print("Body:",request.path)
            snippets=None
            snippets = Snippet3.objects.filter(date__gte=d1-timedelta(seconds=60))
            serializer = SnippetSerializer3(snippets, many=True)
            return JSONResponse(serializer.data)
    if request.method == 'POST':
        print(request.META['HTTP_AUTHORIZATION'])
        o = Oauth(request.META.get('HTTP_AUTHORIZATION',''),request_type='POST',uri=request.build_absolute_uri().split('?')[0],parameters_string=request.build_absolute_uri().split('?')[1])
        if o.checktimestamp()and o.checkconsumerkey() and o.checknonce() and o.optimize_signature(o.make_digest(o.Hash_Message(),o.Hash_Key()))==True:
            data = json.loads(request.body.decode('ISO-8859-1'))
            data1 = {'resource':data['resource'],'operation':data['operation'],'ref':data['ref'],'airdate':data['start'],'end_airdate':data['end'],'content':data['content'],'source':data['source']}
            print("data:",data)
            serializer = SnippetSerializer3(data=data1)
            if serializer.is_valid():
               print("valid:",True)
               serializer.save()
               return JSONResponse(serializer.data, status=200)
            return JSONResponse(serializer.errors, status=400)
        else:
            return HttpResponse(status=401)

def admin(request):
    return render(request,r"client.html")
