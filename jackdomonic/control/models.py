# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin


class Channel(models.Model):
    descrizione = models.CharField(max_length=250, blank=True, null=True)
    attivo = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=10)
    exid = models.IntegerField(unique=True, blank=True, null=True)
    codrep = models.CharField(max_length=5, blank=True, null=True)
    abilita_fatture = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channel'


class Configuration(models.Model):
    location_gestita = models.BigAutoField(primary_key=True)
    url_servizio_prenotazione = models.CharField(max_length=100, blank=True, null=True)
    url_apikey = models.CharField(max_length=250, blank=True, null=True)
    endpoint = models.CharField(max_length=250, blank=True, null=True)
    valida = models.BooleanField()

    def __str__(self):
        return self.url_servizio_prenotazione

    class Meta:
        managed = False
        db_table = 'configuration'


class Email(models.Model):
    login = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    smtp = models.CharField(max_length=150)
    imap = models.CharField(max_length=150, blank=True, null=True)
    pop = models.CharField(max_length=150, blank=True, null=True)
    valido = models.BooleanField()
    smtpport = models.CharField(max_length=10, blank=True, null=True)
    sslenabled = models.BooleanField(blank=True, null=True)
    ttlenabled = models.BooleanField(blank=True, null=True)
    imapport = models.CharField(max_length=10, blank=True, null=True)
    popport = models.CharField(max_length=10, blank=True, null=True)
    channel = models.BigIntegerField()
    is_default = models.BooleanField(blank=True, null=True)
    email_id = models.SmallAutoField(primary_key=True, db_column='id')

    def __str__(self):
        return self.login

    class Meta:
        managed = False
        db_table = 'email'
        unique_together = (('login', 'password', 'smtp', 'channel'),)


class Energymesure(models.Model):
    id = models.SmallAutoField(primary_key=True)
    voltage = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    current_field = models.DecimalField(db_column='current_', max_digits=10, decimal_places=4, blank=True,
                                        null=True)  # Field renamed because it ended with '_'.
    active_power = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    apparent_power = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    reactive_power = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    power_factor = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    frequency = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_active_en = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    e_actve_en = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    t_actvie_en = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ssc = models.ForeignKey('Ssc', models.DO_NOTHING, db_column='ssc')
    plc = models.ForeignKey('Plc', models.DO_NOTHING, db_column='plc')
    d_ins = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'energymesure'


class ExUserToNotifyFault(models.Model):
    email = models.CharField(primary_key=True, max_length=150)
    active = models.BooleanField()
    channel = models.BigIntegerField(blank=True, null=True)
    all_channel = models.BooleanField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    plc = models.ForeignKey('Plc', models.DO_NOTHING, db_column='plc', blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ex_user_to_notify_fault'


class Groups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=20)
    group_desc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Plc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ip_address = models.CharField(max_length=15)
    porta_gestione_servizi = models.BigIntegerField()
    ssc = models.ForeignKey('Ssc', models.DO_NOTHING, db_column='ssc', blank=True, null=True)
    uid = models.CharField(unique=True, max_length=50)
    last_heartbit = models.DateTimeField()
    porta_modbus = models.SmallIntegerField(blank=True, null=True)
    path = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.uid + ':: ip - ' + self.ip_address

    class Meta:
        managed = False
        db_table = 'plc'


class Qrcoderequest(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    plc_uid = models.CharField(max_length=100)
    resource_tag = models.CharField(max_length=100)
    start_val = models.DateTimeField()
    end_val = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'qrcoderequest'


class Resource(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=20)
    reference = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    manage = models.BooleanField()
    ssc = models.ForeignKey('Ssc', models.DO_NOTHING, db_column='ssc', blank=True, null=True)
    bus_id = models.SmallIntegerField(blank=True, null=True)
    plc = models.ForeignKey(Plc, models.DO_NOTHING, db_column='plc', blank=True, null=True)
    start_time_limit = models.TimeField(blank=True, null=True)
    end_time_limit = models.TimeField(blank=True, null=True)
    policy = models.ForeignKey('ResourcePolicy', models.DO_NOTHING, db_column='policy', blank=True, null=True)

    def __str__(self):
        return self.tag + ':: Interna Reference - BUS ID:' + str(self.bus_id)

    class Meta:
        managed = False
        db_table = 'resource'


class ResourcePolicy(models.Model):
    id = models.SmallAutoField(primary_key=True)
    policy_description = models.CharField(max_length=150)
    weekend_available = models.BooleanField()
    daily_hour_limited = models.BooleanField()
    day_of_week = models.CharField(max_length=20, blank=True, null=True)
    hour_of_day = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return 'Policy::  - ' + self.policy_description

    class Meta:
        managed = False
        db_table = 'resource_policy'


class ResourcePolicyAdmin(admin.ModelAdmin):
    list_display = ("policy_description", "weekend_available", "hour_of_day")


class ResourceReservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    payload = models.CharField(max_length=50, blank=True, null=True)
    request_time = models.DateTimeField()
    resource = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resource')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    total_minutes = models.IntegerField(blank=True, null=True)
    received_interrupt = models.BooleanField(blank=True, null=True)
    receved_interrupt_at = models.DateTimeField(blank=True, null=True)
    interrupt_motivation = models.CharField(max_length=100, blank=True, null=True)
    lastupdate = models.DateTimeField(blank=True, null=True)
    schedule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_reservation'


class Networklocation(models.Model):
    reference = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
    last_update = models.DateTimeField()
    lastupdate_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='lastupdate_by', blank=True, null=True)
    ip_port_service = models.IntegerField(blank=True, null=True)
    stato = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    hotspot_tag = models.CharField(max_length=30, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'networklocation'
        unique_together = (('ip_address', 'hotspot_tag'),)


class NetworklocationAdmin(admin.ModelAdmin):
    list_display = ("title", "ip_address", "active", "hotspot_tag")


class Ssc(models.Model):
    id = models.SmallAutoField(primary_key=True)
    mapped_by = models.CharField(unique=True, max_length=20)
    location = models.CharField(max_length=50)
    email_config = models.ForeignKey(Email, models.DO_NOTHING, db_column='email_config')
    name = models.CharField(max_length=50)
    config = models.ForeignKey(Configuration, models.DO_NOTHING, db_column='config', blank=True, null=True)
    location_0 = models.ForeignKey(Networklocation, models.DO_NOTHING, db_column='location_id', blank=True,
                                   null=True)  # Field renamed because of name conflict.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'ssc'


class UserGroups(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group_id'),)


class UserLog(models.Model):
    users = models.ForeignKey('Users', models.DO_NOTHING, db_column='users')
    user_comment = models.CharField(max_length=250, blank=True, null=True)
    connectionn_start = models.DateTimeField()
    connection_end = models.DateTimeField(blank=True, null=True)
    connection_from = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=300)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_log'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=32)
    login = models.CharField(unique=True, max_length=150, blank=True, null=True)
    lastlog = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    access_type = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username+":: "+self.first_name+" "+self.last_name

    class Meta:
        managed = False
        db_table = 'users'
