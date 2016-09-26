{% set mule_home = '<#mule_home#>' %}
{% set mule_name = '<#mule_name#>' %}
run_mule:
  cmd.run:
    - cwd: {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/bin
    - user: muleManager
    - group: muleManager
    - names :
      - ./mule restart
