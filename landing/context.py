from django.urls import reverse_lazy


def navbar_items(request):
    return {
        'navbar_items': [
            {'title': 'Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
            {'title': 'Posts', 'url': reverse_lazy('landing:posts'), 'classes': ""},
        ]
    }
