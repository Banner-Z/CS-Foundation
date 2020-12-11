from django import forms

class UserForm(forms.Form):
	id = forms.CharField(label="学号",
						error_messages={"required":"学号不能为空!"})
	passwd = forms.CharField(label="密码",
						error_messages={"required":"密码不能为空!"})
