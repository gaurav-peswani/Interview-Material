import os

NEWLINE = b'\n'

class Tail:

    def __init__(self, file_path: str, n: int) -> None:
        self.file_path = file_path
        self.n = n

    def _validate_inputs(self) -> None:
        if not self.file_path:
            raise ValueError("File path cannot be empty.")
        if type(self.n) != int:
            raise ValueError("'n' must be an integer.")

    def _is_file_exists(self) -> None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The path {self.file_path} does not exist.")
    
    def _is_text_file(self) -> None:
        if not os.path.isfile(self.file_path):
            raise Exception(f"The path {self.file_path} is not a file.")
    
    def _is_file_accessible(self) -> None:
        if not os.access(self.file_path, mode=os.R_OK):
            raise PermissionError(f"The path {self.file_path} is not accessible.")
        
    def _tail(self) -> None:
        with open(self.file_path, mode='rb') as f:
            # Go to the end of the file
            f.seek(0, os.SEEK_END)

            # file positions
            pos = 0

            # max characters
            characters = f.tell()

            # line counter
            line = 0
            
            while pos < characters:
                character = f.read(1)
                if character == NEWLINE:
                    line += 1
                if line == self.n:
                    break
                pos += 1
                f.seek(-pos, os.SEEK_END)
            
            print(f.read().decode())
    
    def execute(self) -> None:
        self._validate_inputs()
        self._is_file_exists()
        self._is_text_file()
        self._is_file_accessible()
        self._tail()

if __name__ == "__main__":
    Tail(file_path="text_file.txt", n=10).execute()

