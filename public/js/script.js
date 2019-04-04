function getColor(){
    var lang = document.getElementById("languageSelect").value;
    var color = document.getElementById("colorText").value;

    // alert("You asked to see the color "+color.value +" and you wrote that in "+lang.value);
    axios.get("/getColor?color="+color+"&lang="+lang)
        .then(function(response){
            var backghround_string = "background-color: "+response.data+";";
            document.getElementById("colored_div").setAttribute("style", backghround_string);
        })
        .catch(function(error){
            alert(error);
        });
}