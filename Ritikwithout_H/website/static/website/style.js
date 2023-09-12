function loadTheme(themeName){
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

   
function toggleTheme(){
    if(localStorage.getItem('theme') === 'theme-dark'){
        document.getElementById('changeTheme').style.display="block";
        document.getElementById('changeThemeSun').style.display="none";
        loadTheme('theme-light');
    }
    else{
        document.getElementById('changeTheme').style.display="none";
        document.getElementById('changeThemeSun').style.display="block";
        loadTheme('theme-dark');
    }
}


(function(){
    if(localStorage.getItem('theme') === 'theme-dark'){
        document.getElementById('changeThemeSun').style.display="block";
        document.getElementById('changeTheme').style.display="none";
        loadTheme('theme-dark');
    }
    else{
        loadTheme('theme-light');

    }
})();