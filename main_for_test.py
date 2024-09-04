from bs4 import BeautifulSoup

text = """<p>En Actiture somos productores y exportadores de una amplia variedad de hortalizas ecol&oacute;gicas, especializados en el cultivo eco de coliflor y br&oacute;coli, lo que nos permite mantener un amplio calendario de producci&oacute;n.</p> <p>Nos adaptamos a los tiempos y exigencias de los consumidores y tenemos una gran capacidad de respuesta y de reacci&oacute;n a los pedidos de los clientes gracias a unas inversiones continuas en innovaci&oacute;n y desarrollo y en las mejores t&eacute;cnicas de producci&oacute;n.</p> <p>Para garantizar el servicio y una excelente calidad de nuestros productos, desde 2006 adquirimos la mejor finca del Valle del Ebro, donde contamos con 400 Has. de tierra f&eacute;rtil dotada de agua para la producci&oacute;n &oacute;ptima.</p> <p>Si algo nos caracteriza es que todos nuestros productos son ecol&oacute;gicos y que trabajamos preservando la flora y fauna del entorno gracias al uso de t&eacute;cnicas agr&iacute;colas sostenibles y a un consumo responsable que nos permite ofrecer a nuestros clientes el sabor real de las hortalizas.</p>"""

soup = BeautifulSoup(text, 'html.parser')
text = soup.get_text()

print(text)