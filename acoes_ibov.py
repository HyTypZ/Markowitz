import yfinance as yf
import pandas as pd

# Obtenha a lista de tickers que compuseram o índice Ibovespa durante o período desejado
ibovespa_tickers = ['ABEV3.SA', 'AGRO3.SA', 'AMER3.SA', 'B3SA3.SA', 'BBDC4.SA', 'BIDI4.SA', 'BPAC3.SA', 'BRF3.SA', 'BRFS3.SA', 'CIEL3.SA', 'COGN3.SA', 'CSAN3.SA', 'ELET3.SA', 'ELET6.SA', 'ENBR3.SA', 'EWZ.SA', 'FLRY3.SA', 'ITUB4.SA', 'JBS3.SA', 'JHSF3.SA', 'KLBN4.SA', 'KROT3.SA', 'LREN3.SA', 'MGLU3.SA', 'MRVL3.SA', 'MULTI3.SA', 'NATU3.SA', 'PETR3.SA', 'PETR4.SA', 'PSSA3.SA', 'RAIZ3.SA', 'RDOR3.SA', 'SANB11.SA', 'SANB4.SA', 'SULA11.SA', 'TAEE3.SA', 'TAMM3.SA', 'TGMA3.SA', 'TRPL4.SA', 'VALE3.SA', 'VVAR3.SA', 'WEGE3.SA', 'WEGE4.SA']

# Defina o período desejado
start_date = '2019-01-01'
end_date = '2020-12-31'

# Crie um DataFrame vazio para armazenar os dados
ibovespa_data = pd.DataFrame()

# Loop pelos tickers e obter os dados do Yahoo Finance
for ticker in ibovespa_tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    # Adicione a coluna "Adj Close" ao DataFrame ibovespa_data com um nome descritivo
    ibovespa_data[f'{ticker}_Adj_Close'] = data['Adj Close']

# Salve os dados em um arquivo XLSX
ibovespa_data.to_excel('ibovespa_data.xlsx')
