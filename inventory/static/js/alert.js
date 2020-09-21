alertArea = document.getElementById("alert");
var x = document.getElementsByTagName("td").rows[0].length;

if(x)
{
    alertArea.style.display = "block";
    console.log(x);
}

