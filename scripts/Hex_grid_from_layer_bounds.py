##Polygons=group
##input=vector
##cellsize=number 1000.0
##grid=output vector

input = processing.getObject(input)

centerx = (input.extent().xMinimum() + input.extent().xMaximum()) / 2
centery = (input.extent().yMinimum() + input.extent().yMaximum()) / 2
width = input.extent().xMaximum() - input.extent().xMinimum() + cellsize
height = input.extent().yMaximum() - input.extent().yMinimum() + cellsize

#http://docs.qgis.org/2.6/en/docs/user_manual/processing_algs/qgis/vector_creation_tools/creategrid.html
#processing.runalg('qgis:creategrid', type, width, height, hspacing, vspacing, centerx, centery, crs, output)
processing.runalg('qgis:creategrid', 3, width, height, cellsize, cellsize, 
                  centerx, centery, input.crs().authid(), grid)
