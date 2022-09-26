from leitura_logs import *

log_dts_ambiente = "log_dts_ambiente/"
log_dts_medida = "log_dts_medida/"
log_lv_ambiente = "log_lv_ambiente/"
log_lv_calibragem = "log_lv_calibragem/"
log_lv_medida = "log_lv_medida/"
log_output = "log_output/"


def main():



    print(leitura_dados_dts(log_dts_medida)[0][0])
    print(len(leitura_dados_dts(log_dts_medida)[0][0]))
    print(leitura_dados_lv(log_lv_medida)[0])
    print(len(leitura_dados_lv(log_lv_medida)[0]))

if __name__ == '__main__':
    main()