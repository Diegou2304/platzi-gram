from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completition middeware
    Asegurarse que cada usuario que este interacturando
    con la plataforma, tenga su foto de perfil y biografia
    """

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        """Codigo que será ejecutado por cada request antes de que la view es llamada"""

        if not request.user.is_anonymous:

            profile = request.user.profile

            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect("update_profile")

        response = self.get_response(request)
        return response
