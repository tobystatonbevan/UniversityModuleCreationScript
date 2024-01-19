from modules.LecturerInteractionTools import getModuleName, getModuleDuration, checkDestination
from classes.StudentModuleClass import Module
from os import getcwd,chdir

name = getModuleName()
length = getModuleDuration()
try:
    chdir(checkDestination())
except:
    raise

module = Module(getcwd(),name,length)
module.createModuleRoot()
module.createWeeks()
module.createContent()