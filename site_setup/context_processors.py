from site_setup.models import SiteSetup

# podemos utilizar isso quando precisarmos de algo em todos od templates
def context_processor_example (request):

    return {
        'example': 'veio do context_processors (example)'
    }
    
    
def site_setup (request):
    setup = SiteSetup.objects.first()
    return {
        'site_setup': setup
    }