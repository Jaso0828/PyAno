import json
from core.pianos.pianos import Piano
from core.pianos.piano_categories import PianoCategories
from core.pianos.piano_types import PianoType


class PianoRepo:
    def __init__(self, repo_type: str):
        self._repo_type = repo_type
        self._file_path = ''
        self._db_connection = ''
        self._configure(repo_type)

    
    def _configure(self, repo_type: str):
        if repo_type == 'file':
            self._file_path = 'data_store/files/pianos.json'
        elif repo_type == 'db':
            self._db_connection = 'data_store/db/pianos.db'
    

    def save_piano(self, piano: Piano) -> Piano:
        if self._repo_type == 'file':
            pianos = self._read_pianos_from_file()

            if pianos:
                last_id = max(piano.get('id', 0) for piano in pianos)
                next_id = last_id + 1
            else:
                next_id = 1

            piano.id = next_id
            
            pianos.append({
                "id": piano.id,
                "category": piano.category.category,
                "type": piano.type.type,
                "name": piano.name,
                "description": piano.description,
                
            })
            with open(self._file_path, 'w') as file_writer:
                json.dump(pianos, file_writer, indent=4)
            return piano
        elif self._repo_type == 'db':
            # Implement database save logic here
            pass

    
    def get_all_pianos(self) -> Piano:
        if self._repo_type == 'file':
            pianos_data = self._read_pianos_from_file()
            return[self.dict_to_piano(piano) for piano in pianos_data]
        elif self._repo_type == 'db':
            # Implement database retrieval logic here
            pass
        


    def _read_pianos_from_file(self):
        try:
            with open(self._file_path, 'r') as file_reader:
                pianos_data = json.load(file_reader)
                if isinstance(pianos_data, dict):
                    return [pianos_data]
                elif isinstance(pianos_data, list):
                    return pianos_data
                else:
                    return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except Exception as ex:
            print(f"An unexpected error occurred while reading guitars: {ex}")
            return []
        
        
    def dict_to_piano(self, piano_dict: dict):
        return Piano(
            piano_dict['id'],
            piano_dict['category'],
            piano_dict['type'],
            piano_dict['name'],
        )