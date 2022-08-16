from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from applications.account.tasks import celery_send_confirmation_email, celery_send_confirmation_password

# from applications.account.send_mail import send_confirmation_email, forgot_password_email
from applications.hotels.models import Favorite

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm']

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Passwords did nit match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        # send_confirmation_email(code, user.email)
        celery_send_confirmation_email.delay(code, user.email)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован!')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if not user:
                raise serializers.ValidationError('Неверный email или пароль')

            attrs['user'] = user
            return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        celery_send_confirmation_password(user.activation_code, email)


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(min_length=8, required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return code

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def set_new_pass(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()



