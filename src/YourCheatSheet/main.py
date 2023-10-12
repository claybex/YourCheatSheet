from sys import argv

class Parser:
    def __init__(self,json, k1='', k2='', k3=''):
         self.json_object = json
    def main(self):     
        try:
            if len(argv) == 3:
                try:
                    for key in self.json_object[argv[2]]:
                        print(key)
                except(KeyError, TypeError):
                        print('Wrong topic was specified, try one of available bellow:'
                            .format())
                        for key in self.json_object:
                            print(key)
                
            elif len(argv) == 4:
                    try:    
                        if any(key <= str(1) for key in self.json_object[argv[2]][argv[3]]):
                            print(self.json_object[argv[2]][argv[3]])
                        else:
                            for key in self.json_object[argv[2]][argv[3]]:
                                print(key)
                    except(KeyError, TypeError):
                        if argv[2] in self.json_object:
                            print('Wrong topic was specified, try one of available bellow:'
                                .format())
                            for key in self.json_object[argv[2]]:
                                print(key)
                        else:
                             print("Multiple keys error!")
            elif len(argv) == 5:
                try:
                    print(self.json_object[argv[2]][argv[3]][argv[4]])
                except(KeyError, TypeError):
                        if argv[2] in self.json_object and argv[3] in self.json_object[argv[2]]:
                            print('Wrong topic was specified, try one of available bellow:'
                                .format())
                            for key in self.json_object[argv[2]][argv[3]]:
                                print(key)
                        else:
                             print("Multiple keys error!")
            elif len(argv) < 3:
                for key in self.json_object:
                    print(key) 
                        
        except (IndexError):
            print(IndexError)
