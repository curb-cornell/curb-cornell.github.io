def format_date(ctx, d):
    #date = ctx_fetch(ctx, d)
    mo = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][d.tm_mon - 1]
    return str(d.tm_mday) + " " + mo + " " + str(d.tm_year)
macro("formatDate", format_date)

def newest(ctx, count, folder):
    unlimited = type(count) == str and count.lower() == "unlimited"
    s = sorted([x for x in folder.values() if "isFile" in x],
               key=lambda x: x["date"],
               reverse=True)
    return s if unlimited else s[:count]
macro("newest", newest)

def make_menu(ctx, start=True, site_url=None):
    #out = "<ul>"
    sections = {}
    if start:
        site_url = ctx["site"]["url"]
        ctx = ctx["static"]
        out = '<ul class="nav navbar-nav">'#+= "<li><a href='" + site_url + "/'>Home</a></li>"
        out += '<li><a href="' + site_url + '/">Home</a></li>'
    else:
        out = '<ul class="dropdown-menu">'
    for item in sorted(ctx):
        if "isFile" in ctx[item]:
            s = ""
            if "title" in ctx[item] and "unlisted" not in ctx[item]:
                s += "<li><a href='" + site_url + "/" + \
                       ctx[item]["path"] + "'>"
                s += ctx[item]["title"] + "</a></li>"
            if "section" in ctx[item]:
                section = int(ctx[item]["section"])
                if section in sections:
                    sections[section] += s
                else:
                    sections[section] = s
            else:
                out += s
        else:
            #print(ctx, item)
            out += '<li><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">' + item.capitalize() + \
                   ' <span class="caret"></span></a>' + \
                   make_menu(ctx[item], False, site_url)
            out += "</li>"
    
    for section, contents in sorted(sections.items()):
        out += '<li class="divider"></li>'
        out += contents
        
    if start:
        out += '<li class="join-menu-item"><a href="' + site_url + \
               '/pages/about/join.html">Join</a></li>'
    out += "</ul>"
    return out
macro("nav", make_menu)
