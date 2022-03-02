from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    
    # require the user for email to sing up
    email = forms.EmailField(required = True)
    
    class Meta:
        
        # prompting user to input a user, email, and confirm password
        model = User
        fields = ("username", "email", "password1", "password2")
        
         # saving the email to the corresponding user
        def save(self, commit=True):

            # require a non-empty input
            user = super(Register, self).save(commit=False)
            user.email = self.cleaned_data['email']
            
            # once submitted, save the user data
            if commit:
                user.save()
            return user
            
        