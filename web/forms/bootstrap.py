#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
class BootStrap(object):
    bootstrap_class_exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)# 执行父类的__init__方法
        # 循环ModelForm中的所有字段，给每个字段的插件设置

        for name, field in self.fields.items():
            # 不具有样式的表单
            if name in self.bootstrap_class_exclude:
                continue
            old_class = field.widget.attrs.get('class', "")
            field.widget.attrs['class'] = '{} form-control'.format(old_class)
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass

class BootStrapForm(BootStrap, forms.Form):
    pass
