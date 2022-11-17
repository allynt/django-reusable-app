from appconf import AppConf
from django.conf import settings


class {{ camel_case_app_name }}Conf(AppConf):
    class Meta:
        prefix = "{{ app_name }}"

__all__ = ["settings", "{{ camel_case_app_name }}Conf"]
