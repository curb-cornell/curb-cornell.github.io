def format_date(ctx, d):
    #date = ctx_fetch(ctx, d)
    mo = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][d.tm_mon - 1]
    return str(d.tm_mday) + " " + mo + " " + str(d.tm_year)
macro("format_date", format_date)

def newest(ctx, count, folder):
    unlimited = type(count) == str and count.lower() == "unlimited"
    s = sorted([x for x in folder.values() if "is_file" in x],
               key=lambda x: x["date"],
               reverse=True)
    return s if unlimited else s[:count]
macro("newest", newest)

def make_menu(ctx, start=True, site_url=None):
    #out = "<ul>"
    if start:
        site_url = ctx["site"]["url"]
        ctx = ctx["pages"]
        out = '<ul class="nav navbar-nav">'#+= "<li><a href='" + site_url + "/'>Home</a></li>"
        out += '<li><a href="' + site_url + '/">Home</a></li>'
    else:
        out = '<ul class="dropdown-menu">'
    for item in sorted(ctx):
        if "is_file" in ctx[item]:
            if "title" in ctx[item]:
                out += "<li><a href='" + site_url + "/" + \
                       ctx[item]["path"] + "'>"
                out += ctx[item]["title"] + "</a></li>"
        else:
            out += '<li><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button">' + item.capitalize() + \
                   ' <span class="caret"></span></a>' + \
                   make_menu(ctx[item], False, site_url)
            out += "</li>"
    if start:
        out += '<li class="join-menu-item"><a href="' + site_url + \
               '/pages/about/join.html">Join</a></li>'
    out += "</ul>"
    return out
macro("nav", make_menu)
