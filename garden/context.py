from about.models import AboutPage


def global_settings(request):
    return {
        'about_pages': AboutPage.objects.all(),
    }