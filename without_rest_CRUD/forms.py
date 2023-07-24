from django import forms
from without_rest_CRUD.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_field(self):
        inputsal = self.cleaned_data['esal']
        print("from esal is ",inputsal)
        if inputsal<5000:
            raise forms.ValidationError('Minimum salary is grater then 5000') 
        return inputsal        
    class Meta:
        model=Employee
        fields = '__all__'
