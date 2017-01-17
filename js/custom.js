$(".chapter a").click(function(){
	window.setTimeout(function(){
    MathJax.Hub.Rerender();
    console.log("UPDATING");
}, 300);
});


$(".navigation").click(function(){
	window.setTimeout(function(){
    MathJax.Hub.Rerender();
    console.log("UPDATING");
}, 300);
});
