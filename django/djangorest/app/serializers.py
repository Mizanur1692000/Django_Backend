from rest_framework import serializers
from .models import AiQuest

class AiQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiQuest
        fields = '__all__'




# class AiQuestSerializer(serializers.Serializer):
#     teacher_name = serializers.CharField(max_length=100)
#     course_name = serializers.CharField(max_length=100)
#     course_duration = serializers.IntegerField()
#     seat = serializers.IntegerField()


#     def create(self, validated_data):
#         return AiQuest.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
#         instance.course_name = validated_data.get('course_name', instance.course_name)
#         instance.course_duration = validated_data.get('course_duration', instance.course_duration)
#         instance.seat = validated_data.get('seat', instance.seat)
#         instance.save()
#         return instance