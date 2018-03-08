import os
import platform

project_path = os.path.dirname(__file__)
if platform.system() == "Windows":
    chromedriver_path = os.path.join(project_path, 'drivers\\chromedriver.exe')
elif platform.system() == "Linux":
    chromedriver_path = os.path.join(project_path, 'drivers/chromedriver')

