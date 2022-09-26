from main import *
from leitura_logs import *
from calibragem import *

temperatura = leitura_dados_dts(log_dts_medida)[0]
posicao = leitura_dados_dts(log_dts_medida)[1]

x = position_dts(1,1,0,temperatura, posicao)


print(posicao)
print(x)


