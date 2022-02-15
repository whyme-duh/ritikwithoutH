

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
		header: ["Name", "Death toll"],
		rows: [
			["San-Francisco (1906)", 1500],
			["Messina (1908)", 87000],
			["Ashgabat (1948)", 175000],
			["Chile (1960)", 10000],
			["Tian Shan (1976)", 242000],
			["Armenia (1988)", 25000],
			["Iran (1990)", 50000]
	]};

	// create the chart
	var chart = anychart.bar();
	// add the data
	chart.data(data);
	// set the chart title
	chart.title("These are the skills of mine.");

	// draw
	chart.container("barchart_values");
	chart.draw();
});

