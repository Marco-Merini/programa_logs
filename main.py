import logging
import logging.config
import yaml

def setup_logging(default_path='logging_config.yaml', default_level=logging.DEBUG):
    """Configura o logger com base em um arquivo de configuração YAML."""
    with open(default_path, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

def main():
    # Configurar o logging
    setup_logging()

    # Criar um logger
    logger = logging.getLogger('example_logger')

    # Registrar logs em diferentes níveis
    logger.debug('This is a DEBUG message.')
    logger.info('This is an INFO message.')
    logger.warning('This is a WARNING message.')
    logger.error('This is an ERROR message.')
    logger.critical('This is a CRITICAL message.')

if __name__ == "__main__":
    main()
