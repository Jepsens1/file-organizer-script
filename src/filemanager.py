from pathlib import Path
import json
import shutil


class FileManager:

    def __init__(self, folder_path: str, recursive_enabled: bool):
        self.folder_path = folder_path
        self.recursive_enabled = recursive_enabled
        self.files: list[Path] = self.__get_files()
        self.supported_files: dict = self.__read_supported_files()

    @staticmethod
    def __read_supported_files():
        with open('supported_files.json') as json_file:
            return json.load(json_file)

    def __get_files(self):
        if self.recursive_enabled:
            path = Path(self.folder_path).glob('**/*')
        else:
            path = Path(self.folder_path).glob('*')
        return [file for file in path if file.is_file()]

    def __find_category(self, file: Path) -> str | None:
        file_extension = file.suffix.lower()
        found_category = None
        for category, extensions in self.supported_files.items():
            if file_extension in extensions:
                found_category = category
                break
        return found_category

    def sort_preview(self):
        print('----preview option selected----')
        for file in self.files:
            category = self.__find_category(file)
            if category:
                print(
                    f'File "{file.name}" is supported under category "{category.capitalize()}" disable -p or --preview argument to take action into effect"')
            else:
                print(f'File "{file.name}" is not supported')

        print('feel free to modify supported_files.json if you want to add more extensions')

    def sort_files(self):
        for file in self.files:
            category = self.__find_category(file)
            if category:
                destination_dir = Path(self.folder_path) / category.capitalize()
                destination_dir.mkdir(parents=True, exist_ok=True)
                destination_file = destination_dir / file.name
                shutil.move(str(file), str(destination_file))
                print(f'File "{file.name}" moved to "{destination_dir}"')
            else:
                print(f'File "{file.name}" is not supported')
