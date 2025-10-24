import datetime
import os

class Logger:
    def __init__(self):
        self.__log_format = "[{timestamp}], [{level}]: {message}"
    
    def __format_message(self, level, message):
        timestamp = datetime.datetime.now()
        return self.__log_format.format(level = level, timestamp = timestamp, message = message)
    
    def log(self, level, message):
        formatted = self.__format_message(level, message)
        return formatted
    
    def info(self, message):
        return self.log("INFO", message)
    
    def warning(self, message):
        return self.log("WARNING", message)
    
    def error(self, message):
        return self.log("ERROR", message)
    
class FileLogger(Logger):
    def __init__(self, filename="app.log"):
        super().__init__()
        self.__filename = filename
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=== LOG FILE CREATED ===\n")
    
    def log(self, level, message):
        formatted = self._Logger__format_message(level, message)
        with open(self.__filename, "a", encoding="utf-8") as f:
            f.write(formatted + '\n')

class DataBaseLogger(Logger):
    def __init__(self, filename="app.log"):
        super().__init__()
    
    def log(self, level, message):
        formatted = self._Logger__format_message(level, message)
        DataBase = []
        DataBase.append(formatted)
        return DataBase
    
class DataBaseLogger(Logger):
    def __init__(self, filename="app.log"):
        super().__init__()
    
    def log(self, level, message):
        formatted = self._Logger__format_message(level, message)
        print(formatted)


    

log = Logger()
log.log("INFO", "Сообщение")
file = FileLogger()
file.log("INFO", "Сообщение")
data = DataBaseLogger()
data.log("INFO", "Сообщение")
