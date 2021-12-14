"""
This module contains the code to initialise the application and interface with
the AccessController.
"""
from system.controllers.access_controller import AccessController

if __name__ == "__main__":
    controller = AccessController()
    controller.start()
