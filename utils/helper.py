import re
from os import getenv, path, remove

def check_dir_write_permission(directory=str):
    try:
        testfile = path.join(directory, 'test.write_perm')
        with open(testfile, 'w') as file:
            file.write('TEST_WRITE_PERMISSION')
        remove(testfile)
        return True
    except(IOError, PermissionError):
        return False

class nstate:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m[*]\033[0m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m[+]\033[0m'
    INFO    = '\033[93m[i]\033[0m'
    WARNING = '\033[93m'
    FAIL = '\033[91m[-]\033[0m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    LINK = '\033[94m\033[4m'
    clLIGHTBLUE = '\033[36m'
    clRED = '\033[30m'
    clGRAY = '\033[90m'

    def TextBlue(TextToFormat:str) -> str:
        return f'\033[94m{TextToFormat}\033[0m'
    
    def TextLink(TextToFormat:str) -> str:
        return f'\033[94m\033[4m{TextToFormat}\033[0m'
    
    def TextHeader(TextToFormat:str) -> str:
        return f'\033[95m{TextToFormat}\033[0m'
    
    def TextOKGreen(TextToFormat:str) -> str:
        return f'\033[92m[+]\033[0m {TextToFormat}'
    
    def TextOKBlue(TextToFormat:str) -> str:
        return f'\033[94m[*]\033[0m {TextToFormat}'
    
    def TextInfo(TextToFormat:str) -> str:
        return f'\033[93m[i]\033[0m {TextToFormat}'
    
    def TextFail(TextToFormat:str) -> str:
        return f'\033[91m[-]\033[0m {TextToFormat}'
    
class WinEnv:

    target_path = ''
    env_variable = ''
    env_value = ''

    def __init__(self, input_path):
        self.self = self
        self.input_path = input_path

    def CheckEnvVariable(self):
        if re.match(r"^%[^%]+%", self.input_path):
            return True
        else:
            return False

    def LookupEnvironment(self):
        self.env_value = getenv(self.env_variable)
        
    def StripEnvVariable(self):
        match = re.search(r"%(.+?)%", self.input_path)
        if match:
            self.env_variable = match.group(1)

    def ReplaceVarWithValue(self):
        self.target_path = self.input_path.replace(f'%{self.env_variable}%', self.env_value)
    