from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from .models import User


class SnippetSerializer_old(serializers.Serializer):
    id          = serializers.IntegerField(read_only=True)
    title       = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code        = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos     = serializers.BooleanField(required=False)
    language    = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style       = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        print(value)
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value


class SnippetSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def validate_title(self, value):
        """
        Check that the Snippet post is about 51reboot.
        """
        if '51reboot' not in value.lower():
            raise serializers.ValidationError("Snippet post is not about 51reboot")
        return value







class UserSerializer(serializers.Serializer):
    username                    = serializers.CharField(max_length=32)
    password                    = serializers.CharField(max_length=32)
    email                       = serializers.EmailField()
    created                     = serializers.DateTimeField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username       = validated_data.get('username', instance.username)
        instance.password       = validated_data.get('password', instance.password)
        instance.email          = validated_data.get('email', instance.email)
        instance.created        = validated_data.get('created', instance.created)
        instance.save()
        return instance

    def validate_password(self, value):
        pass

        return value




