<h2 align="center">Breve estudo/análise sobre futebol</h2>

<div align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3-blue.svg"
      alt="Standard" />
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Kaggle-Datasets-9cf.svg"
      alt="Standard" />
  </a>
</div>

### Objetivo
O script tem a finalidade de gerar um output para ser carregado no site <a href="https://app.flourish.studio/">Flourish</a> e gerar um gráfico de corrida (Bar Race).
 O gráfico irá correr mês a mês desde 1974 até 2021 mostrando a corrida entre as Seleções de Futebol!

### Exemplo de Output
```csv
Brazil,https://www.countryflags.io/BR/flat/64.png,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,12,12,12,12,12,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,20,20,20,20,20,20,20,20,20,20,20,20,20,21,21,21,21,21,21,21,21,21,21,21,21,21,21,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,29,29,29,29,29,29,29,30,30,30,30,30,30,30,30,30,30,30,30,30,30,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,36,36,36,36,36,36,36,38,41,41,41,41,41,41,41,41,41,41,43,45,46,46,46,46,46,46,46,46,46,46,46,46,46,46,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,53,54,54,54,54,54,54,54,54,54,54,54,54,56,57,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,68,68,68,69,71,71,71,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,73,73,74,74,74,76,80,82,83,86,87,88,88,88,88,88,88,88,92,93,93,95,96,96,96,96,96,96,96,96,96,96,99,104,104,104,104,104,104,104,104,104,108,108,109,109,109,109,111,111,111,114,114,114,117,118,122,123,125,125,125,125,125,125,125,125,125,126,129,130,130,130,130,130,130,130,130,130,130,132,137,141,141,141,141,141,141,141,141,141,143,145,148,148,148,148,148,148,148,148,148,148,148,148,149,150,150,150,150,150,150,150,150,150,150,150,150,154,155,155,156,156,157,157,157,157,157,158,161,167,168,168,168,168,168,168,168,168,168,168,168,168,168,168,169,169,169,169,169,169,169,169,169,174,178,180,180,180,181,182,182,182,182,184,184,185,185,191,191,191,191,191,191,191,194,195,195,201,201,201,202,203,203,203,203,203,203,203,203,203,205,205,205,205,205,205,205,205,205,206,206,206,209,209,209,209,209,209,209,209,209,209,210,215,216,216,216,216,216,216,216,216,216,220,222,225,225,225,225,225,225,225,225,225,226,226,226,226,227,230,230,231,231,231,231,233,233,234,237,239,239,239,239,239,239,240,241,241,243,243,243,245,247,247,247,247,247,247,247,247,247,248,250,254,254,254,254,254,254,254,254,254,254,254,256,256,256,258,258,258,258,258,258,258,258,258,258,260,260,261,262,263,263,264,265,268,271,271,274,274,275,275,275,276,276,276,277,277,278,278,280,283,284,284,284,284,284,284,284,284,284,285,285,287,287,288,289,289,289,289,289,289,289,289,289,290,290,290,290,290,290,290,290,290,290,291,293,296,296,296,296,296,296,296,296,296,296,300,300,304,304,304,304,304,304,304,304,304,304,304,306,309,309,309,309,309,309,310,310,310,310,310,310,310,313,314,314,315,315,315,315,315,316,317,318,319,326,327,328,329,329,330,330,330,330,330,331,334,334,334,334,334,334,334,334,334,334,334,335,335,339,339,339,340,340,341,341,342,342,343,343,343,344,346,347,347,347,348,348,348,348,348,348,350,351,354,356,356,356,357,357,357,358,358,359,363,366,366,366,366,366,367,367,368,368,368,369,372,376,378,378,379,380,381,384,384,385,386,386,386,386,386,386,387,388,389,389,390,390,392,392,399,399,401,402,403,404,409,409,411,412,412,412,416,417,417,417,418,419,419,419,419,420,420,420,425,433,434,435,435,435,435,435,436,436,437,438,439,440,440,441,442,443,443,443,443,444,444,445,445,447,449,449,450,451,451,452,453,455,455,457,464,464,464,464,464,465,465,465,465,465,465,465,467,470,470,472,473,473,473,473,473,473,474,475,476,479,480,481,482,482,482,482,483,484,485,485,489,489,489,490,491,492,492,492,492,493,493,493,498,498,498,500,501,502,502,502,502,504,504,504,504,508,509,511,512,513,513,513,514,515,515,516,516,516,516,517,518,519,519,519,520,520,520,520,527,527,528,529,529,531,531,531,531,532,532,532,537,537,538,538,540,540,540,540,540,541,541,541,542,543,543,545,547,549,549,549,550,550,550,552,552,552,553,556,558,558,558,558,558,558,559,559,565,565,565,567,569,571,571,571,571,572,572,572,576,577,577,577,579,581,581,581,581,583,583,583,587,587,587,588,589,590,590,590,590,590,590,590,591,591,591,593,595,597,597,598,598,600,600,600,601,601,602,602,603,604,604,604,604,606,606,606,610,611,611,613,615,617,617,617,617,618,618,618,622,624,624,624,624,625,625,625,625,625,627,629,629,629,629,629
```

### Dataset
Antes de executar o script, baixe o <a href="https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017">Dataset</a>.

### Pré-reqs
- __Python 3:__ Ter o Python 3 instalado;
- __Pycountry:__ pip3 install pycountry

### Como utilizar o script
python3 --dataset dataset.csv
