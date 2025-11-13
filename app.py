from config import AppConfig

def load_config() -> AppConfig:
    return AppConfig()


def main():
    config = load_config()
    

if __name__ == "__main__":
    main()
