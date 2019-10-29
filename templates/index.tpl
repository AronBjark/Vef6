{% extends "base.html" %}

{% block innihald %}
	<heaer>
		<h1 class = "mama">Bensin Stöðvar</h1>
	</heaer>
{% for x in stations %}

	<div>
		<a href="/company/{{ x }}"><img src="{{ url_for('static', filename='img/'+x+'.jpg') }}" height="130px" title="{{ x }}" alt="{{ x }}"></a>
	</div>
{% endfor %}
{% endblock %}
