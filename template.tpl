{% extends 'basic.tpl'%}

{% block any_cell %}
{% if not cell.metadata.get('hidden',False) %}
              {{ super() }}

{% endif %}
{% endblock any_cell %}

{% block input_group %}
{% if not cell.metadata.get('codehidden',False) %}

              {{ super() }}

{% endif %}
{% endblock input_group %}
