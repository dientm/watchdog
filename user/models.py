from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserType(models.Model):
    USER_TYPE = (('O', 'Owner'),
                 ('L', 'Login User'),
                 ('A', 'Alert User'),
                 )
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=USER_TYPE)

    # site = models.ManyToManyField()

    class Meta:
        verbose_name = _("Form user type")
        verbose_name_plural = _("Form user types")


class AccountSetting(models.Model):
    user = models.ForeignKey(User, to_field="username")
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    company = models.CharField(verbose_name=_("Company"), max_length=255)
    account_description = models.CharField(verbose_name=_("Account Description"), max_length=255)
    billing_email = models.EmailField(verbose_name=_("Billing Email"), max_length=255)
    phone = models.CharField(verbose_name=_("Phone"), max_length=20)
    cell_phone = models.CharField(verbose_name=_("Cell phone"), max_length=20)
    address_one = models.CharField(verbose_name=_("Address 1"), max_length=255)
    address_two = models.CharField(verbose_name=_("Address 2"), max_length=255)
    zipcode = models.CharField(verbose_name=_("Zip/ Location"), max_length=10)
    city = models.CharField(verbose_name=_("City/ Location"), max_length=255)
    state = models.CharField(verbose_name=_("State"), max_length=255)
    country = models.CharField(verbose_name=_("Country"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Form account setting")
        verbose_name_plural = _("Form account settings")


###
# used as temporary table
class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_ip = models.GenericIPAddressField(_("IP Address"), max_length=255)
    port = models.CharField(_("Port"), max_length=10, default="80")
    type = models.CharField(_("Type"), max_length=20)

    class Meta:
        managed = False
        db_table = 'Site'


class UserSetting(models.Model):
    id = models.AutoField(primary_key=True)
    site = models.ForeignKey(Site, to_field='site_id')
    warning_threshold_send_email = models.CharField(_("Warning Threshold Send Email"), max_length=5)
    warning_threshold_send_sms = models.CharField(_("Warning Threshold Send SMS"), max_length=5)
    warning_threshold_phone_call = models.CharField(_("Warning Threshold Phone Call"), max_length=5)
    re_notify_after = models.CharField(_("Re-notify After"), max_length=5)
    user = models.ForeignKey(User, to_field='id')

    class Meta:
        managed = False
        db_table = 'UserSetting'


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='id')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    birthday = models.DateField(null=True)
    is_enable = models.CharField(default='yes', max_length=10)
    email = models.EmailField(default='')
    sms = models.CharField(default='', max_length=20)
    phone = models.CharField(default='', max_length=20)
    email_enable = models.CharField(default='yes', max_length=10)
    call_order = models.IntegerField(default=1)
    sms_order = models.IntegerField(default=2)

    class Meta:
        managed = False
        db_table = 'Contact'


class ContactMethod(models.Model):
    user = models.ForeignKey(User, to_field="username")
    email = models.EmailField(_("Email"), max_length=255)
    sms = models.CharField(_("SMS/Text"), max_length=20)
    phone = models.CharField(_("Phone"), max_length=20)
    email_enable = models.BooleanField(default=1)
    sms_enable = models.BooleanField(default=1)
    phone_enable = models.BooleanField(default=1)

    # enable = models.IntegerField
    # site = models.ForeignKey(Site, to_field="site_id", default='')
    class Meta:
        verbose_name = _("Form contact method")
        verbose_name_plural = _("Form contact methods")

    def is_email_enable(self):
        return bool(self.email_enable)

    def is_sms_enable(self):
        return bool(self.sms_enable)

    def is_phone_enable(self):
        return bool(self.phone_enable)


class ContactPriority(models.Model):
    site = models.ForeignKey(Site)
    contact_method = models.ForeignKey(ContactMethod)
    priority = models.IntegerField

    def get_priority(self):
        return self.priority
