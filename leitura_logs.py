import numpy as np
from funcoes import *
from os import listdir
from os.path import isfile, join
import save

def leitura_dados_dts(path):
    a = [f for f in listdir(path) if isfile(join(path, f))]
    b = []
    for item in a:
        if ".txt" in item:
            b.append(item)

    # -----------------------------------
    # sequencia de logs
    logs = sorted(b)
    # -----------------------------------

    temperaturas = []
    posicao = []

    duration_list = []
    data_list = []
    hora_list = []

    for log in logs:
        # -----------------------------------
        # Abertura do log
        with open(path + log, encoding='iso-8859-1') as f:
            lines = f.readlines()

        # -----------------------------------
        # Pescar linha especifica
        list_lines = list(lines)

        # -----------------------------------
        # Data e hora
        data_list.append(clean(list_lines[10])[:-6])
        hora_list.append(clean(list_lines[10])[8:])

        # -----------------------------------
        # Duração esegundos
        duration_list.append(int(float(clean(list_lines[11]))))

        # -----------------------------------
        # remoção de cabeçalho
        del list_lines[0:41]

        # -----------------------------------
        log_pos = []
        log_temp = []
        # -----------------------------------
        for masure in list_lines:
            line = masure.split('\n')
            data = line[0].split('\t')
            log_pos.append(comma_to_dot(data[0]))
            log_temp.append(comma_to_dot(data[1]))

        # -----------------------------------
        posicao.append(log_pos)
        temperaturas.append(log_temp)

    return temperaturas, posicao, duration_list, data_list, hora_list

def position_dts(ini, fim, t_especifica, temperatura, posicao):

    temperaturas = []
    #############################
    tempValue_posicao = []
    tempValue_temperatura = []
    #############################

    if t_especifica == 0:
        print('errado')
    else:
        for item in range(len(posicao)):
            for temp in posicao[item]:
                location = []
                if temp <= t_especifica + 0.1 and temp >= t_especifica - 0.1:
                    tempValue_posicao.append(temp)
                    location.append(posicao.index(temp))
                for y in location:
                    tempValue_temperatura.append(temperatura[y])
            temperaturas.append(np.mean(tempValue_temperatura))

    #
    #
    # for temp in range(len(posicao)):
    #     #############################
    #     tempValue_posicao = []
    #     tempValue_temperatura = []
    #     if point == 0:
    #         for x in posicao[temp]:
    #             location = []
    #             if x >= ini and x <= fim + 1:
    #                 tempValue_posicao.append(x)
    #                 location.append(posicao.index(x))
    #             for y in location:
    #                 tempValue_temperatura.append(temperatura[y])
    #         temperaturas.append(np.mean(tempValue_temperatura))
    #     else:
    #         for x in posicao[temp]:
    #             location = []
    #             if x <= point + 0.1 and x >= point - 0.1:
    #                 tempValue_posicao.append(x)
    #                 location.append(posicao.index(x))
    #             for y in location:
    #                 tempValue_temperatura.append(temperatura[y])
    #         temperaturas.append(np.mean(tempValue_temperatura))
    #
    # round_temp = []
    # for t in range(len(temperaturas)):
    #     round_temp.append(round(temperaturas[t]))
    #
    # save.save_log(f'{save.save_open()[2]}', f'{round_temp}')

    return temperaturas

def leitura_dados_lv(path_lv):

    ambiente = [] # T meio
    fibra = [] # T inicio
    T_fim = []
    tempo = []
    ##################################################
    a = [f for f in listdir(path_lv) if isfile(join(path_lv, f))]
    b = []

    for item in a:
        if ".txt" in item:
            b.append(item)

    ##################################################
    # sequencia de logs
    logs = sorted(b)
    ##################################################

    for log in logs:
        # -----------------------------------
        # Abertura do log
        with open(path_lv + log, encoding='iso-8859-1') as f:
            lines = f.readlines()

        # -----------------------------------
        # Pescar linha especifica
        list_lines = list(lines)

        del list_lines[0:23]

        for masure in list_lines:
            line = masure.split('\n')
            data = line[0].split('\t')
            tempo.append(comma_to_dot(data[0]))
            fibra.append(comma_to_dot(data[1]))
            ambiente.append(comma_to_dot(data[3]))
            T_fim.append(comma_to_dot(data[5]))

    return ambiente, fibra, T_fim, len(tempo)

