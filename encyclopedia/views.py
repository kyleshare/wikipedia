from django.http.response import HttpResponse
from django.shortcuts import render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


#second param is url (string path in urls.py)
def display_entry(request, entry):
    entry_info = util.get_entry(entry)
    entry_html = None

    #convert markdown to html
    if entry_info:
        entry_html = markdown.markdown(entry_info)
    

    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "entry_info": entry_html
    })

#Why doesn't this func receive a second param?
def search_entry(request):
    print(request)
    print("Exiting search_entry")
    return HttpResponse("TEST")