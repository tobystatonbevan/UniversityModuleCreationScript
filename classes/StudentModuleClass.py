import os

class Module:
    def __init__(self,path,name,weeks):
        self.__destinationDir = path
        self.__name = name
        self.__weeks = weeks

    def createModuleRoot(self):
        os.mkdir(self.__name)

    def createWeeks(self):
        os.chdir(os.path.join(self.__destinationDir,self.__name))
        for i in range(self.__weeks):
            os.mkdir(f"Week {i+1}")

    def createContent(self):
        os.chdir(os.path.join(self.__destinationDir,self.__name))
        for i in os.listdir(os.path.join(self.__destinationDir,self.__name)):
             os.chdir(i)
             os.mkdir("Lectures")
             os.mkdir("Labs")
             os.mkdir("Resources")
             os.chdir(os.path.join(self.__destinationDir,self.__name))