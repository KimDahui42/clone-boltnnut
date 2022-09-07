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

/*sign up route (client/partner)*/
function signupRoute() {
	var signup_card = document.getElementsByClassName("signup__cards__card");
	for (var i = 0; i < 2; i++) {
		var temp_nodes=signup_card[i].childNodes;
		for(var j=0;j<temp_nodes.length;j++){
			temp[j].addEventListener("click", function (event) {
				var params = new URLSearchParams(location.search);
				console.log(event.target.getAttribute("value"));
				params.set("type", event.target.getAttribute("value"));
				window.open(location.pathname + "?" + params.toString(), "_self");
			});
		}
	}
}
/* drag&drop file upload */
var upload_file=document.querySelector('#uploadFile');
var button_upload=upload_file.querySelector('.upload-file__button');
var box_upload=upload_file.querySelector('.upload-file__box');
var files=[]

box_upload.addEventListener('dragenter',function(e){
	console.log('drag enter');
});

box_upload.addEventListener('dragover',function(e){
	e.preventDefault();
	console.log('dragover');
	this.style.backgroundColor='coral';
});

box_upload.addEventListener('dragleave',function(e){
	console.log('drag leave');
	this.style.backgroundColor='white';
});
box_upload.addEventListener('drop',function(e){
	e.preventDefault();
	var files=e.dataTransfer && e.dataTransfer.files
	console.log(files);
	if(files!=null){
		if(files.length<1){
			alert("폴더 업로드 불가");
			return;
		}
		selecFile(files);
	} else{
		alert("ERROR");
	}
	this.style.backgroundColor='aliceblue';
});

/* modify upload project form value(#uploadFile) */
var submit=document.querySelector('#next');

submit.addEventListener('click',function(e){
	
});

/*upload project step control*/
function uploadProjectStepControl(){
	var step=1;
	var step_controls=document.querySelector('.upload__content__step-controls');
	var previous=step_controls.querySelector('#previous');
	var next=step_controls.querySelector('#next');
	var submit=step_controls.querySelector('#projectSubmit');

	if(step==1) previous.style.display='none';
	else previous.style='';
	if(step==4) {
		next.style.display='none';
		submit.style.display='';
	}
	else {
		next.style='';
		submit.style.display='none';
	}

	
}

