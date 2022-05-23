import logging
from toy_car.settings import APP_NAME
logger = logging.getLogger(APP_NAME)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s:%(message)s'")
handler.setFormatter(formatter)
logger.addHandler(handler)
