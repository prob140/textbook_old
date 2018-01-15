require(['gitbook'], function(gitbook) {
    console.log('Initializing MathJax...');
    (function () {
    var head = document.getElementsByTagName("head")[0], script;
    script = document.createElement("script");
    script.type = "text/x-mathjax-config";
    script[(window.opera ? "innerHTML" : "text")] =
      "MathJax.Hub.Config({\n" +
      "  tex2jax: { inlineMath: [['$','$'], ['\\\\(','\\\\)']] },CommonHTML: { linebreaks: { automatic: true } },\"HTML-CSS\": { linebreaks: { automatic: true } },SVG: { linebreaks: { automatic: true } }" +
      "});";
    head.appendChild(script);
    script = document.createElement("script");
    script.type = "text/javascript";
    script.src  = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML";
    head.appendChild(script);
  })();

    gitbook.events.bind('page.change', function() {
      console.log("Running MathJax");
      MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    })
  })