# -*- coding: utf-8 -*-

import pcl

# Cargar la nube de puntos
cloud = pcl.load('remocion_threshold1.pcd')

# Crear un filtro VoxelGrid para la nube de puntos
fvox = cloud.make_voxel_grid_filter()
# Tamaño de voxel
VOXEL_SIZE = 0.01
# Asignar el tamaño del voxel al filtro
fvox.set_leaf_size(VOXEL_SIZE, VOXEL_SIZE, VOXEL_SIZE)

# Ejecutar el filtro
cloud_filtered = fvox.filter()

# Grabar el resultado en disco
filename = "escena_downsampled_%s.pcd" % (VOXEL_SIZE)
pcl.save(cloud_filtered, filename)

