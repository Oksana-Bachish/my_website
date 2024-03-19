from main_page.views import menu


def get_page_context(request):
    return {'mainmenu': menu}

