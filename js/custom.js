$(".chapter a").click(function(){
	window.setTimeout(function(){
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    console.log("UPDATING");
}, 300);
});


$(".navigation").click(function(){
	window.setTimeout(function(){
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    console.log("UPDATING");
}, 300);
});
