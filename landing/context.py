from django.urls import reverse_lazy


def navbar_items(request):
    # if user := request.user.is_authenticated:
    #     print(request.COOKIES)
    #
    #     history = request.session.get('history', [])
    #     request.session['history'] = [*history, request.path]

    return {
        # 'user_history': [] if not user else request.session['history'],
        'user_links': [
            {'title': '🔒 Logout', 'url': reverse_lazy('account:logout'), 'classes': ""},
        ] if request.user.is_authenticated else [
            {'title': '🔑 Register', 'url': reverse_lazy('account:register'), 'classes': ""},
            {'title': '🔓 Login', 'url': reverse_lazy('account:login'), 'classes': ""},
        ],
        'navbar_items': [
            {'title': '🏠 Home', 'url': reverse_lazy('landing:home'), 'classes': ""},
        ]
    }
