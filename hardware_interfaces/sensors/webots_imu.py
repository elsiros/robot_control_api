# TODO: add docs
# TODO: add config read
import logging
from imu_sensor_interface import IMUSensorInterface
from controller import InertialUnit


class WebotsIMU(IMUSensorInterface):
    """[summary]

    Args:
        IMUSensorInterface ([type]): [description]
    """

    def __init__(self, name, robot):
        super().__init__(name)
        self.robot = robot

        self.__in_unit = InertialUnit(self.name)
        self.__in_unit.enable(100)

    def get_param(self, param_name):
        pass

    def start(self):
        try:
            self.__in_unit.enable()
            self.__status = 'enabled'
        except Exception as start_exception:
            self.__status = 'disabled'
            logging.error(start_exception)

        self.__status = 'enabled'

    def _get_orientation(self):
        orientation = None
        if self.__status == 'enabled':
            orientation = self.__in_unit.getRollPitchYaw()
        else:
            logging.error("IMU is not started")
        return orientation
