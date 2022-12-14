from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Se quiser adicionar permicao de ler apenas, basta adicionar um .readonly no fim.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Aqui fica o ID da tabela, que pode ser obtido pelo seu link.
SAMPLE_SPREADSHEET_ID = '1IBHFiLrfxOidVoGGiLJ_laU8B3QkzIPCJKA-OPielzA'
# Aqui fica o intervalo que sera lido, no caso de B2 ate AF10
SAMPLE_RANGE_NAME = 'B2:AF16'


def main():
    # declara as credenciais como vazias
    creeds = None

    # Verifica se o token ja foi criado
    if os.path.exists('token.json'):
        creeds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Se as credencias nao existirem ou nao forem validas, requere as novas credenciais
    if not creeds or not creeds.valid:
        if creeds and creeds.expired and creeds.refresh_token:creeds.refresh(Request())
        else:
            # abre o navegador e pede a autorizacao
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creeds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            # escreve um novo token com as credenciais
            token.write(creeds.to_json())

    try:
        # Le informaçoes do google sheets
        service = build('sheets', 'v4', credentials=creeds)
        sheet = service.spreadsheets()
        # Salva as informacoes em result como um dicionario
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

        # Preenchendo as colunas finais para que todas tenham 31 colunas
        for aluno in result['values']:
            for i in range(31 - len(aluno)):
                aluno.append('')

        # Declaração das chaves dos horários para criar o novo dicionário
        key_lst = ['7h00-7h50', '7h50-8h40', '8h55-9h45', '9h45-10h35', '10h50-11h40', '11h40-12h30', '12h50-13h50',
                   '13h50-14h40', '14h40-15h30', '15h50-16h40', '16h40-17h30', '17h30-18h20', '19h00-19h50',
                   '19h50-20h40']

        # Criando o dicionário a partir da entrada da API
        result = {result['values'][j][0].split(' ', 1)[0]:
                      {'Presencial': {key_lst[i]: result['values'][j][i + 3] for i in range(14)},
                       'Remoto': {key_lst[i]: result['values'][j][i + 17] for i in range(14)}}
                  for j in range(len(result['values']))}

        # Declaração da saída
        output = [
            ["Horario de Dedicacao ao Programa de Educacao Tutorial - Lab. de Robotica (305)"],  # 0
            ["", "SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA"],  # 1
            ["7h00 - 7h50", "", "", "", "", ""],  # 2
            ["7h50 - 8h40", "", "", "", "", ""],  # 3
            ["INTERVALO"],  # 4
            ["8h55 - 9h45", "", "", "", "", ""],  # 5
            ["9h45 - 10h35", "", "", "", "", ""],  # 6
            ["INTERVALO"],  # 7
            ["10h50 - 11h40", "", "", "", "", ""],  # 8
            ["11h40 - 12h30", "", "", "", "", ""],  # 9
            ["ALMOÇO"],  # 10
            ["12h50 - 13h50", "", "", "", "", ""],  # 11
            ["13h50 - 14h40", "", "", "", "", ""],  # 12
            ["14h40 - 15h30", "", "", "", "", ""],  # 13
            ["INTERVALO"],  # 14
            ["15h30 - 16h40", "", "", "", "", ""],  # 15
            ["16h40 - 17h30", "", "", "", "", ""],  # 16
            ["17h30 - 18h20", "", "", "", "", ""],  # 17
            ["JANTAR"],  # 18
            ["19h00 - 19h50", "", "", "", "", ""],  # 19
            ["19h50 - 20h40", "", "", "", "", ""],  # 20
            [],  # 21
            ["* = Horário de dedicação em Trabalho Remoto"],  # 21
        ]

        # Imprimindo a entrada e passando-a para a saída
        for aluno in result:
            print('----------', aluno, '----------')
            for modo in result[aluno]:
                print('\n-', modo, '-\n')
                i = 2
                for horario in result[aluno][modo]:
                    if i == 4 or i == 7 or i == 10 or i == 14 or i == 18:
                        i += 1

                    print(horario, ':', result[aluno][modo][horario])

                    if 'Segunda' in result[aluno][modo][horario]:
                        string = ''
                        if output[i][1]:
                            string += ', '
                        string += aluno
                        if modo == 'Remoto':
                            string += '*'
                        output[i][1] += string

                    if 'Terça' in result[aluno][modo][horario]:
                        string = ''
                        if output[i][2]:
                            string += ', '
                        string += aluno
                        if modo == 'Remoto':
                            string += '*'
                        output[i][2] += string

                    if 'Quarta' in result[aluno][modo][horario]:
                        string = ''
                        if output[i][3]:
                            string += ', '
                        string += aluno
                        if modo == 'Remoto':
                            string += '*'
                        output[i][3] += string

                    if 'Quinta' in result[aluno][modo][horario]:
                        string = ''
                        if output[i][4]:
                            string += ', '
                        string += aluno
                        if modo == 'Remoto':
                            string += '*'
                        output[i][4] += string

                    if 'Sexta' in result[aluno][modo][horario]:
                        string = ''
                        if output[i][5]:
                            string += ', '
                        string += aluno
                        if modo == 'Remoto':
                            string += '*'
                        output[i][5] += string

                    i += 1
            print('\n')

        print('\n-------------------------\n')

        for l in output:
            if len(l) == 6:
                hora, segunda, terca, quarta, quinta, sexta = l
                print('{:<15} {:<40} {:<40} {:<40} {:<40} {:<40}'.format(hora, segunda, terca, quarta, quinta, sexta))

        # Escreve o resultado na página Formatado, a partir de A1
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Formatado!A1", valueInputOption="USER_ENTERED"
                                        , body={'values': output}).execute()
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
