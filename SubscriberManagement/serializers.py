from rest_framework import serializers
from datetime import datetime, date
import random
from dateutil.relativedelta import relativedelta
from .models import Subscriber
class SubscriberSerializer(serializers.ModelSerializer):
    date_of_birth=serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y'])
    time_of_birth=serializers.TimeField(format="%H:%M", input_formats=["%H:%M"])
    special_request=serializers.CharField(required=False, allow_null=True, allow_blank=True)
    description=serializers.CharField(required=False, allow_null=True, allow_blank=True)
    alpha_num_id=serializers.CharField(required=False, allow_null=True, allow_blank=True)
    sub_caste= serializers.CharField(required=False, allow_null=True, allow_blank=True)
    class Meta:
        model = Subscriber
        exclude = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        date_of_birth = datetime.strptime(data['date_of_birth'], '%d-%m-%Y')
        data['age']=  relativedelta(date.today(), date_of_birth).years     
        return data
        
    def create(self, validated_data):
        now = datetime.now()
        random.seed(now.microsecond)
        r_num = str(random.randint(1000000, 9999999))
        name = validated_data['name'][:1].upper()
        city = validated_data['city'][:1].upper()
        validated_data['alpha_num_id'] = 'M'+name+city+r_num if validated_data['gender'] == 'MALE' else 'F'+name+city+r_num
        validated_data['caste'] = validated_data['caste'].lower()
        validated_data['sub_caste'] = validated_data['sub_caste'].lower()
        return super().create(validated_data)