from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from chat import views
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
#from chatbot import Chat, reflections, multiFunctionCall
import webbrowser
from wikipedia import search
#from chatbot import Chat, reflections, multiFunctionCall
import wolframalpha
import wikipedia
import requests
import webbrowser
import wolframalpha
import wikipedia
from chat.wikipedi import main
from django.http import HttpResponseRedirect
import os
from django.http import HttpResponse, JsonResponse
#from chat1.wikipedi import main
#from chat1.wikipedi import search

from django.shortcuts import render
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# Create your views here.
def Home(request):
    return render(request, "home.html")

def chatti(request):

    return render(request,'chatting.html')

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def search_wiki(keyword=''):
       season1234 = ''

    # running the query
       searchResults = wikipedia.search(keyword)
    # If there is no result, print no result
       if not searchResults:
         print("No result from Wikipedia")
         return
    # Search for page... try block
       try:
         page = wikipedia.page(searchResults[0])
       except (wikipedia.DisambiguationError, err):
         page = wikipedia.page(err.options[0])

       wikiTitle = str(page.title.encode('utf-8'))
       wikiSummary = str(page.summary.encode('utf-8'))
   #    print(wikiTitle)
       season1234 += wikiSummary
       # print(wikiSummary)
       return season1234
       #return render(request,'home.html',{'seasonb':wikiSummary,'season1234: season1234'})

def removeBrackets(variable):
            return variable.split('(')[0]

def resolveListOrDict(variable):
            if isinstance(variable, list):
                return variable[0]['plaintext']
            else:
                return variable['plaintext']

# def primaryImage(title=''):
#       url = 'http://en.wikipedia.org/w/api.php'
#       data = {'action': 'query', 'prop': 'pageimages', 'format': 'json', 'piprop': 'original', 'titles': title}
#       try:
#         res = requests.get(url, params=data)
#         key = res.json(['query']['pages']).keys()[0]
#         imageUrl = res.json()['query']['pages'][key]['original']['source']
#         print(imageUrl)
#         breakpoint()
#       except (Exception):
#         print('Exception while finding image:= ' + str(Exception))


def wikipedias(request):
        appId = 'APER4E-58XJGHAVAK'
        client = wolframalpha.Client(appId)

        data = request.GET['fulltextarea']
        res = client.query(data)
        abcd =search_wiki(data)

        # Wolfram cannot resolve the question
        if res['@success'] == 'false':
            print('Question cannot be resolved')
        # Wolfram was able to resolve question
        else:
            result = '',
        #    srsearch: ''
            # pod[0] is the question
            pod0 = res['pod'][0]
            # pod[1] may contains the answer
            pod1 = res['pod'][1]
            # checking if pod1 has primary=true or title=result|definition
            if (('definition' in pod1['@title'].lower()) or ('result' in pod1['@title'].lower()) or (
                    pod1.get('@primary', 'false') == 'true')):
                # extracting result from pod1
                result = resolveListOrDict(pod1['subpod'])
          #      srsearch = resolveListOrDict(pod1['subpod'])
                print(result)
         #       print(srsearch)
         #       question = resolveListOrDict(pod0['subpod'])
        #        question = removeBrackets(question)
     #           primaryImage(question)
            else:
                # extracting wolfram question interpretation from pod0
                question = resolveListOrDict(pod0['subpod'])
                # removing unnecessary parenthesis
                question = removeBrackets(question)
                # searching for response from wikipedia
                search_wiki(question)

              #  print(search_wiki)
              #  return render(request, 'home.html', {'q': q})

       #         primaryImage(question)


           #return render(request,'chatting.html',{'data':data})
   #         else:
 #      q = input('Search anything: ')

 #      search(q)
        return render(request, 'home.html',{'abcd':abcd})

# def wikipedia_search(word):
#     """Search a word meaning on wikipedia."""
#     wikipedia.set_lang('ja')
#     results = wikipedia.search(word)
#
#     # get first result
#     if results:
#         page = wikipedia.page(results[0])
#         msg = page.title + "\n" + page.url
#     else:
#         msg = '`{}` ??????????????'.format(word)
#     return msg


# def whoIs(query,sessionID="general"):
#     try:
#         return wikipedia.summary(query)
#     except:
#         for newquery in wikipedia.search(query):
#             try:
#                 return wikipedia.summary(newquery)
#             except:
#                 pass
#     return "I don't know about "+query
#






