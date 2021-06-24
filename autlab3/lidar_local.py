import numpy as np

ANGLE_MAX = 6.28318977356
ANGLE_INCREMENT = 0.0175019223243

ranges = (1.3482780456542969, 1.296741008758545, 1.308858871459961, 1.2983766794204712, 1.289656639099121, 1.280846118927002, 1.3028526306152344, 1.3007009029388428,1.2957195043563843, 1.307003140449524, 1.3216253519058228, 1.3077366352081299, 1.3274049758911133, 1.3553770780563354, 1.3847346305847168, 1.3708575963974, 1.435846209526062, 1.4353288412094116, 1.5108565092086792, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.7178187370300293, 2.5879316329956055, 2.5239996910095215, 2.463003635406494, 2.4441449642181396, 2.4031989574432373, 2.390012502670288, 2.380622386932373, 2.369335651397705, 2.3456215858459473, 2.35729718208313, 2.3663713932037354, 2.3624045848846436, 2.3619260787963867, 2.3969764709472656, 2.42893385887146, 2.4298088550567627, 2.4762613773345947, 2.5237674713134766, 2.578871488571167, 2.8004891872406006, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.4821473360061646, 1.4447921514511108, 1.4073246717453003, 1.3879282474517822, 1.3523540496826172, 1.356046199798584, 1.3528211116790771)

theta = np.arange(0, ANGLE_MAX, ANGLE_INCREMENT)
max_range = 3.5
min_range = 0.119999997318


# Filtrar los rangos que no son válidos: mantener solo los rangos
# válidos y sus correspondientes ángulos
# obtener valor válidos dentro de los rangos
logi_max = ranges < max_range
logi_min = ranges > min_range
posis_valid = logi_min & logi_max
ranges_mod = ranges[posis_valid]
print('longitud: ', len(posis_valid))
print('posiciones validas: ', posis_valid)
theta_mod = theta[posis_valid]

# Convertir los rangos válidos en x, y
def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

x, y = pol2cart(ranges_mod, theta_mod)

print("x", x)
print("y", y)