# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsd', '0005_auto_20160829_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besversioncore',
            name='bes_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='bes_year',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_anger',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_cholera',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_clinic_malaria_0_4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_clinic_malaria_5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_diarrhea_04',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_diarrhea_15',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_diarrhea_5_14',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_dysentery',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_malaria_0_4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_malaria_5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_measles_24',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_measles_9',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_measles_v9_23',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_meningitis_0_4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_meningitis_5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_nv_measles',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_pfa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_plague',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='cases_tetanus',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='creation_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='creator_uri_user',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='date_week_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='date_week_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_anger',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_cholera',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_clinic_malaria_0_4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_clinic_malaria_5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_diarrhea_04',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_diarrhea_15',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_diarrhea_5_14',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_dysentery',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_malaria_0_4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_malaria_5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_measles_24',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_measles_9',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_measles_nv',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_measles_v_9_23',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_meningitis_04',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_meningitis_5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_pfa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_plague',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='deaths_tetanus',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='device_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='device_id_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='end_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='is_complete',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='last_update_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='last_update_uri_user',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='marked_as_complete_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='meta_instance_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='metadata_note',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='model_version',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_anger',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_cholera',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_diarrhea',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_dysentery',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_intro',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_malaria',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_measles',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_meningitis',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_pfa',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_plague',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='note_tetanus',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='phone_number_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='sim_serial',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='sim_serial_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='skip_open_field',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='skippable_open_field',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='start_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='submission_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='today',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='today_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='ui_version',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='besversioncore',
            name='uri',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='datasetelement',
            name='data_set_id',
            field=models.CharField(default='b136715c-1c88-414e-845c-a8be1e44ec30', max_length=255),
        ),
        migrations.AlterField(
            model_name='datasetelement',
            name='uid',
            field=models.CharField(default='786f9e21-7f57-4b8f-82dd-6e3963c2ed27', max_length=225),
        ),
        migrations.AlterField(
            model_name='district',
            name='data_creation',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='user_creation',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='device_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='fea_us',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='level_us',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='mac_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='person_contact_opt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='phone_contact_opt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='sim_number',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='sim_number_opt',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='sorting_us',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='data_creation',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='user_creation',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='creation_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='creator_uri_user',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='device_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='device_id_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='end_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='is_complete',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='last_update_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='last_update_uri_user',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='marked_as_complete_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='meta_instance_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='metadata_note',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='model_version',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='note_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='note_intro',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='open_field',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='phone_number_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='sim_serial',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='sim_serial_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='start_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='submission_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='today',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='today_test_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='ui_version',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='senderfromversioncore',
            name='uri',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
