from abc import ABC ,abstractmethod
class phone(ABC):
      @abstractmethod
      def call (self):
          pass
      @abstractmethod 
      def msg (self):
          pass
class samsung(phone):
      def details(self):
          print(f'RAM:60\n model:f62')
      def call(self):
          print('calling....')
      def msg(self):
          print('meassaging')
obj=samsung()
obj.call()    
obj.msg()    
obj.details()          


