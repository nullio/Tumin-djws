from tumin_api.viewsets import SerServicioViewset, CueCuentaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('serservicios',SerServicioViewset)  #url/tuminapi/serservicios/$
router.register('cuecuenta', CueCuentaViewset)

