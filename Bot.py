name: LinkedIn AI Bot Sereza

on:
  schedule:
    - cron: '0 */6 * * *' # Ejecuta cada 6 horas
  workflow_dispatch: # Permite ejecutarlo manualmente

jobs:
  publicar:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del código
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: pip install -r requirements.txt

      - name: Ejecutar el bot
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          LINKEDIN_TOKEN: ${{ secrets.LINKEDIN_TOKEN }}
          LINKEDIN_URN: ${{ secrets.LINKEDIN_URN }}
        run: python bot.py
