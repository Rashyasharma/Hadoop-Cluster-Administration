#!/usr/bin/python
	

print "content-type:text/html\n"

print '''<html>

 
 
<link rel="stylesheet" href="../css/semantic.css">

<style>

.div1
{
background-color:red;
margin:0;
height:100%;
width:20%;

border-radius:15px;
}

.outdiv
{

height:100%;
width:100%;
}

.sidediv
{
margin-right:3px;
padding:10px;
}


.button
{



}

.myframe
{
padding:4px;
position:absolute;
top:40px;
left:270px;
height:90%;
width:85%;

}
</style>

 
<link rel="stylesheet" href="../css/semantic.css">

<script type="text/javascript" src="http://192.168.43.101/css/jquery.js"></script>
<script type="text/javascript">

$(document).ready(
function(){
$("#upload").click(function()
		{

var myf=document.getElementById("myf")
myf.src="http://192.168.43.101/upload.html"


});

$("#run").click(function()
		{

var myf=document.getElementById("myf")
myf.src="http://192.168.43.101/cgi-bin/job.py"


});

$("#delete").click(function()
		{

var myf=document.getElementById("myf")
myf.src="http://192.168.43.101/cgi-bin/delete.py"


});

$("#view").click(function()
		{

var myf=document.getElementById("myf")
myf.src="http://192.168.43.101/cgi-bin/view.py"


});
});
</script>
<body>

<div class="outdiv">

<div class="div1">
<button id="view" class="button ui primary" style="position:absolute;
top:100px;
left:30px;font-size: 25px;">View Files</button>
<button id="upload" class="button ui primary" style="position:absolute;
top:200px;
left:30px;font-size: 25px;">Upload File</button>
<button id="run" class="button ui primary" style="position:absolute;
top:300px;
left:30px;font-size: 25px;">Run a Job</button>
<button id="delete" class="button ui primary" style="position:absolute;
top:400px;
left:30px;font-size: 25px;">Delete a File</button>
</div>

<div class="sidediv">
<iframe id="myf" class="myframe ui "></iframe>
</div>


</div>
</body>

</html>


'''





