import flask
app = flask.Flask("search")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_guests():
    guestsdb = open("guestsdb.txt")
    content = guestsdb.read()
    guestsdb.close()
    guests = content.split("\n")
    guests.pop(len(guests) -1)
    return guests

@app.route("/")
def home():
    return get_html("index")
    
@app.route("/result")
def result():
    html_page = get_html("result")
    expression = flask.request.args.get("q")
    result = get_guests()
    people = ""
    for list in result:
        if list.lower().find(expression.lower()) != -1:
            people += "<p>" + list + "</p>"
    if people == "":
        people = "<p>None</p>"
    return html_page.replace("$$RESULT$$", people)

@app.route("/guests")
def guests():
    html_page = get_html("guests")
    guests = get_guests()
    actual_values = ""
    for guest in guests:
        actual_values += "<p>" + guest + "</p>"
    return html_page.replace("$$GUESTS$$", actual_values)
