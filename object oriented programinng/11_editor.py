from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass 

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def open(self):
        print("opening method")

    def write(self):
        print("writting method")


    def debug(self):
        print("debugging method")


    def execute(self):
        print("executing method")

Vscode_instance=Vscode()
Vscode_instance.open()        
Vscode_instance.execute( )
