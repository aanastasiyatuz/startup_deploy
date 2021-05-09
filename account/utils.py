from django.core.mail import send_mail


def send_activation_email(email, activation_code, is_password):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}'
    if not is_password:
        message = f"""
        To activate your account click here {activation_url}
        """
    else:
        message = f"""
        To reset your password click here {activation_url}
"""

    send_mail('StackOverflow Activation',message,'admin@admin.com', [email, ], fail_silently=False, )
