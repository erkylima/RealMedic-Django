
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from core.models import UserProfile
from core.modulos.cliente.cliente import Cliente


class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['nome', 'usuario']


class UsuarioCreateSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(required=True)

    class Meta:
        model = Cliente
        # fields = '__all__'
        fields = ['nome', 'usuario', 'senha']

    def create(self, validated_data):
        print('create')
        print(validated_data)

        senha = validated_data.pop('senha')
        print(validated_data)

        user = User.objects.filter(username=validated_data['usuario'])
        if user.exists():
            print('aaaaaaaaaa')
            raise ValidationError({"detail": "Usuário já existe"})

        user = User()
        user.username = validated_data['usuario']
        user.set_password(senha)
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        usuario = UserProfile()
        usuario.user = user
        usuario.usuario = validated_data['usuario']
        usuario.nome = validated_data['nome']
        usuario.save()
        usuario.senha = ''
        return usuario
