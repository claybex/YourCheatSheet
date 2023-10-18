import json, markdown_to_json, pathlib

class Parser:
    def __init__(self, path: str):
        self.json_object = json        
        ##MD to JSON
        file = pathlib.Path(path)
        content = file.read_text()
        json_string = markdown_to_json.jsonify(content)
        self.json_object = json.loads(json_string)


    def get_data(self, k1='', k2='', k3=''):   
        try:
            if k1 and k2 == '' and k3 == '' :
                try:
                    for key in self.json_object[k1]:
                        print(key)
                except(KeyError, TypeError):
                        print('Wrong topic was specified, try one of available bellow:'
                            .format())
                        for key in self.json_object:
                            print(key)
                
            elif k1 and k2 and k3 == '' :
                    try:    
                        if any(key <= str(1) for key in self.json_object[k1][k2]):
                            print(self.json_object[k1][k2])
                        else:
                            for key in self.json_object[k1][k2]:
                                print(key)
                    except(KeyError, TypeError):
                        def check_k2_in_k3():
                            for key in self.json_object.get(k1, {}):
                                try:
                                    for key2, value in self.json_object.get(k1, {}).get(key, {}).items():
                                        if key2 == k2:
                                            return (value)
                                            
                                except AttributeError:
                                    continue
                        value = check_k2_in_k3()
                        if value: 
                            print(value)
                        else:
                            if k1 in self.json_object:
                                print('Wrong topic was specified, try one of available bellow:'
                                    .format())
                                for key in self.json_object[k1]:
                                    print(key)
                            else:
                                print("Multiple keys error!")
            elif k1 and k2 and k3:
                try:
                    print(self.json_object[k1][k2][k3])
                except(KeyError, TypeError):
                        if k1 in self.json_object and k2 in self.json_object[k1]:
                            print('Wrong topic was specified, try one of available bellow:'
                                .format())
                            for key in self.json_object[k1][k2]:
                                print(key)
                        else:
                             print("Multiple keys error!")
            else:
                for key in self.json_object:
                    print(key) 
                        
        except (IndexError):
            print(IndexError)
