class lapot:

    def __init__(self) -> None:
        self.last_command = 'None'
        self.final_string = ''
        self.list_of_changes = ['']
        self.counter = 0

    def add(self, parameter):
                
        if self.last_command == 'undo':
            self.counter = 0
            self.list_of_changes = [self.final_string]

        self.final_string += str(parameter)
        self.list_of_changes.append(self.final_string)
        self.last_command = 'add'
        self.counter += 1
        
        return self.final_string

    def remove(self, parameter):
        
        if self.last_command == 'undo':
            self.counter = 0
            self.list_of_changes = [self.final_string]
        
        self.counter += 1        
        if len(self.final_string) <= int(parameter):
            self.final_string = ''
            self.list_of_changes.append(self.final_string)
            self.last_command = 'remove'
            return self.final_string

        self.final_string = self.final_string[:-int(parameter)]
        self.list_of_changes.append(self.final_string)
        
        return self.final_string

    def issue(self, parameter):

        if len(self.final_string) < int(parameter):
            return ''

        return self.final_string[int(parameter)]

    def undo(self):
        
        self.last_command = 'undo'
        if self.counter > 0:
            self.counter -= 1
            self.final_string = self.list_of_changes[self.counter]
            
        return self.final_string

    def redo(self):
        
        if self.last_command == 'undo' and len(self.list_of_changes) - 1 > self.counter:
            
            self.final_string = self.list_of_changes[self.counter + 1]
            self.counter += 1
            
        return self.list_of_changes[self.counter]
            
    def choosing_an_operation(self, N, parameter):

        if N == 1:
            return self.add(parameter)
        if N == 2:
            return self.remove(parameter)
        if N == 3:
            return self.issue(parameter)
        if N == 4:
            return self.undo()
        if N == 5:
            return self.redo()
        return self.final_string

project = lapot()        

def BastShoe(command: str) -> str:
    
    N, parameter = int(command[0]), command[1:].strip()

    return project.choosing_an_operation(N, parameter)