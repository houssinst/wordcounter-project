from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render( request, "home.html")

def count (request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist :
        if word in worddict :
            # increase
            worddict[word] += 1
        else:
            # add to the worddict
            worddict [word]  = 1

    return render(request, 'count.html' , {'fulltext' : fulltext  , 'count':len(wordlist),'worddict' : worddict.items() })

def create_about():
    f = open('.\\templates\\about.html' , 'w')
    data = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>  Hello i'm elhoussine</title>
  </head>
  <body>
<h1>Pythin programming with django and html and the good programmer elhoussine </h1>
    <form action="{% url 'count' %}">
  <textarea cols='40' rows='10' name='fulltext'></textarea >
       </br>
<input type="submit" value="Count The Words !"  />

<h1> About as page from this link : </h1>
<form action="{% url 'about'%}">
<a href="about.html" > about as page </a>
    </form>
  </body>
</html>

    """
    f.write(data)
create_about()

def about(request):
    return render( request , ('about.html'))
