# -*- coding: utf-8 -*-
import pcl

# Cargar la nube de puntos
cloud = pcl.load('escena_downsampled_0.01.pcd')

# Crear un filtro PassThrough
passthrough = cloud.make_passthrough_filter()

# Assignar el eje y el rango para el filtro.
filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
min_val = -1.90
max_val = -1.50
passthrough.set_filter_limits(min_val, max_val)

# Usar el filtro para obtener la nube de puntos resultante
cloud_filtered = passthrough.filter()

# Grabar el resultado en disco
filename = "escena_pass_through_min%s_max_%s.pcd" % (min_val, max_val)
pcl.save(cloud_filtered, filename)