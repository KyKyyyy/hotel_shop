from django.core.mail import send_mail

from main.celery import app


@app.task
def celery_send_confirmation_email(code, email):
    # time.sleep(10)
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'From shop project',
        full_link,
        'damirbekovemir@gmail.com',
        [email]
    )


def celery_send_confirmation_password(code, email):
    # time.sleep(10)
    send_mail(
        'From shop project',
        f'Ваш код подтверждения:{code}',
        'damirbekovemir@gmail.com',
        [email]
    )
