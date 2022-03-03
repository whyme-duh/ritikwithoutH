

document.getElementById('defaultActive').click();

document.getElementById('defaultActiveProject').click();


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






anychart.onDocumentReady(function() {
	// set the data
	var data = {
		header: ["Name", "Skill percentage"],
		rows: [
			["HTML", 90],
			["CSS", 60],
			["PYTHON", 70],
			["JAVASCIPRT", 40],
			["DJANGO", 60],
			["FLUTTER", 65],
			["PHOTOSHOP", 65],
			["OTHERS", 35],
			
	]};

	// create the chart
	var chart = anychart.bar();
	// add the data
	chart.data(data);
	// set the chart title
	chart.title("Below are the  tools and programming langauge I am familiar with.");

	// draw
	chart.container("barchart_values");
	chart.draw();
});

