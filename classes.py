from main import * 


class Command:

    def __init__(self, command_name, function_name, command_parameters, 
                 command_description, command_parameters_descriptions): 
        self.name = command_name 
        self.function = function_name 
        self.parameters = command_parameters
        self.description = command_description
        self.parameters_descriptions = command_parameters_descriptions 
    
    def __str__(self): 
        return self.name

    def __repr__(self): 
        return self.name


class Image: 
    
    def __init__(self, name, image=None, path=None): 
        self.name = name 
        self.path = path
        if path != None:
            self.img = imread(path)
        else:
            self.img = image
    
    def __str__(self): 
        return self.name

    def __repr__(self): 
        return self.name
