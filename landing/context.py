from django.urls import reverse_lazy


def navbar_items(request):
    # if user := request.user.is_authenticated:
    #     print(request.COOKIES)
    #
    #     history = request.session.get('history', [])
    #     request.session['history'] = [*history, request.path]

    return {
        # 'user_history': [] if not user else request.session['history'],
        'navbar_items': [
            {'title': 'Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
            {'title': 'Posts', 'url': reverse_lazy('landing:posts'), 'classes': ""},
        ]
    }
