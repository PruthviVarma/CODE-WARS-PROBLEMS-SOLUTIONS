class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
        if(self.name == 'Santa Claus' and self.password == 'Ho Ho Ho!'):
            return True
        else:
            return False
        
