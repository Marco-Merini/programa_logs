## Arquivo de Configuração (`logging_config.yaml`):

- Define o formato das mensagens de log (`detailed`).
- Especifica o nível de log para o handler de arquivo como `DEBUG` e indica que os logs serão gravados em `app.log`.
- Configura o logger chamado `example_logger` para usar este handler e definir o nível de log como `DEBUG`.

## Função `setup_logging`:

- Lê o arquivo de configuração YAML e aplica as configurações de logging.

## Função `main`:

- Configura o logging chamando `setup_logging`.
- Cria um logger chamado `example_logger` e gera logs em vários níveis (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

Link para download do relatório: [Download](https://pt.overleaf.com/read/fphnwsvmmztq#43ddbd)

## By Marco Leone Merini
