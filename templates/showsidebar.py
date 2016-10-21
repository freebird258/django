#!/usr/bin/env python
import datetime
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def activesidebar(context,name):
	li_class=""
	if(name==context['cur_page']):
		li_class="active"
	return li_class
