from django import forms
from django.core.exceptions import ValidationError


class Reform(forms.Form):
    username=forms.CharField(label='用户名：',
                             max_length=15,
                             min_length=5,
                             widget=forms.widgets.TextInput(attrs={'class':'form-control'}),
                             error_messages={'required':'此项不能为空',
                                             'max_length':'最多15位',
                                             'min_length':'最少5位'}

                             )
    password = forms.CharField(label='密码：',
                               max_length=15,
                               min_length=5,
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={'required': '此项不能为空',
                                               'max_length': '最多15位',
                                               'min_length': '最少5位'}
                               )
    password2 = forms.CharField(label='确认密码：',
                               max_length=15,
                               min_length=5,
                                widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
                                error_messages={'required': '此项不能为空',
                                                'max_length': '最多15位',
                                                'min_length': '最少5位'}
                               )
    email=forms.EmailField(label='邮箱：',
                               max_length=30,
                               min_length=5,
                                widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}),
                                error_messages = {'invalid':'邮箱格式不正确',
                                                  'required':'此项不能为空'}
                               )
    def clean_password2(self):
        password=self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError('密码不一致')
        else:
            return password2