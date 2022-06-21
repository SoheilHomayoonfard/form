from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField(min_length=5,max_length=60)  # 5 <= Fullname's length <= 60
    height = forms.IntegerField(min_value=70,max_value=250)     # 70 <= height <= 250
    age = forms.IntegerField(min_value=14,max_value=250)       # 14 <= age <= 99

    def clean_full_name(self):
        full_name = self.changed_data['full_name']
        if str.istitle(full_name):
            return full_name
        raise forms.ValidationError("name or family name should be capitalize")
