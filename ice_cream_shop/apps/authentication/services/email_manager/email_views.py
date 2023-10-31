from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.signing import BadSignature
from django.urls import reverse

from .token_utils import unsign_token
from ...models import UserProfile


@login_required
def verify_email(request):
    token = request.GET.get('token', '')
    try:
        username = unsign_token(token)
    except BadSignature:
        return HttpResponse('<h1>Все сломалось</h1>')

    user = UserProfile.objects.get(username=username)
    user.email_is_verified = True
    user.email_verification_token = None
    user.save()

    login(request, user)

    return redirect(reverse('catalog'))
