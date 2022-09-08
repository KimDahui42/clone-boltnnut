window.onload = function () {
	var current_path=this.location.pathname
	navigationControl();
	if(current_path=="/common/signup/") signupRoute();
	else if(current_path="/boltnnut/uploadProject") uploadProjectStepControl();
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
  	var data = e.dataTransfer;
  	if (data.items) {
    for (var i = 0; i < data.items.length; i++) {
      if (data.items[i].kind == "file") {
        var file = data.items[i].getAsFile(); 
        alert(file.name);
      }
    }
  	} else {
    	for (var i = 0; i < data.files.length; i++) {
      	alert(data.files[i].name);
    	}
  	}
});
/* modify upload project form value(#uploadFile) 
var submit=document.getElementById('projectSubmit');
submit.addEventListener('click',uploadProjectFormControl());

function uploadProjectFormControl(){
	let project_form=document.uploadProject;
	project_form.
}*/

/*upload project step control*/
function uploadProjectStepControl(){
	var step=1;
	var previous=document.getElementById('previous');
	var next=document.getElementById('next');
	var submit=document.getElementById('projectSubmit');
	uploadContentShow(step);
	previous.addEventListener('click',function(){uploadContentShow(--step);});
	next.addEventListener('click',function(){uploadContentShow(++step);});
}
function uploadContentShow(step){
	var previous=document.getElementById('previous');
	var next=document.getElementById('next');
	var submit=document.getElementById('projectSubmit');
	var status=document.getElementsByClassName('upload__content')[0].getAttribute('status');
	var max=(document.getElementsByClassName('upload__content')[0].getAttribute('value')=='True')?4:5;
	console.log(status);
	if(status=='done'){
		step='done';
		previous.style.display='none';
		next.style.display='none';
		submit.style.display='none';
		document.getElementById('uploadStepDone').className='upload__step--selected';
		document.getElementsByClassName('upload__content--0'+step)[0].style.display='flex';
	}
	else{
		if(step==1) {
			previous.style.display='none';
		}
		else {
			previous.style.display='flex'
			console.log(previous.style.display);
		}
		if(step==(max-1)) {
			next.style.display='none';
			submit.style.display='flex';
		}
		else {
			next.style.display='flex';
			submit.style.display='none';
		}
	}
	for(var i=1;i<max;i++){
		if(i==step){
			document.getElementById('uploadStep'+i).className='upload__step--selected';
			document.getElementsByClassName('upload__content--0'+i)[0].style.display='flex';
		}
		else{
			document.getElementById('uploadStep'+i).className='upload__step--nominee';
			console.log(document.getElementsByClassName('upload__content--0'+i)[0]);
			document.getElementsByClassName('upload__content--0'+i)[0].style.display='none';
			
		}
	}
}
