from pathlib import Path
import functools
import logging

file_path = Path(__file__).resolve().parents[1] / "logs" / "mysql_logs.log"

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def database_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Chamando {func.__name__} com args: {args[1:]}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} retornou: {result}")
        return result

    return wrapper
