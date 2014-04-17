from django.core import serializers

jsonify = lambda obj: serializers.serialize('json', obj)