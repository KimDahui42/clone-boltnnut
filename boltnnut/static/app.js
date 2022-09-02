window.addEventListener('scroll', function() {
    var nav_var=document.getElementsByClassName('navigation-container')[0];
    var nav_link=this.document.getElementsByClassName('nav-link');
    var top = window.scrollY 
                || window.pageXOffset 
                || document.documentElement.scrollTop 
                || document.body.scrollTop;
                
    if(top < 50) {
        console.log(top);
        nav_var.style.backgroundColor='transparent';
        document.getElementsByClassName('navigation__brand--logo')[0].src="/static/images/bnlogo.svg";
        for(var i=0;i<nav_link.length;i++){
            nav_link[i].style.color='white';
        }
    } else {
        nav_var.style.backgroundColor='white';
        document.getElementsByClassName('navigation__brand--logo')[0].src="/static/images/MobileLogo.svg";
        for(var i=0;i<nav_link.length;i++){
            nav_link[i].style.color='black';
        }
    }
})



