import json
from core.pianos import Piano, PianoCategories, PianoType
from config import AppConfig
from constants import REPO_TYPE_FILE, REPO_TYPE_DB, CONFIG_FILE_PATH
from infrastructure import PianoRepo


def load_config(file_path: str) -> AppConfig:
    try:
        with open(file_path, 'r') as file_reader:
            config_data = dict(json.load(file_reader))
        
        return AppConfig(
            debug = config_data.get('debug', False),
            database_url= config_data.get('database_url', ''),
            repo_type=config_data.get('repo_type', REPO_TYPE_FILE)
        )
    
    except FileNotFoundError:
        print(f'Error file not found {file_path}')
        return None
    
    except json.JSONDecodeError:
        print(f"Error decoding JSON from config file: {file_path}")
        return None
    
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None



def main():
    app_config = load_config(CONFIG_FILE_PATH)
    if app_config == None:
        print('Faild to load app congif.')
        return
    
   # Kreiraj repozitorij ovisno o tipu (file/db)
    piano_repo = PianoRepo(app_config.repo_type)

    # Kreiraj piano objekte
    piano_type = PianoType(type='Analog')
    piano_category = PianoCategories(category='Electric')
    rhodes = Piano(category=piano_category, type=piano_type, name='Rhodes')

    # Spremi piano
    piano_repo.save_piano(rhodes)
    print("Piano saved successfully!")

    # Ispis svih
    all_pianos = piano_repo.get_all_pianos()
    print("All pianos in repo:", all_pianos)

if __name__ == "__main__":
    main()
