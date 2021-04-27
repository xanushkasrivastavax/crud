from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname', 'roll_no', 'issue_date', 'book_code')
        labels = {
            'fullname': 'Full Name',
            'roll_no': 'Roll No.',
            'issue_date': 'Book Code',
            'book_code': 'Book-Genre'

        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['book_code'].empty_label = "Select"
