{%- extends 'slides_reveal.tpl' -%}

{% block body %}

{{ super() }}

<script>
      // Full list of configuration options available here:
      // https://github.com/hakimel/reveal.js#configuration
Reveal.initialize({
      controls: true,
      progress: true,
      history: true,
      center: true,
      // kgd
      width: 1366,
      height: 768,

      theme: Reveal.getQueryHash().theme || 'default', // available themes are in /css/theme
      transition: Reveal.getQueryHash().transition || 'default', // default/cube/page/concave/zoom/linear/fade/none

      // Parallax scrolling
      // parallaxBackgroundImage: 'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg',
      // parallaxBackgroundSize: '2100px 900px',

      // Optional libraries used to extend on reveal.js
      dependencies: [
      { src: 'lib/js/classList.js', condition: function() { return !document.body.classList; } },
      { src: 'plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
      { src: 'plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
      { src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
      { src: 'plugin/zoom-js/zoom.js', async: true, condition: function() { return !!document.body.classList; } },
      { src: 'plugin/notes/notes.js', async: true, condition: function() { return !!document.body.classList; } }
      ]
});

// Add Github Link
var link = document.createElement("a");
link.href = "https://github.com/jakebrinkmann/2015-PUG-flask-data-vis";
link.alt = "Fork me on GitHub!";
var img = document.createElement("img");
img.src = "https://github-camo.global.ssl.fastly.net/365986a132ccd6a44c23a9169022c0b5c890c387/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f7265645f6161303030302e706e67";
img.style = "position: absolute; top: 0; right: 0; border: 0;";
link.appendChild(img);

document.body.appendChild(link);    


</script>

{% endblock body %}
