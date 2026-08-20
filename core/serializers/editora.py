try:
    from rest_framework import serializers
except Exception:  # fall back for environments without DRF (linting/static analysis)

    class _StubModelSerializer:
        pass

    class _SerializersStub:
        ModelSerializer = _StubModelSerializer

    serializers = _SerializersStub()

from core.models import Editora


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
