from django.core.mail import send_mail

from main.celery import app


@app.task
def order_mail(email, body):
    full_link = f'Привет, спасибо тебе за заказ\nМы с тобой свяжемся \n{body}'
    send_mail(
        'Hotel_Booking',
        full_link,
        'damirbekovemir@gmail.com',
        [email]
    )