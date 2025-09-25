# Documentação do NAPNE IFRN Parnamirim

Esta documentação foi criada usando [Sphinx](https://www.sphinx-doc.org/) com suporte a arquivos Markdown através do [MyST-Parser](https://myst-parser.readthedocs.io/).

## Requisitos

Instale os requisitos listados no `requirements.txt` na raiz do projeto:

```bash
pip install -r requirements.txt
```

## Como construir a documentação

### Usando o Makefile (Linux/Mac):

```bash
cd docs/
make html
```

### Usando o make.bat (Windows):

```bash
cd docs/
make.bat html
```

### Visualização local

Para visualizar a documentação localmente com auto-recarga:

```bash
cd docs/
sphinx-autobuild source build/html
```

Depois acesse `http://localhost:8000` no seu navegador.

## Estrutura dos arquivos

- `source/`: Contém os arquivos fonte da documentação
- `source/conf.py`: Configuração do Sphinx
- `source/index.md`: Página principal (em Markdown)
- `source/*.md`: Páginas da documentação (em Markdown)
- `source/references.bib`: Bibliografia (BibTeX)
- `build/html/`: Documentação HTML gerada

## Extensões utilizadas

- **myst-parser**: Para suporte a Markdown
- **furo**: Tema moderno e responsivo
- **sphinx-copybutton**: Botão de copiar código
- **sphinxcontrib-bibtex**: Suporte a bibliografias
- **sphinxcontrib-mermaid**: Diagramas Mermaid
- **linkify-it-py**: Auto-links

## Como editar

1. Edite os arquivos `.md` na pasta `source/`
2. Execute `make html` para gerar a documentação
3. Visualize o resultado em `build/html/index.html`