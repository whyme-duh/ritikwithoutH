
// these are the code for the scroll animation

// for the div with multiple childs

const childObserver = new IntersectionObserver((entries) =>{
	entries.forEach((entry)=> {
		if(entry.isIntersecting){
			entry.target.classList.add('showChild');
		}
	})

})
const hiddenChild = document.querySelectorAll('.child');
hiddenChild.forEach((el) => childObserver.observe(el));

// this code is for opacity
const observer = new IntersectionObserver((entries) => {
	entries.forEach((entry) => {
		if(entry.isIntersecting){
			entry.target.classList.add('show');

		}
		// else{
		// 	entry.target.classList.remove('show');

		// }
	});
})

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));






//  this is for splash screen

let intro = document.querySelector('.intro');

let logo = document.querySelector('.intro-header');
let logoSpan = document.querySelectorAll('.logo');

window.addEventListener("DOMContentLoaded", ()=>{
	setTimeout(()=>{
		logoSpan.forEach((logo ,index)=>{
			setTimeout(()=>{
				logo.classList.add('active');
			}, (index + 1) * 300)
		});

		setTimeout(() =>{
			logoSpan.forEach((logo, index) =>{
				setTimeout(()=>{
					logo.classList.remove('active');
					logo.classList.add('fade');
				}, (index+1) * 50);
			})
		}, 2000)

		setTimeout(()=>{
			intro.style.top = '-100vh';
		},2300)
	})
});
// document.getElementById('defaultActive').click();

// document.getElementById('defaultActiveProject').click();

// document.getElementById('contactWithMe').addEventListener("click", function(){
// 	var popUp = document.getElementsByClassName('contact-me-form');
// 	popUp.style.display = "flex";
// 	alert("hello");
// });


// document.getElementById('contact').addEventListener("click", contactFunction());
// if ( window.history.replaceState ) {
//   window.history.replaceState( null, null, window.location.href );
// }
// function contactFunction(){
	
// 	document.getElementsByClassName('contact-container')[0].style.display = "flex";
// 	focument.getElementById('main-body')[0].q

// }

// function cancelButton(){
// 	document.getElementsByClassName('contact-container')[0].style.display = "none";
// }

const all = document.getElementById('All');
all.style.display = "flex";

function openTab(evt, tabName){
	var i, tabContent, tabLinks;
	tabContent = document.getElementsByClassName('content');
	for(i = 0 ;i< tabContent.length; i++){
		tabContent[i].style.display="none";
	}
	tabLinks = document.getElementsByClassName('nav-link-tab');
	for(i=0;i<tabLinks.length ;i++){
		tabLinks[i].className = tabLinks[i].className.replace(" active", "");
	}
	document.getElementById(tabName).style.display = "flex";
	evt.currentTarget.className += ' active';
}

function openTabProject(evt, tabName){
	var i, tabContent, tabLinks;
	tabContent = document.getElementsByClassName('content-project');
	console.log(tabContent[0]);
	for(i = 0 ;i< tabContent.length; i++){
		tabContent[i].style.display="none";
	}
	tabLinks = document.getElementsByClassName('nav-link-tab-project');
	for(i=0;i<tabLinks.length ;i++){
		tabLinks[i].className = tabLinks[i].className.replace(" active", "");
	}
	document.getElementById(tabName).style.display = "flex";
	evt.currentTarget.className += ' active';
}





