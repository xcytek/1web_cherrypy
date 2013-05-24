"""
PRIMER SITIO HECHO CON CHERRYPY
Alejandro Acosta Barrios
"""

import cherrypy

class Site :	

	def set_title(self, title) :
		self.title = title

	def get_title(self):
		return self.title

	def set_bodycontent(self, body) :
		self.body = body

	def get_bodycontent(self) :
		return self.body	

	def get_style(self):
			return '''
				<style>		
					*{
						margin: 0 auto;				
					}		
					body{
						background-color: white;
					}
					#main{
						width: 900px;						
						text-align: center;
						padding: 150px 0;			
					}	
					nav {
						text-align: center;
						padding: 15px 0;
						background-color: black;				
					}	
					li {								
						display : inline-block;
						padding : 0 20px;
					}
					li a, footer a{
						color: white;
						text-decoration: none;
						font-size: 22px;
					}			
					footer{
						color: white;
						padding: 25px 0;
						background-color: #999;
						text-align: center;
					}			
					footer a{
						font-size: 18px;
					}
				</style>
			'''	

	def get_html_doc(self):
		return '''		
			<!DOCTYPE html>
			<html>
			<head>
				<title>''' + self.get_title() + '''</title>
			</head>
			<nav>
				<ul>
					<li><a href="/">Inicio</a></li>
					<li><a href="servicios">Servicios</a></li>
					<li><a href="acercade">Acerca de</a></li>
					<li><a href="contacto">Contacto</a></li>
				</ul>
			</nav>
			<body>
				<section id="main">
				''' + self.get_bodycontent() + '''
				</section>
			</body>
			<footer>
				Desarrollado por <a href="http://twitter.com/xcytek" >@xcytek</a>
			</footer>
			</html>
			'''

	@cherrypy.expose
	def index(self) :
		self.set_title("Inicio")
		self.set_bodycontent("<p>Pagina de Inicio</p>")

		return self.get_style() + self.get_html_doc()
		
			
	@cherrypy.expose
	def servicios(self) :
		self.set_title("Servicios")
		self.set_bodycontent("<p>Servicios Alejandro Acosta @xcytek</p>")

		return self.get_style() + self.get_html_doc()
			
	@cherrypy.expose
	def acercade(self) :
		self.set_title("Acerca de mi")
		self.set_bodycontent("<p>Ingeniero en Computacion</p>")

		return self.get_style() + self.get_html_doc()
			
	@cherrypy.expose
	def contacto(self) :
		self.set_title("Contacto")
		self.set_bodycontent("<p>Llamame a mi numero</p>")

		return self.get_style() + self.get_html_doc()

import os.path
siteconf = os.path.join(os.path.dirname(__file__), 'site.conf')

if __name__ == '__main__':
	site = Site()
	print siteconf
	cherrypy.quickstart(site, config=siteconf)
else:    
    cherrypy.tree.mount(site, config=siteconf)
