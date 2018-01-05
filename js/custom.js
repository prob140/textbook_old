require(['gitbook'], function(gitbook) {
    console.log('Initializing interact...');
  
    gitbook.events.bind('page.change', function() {
      console.log('Running interact:');
      MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    })
  })