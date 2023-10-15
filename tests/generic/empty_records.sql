{% test empty_records(model,column_name) %}
    select {{ column_name }}
    from {{ model }}
    where trim({{ column_name }}) = ''
{% endtest %}