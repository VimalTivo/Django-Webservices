from rest_framework import serializers
from snippets1.models import Snippet,Snippet2,Snippet3,Snippet4,Snippet5,Snippet6,Snippet7,Snippet8,Snippet9,Snippet10,LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    # ids = serializers.CharField(required=False, allow_blank=True, max_length=200)
    resource = serializers.CharField(required=False, allow_blank=True, max_length=200)
    operation = serializers.CharField(required=False, allow_blank=True, max_length=200)
    ref = serializers.JSONField()
    airdate = serializers.CharField(required=False, allow_blank=True, max_length=200)
    end_airdate = serializers.CharField(required=False, allow_blank=True, max_length=200)
    content = serializers.JSONField()
    source = serializers.JSONField()
    snippet = 'Snippet'
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #return Snippet.objects.create(**validated_data)
        return eval(SnippetSerializer.snippet+".objects.create(**validated_data)")

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.ids = validated_data.get('ids', instance.ids)
        instance.resource = validated_data.get('resource', instance.resource)
        instance.operation = validated_data.get('operation', instance.operation)
        instance.ref = validated_data.get('ref', instance.ref)
        instance.airdate = validated_data.get('airdate', instance.airdate)
        instance.end_airdate = validated_data.get('end_airdate', instance.end_airdate)
        instance.content = validated_data.get('content', instance.content)
        instance.source = validated_data.get('source', instance.source)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    def set_snippetmodel(self,s):
        SnippetSerializer.snippet=s

class SnippetSerializer2(serializers.Serializer):
    resource = serializers.CharField(required=False, allow_blank=True, max_length=200)
    operation = serializers.CharField(required=False, allow_blank=True, max_length=200)
    ref = serializers.JSONField()
    airdate = serializers.CharField(required=False, allow_blank=True, max_length=200)
    end_airdate = serializers.CharField(required=False, allow_blank=True, max_length=200)
    content = serializers.JSONField()
    source = serializers.JSONField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet2.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.ids = validated_data.get('ids', instance.ids)
        instance.resource = validated_data.get('resource', instance.resource)
        instance.operation = validated_data.get('operation', instance.operation)
        instance.ref = validated_data.get('ref', instance.ref)
        instance.airdate = validated_data.get('airdate', instance.airdate)
        instance.end_airdate = validated_data.get('end_airdate', instance.end_airdate)
        instance.content = validated_data.get('content', instance.content)
        instance.source = validated_data.get('source', instance.source)
        instance.save()
        return instance

class SnippetSerializer3(serializers.Serializer):
    resource = serializers.CharField(required=False, allow_blank=True, max_length=200)
    operation = serializers.CharField(required=False, allow_blank=True, max_length=200)
    ref = serializers.JSONField()
    airdate = serializers.CharField(required=False, allow_blank=True, max_length=200)
    end_airdate = serializers.CharField(required=False, allow_blank=True, max_length=200)
    content = serializers.JSONField()
    source = serializers.JSONField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet3.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.ids = validated_data.get('ids', instance.ids)
        instance.resource = validated_data.get('resource', instance.resource)
        instance.operation = validated_data.get('operation', instance.operation)
        instance.ref = validated_data.get('ref', instance.ref)
        instance.airdate = validated_data.get('airdate', instance.airdate)
        instance.end_airdate = validated_data.get('end_airdate', instance.end_airdate)
        instance.content = validated_data.get('content', instance.content)
        instance.source = validated_data.get('source', instance.source)
        instance.save()
        return instance
