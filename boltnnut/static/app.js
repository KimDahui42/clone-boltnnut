window.addEventListener('scroll', function() {
    var nav_var=document.getElementsByClassName('navigation-container')[0];
    var top = window.scrollY 
                || window.pageXOffset 
                || document.documentElement.scrollTop 
                || document.body.scrollTop;
                
    if(top < 50) {
        console.log(top);
        nav_var.style.backgroundColor='transparent';
    } else {
        nav_var.style.backgroundColor='white';
    }
})



