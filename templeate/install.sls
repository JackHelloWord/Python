{% set path = '<#path#>' %}
{% set tar_name = '<#tar_name#>' %}
{% set mule_home = '<#mule_home#>' %}
{% set mule_name = '<#mule_name#>' %}
mule_source:
  file.managed:
    - name: {{ path }}/{{ tar_name }}
    - source: salt://mule/files/{{ tar_name }}
    - user: muleManager
    - group: muleManager
    - mode: 644
extract_mule:
  cmd.run:
    - cwd: {{ path }}
    - names :
      - tar zxvf {{ tar_name }} -C {{ mule_home }}
    - require:
      - file: mule_source
rename__mule:
  cmd.run:
    - cwd: {{ mule_home }}
    - names :
      - mv mule {{ mule_name }}
