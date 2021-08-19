from re import sub
from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


#second param is url (string path in urls.py)
def display_entry(request, entry):
    entry_info = util.get_entry(entry)
    entry_md = None

    #convert info to markdown
    if entry_info:
        entry_md = markdown.markdown(entry_info)
    

    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "entry_md": entry_md
    })

#Why doesn't this func receive a second param?
def search_entry(request):
    if request.method == "POST":
        #request.POST includes submitted data & other info such as csrftoken
        post_data = request.POST
        query = post_data['q']
        entry_info = util.get_entry(query)

        #no entry found, get entries where query is a substring
        if not entry_info:
            entry_matches = check_substring(query)

            return render(request, "encyclopedia/search.html", {
                "entries": entry_matches
            })

            #display search results page of entry_matches


            #display error page, no entries found
            #TODO: Create error page, or return Page Not Found!

        #display existing entry page
        else:
            return render(request, "encyclopedia/search.html", {
                "entry": query,
                "entry_md": entry_md
            })
        


#Check if query is substring of an entry, return entry(s) if so
def check_substring(substring):
    entries = util.list_entries()
    entry_matches = []

    for entry in entries:
        print(f"entry: {entry} substring: {substring}")
        print(substring in entry)
        if substring.lower() in entry.lower():
            entry_matches.append(entry)

    return entry_matches


def create_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        print(title)
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "entry": title,
            "entry_md":  markdown.markdown(util.get_entry(title))
        })