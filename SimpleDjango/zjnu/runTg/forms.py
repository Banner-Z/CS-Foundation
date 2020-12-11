from django import forms

class RunRecordForm(forms.Form):
	name = forms.CharField(label="标签",
						error_messages={"required":"标签不能为空!"})
	content = forms.CharField(label="描述",
						help_text="最多250个字")
	time = forms.DateTimeField(label="跑步时间",
						error_messages={"required":"必须指定时间!"})
	num = forms.IntegerField(label="人数",
						min_value=1,
						error_messages={"min_value":"最少为1!", "required":"必须指定人数!"})
