function startAnimation(){
    document.getElementById("persona-1").className = "animated";
    document.getElementById("persona-2").className = "animated";
    document.getElementById("persona-3").className = "animated";
    document.getElementById("persona-4").className = "animated";
    
    setTimeout(function(){ 
        document.getElementById("persona-1").classList.remove("animated");
        document.getElementById("persona-2").classList.remove("animated");
        document.getElementById("persona-3").classList.remove("animated");
        document.getElementById("persona-4").classList.remove("animated");
    }, 5000);
    
}