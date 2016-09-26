{% set mule_home = '<#mule_home#>' %}
{% set mule_name = '<#mule_name#>' %}
chown_mule:
  cmd.run:
    - cwd: {{ mule_home }}
    - names :
      - chown -R muleManager:muleManager {{ mule_name }}
chmod_mule:
  cmd.run:
    - cwd: /
    - names :
      - chmod +x {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/bin/mule
      - chmod +x {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/bin/launcher
      - chmod -R +x {{ mule_home }}/{{ mule_name }}/mule-standalone-3.7.0/lib/boot/exec
