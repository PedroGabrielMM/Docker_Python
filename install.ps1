# Cria o ambiente virtual
python -m venv .venv

# Ativa o ambiente virtual no PowerShell
. .\.venv\Scripts\Activate.ps1

# Instala as dependências
pip install -r requirements.txt
