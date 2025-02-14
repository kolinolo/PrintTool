PrintTool é uma ferramenta para centralizar ou colorizar um texto.

para colorizar:

    vermelho = printTool.configColorizar('vermelho').colorizar # Cria a variável "vermelho" como uma configuração do colorizar()
    textoEmVermelho = vermelho("uma string colorizada") # retorna o texto "uma string colorizada" em vermelho, de acordo com a configuração da função

    print(textoEmVermelho)

    saída:

      '\x1b[91mtextoEmVermelho\x1b[0m' # e no console: "textoEmVermelho" em vermelho

  parâmetros:
  
    configColorizar(cor: str,autoPrint: bool = False)
    
  cor: deve ser uma string: rosa, azul, verde, amarelo ou vermelho

  autoPrint: deve ser True ou False, parâmetro opicional, False por padrão. Se True, a função printa o texto colorizado, se false a função RETORNA o texto colorizado 
  
============================================================================================

Centralizar:

centraliza um texto na tela:
    
    exemplo:

            titulo = printTool.configCentralizar(20,"-").centralizar
            titulo("Um texto")

            saida:
            
                ------ Um texto ------
Parametros:

    configCentralizar(MX: int , borda: str)

MX: um numero inteiro que representa o tamanho da linha aonde o texto vai estar

borda: uma string que representa o character que sera usado para criar a borda
    
