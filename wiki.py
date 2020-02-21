import webbrowser

def open_wiki(directory):
    print(open(directory + "wiki_print.txt", "r", encoding = "utf8").read())
    webbrowser.open(open(directory + "wiki.txt", "r", encoding = "utf8").read())


