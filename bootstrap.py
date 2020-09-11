import ht
material
def material_head():
	return ht.meta(charset='utf-8')+ht.meta(name='viewport',content='width=device-width, initial-scale=1, shrink-to-fit=no')+ht.link(rel='stylesheet',href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons", crossorigin="anonymous")+ht.link(rel='stylesheet',href="https://unpkg.com/bootstrap-material-design@4.1.1/dist/css/bootstrap-material-design.min.css", crossorigin="anonymous")
def setup_head():
	return ht.meta(charset='utf-8')+ht.link(rel='stylesheet',href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css", crossorigin="anonymous")
def material_body():
	return ht.script('',src="https://code.jquery.com/jquery-3.5.1.slim.min.js", crossorigin="anonymous")+ht.script('',src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js", crossorigin="anonymous")+ht.script('',src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js", crossorigin="anonymous")+ht.script("$(document).ready(function() { $('body').bootstrapMaterialDesign(); });")
def setup_body():
	return ht.script('',src="https://code.jquery.com/jquery-3.5.1.slim.min.js", crossorigin="anonymous")+ht.script('',src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js", crossorigin="anonymous")+ht.script('',src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js", crossorigin="anonymous")
