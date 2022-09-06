window.onload = function () {
	var current_path=this.location.pathname
	navigationControl();
	if(current_path=="/common/signup/") signupRoute();
};

function navigationControl(){
	var nav_bar = document.getElementsByClassName("navigation-container")[0];
	var nav_link = this.document.getElementsByClassName("nav-link");
	var current_path=this.location.pathname
	console.log(current_path)
	if(current_path=='/boltnnut/'){
		window.addEventListener("scroll", function () {
			var nav_bar = document.getElementsByClassName("navigation-container")[0];
			var nav_link = this.document.getElementsByClassName("nav-link");
			var top =
				window.scrollY ||
				window.pageXOffset ||
				document.documentElement.scrollTop ||
				document.body.scrollTop; 
			if (top < 50) {
				nav_bar.style.backgroundColor = "transparent";
				document.getElementsByClassName("navigation__brand--logo")[0].src =
					"/static/images/bnlogo.svg";
				for (var i = 0; i < nav_link.length; i++) {
					nav_link[i].style.color = "white";
				}
			}
			else {
				nav_bar.style.backgroundColor = "white";
				nav_bar.style.boxShadow = "-1px 1px 5px -2px rgba(0,0,0,0.15)";
				document.getElementsByClassName("navigation__brand--logo")[0].src =
					"/static/images/MobileLogo.svg";
				for (var i = 0; i < nav_link.length; i++) {
					nav_link[i].style.color = "black";
				}
			}
		});
	}
	else{
		nav_bar.style.backgroundColor = "white";
		nav_bar.style.boxShadow = "-1px 1px 5px -2px rgba(0,0,0,0.15)";
		document.getElementsByClassName("navigation__brand--logo")[0].src =
			"/static/images/MobileLogo.svg";
		for (var i = 0; i < nav_link.length; i++) {
			nav_link[i].style.color = "black";
		}
	}
}


function signupRoute() {
	var signup_card = document.getElementsByClassName("signup__cards__card");
	for (var i = 0; i < 2; i++) {
		signup_card[i].addEventListener("click", function (event) {
			var params = new URLSearchParams(location.search);
			console.log(event.target.getAttribute("value"));
			params.set("type", event.target.getAttribute("value"));
			window.open(location.pathname + "?" + params.toString(), "_self");
		});
	}
}
