from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_an_email_to_confirm_email(user, token: str) -> None:
    confirmation_link = _get_confirmation_link(token)
    html_message = render_to_string('authentication/email_manager/email_confirm.html', {'confirmation_link': confirmation_link})

    subject = 'Подтвердите ваш email'
    from_email = 'kornevstepan169@gmail.com'
    recipient_list = [user.email]

    email = EmailMessage(subject, html_message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.send()


def _get_confirmation_link(token: str) -> str:
    confirmation_link = f'{settings.BASE_URL}email/verify/?token={token}'
    return confirmation_link
