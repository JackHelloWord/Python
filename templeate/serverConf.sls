{% set mule_home = '<#mule_home#>' %}
{% set mule_name = '<#mule_name#>' %}
{% set db_user = '<#db_user#>' %}
{% set db_password = '<#db_password#>' %}
{% set db_tns = '<#db_tns#>' %}
{% set config_name = '<#config_name#>' %}
{% set config_resources = '<#config_resources#>' %}

{% set program_id = '<#program_id#>' %}
{% set repository_name = '<#repository_name#>' %}
{% set jcoSysnr = '<#jcoSysnr#>' %}
{% set gateway_host = '<#gateway_host#>' %}
{% set SAProuter = '<#SAProuter#>' %}
{% set jcoClient = '<#jcoClient#>' %}
{% set jcoUser = '<#jcoUser#>' %}
{% set jcoPasswd = '<#jcoPasswd#>' %}
{% set jcoLang = '<#jcoLang#>' %}
{% set respository_destination = '<#respository_destination#>' %}
idoc_conf1:
  file.managed:
    - name: {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/apps/idoc/server1.properties
    - source: salt://mule/files/{{ config_name }}
    - user: muleManager
    - group: muleManager
    - template: jinja
    - defaults:
      db_user: {{ db_user }}
      db_password: {{ db_password }}
      db_tns: {{ db_tns }}
      mule_home: {{ mule_home }}
      mule_name: {{ mule_name }}
      program_id: {{ program_id }}
      repository_name: {{ repository_name }}
      jcoSysnr: {{ jcoSysnr }}
      gateway_host: {{ gateway_host }}
      SAProuter: {{ SAProuter }}
      jcoClient: {{ jcoClient }}
      jcoUser: {{ jcoUser }}
      jcoPasswd: {{ jcoPasswd }}
      jcoLang: {{ jcoLang }}
      respository_destination: {{ respository_destination }}
cp_conf1:
  cmd.run:
    - cwd: {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/apps/idoc/
    - names :
      - cp server1.properties classes/server1.properties
idoc_conf2:
  file.managed:
    - name: {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/apps/idoc/mule-deploy.properties
    - source: salt://mule/files/mule-deploy.properties
    - user: muleManager
    - group: muleManager
    - template: jinja
    - defaults:
      config_resources: {{ config_resources }}
cp_conf2:
  cmd.run:
    - cwd: {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/apps/idoc/
    - names :
      - cp mule-deploy.properties classes/mule-deploy.properties
