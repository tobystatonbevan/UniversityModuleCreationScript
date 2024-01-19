import os

class Module:
    def __init__(self,path,name,weeks):
        self.__destinationDir = path
        self.__name = name
        self.__weeks = weeks

    def createModuleRoot(self):
        try:
            os.mkdir(self.__name)
        except:
            raise

    def createWeeks(self):
        try:
            os.chdir(os.path.join(self.__destinationDir,self.__name))
            for i in range(self.__weeks):
                if i < 9:
                    os.mkdir(f"Week 0{i+1}")
                else:
                    os.mkdir(f"Week {i+1}")
        except:
            raise

    def createContent(self):
        try:
            os.chdir(os.path.join(self.__destinationDir,self.__name))
            for i in os.listdir(os.path.join(self.__destinationDir,self.__name)):
                os.chdir(i)
                os.mkdir("Lectures")
                os.mkdir("Labs")
                os.mkdir("Resources")
                os.chdir(os.path.join(self.__destinationDir,self.__name))
        except:
            raise