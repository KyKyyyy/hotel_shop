# from django.core.mail import send_mail
#
#
# def send_confirmation_email(code, email):
#     full_link = f'http://localhost:8000/api/v1/account/activate/{code}'
#     send_mail(
#         'From shop project',
#         full_link,
#         'damirbekovemir@gmail.com',
#         [email]
#     )
#
#
# def forgot_password_email(code, email):
#     send_mail(
#         'Восстановление пароля',
#         f'Ваш код подтверждения: {code}',
#         'damirbekovemir@gmail.com',
#         [email]
#     )