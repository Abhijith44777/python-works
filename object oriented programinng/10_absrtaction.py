from abc import ABC,abstractmethod

class bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Hunter(bike):

    
    def start(self):
        print("hunter starting method")

 
    def accelarate(self):
        print("hunter accelarate method")


    def stop(self):
        print("hunter breaking method")           

Hunter_instance=Hunter()

Hunter_instance.start()

Hunter_instance.stop()