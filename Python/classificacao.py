import pandas as pd

canditatos = """
10011661, Abel Batista Ribeiro, 12.00, 28.00, 40.00 / 10012278, Abelardo Rufino Barges Neto, 11.00,
60.00, 71.00 / 10002481, Abner Ribeiro Negrao, 13.00, 62.00, 75.00 / 10009386, Abner Silva, 9.00, 24.00,
33.00 / 10011748, Abraao do Nascimento Juca, 6.00, 26.00, 32.00 / 10010659, Abraao Pereira Lacerda,
12.00, 46.00, 58.00 / 10001621, Ackton Stive Candido Stevanelli, 12.00, 58.00, 70.00 / 10005557, Acsa
Gabriely da Silva Barros, 10.00, 44.00, 54.00 / 10008198, Adailton Braga Viana, 4.00, 22.00, 26.00 /
10011740, Adailton dos Santos Betcel Vasconcelos, 15.00, 40.00, 55.00 / 10005384, Adam Jose Tavares
Bastos, 13.00, 54.00, 67.00 / 10001033, Adam Silva Costa, 11.00, 38.00, 49.00 / 10011741, Adamara da
Silva Ferro Miranda, 10.00, 34.00, 44.00 / 10007155, Adauane Alves Belfort, 4.00, 38.00, 42.00 /
10002375, Adauto Carlos Pereira Vasconcelos, 14.00, 62.00, 76.00 / 10002939, Adaylton Santos da Costa,
8.00, 38.00, 46.00 / 10000617, Adeblonio Oliveira Dias, 11.00, 54.00, 65.00 / 10001468, Adeilton da Silva
de Aquino, 7.00, 64.00, 71.00 / 10002295, Adelino Amancio dos Reis Neto, 8.00, 50.00, 58.00 / 10011566,
Ademar Ferreira Evangelista, 14.00, 50.00, 64.00 / 10001547, Adenilce Sena dos Santos, 9.00, 40.00, 49.00
/ 10013418, Adercio Lima Rabelo, 7.00, 32.00, 39.00 / 10010350, Adila Pereira Nascimento Moraes, 12.00,
64.00, 76.00 / 10008189, Adley Rubens Rodrigues dos Santos, 9.00, 48.00, 57.00 / 10000181, Admir do
Couto Costa, 5.00, 38.00, 43.00 / 10002473, Adnilton de Sousa Paiva, 7.00, 38.00, 45.00 / 10000041,
Adrian Caldas Po, 9.00, 46.00, 55.00 / 10001932, Adriana Fatima Godot Pinheiro de Souza, 7.00, 28.00,
35.00 / 10002916, Adriana Ferreira Rabelo, 15.00, 58.00, 73.00 / 10013294, Adriana Oliveira dos Santos,
14.00, 48.00, 62.00 / 10011862, Adriana Sousa Ferreira, 8.00, 40.00, 48.00 / 10016086, Adriana Teixeira
Sacco, 7.00, 32.00, 39.00 / 10002607, Adriane Balieiro dos Santos, 3.00, 22.00, 25.00 / 10002885, Adriane
Gomes Dolzane, 13.00, 60.00, 73.00 / 10013221, Adriano Cesar Franco Cardoso, 11.00, 46.00, 57.00 /
10011726, Adriano de Moraes Barros, 12.00, 60.00, 72.00 / 10013459, Adriano Denizard Brito Pinheiro,
11.00, 38.00, 49.00 / 10000901, Adriano do Nascimento Feitosa, 11.00, 48.00, 59.00 / 10016197, Adriano
Ferreira de Souza, 9.00, 26.00, 35.00 / 10010097, Adriano Loureiro dos Santos, 13.00, 60.00, 73.00 /
10002506, Adriano Maia Monteiro, 11.00, 58.00, 69.00 / 10002495, Adriano Mesquita Chagas, 10.00,
34.00, 44.00 / 10007923, Adriano Pereira Carneiro, 9.00, 36.00, 45.00 / 10005626, Adriano Ramon de
Castro Silva, 6.00, 44.00, 50.00 / 10015915, Adriany da Silva Castro, 9.00, 56.00, 65.00 / 10000479, Adriel
Martins Noleto, 9.00, 42.00, 51.00 / 10005347, Adriel Quesede de Oliveira Pereira, 14.00, 64.00, 78.00 /
10001977, Adriel Roberto Vitelli da Silva, 6.00, 32.00, 38.00 / 10000253, Adriele do Socorro Barroso de
Moraes, 8.00, 58.00, 66.00 / 10006991, Adriele Gomes de Oliveira, 8.00, 46.00, 54.00 / 10010979, Adriele
Silva da Veiga, 7.00, 40.00, 47.00 / 10013161, Adriely Cristiny Barbosa Maciel, 10.00, 56.00, 66.00 /
10000289, Adrina Malcher de Oliveira, 10.00, 60.00, 70.00 / 10003038, Adryelle Schleiden Costa da Silva,
8.00, 48.00, 56.00 / 10016025, Adson Sousa de Lima, 9.00, 30.00, 39.00 / 10001448, Agatha Macambira
Monte de Lima, 17.00, 64.00, 81.00 / 10008167, Agnaldo Luis Castro Lopes, 10.00, 54.00, 64.00 /
10009331, Agta da Silva Barros, 7.00, 24.00, 31.00 / 10011878, Aias de Paula da Silva, 5.00, 50.00, 55.00
/ 10011054, Ailime Suianne Lisboa e Silva, 8.00, 46.00, 54.00 / 10009400, Ailyme Thanara Ribeiro Dias,
5.00, 26.00, 31.00 / 10005309, Ajax da Paixao Santos Filho, 9.00, 34.00, 43.00 / 10006714, Alailson Aguiar
Ribeiro Junior, 10.00, 50.00, 60.00 / 10012540, Alan Batista Costa, 5.00, 38.00, 43.00 / 10010869, Alan
 
Caio Rodrigues Pimenta, 8.00, 30.00, 38.00 / 10001509, Alan da Silva Tavares, 12.00, 66.00, 78.00 /
10016188, Alan dos Santos Souza, 10.00, 32.00, 42.00 / 10000348, Alan Jose Araujo Evangelista, 12.00,
62.00, 74.00 / 10003194, Alan Jose de Jesus Silva, 9.00, 34.00, 43.00 / 10010261, Alan Kayky Guedes
Cardoso, 14.00, 40.00, 54.00 / 10010436, Alan Kelvin dos Santos Rosas, 1.00, 24.00, 25.00 / 10010525,
Alan Lucas Alves Costa, 7.00, 54.00, 61.00 / 10013517, Alan Santos Farias, 9.00, 48.00, 57.00 / 10009495,
Alana Assiria Gaia Sassim, 6.00, 34.00, 40.00 / 10011256, Alana Carvalho Silva, 11.00, 56.00, 67.00 /
10010700, Alana Coelho Lima, 7.00, 68.00, 75.00 / 10011715, Alana Farias Santos, 15.00, 66.00, 81.00 /
10001342, Alana Gabriela Costa Freitas, 7.00, 52.00, 59.00 / 10010454, Alana Kallyne Coimbra da Silva,
10.00, 44.00, 54.00 / 10001976, Alanna Karolaine da Silva Moraes, 15.00, 64.00, 79.00 / 10012004, Alaor
da Silva Lima Neto, 9.00, 42.00, 51.00 / 10009673, Alayn Daniel Bitencourt Alexandre, 9.00, 46.00, 55.00
/ 10005247, Albergio Fabricio da Silva, 12.00, 68.00, 80.00 / 10013293, Albert Ramos Freitas, 11.00,
48.00, 59.00 / 10002727, Alberth Matheus Clementino Cruz, 9.00, 56.00, 65.00 / 10012177, Alcimar
Freitas de Oliveira Neto, 12.00, 64.00, 76.00 / 10005436, Alcimara de Sousa Lima, 10.00, 52.00, 62.00 /
10003073, Alcineia Lobato Viana, 14.00, 34.00, 48.00 / 10011363, Alcy Augusto Diniz da Silva, 8.00,
32.00, 40.00 / 10016118, Aldair Junior Franco da Conceicao, 8.00, 40.00, 48.00 / 10012227, Alderlaine
Samanta Ferreira do Nascimento, 7.00, 48.00, 55.00 / 10002042, Aldicelio Farias de Oliveira, 13.00, 66.00,
79.00 / 10005761, Aldo Victor Alves Venceslau, 15.00, 66.00, 81.00 / 10016374, Aleciany de Fatima
Pereira de Lima, 3.00, 26.00, 29.00 / 10000129, Alef Yann de Sousa Pinheiro, 9.00, 52.00, 61.00 /
10015950, Alefe Sam Correa Castro da Silva, 9.00, 38.00, 47.00 / 10012873, Alefy Cristiam Reis Narciso,
9.00, 44.00, 53.00 / 10010427, Alesandro Matos Pampolha, 10.00, 48.00, 58.00 / 10011455, Alessa Dafny
Ferreira Cardoso, 9.00, 18.00, 27.00 / 10000268, Alessandra Barbosa Pinheiro, 12.00, 68.00, 80.00 /
10005340, Alessandra Gomes Ramos Machado, 13.00, 66.00, 79.00 / 10016290, Alessandra Mendonca
Reis, 8.00, 44.00, 52.00 / 10001758, Alessandra Silva dos Santos, 8.00, 30.00, 38.00 / 10016791,
Alessandra Thais Ribeiro Sousa, 7.00, 40.00, 47.00 / 10005350, Alessandra Yakushiji Fonteles, 3.00, 22.00,
25.00 / 10000065, Alessandro do Carmo Cromwell, 12.00, 56.00, 68.00 / 10010618, Alessandro Jonhnath
Borges Lopes, 9.00, 42.00, 51.00 / 10005259, Alessandro Wenderson Lima Alexandre, 9.00, 48.00, 57.00
/ 10011767, Alessandro Willian Dias Teles, 9.00, 44.00, 53.00 / 10000214, Alex Bruno Nunes Flores, 7.00,
34.00, 41.00 / 10004206, Alex da Conceicao Silva Fonseca, 10.00, 42.00, 52.00 / 10012397, Alex da Silva
Souza, 8.00, 48.00, 56.00 / 10012603, Alex Junior Sousa Duarte, 6.00, 52.00, 58.00 / 10001379, Alex
Magalhaes Pereira, 12.00, 62.00, 74.00 / 10011734, Alex Silva de Oliveira, 9.00, 56.00, 65.00 / 10007066,
Alex Victor Cunha Negidio, 12.00, 54.00, 66.00 / 10015727, Alexander Kyushima, 7.00, 34.00, 41.00 /
10012101, Alexander Santana Alcantara, 7.00, 46.00, 53.00 / 10011202, Alexandra Rodrigues Goncalves,
12.00, 50.00, 62.00 / 10007938, Alexandre Azevedo Aragao, 8.00, 28.00, 36.00 / 10009321, Alexandre
Borges de Souza, 9.00, 54.00, 63.00 / 10012535, Alexandre Bruno Grube Freitas, 8.00, 38.00, 46.00 /
10000434, Alexandre Carneiro Pinheiro, 6.00, 42.00, 48.00 / 10013609, Alexandre de Lucca Veras Gomes,
7.00, 24.00, 31.00 / 10013411, Alexandre Lima Ferreira, 13.00, 42.00, 55.00 / 10013092, Alexandre Naoto
Yamazaki da Silva, 17.00, 58.00, 75.00 / 10013114, Alexandre Neto Pinheiro Morais, 11.00, 44.00, 55.00
/ 10007408, Alexandrina Schusterschitz Silva, 7.00, 40.00, 47.00 / 10016919, Alexia Alho Fuziel, 6.00,
30.00, 36.00 / 10008228, Alexia Rodrigues dos Santos, 12.00, 62.00, 74.00 / 10001752, Alexsand
Nascimento Ferreira, 8.00, 40.00, 48.00 / 10006760, Alexsander Oliveira D Sousa Costa, 14.00, 60.00,
74.00 / 10012218, Alexsandy Wevany de Castro Araujo, 9.00, 32.00, 41.00 / 10001787, Alfeu Silva de
Souza, 11.00, 56.00, 67.00 / 10005269, Ali Hussein Yassine, 10.00, 44.00, 54.00 / 10012524, Alice Barbosa
Guerreiro dos Santos, 8.00, 22.00, 30.00 / 10016218, Alice Rocha da Conceicao, 5.00, 22.00, 27.00 /
10000584, Alice Vilhena do Couto, 8.00, 28.00, 36.00 / 10005245, Alicia Ferreira dos Santos, 9.00, 46.00,
55.00 / 10000892, Alicia Hellen Sousa Oliveira, 11.00, 54.00, 65.00 / 10013404, Alicio Victor Machado
Amaral, 14.00, 64.00, 78.00 / 10010102, Aline Costa Silva, 12.00, 24.00, 36.00 / 10010487, Aline Farias
da Costa, 8.00, 48.00, 56.00 / 10009535, Aline Handara Lacerda da Silva, 2.00, 28.00, 30.00 / 10005303,
Aline Larliany Moraes Martins, 7.00, 42.00, 49.00 / 10007128, Aline Lima de Sousa, 6.00, 16.00, 22.00 /
10007995, Aline Naiara Sousa do Carmo, 18.00, 60.00, 78.00 / 10011814, Aline Ribeiro Aragao, 10.00,
52.00, 62.00 / 10001215, Aline Sobrinho de Medeiros, 8.00, 40.00, 48.00 / 10005215, Aline Stephane dos
Santos Barbosa, 9.00, 28.00, 37.00 / 10010627, Aline Szaubram, 15.00, 48.00, 63.00 / 10007566, Aline
Torres Escudeiro, 13.00, 46.00, 59.00 / 10006818, Aline Vanessa Silva Pinto, 6.00, 42.00, 48.00 /
 
10012151, Aline Xavier Oliveira, 7.00, 24.00, 31.00 / 10007883, Alinna Cunha Leite, 14.00, 44.00, 58.00
/ 10010494, Alison da Silva de Jesus, 12.00, 42.00, 54.00 / 10016904, Alison Victor Santos Mendes, 11.00,
12.00, 23.00 / 10011016, Alisson Oliveira Leite, 12.00, 38.00, 50.00 / 10005445, Alisson Rodrigo
Paraguacu de Oliveira, 9.00, 46.00, 55.00 / 10015889, Allan Cassio Pereira Baia de Almeida, 11.00, 58.00,
69.00 / 10012765, Allan Freitas Moreira, 9.00, 54.00, 63.00 / 10002815, Allan Jose Santana Costa, 8.00,
52.00, 60.00 / 10005469, Allan Patrick Batista de Oliveira, 9.00, 54.00, 63.00 / 10001017, Allan Rafael
Sousa Conde, 12.00, 42.00, 54.00 / 10001798, Allan Victor Siqueira Campos da Silva, 13.00, 52.00, 65.00
/ 10013193, Allanis Cardoso Araujo, 6.00, 26.00, 32.00 / 10000872, Allef Aguiar Diniz, 9.00, 42.00, 51.00
/ 10013475, Allex Lima da Silva, 14.00, 42.00, 56.00 / 10003176, Allisson Patrick Silva Ferreira, 11.00,
68.00, 79.00 / 10001322, Allisson Sequeira Campos da Silva, 7.00, 50.00, 57.00 / 10000736, Allycia Araujo
Jovelino, 9.00, 46.00, 55.00 / 10002638, Almiqueias Melo da Silva, 14.00, 40.00, 54.00 / 10011615,
Alrivan dos Santos Pereira, 9.00, 40.00, 49.00 / 10013143, Alvaro Augusto Soares Pontes, 13.00, 44.00,
57.00 / 10007667, Alvaro Freitas Pereira Filho, 7.00, 30.00, 37.00 / 10012602, Alvaro Henrique Seabra de
Freitas, 9.00, 64.00, 73.00 / 10009280, Alwyma Campos Amaral, 14.00, 58.00, 72.00 / 10016231, Alysson
Julio Ferreira Sousa, 6.00, 26.00, 32.00 / 10012411, Amanda Alves Gomes da Silva, 7.00, 34.00, 41.00 /
10000231, Amanda Araujo de Azevedo, 10.00, 30.00, 40.00 / 10015794, Amanda Coimbra Coelho, 11.00,
40.00, 51.00 / 10007814, Amanda Cristina Brito Machado, 9.00, 40.00, 49.00 / 10013530, Amanda Cristina
Vieira Martins, 8.00, 30.00, 38.00 / 10010012, Amanda Cristinny Martins Alves, 5.00, 30.00, 35.00 /
10007685, Amanda da Silva Oeiras Sousa, 9.00, 28.00, 37.00 / 10000697, Amanda da Silva Pinheiro, 12.00,
66.00, 78.00 / 10012925, Amanda Ferreira Silva, 10.00, 30.00, 40.00 / 10012454, Amanda Gabriela Gomes
Palheta, 13.00, 36.00, 49.00 / 10000916, Amanda Gomes Barreira, 10.00, 48.00, 58.00 / 10000705, Amanda Jaqueline Monteiro Santos Pereira, 0.00, 24.00, 24.00 / 10007035, Amanda Leticia Panagio de Carvalho, 8.00, 44.00, 52.00 / 10011924, Amanda Lima de Oliveira, 11.00, 50.00, 61.00 / 10005717, Amanda Luiza
Rosa dos Santos, 6.00, 40.00, 46.00 / 10007863, Amanda Maria de Almeida Nunes, 13.00, 52.00, 65.00 /
10000257, Amanda Moreno de Jesus, 12.00, 62.00, 74.00 / 10002184, Amanda Pequeno de Brito, 4.00,
40.00, 44.00 / 10007845, Amanda Priscila Soares Azevedo, 11.00, 54.00, 65.00 / 10002651, Amanda
Renata Silva Bastos, 9.00, 36.00, 45.00 / 10010260, Amanda Rios de Oliveira, 9.00, 30.00, 39.00 /
10011699, Amanda Samela da Silva Goncalves, 9.00, 64.00, 73.00 / 10015743, Amanda Sarges Garcia,
7.00, 38.00, 45.00 / 10000957, Amanda Travassos da Silva, 5.00, 36.00, 41.00 / 10005767, Amanda Vitoria
de Sousa Victor, 10.00, 40.00, 50.00 / 10002380, Amandah Kalita do Nascimento Cirqueira, 10.00, 42.00,
52.00 / 10012956, Amando de Oliveira Beserra, 6.00, 36.00, 42.00 / 10011565, Amayna Beatriz Neves
Farias Dantas da Cunha, 15.00, 68.00, 83.00 / 10015766, Amilton Alvares da Fonseca Junior, 9.00, 52.00,
61.00 / 10000416, Ammanda Miranda Cruz, 8.00, 24.00, 32.00 / 10007033, Amos do Vale Morais, 12.00,
56.00, 68.00 / 10012369, Ana Alyne Santana do Carmo, 5.00, 24.00, 29.00 / 10013237, Ana Barbara Bentes
Rodrigues, 12.00, 44.00, 56.00 / 10015804, Ana Beatriz Dias dos Santos, 11.00, 22.00, 33.00 / 10005620,
Ana Carla Cunha Lobato, 8.00, 52.00, 60.00 / 10013450, Ana Carla Figueira Maia, 7.00, 14.00, 21.00 /
10012761, Ana Carla Moreira Santos, 12.00, 60.00, 72.00 / 10013044, Ana Carolina, 11.00, 22.00, 33.00 /
10010829, Ana Carolina Cavalcante da Silva, 11.00, 62.00, 73.00 / 10010276, Ana Carolina da Silva
Mendonca Scienza, 14.00, 58.00, 72.00 / 10000980, Ana Carolina de Sousa Moreira Raposo Seba, 14.00,
70.00, 84.00 / 10001091, Ana Carolina Ereiro Pereira, 10.00, 34.00, 44.00 / 10010741, Ana Carolina Lobato
Oliveira, 11.00, 42.00, 53.00 / 10002798, Ana Carolina Medeiros de Moura, 10.00, 62.00, 72.00 /
10007927, Ana Carolina Santana Chaves, 12.00, 50.00, 62.00 / 10016454, Ana Carolina Santos de Souza,
8.00, 44.00, 52.00 / 10002864, Ana Carolina Saraiva de Oliveira Vieira, 11.00, 58.00, 69.00 / 10002214,
Ana Carolina Silva da Silva, 8.00, 48.00, 56.00 / 10003111, Ana Carolina Silva Tenreiro Lima, 14.00,
52.00, 66.00 / 10009726, Ana Carolina Souza da Silva, 7.00, 20.00, 27.00 / 10011729, Ana Caroline
Almeida Ferreira, 10.00, 36.00, 46.00 / 10012800, Ana Caroline Alves Paier, 11.00, 36.00, 47.00 /
10013576, Ana Caroline Martins Maciel, 10.00, 50.00, 60.00 / 10001235, Ana Caroline Parente Bahia de
Souza, 10.00, 46.00, 56.00 / 10017002, Ana Caroline Pereira Araujo, 7.00, 22.00, 29.00 / 10016391, Ana
Caroline Santos Costa, 10.00, 46.00, 56.00 / 10010696, Ana Carolyne de Azevedo Correa, 6.00, 38.00,
44.00 / 10001960, Ana Catarina Mota Pereira, 10.00, 24.00, 34.00 / 10013280, Ana Clara da Silva Melo,
14.00, 56.00, 70.00 / 10016141, Ana Clara de Vasconcelos Kanegae, 11.00, 46.00, 57.00 / 10000606, Ana
Clara Farias Barata, 10.00, 24.00, 34.00 / 10011144, Ana Clara Santiago Silva Lima, 17.00, 60.00, 77.00 /
 
10016063, Ana Claudia Neves de Jesus Pimentel, 9.00, 28.00, 37.00 / 10012161, Ana Cristina Cardoso
Soares, 9.00, 38.00, 47.00 / 10000392, Ana Cristina de Oliveira Moreira, 11.00, 46.00, 57.00 / 10000235,
Ana Elisa Medeiros Castro, 6.00, 18.00, 24.00 / 10016142, Ana Flavia Fonseca de Queiroz, 8.00, 40.00,
48.00 / 10010229, Ana Flavia Passos Maia, 10.00, 46.00, 56.00 / 10013380, Ana Gabriela Mesquita Silva,
13.00, 52.00, 65.00 / 10002982, Ana Gabriella Pinheiro Barbosa da Costa, 10.00, 48.00, 58.00 / 10012199,
Ana Izele de Deus Sousa, 6.00, 40.00, 46.00 / 10016240, Ana Karina Ramos Monteiro, 6.00, 20.00, 26.00
/ 10013188, Ana Kariny Viana Fernandes, 7.00, 24.00, 31.00 / 10010907, Ana Karoline Conceicao
Rodrigues, 10.00, 52.00, 62.00 / 10001077, Ana Karoline dos Santos Lemos, 7.00, 26.00, 33.00 / 10009447,
Ana Karolynne Silva Duarte, 7.00, 42.00, 49.00 / 10013255, Ana Kelly Pimentel Gomes, 9.00, 38.00, 47.00
/ 10000659, Ana Kemlly Andrade Monteiro, 11.00, 48.00, 59.00 / 10010432, Ana Larissa Santiago de
Lima, 7.00, 38.00, 45.00 / 10012697, Ana Laura Moncao Miranda, 11.00, 52.00, 63.00 / 10010994, Ana
Laura Silva Gemaque, 13.00, 48.00, 61.00 / 10016582, Ana Leticia Gomes Carvalho Lima, 13.00, 44.00,
57.00 / 10000021, Ana Luisa Brabo Soares, 14.00, 66.00, 80.00 / 10001377, Ana Luiza Lino Santos, 8.00,
30.00, 38.00 / 10002195, Ana Manoela Piedade Pinheiro, 11.00, 42.00, 53.00 / 10008234, Ana Maria Braga
Cordeiro Castro, 7.00, 24.00, 31.00 / 10008230, Ana Maria Oliveira da Silva, 6.00, 20.00, 26.00 /
10002211, Ana Mirlene dos Santos Fiel, 11.00, 52.00, 63.00 / 10012643, Ana Paula Correa do Nascimento,
5.00, 38.00, 43.00 / 10016207, Ana Paula Fonteles Santos, 12.00, 42.00, 54.00 / 10012302, Ana Paula Lima
Monteiro, 11.00, 46.00, 57.00 / 10001919, Ana Paula Miranda Viana, 9.00, 20.00, 29.00 / 10012950, Ana
Paula Moraes Mesquita, 5.00, 32.00, 37.00 / 10001111, Ana Paula Pereira Lucas, 12.00, 50.00, 62.00 /
10002581, Ana Paula Ramos Silva, 10.00, 38.00, 48.00 / 10012429, Ana Paula Sampaio de Sousa, 13.00,
62.00, 75.00 / 10015967, Ana Paula Santos de Lima, 11.00, 52.00, 63.00 / 10012777, Ana Paula Santos
Monteiro, 9.00, 28.00, 37.00 / 10000092, Ana Paula Soares Coelho, 8.00, 32.00, 40.00 / 10010395, Ana
Paula Souza Leite, 3.00, 38.00, 41.00 / 10010780, Ana Rafaela Mesquita Silva, 8.00, 36.00, 44.00 /
10001293, Ana Rebeca Rodrigues Pereira, 9.00, 42.00, 51.00 / 10006969, Ana Rosa da Costa Bronze,
10.00, 54.00, 64.00 / 10011328, Ana Thalia da Silva Vitor Soares Diniz, 14.00, 56.00, 70.00 / 10010035,
Ana Victoria Sousa da Silva, 11.00, 42.00, 53.00 / 10011271, Ana Vitoria de Sousa Oliveira, 12.00, 58.00,
70.00 / 10010647, Ananda Carla dos Santos Costa, 10.00, 66.00, 76.00 / 10016315, Ananda Cordeiro do
Santos, 10.00, 38.00, 48.00 / 10006901, Ananda Cris di Tomaso Santos Pereira, 13.00, 54.00, 67.00 /
10005343, Ananda Pinheiro das Candeia, 10.00, 44.00, 54.00 / 10012646, Ananda Sousa dos Santos, 12.00,
40.00, 52.00 / 10003138, Anderlan Canuto Machado, 10.00, 54.00, 64.00 / 10009624, Anderley da S Leao,
9.00, 60.00, 69.00 / 10012170, Anderson de Jesus Fonseca, 9.00, 34.00, 43.00 / 10007985, Anderson de
Oliveira Teixeira, 10.00, 38.00, 48.00 / 10006698, Anderson Denis Andrade de Sousa, 15.00, 64.00, 79.00
/ 10012165, Anderson Farias de Brito, 9.00, 42.00, 51.00 / 10008203, Anderson Felipe Nunes Pereira,
15.00, 62.00, 77.00 / 10010385, Anderson Lima da Silva, 14.00, 56.00, 70.00 / 10000196, Anderson Lima
e Silva, 9.00, 56.00, 65.00 / 10005716, Anderson Rodrigo Brito de Souza, 4.00, 34.00, 38.00 / 10016492,
Anderson Rodrigues Caminha, 9.00, 30.00, 39.00 / 10000393, Anderson Silva Cunha, 10.00, 44.00, 54.00
/ 10009503, Anderson Soares Brandao Ribeiro, 13.00, 56.00, 69.00 / 10009585, Andre Arnobio Pinheiro
Brito, 12.00, 62.00, 74.00 / 10016333, Andre de Souza Silva, 12.00, 62.00, 74.00 / 10010925, Andre dos
Santos Rodrigues, 12.00, 48.00, 60.00 / 10009621, Andre Felipe Felix Ulisses Morais, 12.00, 56.00, 68.00
/ 10015941, Andre Henrique Goncalves Miranda, 7.00, 32.00, 39.00 / 10000388, Andre Lima de Souza,
10.00, 66.00, 76.00 / 10011490, Andre Luis de Paula, 9.00, 48.00, 57.00 / 10011444, Andre Luis Pereira
Teixeira, 5.00, 36.00, 41.00 / 10013723, Andre Luis Ramos Maciel, 5.00, 24.00, 29.00 / 10011939, Andre
Luiz Casanova de Amorim, 12.00, 54.00, 66.00 / 10000369, Andre Luiz Costa dos Santos, 13.00, 30.00,
43.00 / 10003060, Andre Luiz Gomes Lopes, 15.00, 56.00, 71.00 / 10016348, Andre Parente da Silva, 5.00,
20.00, 25.00 / 10000039, Andre Pinheir Martins, 5.00, 46.00, 51.00 / 10005488, Andre Ricardo Pedroso de
Sousa, 9.00, 60.00, 69.00 / 10011817, Andre Salim Paz Guedes, 9.00, 42.00, 51.00 / 10000262, Andre
Victor Antonio Jose dos Santos, 10.00, 40.00, 50.00 / 10011988, Andre Victor Silva de Araujo, 8.00, 32.00,
40.00 / 10007677, Andrea Soares Ribeiro, 9.00, 40.00, 49.00 / 10012572, Andrei Kanchelskis Pereira
Fonseca, 12.00, 54.00, 66.00 / 10010984, Andrelma Neves Martins, 10.00, 50.00, 60.00 / 10012928,
Andressa Caroline de Freitas Pinho, 10.00, 62.00, 72.00 / 10016061, Andressa Ferreira Reis, 6.00, 48.00,
54.00 / 10007882, Andrew Costa Pinheiro, 9.00, 52.00, 61.00 / 10013420, Andrew Kaua da Silva Benicio,
11.00, 34.00, 45.00 / 10011964, Andrew Lucas Leal Dias, 11.00, 38.00, 49.00 / 10016647, Andrew Lucca
 
Pantoja de Souza, 11.00, 44.00, 55.00 / 10000691, Andrey Barros de Alencar, 15.00, 68.00, 83.00 /
10009357, Andrey Cereja Oliveira Rodrigues, 9.00, 52.00, 61.00 / 10010377, Andrey Levi Oliveira de
Lima, 7.00, 28.00, 35.00 / 10000071, Andrey Ruan de Moraes Sampaio, 9.00, 48.00, 57.00 / 10002023,
Andrey Siqueira Savino, 12.00, 62.00, 74.00 / 10010919, Andreza Beatriz Rodrigues de Figueiredo, 13.00,
60.00, 73.00 / 10009573, Andreza Goncalves Lima, 13.00, 40.00, 53.00 / 10016265, Andreza Karoliny
Ferreira Goncalves, 11.00, 42.00, 53.00 / 10016532, Andreza Viana Souza, 12.00, 38.00, 50.00 / 10010990, Andrezza Ketterine Juca da Silva, 10.00, 40.00, 50.00 / 10012229, Andson Cordeiro da Silva Barbosa, 11.00, 48.00, 59.00 / 10012904, Ane Caroline Cabral Ribeiro, 12.00, 28.00, 40.00 / 10013060, Ane Cecilia
Costa Batista, 11.00, 48.00, 59.00 / 10000703, Angel Santos dos Santos, 8.00, 48.00, 56.00 / 10013468,
Angela Calandrini Fulco, 9.00, 34.00, 43.00 / 10015884, Angela Maria Dantas da Costa, 4.00, 18.00, 22.00
/ 10007077, Angelica Joana Alves de Sousa, 9.00, 48.00, 57.00 / 10009325, Angelica Marrie Maciel de
Souza, 11.00, 72.00, 83.00 / 10002780, Angelo Brandao Dolzane, 12.00, 56.00, 68.00 / 10000573, Angelo
Marcos Bordalo da Silva, 11.00, 44.00, 55.00 / 10010498, Anibal Fernandes de Carvalho, 8.00, 22.00,
30.00 / 10002941, Anibal Teixeira Fonseca, 10.00, 46.00, 56.00 / 10000191, Anna Beatriz Cavalcante
Nobrega Silva, 13.00, 58.00, 71.00 / 10016147, Anna Carolina de Moura Epaminondas, 7.00, 26.00, 33.00
/ 10012487, Anna Carolina Silva Abreu, 6.00, 28.00, 34.00 / 10005733, Anna Clara Silva Ramos, 16.00,
34.00, 50.00 / 10012451, Anna Clara Soares Palheta, 11.00, 48.00, 59.00 / 10001426, Anna Karolyna Silva
de Aguiar Ledo, 16.00, 58.00, 74.00 / 10001727, Anna Luiza Correa dos Santos, 7.00, 46.00, 53.00 /
10003052, Anna Maria dos Santos Soares, 7.00, 28.00, 35.00 / 10007538, Anna Vitoria Araujo Sousa,
12.00, 50.00, 62.00 / 10013520, Annanda Eileen Aguiar da Silva, 15.00, 56.00, 71.00 / 10000322, Anne
Brenda Maciel dos Santos, 8.00, 36.00, 44.00 / 10012114, Anne Hellen Barbosa de Oliveira, 7.00, 38.00,
45.00 / 10003025, Annie Julliete Rodrigues de Sousa e Souza, 8.00, 42.00, 50.00 / 10011706, Anny
Carolina Barros Oliveira, 10.00, 40.00, 50.00 / 10013497, Anny Caroline Ribeiro Arouxa, 12.00, 62.00,
74.00 / 10011273, Anthony Paulo de Souza Monteiro, 13.00, 54.00, 67.00 / 10011892, Antonia Giane de
Sousa Pires, 12.00, 48.00, 60.00 / 10000721, Antonia Janyelle dos Santos Felix, 14.00, 66.00, 80.00 /
10016005, Antonia Jhelie Silva Amaro, 8.00, 34.00, 42.00 / 10016515, Antonia Julliheny Sousa Silva, 8.00,
26.00, 34.00 / 10010294, Antonio Danilo de Carvalho Teixeira, 12.00, 50.00, 62.00 / 10000898, Antonio
Edivan dos Santos Moreira, 7.00, 30.00, 37.00 / 10009300, Antonio Ednaldo Silva Rocha, 8.00, 48.00,
56.00 / 10014718, Antonio Eduardo Moraes Sampaio, 12.00, 42.00, 54.00 / 10008186, Antonio Evandro
de Oliveira Brito Junior, 8.00, 48.00, 56.00 / 10000028, Antonio Felipe Silva Farias, 7.00, 58.00, 65.00 /
10010698, Antonio Francielton Gomes dos Santos, 6.00, 26.00, 32.00 / 10010750, Antonio Francisco do
Nascimento Filho, 9.00, 64.00, 73.00 / 10002575, Antonio Francisco Ferreira de Lima Sousa, 9.00, 46.00,
55.00 / 10012682, Antonio Franco Sardo Leao Neto, 7.00, 28.00, 35.00 / 10016367, Antonio Galden Silva
da Conceicao, 8.00, 42.00, 50.00 / 10009471, Antonio Jonaelson de Sousa Paiva, 9.00, 66.00, 75.00 /
10016866, Antonio Lucas Nacif Sirotheau Rodrigues, 9.00, 38.00, 47.00 / 10012373, Antonio Lucas
Santiago Bittencourt dos Santos, 10.00, 48.00, 58.00 / 10009529, Antonio Marcio da Costa Rocha, 11.00,
50.00, 61.00 / 10013246, Antonio Marcos Andrade Sousa Alves, 6.00, 42.00, 48.00 / 10002243, Antonio
Marcos Moraes Cardoso, 10.00, 54.00, 64.00 / 10006817, Antonio Matheus Sardinha Santos, 15.00, 58.00,
73.00 / 10001164, Antonio Moreira Lima Filho, 11.00, 42.00, 53.00 / 10002091, Antonio Rafael Silva
Correa, 5.00, 42.00, 47.00 / 10002656, Antonio Robson Nobre Farias, 8.00, 42.00, 50.00 / 10010651,
Antonio Sammy Costa Neves, 10.00, 54.00, 64.00 / 10007026, Antonio Wairan da Silva Ferreira, 11.00,
58.00, 69.00 / 10005766, Antonio Winicius de Melo Rodrigues, 9.00, 38.00, 47.00 / 10000016, Antonio
Zito Severino Costa Junior, 13.00, 62.00, 75.00 / 10015933, Antony Gabriel dos Santos Pastana, 9.00,
58.00, 67.00 / 10011793, Aprigio Pereira do Nascimento Junior, 8.00, 58.00, 66.00 / 10000695, Arella
Cristhine Cardoso Viana, 9.00, 60.00, 69.00 / 10016593, Arethuza Magno Borges Trindade, 8.00, 38.00,
46.00 / 10011750, Ariadna Jordana Rodrigues Albuquerque Gomes, 7.00, 28.00, 35.00 / 10001596, Arian
Magalhaes de Souza, 8.00, 30.00, 38.00 / 10013019, Ariana Carla Martins Favacho, 5.00, 32.00, 37.00 /
10017023, Ariane Barbosa Alves, 8.00, 28.00, 36.00 / 10000394, Ariane da Silva Ferreira, 10.00, 26.00,
36.00 / 10010262, Ariane Figueiredo Baia, 10.00, 42.00, 52.00 / 10000777, Ariane Pinto Alves, 11.00,
46.00, 57.00 / 10002820, Ariel Correa de Cerqueira, 10.00, 52.00, 62.00 / 10007961, Ariel Henrique Dias
de Castro, 11.00, 36.00, 47.00 / 10009384, Ariene de Sousa de Almeida, 8.00, 36.00, 44.00 / 10000043,
Arilson Luis Pontes da Rosa, 6.00, 38.00, 44.00 / 10011990, Arinaldo Alves, 10.00, 46.00, 56.00 /
 
10000734, Ariolino Ferreira da Costa Neto, 13.00, 52.00, 65.00 / 10002806, Arivaldo dos Santos Pastana,
15.00, 64.00, 79.00 / 10012830, Arlan Pereira Coelho, 11.00, 40.00, 51.00 / 10009254, Arleison Glauber
Pinheiro Sousa, 7.00, 38.00, 45.00 / 10002948, Arley Taffarel Arruda Marques, 7.00, 46.00, 53.00 /
10001411, Arlisson Silva Cunha, 8.00, 44.00, 52.00 / 10011287, Armando Neto Vasconcelos Pinto, 9.00,
32.00, 41.00 / 10000668, Arnaldo Caetano Tome Junior, 10.00, 38.00, 48.00 / 10015783, Arnaldo
Rodrigues Marvao Junior, 6.00, 42.00, 48.00 / 10013062, Arnold Willian Lopes de Souza, 7.00, 24.00,
31.00 / 10012110, Arnowdhy Hudson Saraiva Silva, 14.00, 34.00, 48.00 / 10009698, Artemise Oliveira de
Araujo, 8.00, 36.00, 44.00 / 10011433, Arthur Andrey Viana da Cunha, 9.00, 34.00, 43.00 / 10000228,
Arthur da Costa Vieira, 15.00, 60.00, 75.00 / 10016196, Arthur Dornelas Nascimento, 7.00, 26.00, 33.00 /
10007591, Arthur Durval Dantas da Cunha, 9.00, 62.00, 71.00 / 10006779, Arthur Felipe de Oliveira
Martins, 10.00, 42.00, 52.00 / 10007345, Arthur Felipe Souza Gomes, 10.00, 58.00, 68.00 / 10011507,
Arthur Fernandes dos Santos, 11.00, 44.00, 55.00 / 10007304, Arthur Gomes Salles, 15.00, 64.00, 79.00 /
10012601, Arthur Guilherme Pimentel Lindoso, 11.00, 52.00, 63.00 / 10001821, Arthur Matheus Melo
Alves, 9.00, 30.00, 39.00 / 10012508, Arthur Pazinato Donatti, 16.00, 66.00, 82.00 / 10013398, Arthur
Ramos Duarte, 9.00, 36.00, 45.00 / 10011601, Arthur Schowantz, 8.00, 26.00, 34.00 / 10000576, Arthur
Vinicius Alves Vencao, 9.00, 62.00, 71.00 / 10000737, Artur Gabriel Sousa Calaca, 9.00, 44.00, 53.00 /
10012392, Artur Henrique Gomes de Oliveira, 9.00, 30.00, 39.00 / 10011069, Artur Santos dos Santos,
9.00, 28.00, 37.00 / 10007922, Asafe Farias Lima, 14.00, 46.00, 60.00 / 10010669, Asnan Pedreira
Rodrigues, 11.00, 62.00, 73.00 / 10001001, Atila Cavalcante Alves, 12.00, 54.00, 66.00 / 10005756, Atila
Mota Silva, 8.00, 42.00, 50.00 / 10016018, Atila Santos Rocha, 12.00, 38.00, 50.00 / 10013545, Augusto
Araujo Marques, 10.00, 38.00, 48.00 / 10013595, Augusto Muller Costa Penha, 12.00, 64.00, 76.00 /
10008193, Aurelio Victor Nunes de Paiva, 9.00, 24.00, 33.00 / 10015865, Avelar Feitosa Ribeiro Filho,
14.00, 56.00, 70.00 / 10009464, Avne Nascimento do Rosario, 15.00, 66.00, 81.00 / 10008124, Axel Lima
de Souza, 10.00, 50.00, 60.00 / 10000441, Ayla Carolina Dias da Silva, 5.00, 38.00, 43.00 / 10012996,
Barbara Araujo da Silva, 9.00, 48.00, 57.00 / 10016964, Barbara Chaves Rezegue, 15.00, 50.00, 65.00 /
10012870, Barbara Ellen da Silva Moura, 7.00, 26.00, 33.00 / 10011119, Barbara Fabiola Freire Siqueira,
10.00, 46.00, 56.00 / 10017104, Barbara Karina de Araujo Lima, 7.00, 20.00, 27.00 / 10002323, Barbara
Katarine Melo Costa, 6.00, 46.00, 52.00 / 10012529, Barbara Maria Balieiro de Oliveira, 10.00, 40.00,
50.00 / 10000402, Barbara Michele Teles Barros, 8.00, 22.00, 30.00 / 10009294, Barbara Renata da Silva
Dias, 11.00, 42.00, 53.00 / 10013540, Barbara Victoria Alves Rodrigues, 10.00, 50.00, 60.00 / 10011612,
Beatriz Aparecida Cardoso, 15.00, 62.00, 77.00 / 10005528, Beatriz Beckman Ferreira Soares, 9.00, 50.00,
59.00 / 10012029, Beatriz Caluff Canto, 14.00, 66.00, 80.00 / 10002838, Beatriz Caroline Lucena de Melo,
14.00, 58.00, 72.00 / 10006771, Beatriz Carolinne da Silva Soares, 10.00, 50.00, 60.00 / 10013512, Beatriz
dos Prazeres Viana, 10.00, 46.00, 56.00 / 10005285, Beatriz dos Santos Magalhaes, 10.00, 22.00, 32.00 /
10005625, Beatriz dos Santos Oliveira, 13.00, 40.00, 53.00 / 10013115, Beatriz Fernanda Silva Favacho,
9.00, 28.00, 37.00 / 10010993, Beatriz Freitas Pantoja, 8.00, 36.00, 44.00 / 10013585, Beatriz Helena
Almeida Pereira, 10.00, 64.00, 74.00 / 10001716, Beatriz Martins dos Santos, 10.00, 40.00, 50.00 /
10015784, Beatriz Melo da Silva, 10.00, 56.00, 66.00 / 10002767, Beatriz Mota de Sousa, 6.00, 44.00,
50.00 / 10007673, Beatriz Nunes de Castro, 10.00, 48.00, 58.00 / 10003108, Beatriz Oliveira Costa, 8.00,
52.00, 60.00 / 10005449, Beatriz Pereira de Oliveira, 8.00, 22.00, 30.00 / 10009319, Beatriz Portal Furtado,
7.00, 32.00, 39.00 / 10010820, Beatriz Ramos de Souza, 9.00, 52.00, 61.00 / 10003177, Beatriz Rodrigues
da Silva, 7.00, 28.00, 35.00 / 10013249, Beatriz Soares Souza, 10.00, 44.00, 54.00 / 10013272, Beatriz
Souza da Cruz, 8.00, 40.00, 48.00 / 10013282, Beattrys Baldo Bergamim, 11.00, 58.00, 69.00 / 10016407,
Bellingthon Alberto Marinho da Silva, 5.00, 22.00, 27.00 / 10013699, Belyne Figueiredo Nascimento, 3.00,
24.00, 27.00 / 10002471, Benedito Pereira Ferreira Neto, 9.00, 26.00, 35.00 / 10000647, Benicio Francisco
de Oliveira Neto, 9.00, 36.00, 45.00 / 10008130, Bennet da Silva Ferreira, 11.00, 52.00, 63.00 / 10010197,
Bento Sobrinho de Sousa Lima, 13.00, 50.00, 63.00 / 10001711, Bernard Santos Brigida de Souza, 5.00,
40.00, 45.00 / 10010161, Bernardo Brito de Souza, 12.00, 58.00, 70.00 / 10011477, Bernardo Farias Blanco
da Silva, 10.00, 50.00, 60.00 / 10007558, Bia Lorena Ribeiro Melo, 11.00, 54.00, 65.00 / 10013194, Bianca
Correa Goncalves, 8.00, 44.00, 52.00 / 10002409, Bianca Cristina da Silva Pereira, 8.00, 50.00, 58.00 /
10016314, Bianca da Costa Monteiro, 7.00, 32.00, 39.00 / 10010855, Bianca de Holanda, 10.00, 42.00,
52.00 / 10007063, Bianca de Sousa Costa, 9.00, 60.00, 69.00 / 10013208, Bianca Dias Antunes, 10.00,
 
58.00, 68.00 / 10005235, Bianca dos Santos Fernandes Nunes, 6.00, 40.00, 46.00 / 10007439, Bianca Inacio
dos Santos, 12.00, 64.00, 76.00 / 10011927, Bianca Juliao da Silva, 8.00, 38.00, 46.00 / 10011940, Bianca
Katrine de Carvalho Oliveira, 9.00, 44.00, 53.00 / 10006967, Bianca Lobato de Menezes, 13.00, 56.00,
69.00 / 10002000, Bianca Luciana da Silva Henriques, 10.00, 40.00, 50.00 / 10007123, Bianca Souza
Araujo, 10.00, 66.00, 76.00 / 10007910, Bill Maciel da Costa, 10.00, 36.00, 46.00 / 10002491, Blendo
Ferreira Correa, 12.00, 52.00, 64.00 / 10002817, Blyzya Kallyta Soares de Sousa, 10.00, 32.00, 42.00 /
10005726, Brena Marcela Oeiras Cordeiro, 10.00, 60.00, 70.00 / 10016700, Brenda Aparecida da Silva,
8.00, 52.00, 60.00 / 10016659, Brenda Caroline Castro da Silva, 9.00, 36.00, 45.00 / 10000259, Brenda
Christie Lima de Souza, 9.00, 60.00, 69.00 / 10001421, Brenda da Silva do Nascimento, 9.00, 34.00, 43.00
/ 10003115, Brenda da Silva Nunes, 11.00, 58.00, 69.00 / 10016271, Brenda Daniella Campelo Correa,
10.00, 54.00, 64.00 / 10002945, Brenda de Castro Garcia Maciel, 13.00, 54.00, 67.00 / 10002915, Brenda
dos Santos Valadares, 8.00, 48.00, 56.00 / 10002654, Brenda Estefany Cunha Melo da Gama, 12.00, 42.00,
54.00 / 10001246, Brenda Franco Dantas Lima, 10.00, 52.00, 62.00 / 10011391, Brenda Karine Mendes
Marques, 10.00, 38.00, 48.00 / 10001146, Brenda Karoline de Miranda Costa, 11.00, 38.00, 49.00 /
10012291, Brenda Lara de Souza Brito, 9.00, 24.00, 33.00 / 10016618, Brenda Martins Tomaz, 8.00, 48.00,
56.00 / 10001484, Brenda Matos Cunha, 16.00, 54.00, 70.00 / 10015961, Brenda Mayara Farias Barros,
10.00, 40.00, 50.00 / 10000988, Brenda Naligia de Almeida Carvalho, 14.00, 56.00, 70.00 / 10016626,
Brenda Sabrina da Silva Gomes, 10.00, 28.00, 38.00 / 10011231, Brenda Stephane Pires Brito, 11.00, 38.00,
49.00 / 10016575, Brenda Thaynara Costa Sarmento, 6.00, 28.00, 34.00 / 10012434, Brendo Lisandro
Ferreira da Silva, 14.00, 58.00, 72.00 / 10003001, Brendo Lohan dos Santos Tourao, 7.00, 58.00, 65.00 /
10010967, Brendo Nascimento Aguiar, 7.00, 40.00, 47.00 / 10010594, Brendo Santiago Felipe, 8.00, 50.00,
58.00 / 10012522, Brenna Karine dos Santos Paz, 4.00, 26.00, 30.00 / 10011860, Brenno Ribeiro Cardoso,
12.00, 56.00, 68.00 / 10007044, Breno Costa da Silva, 9.00, 46.00, 55.00 / 10005438, Breno dos Santos
Cartagenes, 6.00, 28.00, 34.00 / 10008030, Breno dos Santos Melo, 4.00, 32.00, 36.00 / 10000438, Breno
Felipe Farias de Freitas, 5.00, 26.00, 31.00 / 10008157, Breno Ferreira Macedo, 13.00, 36.00, 49.00 /
10010599, Breno Rafael dos Santos Tourao, 7.00, 70.00, 77.00 / 10009581, Breno Tavares Cardoso Souza,
10.00, 34.00, 44.00 / 10009378, Breno Vieira Batista, 10.00, 42.00, 52.00 / 10010392, Breno Yago de Lima
Alves, 11.00, 52.00, 63.00 / 10000342, Brian Lima dos Santos, 8.00, 44.00, 52.00 / 10009514, Bruce
Williams Santos Pires, 14.00, 62.00, 76.00 / 10010957, Bruna Alves Paiano, 10.00, 34.00, 44.00 /
10009894, Bruna Alves Sousa, 13.00, 46.00, 59.00 / 10007737, Bruna Araujo Vaz, 15.00, 58.00, 73.00 /
10007175, Bruna Caroline dos Santos Vieira, 10.00, 50.00, 60.00 / 10000174, Bruna Caroline Farias Alves,
8.00, 32.00, 40.00 / 10000090, Bruna Cecilia Carvalho Nascimento, 9.00, 42.00, 51.00 / 10015735, Bruna
Cruz de Araujo, 10.00, 56.00, 66.00 / 10000558, Bruna da Conceicao Barbosa Moraes, 9.00, 40.00, 49.00
/ 10016243, Bruna da Costa Vargens, 10.00, 66.00, 76.00 / 10015751, Bruna da Silva dos Anjos, 6.00,
28.00, 34.00 / 10008154, Bruna das Gracas Garcia Lopes, 8.00, 28.00, 36.00 / 10007133, Bruna Diniz
Macedo, 6.00, 32.00, 38.00 / 10013546, Bruna do Monte Chaves, 10.00, 40.00, 50.00 / 10010610, Bruna
Eduarda Lopes de Freitas, 13.00, 44.00, 57.00 / 10013389, Bruna Fernanda Silva de Araujo, 13.00, 62.00,
75.00 / 10001816, Bruna Goncalves Farias, 11.00, 42.00, 53.00 / 10010715, Bruna Larissa Lopes de Lima,
13.00, 56.00, 69.00 / 10013557, Bruna Laryssa Oliveira Monteiro, 10.00, 36.00, 46.00 / 10000309, Bruna
Leticia Batista Lobao da Silveira, 15.00, 36.00, 51.00 / 10013117, Bruna Leticia Marques Siqueira, 6.00,
32.00, 38.00 / 10001375, Bruna Lorena Silva de Souza, 8.00, 34.00, 42.00 / 10009302, Bruna Lys Modesto
Goncalves, 9.00, 36.00, 45.00 / 10007650, Bruna Marinho de Jesus, 14.00, 60.00, 74.00 / 10012143, Bruna
Moraes Pereira, 7.00, 32.00, 39.00 / 10011353, Bruna Rodrigues Mesquita, 15.00, 58.00, 73.00 / 10010460,
Bruna Ruana Medeiros Franco, 9.00, 32.00, 41.00 / 10011821, Bruna Sousa Rodrigues de Jesus, 13.00,
36.00, 49.00 / 10000383, Bruna Thais Pereira dos Santos, 11.00, 56.00, 67.00 / 10010125, Brunna Daniele
Menezes Farias, 5.00, 42.00, 47.00 / 10009767, Bruno Andrey Peres Alves, 8.00, 40.00, 48.00 / 10010549,
Bruno Campos de Abreu, 15.00, 56.00, 71.00 / 10011980, Bruno Cardoso da Silva, 6.00, 26.00, 32.00 /
10001796, Bruno Cardoso Oliveira, 12.00, 62.00, 74.00 / 10012931, Bruno Costa Marinho, 9.00, 46.00,
55.00 / 10010359, Bruno da Silva Alves, 10.00, 44.00, 54.00 / 10008004, Bruno da Silva Fonseca, 10.00,
68.00, 78.00 / 10007905, Bruno de Carvalho Leite Filho, 12.00, 36.00, 48.00 / 10012638, Bruno de
Carvalho Pinheiro, 9.00, 44.00, 53.00 / 10006781, Bruno de Souza Duarte, 7.00, 36.00, 43.00 / 10005682,
Bruno Diniz Calandrini de Azevedo, 9.00, 54.00, 63.00 / 10007436, Bruno Everton de Neres, 16.00, 66.00,
 
82.00 / 10001229, Bruno Ferreira da Silva, 11.00, 34.00, 45.00 / 10005760, Bruno Garcia Lisboa Borges,
8.00, 36.00, 44.00 / 10011653, Bruno Goncalves da Silva, 9.00, 42.00, 51.00 / 10012503, Bruno Henrique
Alves de Lima, 10.00, 58.00, 68.00 / 10011623, Bruno Ivair Ferreira Silva, 8.00, 48.00, 56.00 / 10002533,
Bruno Lima Gurjao, 6.00, 24.00, 30.00 / 10009991, Bruno Lima Sena, 10.00, 32.00, 42.00 / 10016458,
Bruno Luso Vieira da Cruz, 5.00, 38.00, 43.00 / 10007251, Bruno Maisto Ventre, 11.00, 58.00, 69.00 /
10013049, Bruno Martins Piauilino, 10.00, 42.00, 52.00 / 10011449, Bruno Mateus Rodrigues Alves,
12.00, 62.00, 74.00 / 10000040, Bruno Pinheiro Malcher, 10.00, 62.00, 72.00 / 10000640, Bruno Pio Bento,
6.00, 36.00, 42.00 / 10001872, Bruno Pires Siqueira Neto, 13.00, 52.00, 65.00 / 10016169, Bruno Ricardo
da Silva Melo, 11.00, 48.00, 59.00 / 10000810, Bruno Savio de Sousa Azevedo, 10.00, 56.00, 66.00 /
10016044, Bruno Siqueira de Souza, 11.00, 58.00, 69.00 / 10009946, Bruno Souza Damacena, 7.00, 36.00,
43.00 / 10000761, Bruno Vinicius da Silva Santos, 14.00, 54.00, 68.00 / 10015852, Bruno Vinicius de
Sousa Lopes Cavalcante, 7.00, 22.00, 29.00 / 10010175, Bryan Braga Batista, 11.00, 54.00, 65.00 /
10013268, Buenny Silva Barros, 12.00, 52.00, 64.00 / 10010266, Byanca de Sa Ramos, 8.00, 40.00, 48.00
/ 10011277, Cadson Martins de Figueiredo, 6.00, 48.00, 54.00 / 10000806, Caike Dias Rodrigues, 5.00,
32.00, 37.00 / 10007755, Caimmy Sousa de Sa Rocha, 15.00, 54.00, 69.00 / 10002663, Caio Adamor
Formigosa dos Santos, 14.00, 42.00, 56.00 / 10007452, Caio Augusto Santos Medeiros, 10.00, 56.00, 66.00
/ 10010176, Caio Benjamin da Silva Guedes, 9.00, 38.00, 47.00 / 10011203, Caio Cavalcante Reis, 16.00,
62.00, 78.00 / 10011914, Caio Cezar Perna Ferreira, 3.00, 42.00, 45.00 / 10011502, Caio Couto Silva,
10.00, 64.00, 74.00 / 10000648, Caio Daniel Lima Arrais, 10.00, 42.00, 52.00 / 10000113, Caio Dias
Rodrigues, 13.00, 58.00, 71.00 / 10005502, Caio Gaby Pinheiro, 13.00, 58.00, 71.00 / 10010419, Caio
Goncalves Correa, 8.00, 62.00, 70.00 / 10016282, Caio Henrique de Oliveira Pereira, 7.00, 46.00, 53.00 /
10012502, Caio Igor Rodrigues Fernandes, 15.00, 54.00, 69.00 / 10009322, Caio Julius Mota Sussuarana,
10.00, 32.00, 42.00 / 10015942, Caio Lobato Barroso, 11.00, 44.00, 55.00 / 10007544, Caio Lucas Santana
da Silva, 9.00, 36.00, 45.00 / 10011102, Caio Miguel Brandao Goncalves, 9.00, 50.00, 59.00 / 10011898,
Caio Rian Pereira de Andrade, 16.00, 50.00, 66.00 / 10007531, Caio Ricardo Pinho Cristo, 7.00, 32.00,
39.00 / 10012013, Caio Siqueira Sena, 11.00, 38.00, 49.00 / 10007645, Caio Vaz Rocha da Silva, 11.00,
50.00, 61.00 / 10011160, Caio William Barcelos Santos, 10.00, 48.00, 58.00 / 10010762, Caique Medeiros
Acacio, 10.00, 52.00, 62.00 / 10012621, Calebe de Mello Pessoa, 8.00, 32.00, 40.00 / 10010273, Calebe
Silva Almeida, 8.00, 62.00, 70.00 / 10010558, Callyne Victoria de Oliveira da Costa, 8.00, 42.00, 50.00 /
10000138, Calyma Jardene Carvalho Barbosa da Conceicao, 12.00, 68.00, 80.00 / 10007666, Camila
Adriele da Silva Sousa, 13.00, 54.00, 67.00 / 10006725, Camila Araujo Escolastico de Macedo, 13.00,
50.00, 63.00 / 10011185, Camila Caluff Rodrigues de Lima, 13.00, 38.00, 51.00 / 10005401, Camila
Cristina dos Santos Soares, 7.00, 46.00, 53.00 / 10000880, Camila de Lima Fonseca, 7.00, 52.00, 59.00 /
10010977, Camila de Oliveira Ferreira, 9.00, 36.00, 45.00 / 10012993, Camila de Sa Calumby, 10.00,
58.00, 68.00 / 10011644, Camila de Souza dos Santos, 8.00, 36.00, 44.00 / 10013320, Camila Dheiry Farias
Saraiva, 6.00, 32.00, 38.00 / 10001781, Camila Estephany Cardoso de Souza, 8.00, 54.00, 62.00 /
10016206, Camila Freitas dos Santos, 7.00, 30.00, 37.00 / 10010420, Camila Lima Aguiar, 8.00, 52.00,
60.00 / 10010067, Camila Lima Maia, 11.00, 46.00, 57.00 / 10000878, Camila Nathercia Silva Moura,
15.00, 58.00, 73.00 / 10011331, Camila Oliveira da Silva, 8.00, 28.00, 36.00 / 10007855, Camila Pontes
Goes, 9.00, 42.00, 51.00 / 10003100, Camila Rabelo de Oliveira, 12.00, 34.00, 46.00 / 10010002, Camila
Santos Sa, 14.00, 64.00, 78.00 / 10006992, Camila Sara Ferreira Henrique, 10.00, 50.00, 60.00 / 10017085,
Camila Silva Junqueira, 6.00, 28.00, 34.00 / 10010714, Camila Silva Pereira, 6.00, 34.00, 40.00 / 10007349,
Camila Victoria Matos Barbosa, 11.00, 42.00, 53.00 / 10001874, Camila Wakimoto Fonseca, 10.00, 48.00,
58.00 / 10007947, Camili Pinto Nascimento, 5.00, 20.00, 25.00 / 10006803, Camilli Henrielle Vilhena
Nogueira, 11.00, 44.00, 55.00 / 10000045, Camilly Barbosa Sousa, 8.00, 38.00, 46.00 / 10011471, Carina
da Silva Souza, 13.00, 46.00, 59.00 / 10001837, Carla Beatriz Quaresma Sobral, 9.00, 40.00, 49.00 /
10007500, Carla Caroline dos Santos Baia, 10.00, 56.00, 66.00 / 10015796, Carla Cristina da Silva
Rodrigues, 5.00, 30.00, 35.00 / 10011240, Carla Fabiana Silva Gomes, 12.00, 54.00, 66.00 / 10000200,
Carla Gabriela Cruz Ribeiro, 8.00, 40.00, 48.00 / 10007880, Carla Juliana de Souza Nascimento, 7.00,
30.00, 37.00 / 10011665, Carla Layla Santos Pantoja, 9.00, 36.00, 45.00 / 10002983, Carla Lyegi Couto
Almeida, 7.00, 34.00, 41.00 / 10001195, Carla Sabrina Pereira Ramos, 10.00, 40.00, 50.00 / 10001995,
Carla Vanessa Alves Monteiro, 15.00, 58.00, 73.00 / 10006824, Carla Vanessa Manari Lobato, 13.00,
 
54.00, 67.00 / 10013303, Carla Yukie Ribeiro Motizuki, 14.00, 56.00, 70.00 / 10012618, Carlos Alberto
Batistajunior, 8.00, 52.00, 60.00 / 10000318, Carlos Alef de Paiva Gurjao, 10.00, 40.00, 50.00 / 10007202,
Carlos Alfredo Pantoja Lopes, 13.00, 48.00, 61.00 / 10001778, Carlos Alves Rosa Junior, 11.00, 58.00,
69.00 / 10017009, Carlos Antonio Cabral da Paz Junior, 6.00, 38.00, 44.00 / 10010187, Carlos Augusto
Ayres Santos, 16.00, 74.00, 90.00 / 10002732, Carlos Augusto Rocha Pamplona, 1.00, 6.00, 7.00 /
10000158, Carlos Caique de Araujo Silva, 6.00, 48.00, 54.00 / 10016806, Carlos Daniel da Costa Farias,
11.00, 46.00, 57.00 / 10009632, Carlos Denis Quaresma Ferreira, 13.00, 26.00, 39.00 / 10009556, Carlos
dos Santos Silva, 9.00, 42.00, 51.00 / 10001585, Carlos Eduardo Andrade Rabelo, 7.00, 56.00, 63.00 /
10001720, Carlos Eduardo de Sousa Pinto, 13.00, 70.00, 83.00 / 10001712, Carlos Eduardo Franco da
Silva, 6.00, 42.00, 48.00 / 10013676, Carlos Eduardo Freitas da Silva, 10.00, 56.00, 66.00 / 10001073,
Carlos Eduardo Gato dos Santos, 11.00, 36.00, 47.00 / 10009775, Carlos Eduardo Gomes Duarte, 5.00,
40.00, 45.00 / 10007006, Carlos Eduardo Lima Botelho, 9.00, 54.00, 63.00 / 10012932, Carlos Eduardo
Lima Pereira, 14.00, 40.00, 54.00 / 10010962, Carlos Eduardo Risuenho Abdon da Cunha, 9.00, 26.00,
35.00 / 10012222, Carlos Eduardo Rodrigues Cardoso, 13.00, 52.00, 65.00 / 10001784, Carlos Eduardo
Rodrigues de Alencar, 8.00, 30.00, 38.00 / 10012526, Carlos Eduardo Silva Lins, 7.00, 42.00, 49.00 /
10012975, Carlos Felipe Frazao Henriques, 7.00, 44.00, 51.00 / 10011258, Carlos Gabriel Acioli
Taumaturgo, 8.00, 32.00, 40.00 / 10005605, Carlos Henrique Miranda Barros, 12.00, 52.00, 64.00 /
10009655, Carlos Henrique Pinho da Silva, 13.00, 58.00, 71.00 / 10010492, Carlos Henrique Santos Nunes,
13.00, 50.00, 63.00 / 10009909, Carlos Henrique Sousa Nascimento, 8.00, 48.00, 56.00 / 10016812, Carlos
Joas Navegantes dos Santos, 11.00, 38.00, 49.00 / 10011896, Carlos Laurean Silva Farias, 9.00, 32.00,
41.00 / 10012209, Carlos Lucas Meireles da Silva, 8.00, 42.00, 50.00 / 10006957, Carlos Martins da Silva
Junior, 10.00, 50.00, 60.00 / 10005498, Carlos Patrick Carvalho da Silva, 6.00, 30.00, 36.00 / 10008069,
Carlos Ramon Santos de Carvalho, 12.00, 56.00, 68.00 / 10007522, Carlos Renan Sousa Silva, 10.00, 44.00,
54.00 / 10001645, Carlos Wagner Santos de Jesus, 3.00, 40.00, 43.00 / 10013519, Carlos Willames Santos
de Macedo, 11.00, 46.00, 57.00 / 10010742, Carmem Suellen Ferreira Ventura, 9.00, 28.00, 37.00 /
10007114, Carolina Lima Pinheiro, 11.00, 34.00, 45.00 / 10013571, Carolina Marinho de Lacerda, 10.00,
26.00, 36.00 / 10012725, Carolina Monteiro Barros, 3.00, 18.00, 21.00 / 10000219, Carolina Rodrigues
Souza, 10.00, 42.00, 52.00 / 10005740, Caroline Cardoso Macedo da Rocha, 9.00, 28.00, 37.00 / 10002454,
Caroline Freitas de Oliveira, 12.00, 56.00, 68.00 / 10013402, Caroline Mota, 8.00, 34.00, 42.00 / 10010866,
Caroline Oliveira Schmidt, 16.00, 56.00, 72.00 / 10011529, Carolini do Socorro Sena Reis, 5.00, 32.00,
37.00 / 10016692, Caroliny Beatriz Franca Dias, 6.00, 32.00, 38.00 / 10000619, Carollina Gelabert Mafra,
8.00, 44.00, 52.00 / 10011557, Cassamea da Silva Freire Andrade, 8.00, 44.00, 52.00 / 10010641, Cassia
Alexandra Amaral de Alexandria, 13.00, 40.00, 53.00 / 10012053, Cassia de Sousa Almeida, 8.00, 38.00,
46.00 / 10001409, Cassiano da Mata Oliveira Neto, 9.00, 30.00, 39.00 / 10016057, Cassio Cunha Lisboa,
8.00, 58.00, 66.00 / 10007506, Cassio Felipe Sousa da Silva, 8.00, 44.00, 52.00 / 10000051, Cassio Pereira
Costa Oliveira, 7.00, 36.00, 43.00 / 10003197, Cassio Pereira de Oliveira, 14.00, 26.00, 40.00 / 10011274,
Cassio Santos Fonseca, 11.00, 64.00, 75.00 / 10016341, Catarina Nogueira Nascimento, 11.00, 26.00, 37.00
/ 10011512, Caymmi Lima Maia, 9.00, 26.00, 35.00 / 10006930, Cayo Jordan Barbosa do Rosario, 10.00,
42.00, 52.00 / 10001608, Cednei Paulino Paixao dos Santos, 3.00, 26.00, 29.00 / 10005509, Celia Maria
Silva Ramos, 13.00, 54.00, 67.00 / 10011017, Celso Monteiro da Silva Marques, 13.00, 30.00, 43.00 /
10001419, Cesar Augusto Sosa Camino Silva, 9.00, 38.00, 47.00 / 10010572, Cesar Augusto Teixeira
Santos, 12.00, 64.00, 76.00 / 10002049, Cesar Henrique Silva Palheta, 13.00, 44.00, 57.00 / 10009790,
Cezar Augusto Borges da Silva, 9.00, 38.00, 47.00 / 10011013, Chaiane Pagliari, 13.00, 48.00, 61.00 /
10006861, Charles Lira de Melo, 7.00, 32.00, 39.00 / 10015752, Chrisla Bruna Malheiro Lima, 11.00,
42.00, 53.00 / 10012807, Christian Costa Pereira, 9.00, 46.00, 55.00 / 10007014, Christian Hendson Farias
da Silva, 10.00, 46.00, 56.00 / 10009820, Chrystian Vidal de Oliveira, 15.00, 58.00, 73.00 / 10012000,
Cibele da Rocha Dias, 8.00, 56.00, 64.00 / 10002586, Cicero Antonio Silva de Oliveira, 14.00, 58.00, 72.00
/ 10011055, Cicero Augusto Chaves Gomes, 14.00, 56.00, 70.00 / 10001924, Cicero Lucas Lacerda Pereira,
11.00, 46.00, 57.00 / 10007231, Cicero Sigliney Serra Silva, 9.00, 38.00, 47.00 / 10008153, Cindy Mary
da Silva Miralha Rodrigues, 8.00, 46.00, 54.00 / 10001684, Cinthia de Vasconcelos Silva, 15.00, 60.00,
75.00 / 10011872, Cintia Vieira Reis, 12.00, 48.00, 60.00 / 10007226, Ciro Morais de Oliveira Melo, 9.00,
40.00, 49.00 / 10016396, Clara da Costa Aquino, 12.00, 32.00, 44.00 / 10012756, Clarice Souza Santiago,
 
8.00, 34.00, 42.00 / 10007627, Clark Clinsmann Miranda de Campos, 9.00, 32.00, 41.00 / 10010464,
Claudemir de Souza Cavalcante, 11.00, 56.00, 67.00 / 10012748, Claudiane Rithyele Barros Lopes, 14.00,
52.00, 66.00 / 10015907, Claudio Cesar de Farias Progenio, 6.00, 38.00, 44.00 / 10013059, Claudio
Nascimento da Silva, 6.00, 40.00, 46.00 / 10010156, Claudio Victor Baia Lisboa Nascimento, 6.00, 32.00,
38.00 / 10010635, Clayton Robson Melo da Costa, 11.00, 60.00, 71.00 / 10000310, Clebervaldo Almeida
dos Santos Junior, 9.00, 56.00, 65.00 / 10004204, Cleib Nascimento de Lima, 11.00, 50.00, 61.00 /
10016526, Cleise Baia Silva, 6.00, 24.00, 30.00 / 10001883, Cleise Kelly Carvalho dos Santos, 7.00, 26.00,
33.00 / 10002666, Cleiton Fernandes da Silva, 11.00, 30.00, 41.00 / 10009884, Cleliane Dias dos Santos,
8.00, 24.00, 32.00 / 10013620, Clelio Roberto Rego Monteiro, 9.00, 50.00, 59.00 / 10015842, Clenilson
Peniche Galisa, 15.00, 62.00, 77.00 / 10011626, Cleofas Bertolino da Silva, 11.00, 44.00, 55.00 / 10007438,
Cleomatson Fernando Poderoso Silva, 11.00, 56.00, 67.00 / 10013065, Cleudimar Gonzaga dos Santos,
9.00, 40.00, 49.00 / 10000986, Cleudison Ferreira de Melo e Silva Junior, 14.00, 54.00, 68.00 / 10005471,
Cleyton dos Santos Nascimento, 8.00, 40.00, 48.00 / 10008225, Clint Maciel da Costa, 13.00, 48.00, 61.00
/ 10010928, Cloves Vilar da Silva, 9.00, 60.00, 69.00 / 10002804, Clovis Jordao Faro Junior, 10.00, 56.00,
66.00 / 10009281, Clycia Medeiros Baia, 9.00, 26.00, 35.00 / 10013239, Crinson Potiguara de Souza, 7.00,
40.00, 47.00 / 10013174, Crisangela Barbosa Teixeira da Silva, 12.00, 38.00, 50.00 / 10016381, Crissia
Talita Lima Silva, 8.00, 24.00, 32.00 / 10011014, Cristian Fuziel Lima, 8.00, 52.00, 60.00 / 10007725,
Cristiane da Silva Goncalves, 11.00, 50.00, 61.00 / 10000789, Cristiane Vale Assuncao Pinheiro, 8.00,
30.00, 38.00 / 10002457, Cristiano Modesto Pinheiro, 10.00, 54.00, 64.00 / 10006773, Cristielen Capareli
Bezerra, 10.00, 60.00, 70.00 / 10009362, Cybelle Barbosa Pires da Silva, 8.00, 16.00, 24.00 / 10010401,
Cynara Vitoria Barros dos Santos, 9.00, 40.00, 49.00 / 10006916, Cynthia Macedo da Silva, 9.00, 28.00,
37.00 / 10013670, Cynthia Sabrina Vieira Figueiredo, 7.00, 38.00, 45.00 / 10010636, Cyntia dos Santos
Felix, 8.00, 44.00, 52.00 / 10009317, Dacia Davila de Sousa Lopes, 10.00, 26.00, 36.00 / 10002353, Daiane
Carreiro dos Santos, 10.00, 44.00, 54.00 / 10007108, Daiane Teles dos Santos, 9.00, 48.00, 57.00 /
10003163, Daiane Viana Silva, 13.00, 54.00, 67.00 / 10016184, Dalton Pinto Lima Filho, 9.00, 26.00, 35.00
/ 10009756, Damires Karolayne Modesto Castelo Branco, 6.00, 30.00, 36.00 / 10007134, Dandara dos
Santos Albuquerque, 12.00, 52.00, 64.00 / 10007420, Dandara Furtado Monteiro, 10.00, 32.00, 42.00 /
10010568, Daniel Araujo Rezende, 8.00, 30.00, 38.00 / 10016541, Daniel Assuncao Silva, 14.00, 62.00,
76.00 / 10011082, Daniel Augusto da Silva e Silva, 9.00, 56.00, 65.00 / 10016513, Daniel Benedito Leal
Neto, 4.00, 48.00, 52.00 / 10001290, Daniel Brasil Cunha Carneiro, 13.00, 64.00, 77.00 / 10010343, Daniel
Cardoso Zahlouth, 14.00, 68.00, 82.00 / 10016179, Daniel Cleino Pinheiro Tavares, 6.00, 54.00, 60.00 /
10007352, Daniel da Silva Araujo, 10.00, 48.00, 58.00 / 10000278, Daniel da Silva Santos, 11.00, 50.00,
61.00 / 10002677, Daniel de Freitas Correa, 13.00, 66.00, 79.00 / 10008080, Daniel de Sousa Figueiredo,
13.00, 52.00, 65.00 / 10012530, Daniel de Souza Caliari Ferreira, 6.00, 26.00, 32.00 / 10000572, Daniel do
Nascimento Louzeiro, 14.00, 70.00, 84.00 / 10011365, Daniel Farage Filho, 11.00, 36.00, 47.00 /
10000183, Daniel Fernandes Monteiro, 6.00, 32.00, 38.00 / 10005549, Daniel Igor Cordeiro de Oliveira,
11.00, 36.00, 47.00 / 10010630, Daniel Julio Borges, 9.00, 60.00, 69.00 / 10015771, Daniel Lima Tavares,
9.00, 48.00, 57.00 / 10007216, Daniel Markus Guimaraes Miranda, 9.00, 66.00, 75.00 / 10009334, Daniel
Martinho Damasceno Pinto, 12.00, 50.00, 62.00 / 10002587, Daniel Nunes de Abreu, 10.00, 68.00, 78.00
/ 10007485, Daniel Pereira da Silva, 8.00, 56.00, 64.00 / 10000408, Daniel Prieto de Souza, 11.00, 56.00,
67.00 / 10000515, Daniel Ramon da Silva, 11.00, 60.00, 71.00 / 10001962, Daniel Rhimom Oliveira
Ribeiro, 17.00, 64.00, 81.00 / 10000785, Daniel Rodolfo de Araujo Rodrigues, 11.00, 56.00, 67.00 /
10000121, Daniel Rodrigues Leite, 11.00, 66.00, 77.00 / 10003069, Daniel Savio Costa Santos, 6.00, 30.00,
36.00 / 10007415, Daniel Silva Pereira, 7.00, 42.00, 49.00 / 10011966, Daniel Sousa Medeiros, 10.00,
46.00, 56.00 / 10009835, Daniel Victor de Lima Silva, 10.00, 44.00, 54.00 / 10010127, Daniel Vitor
Rodrigues Ferreira Lima, 11.00, 56.00, 67.00 / 10005444, Daniela Bastos da Silva, 16.00, 58.00, 74.00 /
10013363, Daniela de Cassia Costa Tavares Mesquita, 11.00, 40.00, 51.00 / 10002655, Daniela de Lourdes
Almeida Costa, 13.00, 48.00, 61.00 / 10001045, Daniela Monteiro Miranda, 9.00, 48.00, 57.00 / 10010320,
Daniele da Costa Vieira, 12.00, 54.00, 66.00 / 10012690, Daniele Ferreira Miranda, 12.00, 68.00, 80.00 /
10005208, Daniele Rodrigues Mota, 7.00, 34.00, 41.00 / 10016277, Danieli Alves, 8.00, 40.00, 48.00 /
10007283, Danieli Freitas Lopes, 17.00, 56.00, 73.00 / 10010184, Daniella Figueiredo Miranda, 15.00,
48.00, 63.00 / 10009676, Danielle Carolina Sant Anna da Silva, 9.00, 50.00, 59.00 / 10010694, Danielle
 
dos Santos Prazeres, 11.00, 62.00, 73.00 / 10007499, Danielly Cristina Ribeiro dos Reis, 7.00, 24.00, 31.00
/ 10011117, Danielly Negreiros Brandao, 3.00, 28.00, 31.00 / 10000503, Danielly Santos Mello, 9.00,
44.00, 53.00 / 10009788, Danilo Bruzaca Pinheiro, 15.00, 44.00, 59.00 / 10007484, Danilo de Araujo
Cabral, 9.00, 22.00, 31.00 / 10012393, Danilo de Araujo Falcao, 14.00, 50.00, 64.00 / 10008031, Danilo
de Assis Bessa Santana, 11.00, 38.00, 49.00 / 10003103, Danilo Gilvani Cabral Passinho, 13.00, 66.00,
79.00 / 10010066, Danilo Henrique dos Santos Lima, 12.00, 40.00, 52.00 / 10013263, Danilo Moreira da
Silva, 9.00, 42.00, 51.00 / 10015975, Danilo Pantoja de Assuncao, 12.00, 62.00, 74.00 / 10007445, Danilo
Silva do Nascimento, 8.00, 60.00, 68.00 / 10012321, Danilo Tavares Coutinho Cardoso, 10.00, 42.00, 52.00
/ 10007588, Danilo Wesley Maciel Souza, 9.00, 46.00, 55.00 / 10000143, Danuza do Vale Campos, 12.00,
62.00, 74.00 / 10006966, Danyelle Delgado Viana, 12.00, 70.00, 82.00 / 10008006, Danyewellin Pinheiro
de Souza, 11.00, 54.00, 65.00 / 10013223, Danyllo Luiz Moraes da Silva, 6.00, 42.00, 48.00 / 10013598,
Daphne Luana Sauma Figueira Pereira, 9.00, 46.00, 55.00 / 10011635, Dara Vitoria Miranda Costa, 9.00,
44.00, 53.00 / 10016540, Dariane Cristina da Silva Negrao, 6.00, 24.00, 30.00 / 10013162, Darlene Cardoso
Campos, 7.00, 38.00, 45.00 / 10011447, Darliane Alves Nogueira, 13.00, 46.00, 59.00 / 10008002, Davi
Bezerra de Vaconcelos, 13.00, 64.00, 77.00 / 10013360, Davi da Silva Freire Rios, 13.00, 58.00, 71.00 /
10011326, Davi Jose Ribeiro de Barros, 12.00, 48.00, 60.00 / 10012274, Davi Mendes Rodrigues, 10.00,
46.00, 56.00 / 10009793, Davi Moises Negrao Silva, 9.00, 34.00, 43.00 / 10012042, Davi Moura Bezerra
Abtibol, 15.00, 54.00, 69.00 / 10016162, Davi Moura do Nascimento Junior, 5.00, 24.00, 29.00 / 10015999,
Davi Nascimento da Silva, 9.00, 44.00, 53.00 / 10002529, Davi Sarmento da Cunha, 12.00, 40.00, 52.00 /
10010545, David Alfredo da Silva Rosa, 16.00, 56.00, 72.00 / 10012178, David Anderson Miranda Ribeiro,
13.00, 46.00, 59.00 / 10000103, David de Oliveira Lauzid, 15.00, 64.00, 79.00 / 10006914, David Felipe
Santos Lica, 5.00, 38.00, 43.00 / 10010663, David Gomes Lima, 11.00, 42.00, 53.00 / 10010195, David
Malaquias Sousa Junior, 9.00, 62.00, 71.00 / 10013206, David Pantoja da Costa Neto, 8.00, 32.00, 40.00 /
10002014, David Salomao Lima Goncalves, 8.00, 40.00, 48.00 / 10010665, David Washington Sousa
Santos, 8.00, 30.00, 38.00 / 10000473, David Willy dos Santos Silva, 6.00, 42.00, 48.00 / 10012937,
Davison Felipe de Azevedo Barros, 3.00, 30.00, 33.00 / 10012185, Davisson Henrique Ramos Batista, 6.00,
38.00, 44.00 / 10015998, Davy Dourado Souza Silva, 13.00, 58.00, 71.00 / 10001852, Davyd Marcelo
Neves Correa, 4.00, 36.00, 40.00 / 10007596, Davyson da Silva Serrao, 9.00, 38.00, 47.00 / 10016848,
Dayana Oliveira da Costa, 3.00, 26.00, 29.00 / 10012372, Dayane do Socorro Barros Torres, 12.00, 32.00,
44.00 / 10002869, Dayane Ketleyn dos Santos Barros, 9.00, 32.00, 41.00 / 10007739, Dayane Silva dos
Santos, 6.00, 30.00, 36.00 / 10000852, Dayane Silva Oliveira, 7.00, 34.00, 41.00 / 10007166, Dayanne
Stephanie Azevedo de Castro, 8.00, 38.00, 46.00 / 10010814, Dayara Aires de Souza, 8.00, 50.00, 58.00 /
10015869, Dayrony Andrade Moreira, 7.00, 52.00, 59.00 / 10007580, Dayse Cleinauany Pinheiro Tavares,
9.00, 30.00, 39.00 / 10009685, Dayse de Sousa Honorato, 8.00, 52.00, 60.00 / 10011668, Dearly Silva
Machado, 9.00, 44.00, 53.00 / 10016638, Deberton do Vale Meireles, 7.00, 46.00, 53.00 / 10008064,
Debora Alves Resplande, 10.00, 40.00, 50.00 / 10007097, Debora Baima de Araujo, 9.00, 38.00, 47.00 /
10012305, Debora Cristina Batista de Oliveira, 6.00, 38.00, 44.00 / 10016125, Debora Cristina da Cruz
Cordeiro, 9.00, 48.00, 57.00 / 10012512, Debora Cristina de Matos Cardoso, 7.00, 48.00, 55.00 / 10010727,
Debora da Mota Zankanol, 11.00, 58.00, 69.00 / 10001094, Debora Ellem Sousa da Silva, 6.00, 42.00,
48.00 / 10009335, Debora Emmylly de Oliveira Arruda, 16.00, 66.00, 82.00 / 10011083, Debora Evelen
Silva Ribeiro, 10.00, 36.00, 46.00 / 10015819, Debora Gloria Nina Ferreira, 13.00, 36.00, 49.00 /
10002270, Debora Gomes dos Santos, 4.00, 44.00, 48.00 / 10002746, Debora Hester Meireles Galvao,
11.00, 42.00, 53.00 / 10005593, Debora Santana de Sousa, 7.00, 28.00, 35.00 / 10005292, Debora Silva de
Souza, 9.00, 38.00, 47.00 / 10016066, Debora Thais dos Santos Fonseca, 14.00, 64.00, 78.00 / 10002041,
Debora Vanessa Silva Cezar da Cruz, 10.00, 26.00, 36.00 / 10006926, Deborah Alves Macedo, 12.00,
34.00, 46.00 / 10000405, Deborah Costa Lima, 15.00, 64.00, 79.00 / 10016375, Deborah Paternostro de
Araujo, 4.00, 26.00, 30.00 / 10000613, Decio Caldas Machado Junior, 7.00, 42.00, 49.00 / 10000209,
Deidiane Cardoso Soares, 9.00, 58.00, 67.00 / 10008056, Deimen Kelly David de Oliveira Cordeiro, 4.00,
18.00, 22.00 / 10015871, Deise Anne Furtado do Santos, 9.00, 54.00, 63.00 / 10016753, Deisyane Sobreira
da Silva, 5.00, 28.00, 33.00 / 10000336, Deivid An Martins de Arruda, 11.00, 62.00, 73.00 / 10001009,
Deivide da Silva de Oliveira, 13.00, 52.00, 65.00 / 10002197, Deivison Rubens Reis Brigido, 6.00, 20.00,
26.00 / 10016763, Deiwison de Lima Coqueiro, 8.00, 38.00, 46.00 / 10001277, Delany Luiza Amorim
 
Piedade, 16.00, 52.00, 68.00 / 10016957, Delbson Cereija Almeida, 8.00, 42.00, 50.00 / 10000583,
Delciana Novaes da Silva, 11.00, 30.00, 41.00 / 10009961, Delcivania de Sa Silva, 8.00, 48.00, 56.00 /
10017052, Delnirya Alessandra da Costa Moraes, 7.00, 22.00, 29.00 / 10011688, Deltonio Aires de Morais
Junior, 13.00, 66.00, 79.00 / 10001369, Demerson Daniel da Costa e Silva, 8.00, 46.00, 54.00 / 10009693,
Denilson dos Santos de Santana, 10.00, 32.00, 42.00 / 10011690, Denilson Lima Ferreira, 9.00, 46.00,
55.00 / 10007468, Denis Deividy de Souza, 10.00, 54.00, 64.00 / 10010306, Denis Pereira de Oliveira,
11.00, 60.00, 71.00 / 10009955, Denise Aguiar Cordeiro, 10.00, 42.00, 52.00 / 10011526, Denise Porto
Pereira, 10.00, 64.00, 74.00 / 10008151, Denise Sousa Rossato, 12.00, 66.00, 78.00 / 10000378, Denize do
Rosario Rabelo dos Santos, 10.00, 40.00, 50.00 / 10012891, Denys Silva dos Santos, 9.00, 44.00, 53.00 /
10013391, Deo Nascimento Barroso, 8.00, 24.00, 32.00 / 10016015, Deosmar Batista de Aquino Neto,
9.00, 46.00, 55.00 / 10011531, Derivan de Moraes Torres, 7.00, 46.00, 53.00 / 10011462, Dewison Rikarth
da Silva Oliveira, 14.00, 46.00, 60.00 / 10008019, Deylon Lima Miranda, 9.00, 42.00, 51.00 / 10016821,
Deyse de Sousa Jardim, 6.00, 30.00, 36.00 / 10002229, Deyvison Roberto de Souza Martinez, 13.00, 56.00,
69.00 / 10016399, Dhaylla Thayna da Conceicao Vieira, 10.00, 44.00, 54.00 / 10005694, Dhemisson dos
Santos Sousa, 7.00, 30.00, 37.00 / 10011631, Dhenner Lussac de Lima Pinheiro, 15.00, 50.00, 65.00 /
10011696, Dhennifer Nunes da Silva, 12.00, 48.00, 60.00 / 10016505, Dhiulycelly Domingues Pereira,
8.00, 46.00, 54.00 / 10000496, Dhulyenne da Silva Goncalves, 6.00, 30.00, 36.00 / 10015757, Dhyordan
Olegario Almeida Martins, 11.00, 24.00, 35.00 / 10016150, Diago Correia Pantoja, 8.00, 30.00, 38.00 /
10012332, Diego Alexandre de Sousa Franco, 7.00, 38.00, 45.00 / 10001627, Diego Barros Rodrigues,
8.00, 44.00, 52.00 / 10000882, Diego Braga Modesto, 10.00, 34.00, 44.00 / 10011041, Diego Bruno de
Moraes Tavares, 9.00, 40.00, 49.00 / 10011543, Diego Castro dos Santos, 7.00, 38.00, 45.00 / 10010516,
Diego Coelho de Abreu, 13.00, 64.00, 77.00 / 10013547, Diego de Oliveira Miranda, 7.00, 24.00, 31.00 /
10009798, Diego Ferreira da Silva, 11.00, 44.00, 55.00 / 10000397, Diego Gomes Capela Barradas, 12.00,
52.00, 64.00 / 10012032, Diego Henrique de Souza Machado, 11.00, 48.00, 59.00 / 10011616, Diego Lima
de Oliveira, 8.00, 58.00, 66.00 / 10013082, Diego Lima dos Santos, 12.00, 40.00, 52.00 / 10002629, Diego
Luglime Santa Rosa, 9.00, 52.00, 61.00 / 10000835, Diego Martins da Silva, 5.00, 26.00, 31.00 / 10011012,
Diego Miranda Saraiva, 8.00, 42.00, 50.00 / 10007243, Diego Monteiro Pinheiro, 14.00, 56.00, 70.00 /
10000860, Diego Pena Nunes, 9.00, 38.00, 47.00 / 10010662, Diego Ricardo Souza da Cruz, 14.00, 64.00,
78.00 / 10007600, Diego Rodrigues do Nascimento, 9.00, 44.00, 53.00 / 10012002, Diego Sarges Ramos,
6.00, 36.00, 42.00 / 10000680, Diego Severiano, 12.00, 62.00, 74.00 / 10000746, Diego Souza dos Santos,
5.00, 26.00, 31.00 / 10001949, Dieisom Samuel Cardoso de Melo, 8.00, 50.00, 58.00 / 10001637, Dieison
Teixeira da Silva, 7.00, 48.00, 55.00 / 10000521, Dilcon de Souza Leao Junior, 14.00, 68.00, 82.00 /
10007765, Dimison de Assis Reis, 13.00, 66.00, 79.00 / 10009504, Dimitri Polichouk, 10.00, 50.00, 60.00
/ 10012333, Dimitry Jose Francisco, 11.00, 44.00, 55.00 / 10005278, Dinelton Costa Santos, 11.00, 46.00,
57.00 / 10001870, Diogo Figueiredo Amorim, 10.00, 58.00, 68.00 / 10000472, Diogo Low Castro, 6.00,
40.00, 46.00 / 10016780, Diogo Matheus Moreira de Abreu, 15.00, 46.00, 61.00 / 10012691, Diogo
Rodrigues Lima de Assuncao, 10.00, 40.00, 50.00 / 10001900, Diomar Pinheiro Cabral, 10.00, 32.00, 42.00
/ 10016233, Diones Moreira Lima Junior, 11.00, 48.00, 59.00 / 10011926, Dionisio Alecxander Nunes
Soares, 14.00, 60.00, 74.00 / 10002537, Dionisio Mendes da Costa Silva, 6.00, 22.00, 28.00 / 10001118,
Dionyllo Cabral Rocha, 12.00, 48.00, 60.00 / 10016609, Diva Nathaly Silva de Almeida Lins, 10.00, 54.00,
64.00 / 10005583, Divino Breno Benicio de Sa, 11.00, 60.00, 71.00 / 10016131, Djalmy Souza Mariz, 9.00,
50.00, 59.00 / 10001219, Djehine Richards Castro de Sousa, 9.00, 46.00, 55.00 / 10000838, Domingos do
Socorro Vilhena Machado, 9.00, 30.00, 39.00 / 10000110, Donizete Bezerra Lima, 9.00, 36.00, 45.00 /
10007861, Douglas Cardoso, 8.00, 40.00, 48.00 / 10013700, Douglas de Sousa Ferreira, 6.00, 44.00, 50.00
/ 10015896, Douglas Dornelas Nascimento, 14.00, 36.00, 50.00 / 10013510, Douglas Fell Droppa, 11.00,
58.00, 69.00 / 10010356, Douglas Israel Amaro de Oliveira Bentes, 16.00, 44.00, 60.00 / 10011664,
Douglas Motta Ferreira, 12.00, 46.00, 58.00 / 10001040, Douglas Nascimento Lopes, 5.00, 40.00, 45.00 /
10011368, Douglas Silva Galeno de Souza, 8.00, 32.00, 40.00 / 10000213, Douglas Silva Maciel, 9.00,
38.00, 47.00 / 10009589, Drielle Ferreira Damasceno, 11.00, 46.00, 57.00 / 10007585, Drielly Karine
Almeida Frazao, 15.00, 68.00, 83.00 / 10005690, Drierick Carvalho Cavalcante, 10.00, 64.00, 74.00 /
10009278, Dyego Waad Patroca, 8.00, 42.00, 50.00 / 10011827, Dyllan Vieira da Silva, 9.00, 40.00, 49.00
/ 10001148, Edelvan Rodrigues Braga, 10.00, 34.00, 44.00 / 10001550, Eden Alves Felizardo, 10.00, 46.00,
 
56.00 / 10005693, Eden Lucas da Silva Santos, 8.00, 52.00, 60.00 / 10010355, Eden Raul Araujo, 13.00,
34.00, 47.00 / 10005574, Eder Jose Martins Pereira e Silva, 11.00, 44.00, 55.00 / 10005529, Ederson
Fonseca da Cruz Filho, 8.00, 22.00, 30.00 / 10010328, Edgar Luiz Neves dos Santos, 12.00, 24.00, 36.00 /
10010916, Edgar Pinto da Costa de Mendonca, 11.00, 30.00, 41.00 / 10007547, Ediana Sousa da Costa,
6.00, 32.00, 38.00 / 10011157, Ediane Tamiles Souza de Souza, 7.00, 24.00, 31.00 / 10005677, Edil Silva
de Vilhena, 10.00, 36.00, 46.00 / 10012900, Edilayne Oliveira Barbosa, 15.00, 56.00, 71.00 / 10012988,
Edilberto da Silva Carreteiro Filho, 5.00, 38.00, 43.00 / 10008035, Edineire Castro Chumber, 7.00, 40.00,
47.00 / 10011360, Ediney Moura, 8.00, 26.00, 34.00 / 10011547, Edionei dos Santos Castro, 7.00, 38.00,
45.00 / 10000707, Edison da Silva Brandao, 10.00, 28.00, 38.00 / 10012036, Edison Jose de Araujo Neto,
11.00, 60.00, 71.00 / 10007318, Edmar Silva Pereira Filho, 7.00, 46.00, 53.00 / 10002660, Ednando Martins
Silva, 12.00, 54.00, 66.00 / 10010788, Edson Baratinha Pinheiro Junior, 13.00, 48.00, 61.00 / 10016602,
Edson Carlos Souza Junior, 8.00, 58.00, 66.00 / 10002718, Edson Cassio Mendes Farias, 9.00, 62.00, 71.00
/ 10001042, Edson Freire de Alencar Neto, 14.00, 66.00, 80.00 / 10010418, Edson Junior Lobato Ferreira,
8.00, 32.00, 40.00 / 10012604, Edson Maia Rocha, 6.00, 30.00, 36.00 / 10011783, Edson Sobral dos Santos,
13.00, 50.00, 63.00 / 10002047, Eduarda Abreu do Nascimento, 10.00, 40.00, 50.00 / 10010461, Eduarda
Afonso Trindade, 6.00, 34.00, 40.00 / 10002819, Eduarda Correa Amorim, 17.00, 66.00, 83.00 / 10013690,
Eduarda Fabiane Silva Raiol, 6.00, 40.00, 46.00 / 10006983, Eduarda Gabrielle Baia Ferreira, 12.00, 52.00,
64.00 / 10012685, Eduarda Sales de Moura, 14.00, 58.00, 72.00 / 10011683, Eduarda Salviano Pinheiro da
Silva, 11.00, 24.00, 35.00 / 10005492, Eduarda Santiago de Alencar, 13.00, 48.00, 61.00 / 10016772,
Eduardo Abraao Monteiro Feijao, 8.00, 32.00, 40.00 / 10015737, Eduardo Amaral de Moraes, 13.00, 54.00,
67.00 / 10008140, Eduardo de Sousa Sipiao, 8.00, 56.00, 64.00 / 10012271, Eduardo Felipe Silva da Silva,
14.00, 50.00, 64.00 / 10010092, Eduardo Lima da Silva, 8.00, 54.00, 62.00 / 10002985, Eduardo Lima de
Oliveira, 12.00, 62.00, 74.00 / 10002305, Eduardo Lima Oliveira, 10.00, 32.00, 42.00 / 10011424, Eduardo
Mendes Pillar Benchimol, 14.00, 56.00, 70.00 / 10007381, Eduardo Pepe Larrat, 13.00, 64.00, 77.00 /
10001917, Eduardo Pinheiro de Araujo, 10.00, 50.00, 60.00 / 10009972, Eduardo Rebelo da Silva, 8.00,
32.00, 40.00 / 10012515, Eduardo Santana Lins, 11.00, 60.00, 71.00 / 10003010, Eduardo Silva de Oliveira,
11.00, 36.00, 47.00 / 10010347, Eduardo Valente Silva, 12.00, 68.00, 80.00 / 10000452, Eduardo Vinicius
Sousa Salles, 15.00, 50.00, 65.00 / 10009806, Edwin Rocha Moutinho, 10.00, 30.00, 40.00 / 10001800,
Efrem Pereira Pamplona, 8.00, 22.00, 30.00 / 10009944, Efren Branches Galvao, 12.00, 56.00, 68.00 /
10013584, Elaina Sirotheau de Sousa, 11.00, 42.00, 53.00 / 10012629, Elaine Cristina da Silva Rodrigues,
7.00, 38.00, 45.00 / 10015891, Elane Farias dos Santos, 9.00, 50.00, 59.00 / 10012520, Elane Neube Silva
de Oliveira, 9.00, 60.00, 69.00 / 10001774, Elba Maria Silva de Carvalho, 12.00, 56.00, 68.00 / 10011904,
Elber Natalino Neves Souza, 7.00, 28.00, 35.00 / 10005640, Elber Rogerio Damasceno Pinheiro, 10.00,
64.00, 74.00 / 10000738, Elcio Marthan Rodrigues da Costa, 12.00, 40.00, 52.00 / 10001676, Elder de
Carvalho Silva, 12.00, 60.00, 72.00 / 10001921, Elder Douglas de Oliveira Borges, 13.00, 58.00, 71.00 /
10016816, Elder Ferreira da Costa, 7.00, 32.00, 39.00 / 10013751, Elder Miranda de Castro, 12.00, 62.00,
74.00 / 10010206, Eldisnan dos Santos Rosario, 12.00, 64.00, 76.00 / 10012667, Eldo Almeida Luiz, 9.00,
56.00, 65.00 / 10012117, Elem Cristina Santos Pereira, 7.00, 26.00, 33.00 / 10011559, Elenilson Almeida
de Macedo, 6.00, 62.00, 68.00 / 10010595, Elenise Nascimento Lira, 17.00, 70.00, 87.00 / 10016473,
Eleonora Nobrega de Lima, 7.00, 26.00, 33.00 / 10007877, Eliada Cardoso dos Santos, 9.00, 24.00, 33.00
/ 10009272, Eliakim Celestino Barroso, 11.00, 46.00, 57.00 / 10000390, Eliakim dos Santos Costa, 7.00,
54.00, 61.00 / 10010718, Eliakim dos Santos Dinisio, 6.00, 50.00, 56.00 / 10005758, Elian Reis Felgueiras,
10.00, 28.00, 38.00 / 10000380, Eliane Viana Pinto, 9.00, 30.00, 39.00 / 10013172, Eliardson Silva Sousa,
11.00, 52.00, 63.00 / 10005638, Elias Alexandre Lombe de Oliveira, 12.00, 30.00, 42.00 / 10000185, Elias
Araujo de Souza Junior, 10.00, 68.00, 78.00 / 10010167, Elias da Silva Lobato, 10.00, 54.00, 64.00 /
10013438, Elias Fernando Malheiros da Costa Junior, 9.00, 38.00, 47.00 / 10016566, Elias Ibernom
Cavalcantes, 5.00, 34.00, 39.00 / 10002251, Elias Mateus Alves Pereira, 11.00, 38.00, 49.00 / 10006925,
Elias Santos Marques, 10.00, 70.00, 80.00 / 10000580, Eliase da Silva Barbosa, 12.00, 62.00, 74.00 /
10002596, Elice Oliveira Lobo, 9.00, 40.00, 49.00 / 10011246, Elida Vanice Ribeiro Gomes, 10.00, 44.00,
54.00 / 10011404, Eliel Rezendes Nascimento, 11.00, 44.00, 55.00 / 10000406, Elielson Raone Mesquita
da Costa, 9.00, 32.00, 41.00 / 10001025, Elienay Santos Barbosa, 11.00, 68.00, 79.00 / 10000360, Eliezer
Silva Soares, 12.00, 60.00, 72.00 / 10016065, Eline Araujo Souza Barreira, 15.00, 50.00, 65.00 / 10000215,
 
Elisa Cristina Soares Borges, 8.00, 44.00, 52.00 / 10016660, Elisvam Fernando de Sousa Oliveira, 6.00,
40.00, 46.00 / 10000053, Elivaldo Pereira Ribeiro, 13.00, 60.00, 73.00 / 10016709, Eliza Roso Danin
Franco, 8.00, 42.00, 50.00 / 10016554, Elizabeth Dwan Favacho do Nascimento, 7.00, 44.00, 51.00 /
10000011, Elizabeth Lopes Bitencourt, 12.00, 60.00, 72.00 / 10000864, Elizabeth Parente e Silva de
Medeiros, 12.00, 68.00, 80.00 / 10000650, Elizangela Rodrigues Pereira, 10.00, 60.00, 70.00 / 10001087,
Ellen Alves Aranha de Sousa, 11.00, 52.00, 63.00 / 10001137, Ellen Carla Silva Nascimento, 8.00, 28.00,
36.00 / 10013654, Ellen Chistiny dos Santos Caldas, 9.00, 38.00, 47.00 / 10011180, Ellen Cristina Alves
Alvarena, 10.00, 44.00, 54.00 / 10009548, Ellen Fernanda Ferreira Vale, 5.00, 32.00, 37.00 / 10001548,
Ellen Kamila Melo de Oliveira, 7.00, 44.00, 51.00 / 10005738, Ellen Vanessa Nunes Gomes Pereira, 14.00,
48.00, 62.00 / 10017075, Ellis D Angeles Noronha Matins, 7.00, 38.00, 45.00 / 10013012, Elmer John de
Abreu Lessa, 10.00, 38.00, 48.00 / 10012771, Eloisa de Jesus Silva Amaral, 8.00, 48.00, 56.00 / 10011712,
Eloisa Paiva Oliveira, 14.00, 48.00, 62.00 / 10011881, Elora Patricia Monteiro da Silva, 6.00, 42.00, 48.00
/ 10010758, Elton Evangelistra Quintos de Oliveira, 10.00, 32.00, 42.00 / 10001126, Elton Ferreira
Monteiro, 15.00, 52.00, 67.00 / 10013652, Elton Jose da Silva Aguiar, 13.00, 44.00, 57.00 / 10001125,
Elton Silva de Moraes, 9.00, 38.00, 47.00 / 10011393, Elton Tobias Conte Lima, 6.00, 46.00, 52.00 /
10002649, Elvis Amaral Diniz, 10.00, 44.00, 54.00 / 10012188, Elvis Andre Marinho Vidal, 12.00, 54.00,
66.00 / 10011123, Elyandra Leal Macedo, 8.00, 40.00, 48.00 / 10012892, Emanoel Filipe Medeiros de
Castro, 3.00, 20.00, 23.00 / 10001615, Emanoel Mariano Castro, 7.00, 28.00, 35.00 / 10011175, Emanoelle
Nazare Vinhas, 10.00, 56.00, 66.00 / 10015814, Emanuel Pedro Silva Goncalves, 11.00, 32.00, 43.00 /
10016538, Emanuel Silva Carvalho, 8.00, 50.00, 58.00 / 10013133, Emanuel Vitor Belo Amaral, 11.00,
52.00, 63.00 / 10001197, Emanuel Zico Barroso da Silva, 10.00, 40.00, 50.00 / 10013371, Emanuele
Machado Barbosa, 6.00, 20.00, 26.00 / 10015921, Emanuelle Lira Pereira, 7.00, 52.00, 59.00 / 10007377,
Emanuelle Santos Gato de Oliveira, 8.00, 56.00, 64.00 / 10003068, Emanuelly Santos Dias, 7.00, 40.00,
47.00 / 10005779, Emelly Raissa da Silva Neves, 6.00, 26.00, 32.00 / 10013619, Emerson Andre Souza da
Silva, 10.00, 40.00, 50.00 / 10001043, Emerson de Souza Fonseca, 9.00, 60.00, 69.00 / 10001325, Emerson
Junio Monteiro Furtado, 15.00, 62.00, 77.00 / 10001536, Emerson Lucas Teto Joaquim, 7.00, 44.00, 51.00
/ 10002855, Emerson Mota Fernandes, 11.00, 70.00, 81.00 / 10000190, Emerson Santos Machado da Silva,
11.00, 54.00, 65.00 / 10001701, Emille Mayza de Moraes Monteiro, 10.00, 32.00, 42.00 / 10016168, Emilly
Carolaine Guimaraes Ferreira, 7.00, 32.00, 39.00 / 10015962, Emilly Rodrigues Gomes, 10.00, 58.00, 68.00
/ 10007017, Emily Agda Lima Ludovico, 9.00, 32.00, 41.00 / 10012325, Emily Kisley do Amaral Ferreira,
13.00, 62.00, 75.00 / 10000725, Emmyle Kelve dos Santos Reis, 7.00, 44.00, 51.00 / 10011875, Emylle
Kerolen Souza de Moraes, 7.00, 20.00, 27.00 / 10012358, Enderson Melo Rodrigues de Sousa, 8.00, 52.00,
60.00 / 10001328, Eniane Talita Gomes Magalhaes, 15.00, 54.00, 69.00 / 10001828, Enio Luiz Santos Dias,
13.00, 52.00, 65.00 / 10010729, Enos dos Santos Ferreira, 9.00, 34.00, 43.00 / 10010258, Enzo Martins
Wanderbrock, 8.00, 48.00, 56.00 / 10016584, Eric Henrique Lobato Duarte, 9.00, 46.00, 55.00 / 10006710,
Erica Alcina Santos da Silva, 11.00, 32.00, 43.00 / 10016079, Erica Romano Esteves, 12.00, 62.00, 74.00
/ 10006798, Erica Thalicia Silva da Rocha, 10.00, 46.00, 56.00 / 10003046, Erick Aguiar Gomes, 14.00,
68.00, 82.00 / 10007675, Erick Alayr Meireles Costa, 11.00, 24.00, 35.00 / 10016267, Erick Bouth Lopes,
14.00, 56.00, 70.00 / 10012184, Erick Brendow Silva Brasil, 9.00, 40.00, 49.00 / 10001166, Erick da Costa
Rodrigues, 12.00, 58.00, 70.00 / 10006752, Erick Henrique Gaia da Silva, 9.00, 40.00, 49.00 / 10008238,
Erick Souza Machado, 10.00, 34.00, 44.00 / 10010640, Ericlis Gabriel Cunha Silva Morais, 11.00, 54.00,
65.00 / 10010274, Erielton Lobato Brito, 10.00, 66.00, 76.00 / 10013732, Erik Pinheiro Barbosa, 8.00,
34.00, 42.00 / 10016769, Erik Rangel Pinheiro Casanova, 9.00, 50.00, 59.00 / 10000836, Erik Silva, 10.00,
56.00, 66.00 / 10015795, Erika Daianny Cardoso Araujo, 11.00, 48.00, 59.00 / 10012922, Erika Giovana
Trindade Brito, 10.00, 42.00, 52.00 / 10002271, Erlan da Silva Lima, 14.00, 56.00, 70.00 / 10002556,
Erlando Silva de Medeiros, 12.00, 68.00, 80.00 / 10001661, Ernilson Rodrigues da Silva Junior, 15.00,
48.00, 63.00 / 10001084, Eryka Vanessa Carvalho de Araujo, 11.00, 52.00, 63.00 / 10001986, Esau Thiago
Tavares Chagas, 9.00, 50.00, 59.00 / 10013647, Esmeralda Nonato Nascimento, 7.00, 18.00, 25.00 /
10010983, Estanislau Pereira Lobo Neto, 6.00, 64.00, 70.00 / 10016008, Estefane Kelly Silva de Souza,
13.00, 46.00, 59.00 / 10000565, Estefani da Costa Medeiros, 9.00, 54.00, 63.00 / 10000478, Estefany
Caroline Monteiro Duarte, 9.00, 44.00, 53.00 / 10015841, Esteffanny Furtado Frazao, 8.00, 48.00, 56.00 /
10000634, Ester da Conceicao Siqueira, 9.00, 66.00, 75.00 / 10010365, Ester Moreira da Silva, 11.00,
 
46.00, 57.00 / 10000112, Ester Silveira Lima Neto, 6.00, 24.00, 30.00 / 10016181, Estevao Paulo Ribeiro
da Silva, 10.00, 64.00, 74.00 / 10011050, Esther da Silva Santos, 2.00, 12.00, 14.00 / 10002381, Eudoxon
Costa Camilo, 8.00, 50.00, 58.00 / 10016009, Euller Sousa Gomes, 13.00, 42.00, 55.00 / 10002569, Eunna
Karolyne Camarotta dos Santos, 4.00, 12.00, 16.00 / 10013296, Evair Elian Alves Freitas, 7.00, 38.00,
45.00 / 10012324, Evaldo Mycael Costa de Sousa, 12.00, 52.00, 64.00 / 10011178, Evandro Bentes Lima,
8.00, 52.00, 60.00 / 10012726, Evandro Carneiro Sozinho Souza, 9.00, 38.00, 47.00 / 10013407, Evandro
da Silva Cavalcante Junior, 11.00, 38.00, 49.00 / 10000271, Evany Pinheiro Salomao, 11.00, 56.00, 67.00
/ 10013323, Evellyn Nayla Borges Sobrinho, 13.00, 70.00, 83.00 / 10001602, Evelyn de Vasconcelos
Batista, 14.00, 54.00, 68.00 / 10010807, Evelyn Moraes de Albuquerque, 10.00, 32.00, 42.00 / 10005359,
Evelyn Munarini Gualberto, 13.00, 44.00, 57.00 / 10010765, Evelyn Vitoria Camarotta dos Santos, 9.00,
46.00, 55.00 / 10013728, Everson Taffarel Correa Santana, 7.00, 40.00, 47.00 / 10011031, Everson
Wanrley Sousa Ribeiro, 14.00, 32.00, 46.00 / 10012460, Everton Danrley Sousa Ribeiro, 11.00, 46.00,
57.00 / 10005406, Everton Gomes de Oliveira, 9.00, 54.00, 63.00 / 10011068, Everton Jorge Gomes da
Silva, 8.00, 48.00, 56.00 / 10001115, Everton Juan Santos Brito, 10.00, 56.00, 66.00 / 10011812, Evilly
Ribeiro Almada, 6.00, 26.00, 32.00 / 10002073, Ewerthon Cruz Ribeiro, 12.00, 62.00, 74.00 / 10006754,
Ewerton Bruno Magno dos Santos, 7.00, 32.00, 39.00 / 10011441, Expedito Almeida dos Santos, 9.00,
50.00, 59.00 / 10010424, Ezabele Mota Moreira, 7.00, 28.00, 35.00 / 10015986, Ezequiel da Silva Sousa,
12.00, 68.00, 80.00 / 10011819, Ezequiel Miranda Petronilo, 6.00, 32.00, 38.00 / 10005291, Fabia Helen
Botelho Lopes, 6.00, 36.00, 42.00 / 10002921, Fabiana Costa, 3.00, 22.00, 25.00 / 10009712, Fabiana
Moreira Pinto, 9.00, 44.00, 53.00 / 10017087, Fabiana Sarges Silva, 8.00, 28.00, 36.00 / 10016235, Fabiana
Varela dos Santos, 10.00, 46.00, 56.00 / 10000376, Fabianne Suellen da Silva Bastos, 8.00, 42.00, 50.00 /
10012939, Fabianny Leticia Cardoso de Souza, 12.00, 48.00, 60.00 / 10007078, Fabiano Junior da Silva,
10.00, 54.00, 64.00 / 10002645, Fabiano Pedro da Silva, 12.00, 60.00, 72.00 / 10012388, Fabienny Gomes
de Oliveira, 8.00, 34.00, 42.00 / 10008133, Fabine Elen Silva Sousa, 9.00, 54.00, 63.00 / 10016264, Fabio
Alex Silva Conduru Junior, 7.00, 46.00, 53.00 / 10007682, Fabio Alves Feitosa Junior, 4.00, 34.00, 38.00
/ 10007912, Fabio Bernardes Batista, 9.00, 46.00, 55.00 / 10012587, Fabio Bruno Sozinho de Holanda,
7.00, 44.00, 51.00 / 10016482, Fabio de Azevedo Taveira Junior, 8.00, 26.00, 34.00 / 10007319, Fabio de
Melo Auad da Silveira, 9.00, 46.00, 55.00 / 10016536, Fabio Dirlan Souza Neves, 6.00, 28.00, 34.00 /
10011923, Fabio Henrique Costa Nascimento, 11.00, 40.00, 51.00 / 10000868, Fabio Henrique da Silva
Teobaldo, 5.00, 32.00, 37.00 / 10012833, Fabio Jose Goncalves do Espirito Santo, 13.00, 52.00, 65.00 /
10010250, Fabio Laranjeira Aragao, 9.00, 36.00, 45.00 / 10012037, Fabio Lucas Alves da Silva, 8.00,
48.00, 56.00 / 10016847, Fabio Oliveira da Silva, 11.00, 52.00, 63.00 / 10006977, Fabio Silva de Oliveira,
7.00, 34.00, 41.00 / 10011955, Fabio Soares Almeida, 10.00, 48.00, 58.00 / 10015726, Fabio Souza da
Costa, 8.00, 32.00, 40.00 / 10016013, Fabio Victor Silva Seade, 6.00, 22.00, 28.00 / 10000320, Fabricia
Maiath de Souza Silva, 4.00, 34.00, 38.00 / 10010791, Fabricio Assuncao de Andrade, 6.00, 42.00, 48.00 /
10001004, Fabricio Lopes da Silva, 10.00, 36.00, 46.00 / 10013147, Fabricio Luiz Matos Boucao, 9.00,
36.00, 45.00 / 10003061, Fabricio Nascimento de Oliveira, 10.00, 40.00, 50.00 / 10013446, Fabricio
Nazario de Lima, 8.00, 62.00, 70.00 / 10011562, Fabricio Nogueira Feitosa, 9.00, 54.00, 63.00 / 10005364,
Fabricio Quaresma de Sousa, 14.00, 62.00, 76.00 / 10007431, Fabricio Rodrigues Arruda, 15.00, 56.00,
71.00 / 10002118, Fabricio Rodrigues de Azevedo, 17.00, 54.00, 71.00 / 10007074, Fabricio Silva dos Reis,
6.00, 28.00, 34.00 / 10007054, Fabricio Slando da Silva Mendes, 10.00, 50.00, 60.00 / 10016019, Fabricio
Soares dos Santos, 13.00, 46.00, 59.00 / 10012920, Fabricio Souza do Nascimento, 11.00, 56.00, 67.00 /
10010528, Fagner Pereira Teodosio, 13.00, 46.00, 59.00 / 10009493, Fagner Wemerson da Silva, 13.00,
50.00, 63.00 / 10013042, Falon Demes Goncalves, 8.00, 50.00, 58.00 / 10001005, Fayla Sousa dos Santos,
13.00, 60.00, 73.00 / 10002657, Feliciano Bruno Galdino Patricio, 7.00, 52.00, 59.00 / 10016822, Felipe
Antonio Gualberto Bernardes, 12.00, 50.00, 62.00 / 10009715, Felipe Arthur da Silva Nogueira, 1.00,
44.00, 45.00 / 10002151, Felipe Augusto Goes de Almeida, 6.00, 36.00, 42.00 / 10013618, Felipe Augusto
Monteiro Saraiva, 8.00, 36.00, 44.00 / 10011906, Felipe Barroso de Mendonca, 12.00, 42.00, 54.00 /
10007909, Felipe Caetano Santos Pereira, 13.00, 62.00, 75.00 / 10001657, Felipe da Silva Alves, 11.00,
50.00, 61.00 / 10010760, Felipe Daniel Santos Brasil, 11.00, 48.00, 59.00 / 10009952, Felipe de Souza
Amaral Lara, 10.00, 44.00, 54.00 / 10011224, Felipe dos Santos Souza, 10.00, 40.00, 50.00 / 10007753,
Felipe Feliciano Silva Rodrigues, 9.00, 60.00, 69.00 / 10005565, Felipe Fiares Lacerda, 4.00, 24.00, 28.00
 
/ 10003091, Felipe Fonseca de Sousa, 6.00, 14.00, 20.00 / 10012681, Felipe Leonardo Alves de Andrade,
10.00, 24.00, 34.00 / 10005643, Felipe Miranda Paiva, 6.00, 24.00, 30.00 / 10000704, Felipe Rocha Silva,
10.00, 60.00, 70.00 / 10016007, Felipe Santos Souza, 8.00, 54.00, 62.00 / 10010352, Felipe Seabra dos
Santos Barreto, 12.00, 46.00, 58.00 / 10011769, Felipe Sena Fontoura, 8.00, 30.00, 38.00 / 10013091,
Felipe Silva Ferreira, 9.00, 32.00, 41.00 / 10008207, Felipe Silva Nunes, 7.00, 44.00, 51.00 / 10017062,
Felipe Sousa da Silva, 9.00, 64.00, 73.00 / 10016278, Felipe Tavares Nascimento, 6.00, 40.00, 46.00 /
10011267, Felipe Thiago de Carvalho Soares, 14.00, 60.00, 74.00 / 10007080, Felippe Silva dos Reis, 7.00,
50.00, 57.00 / 10010217, Fellipe de Sousa Pantoja, 13.00, 64.00, 77.00 / 10000925, Fellipe Henrique
Nogueira Reis, 6.00, 36.00, 42.00 / 10007433, Fellype Grandet Silva do Rosario, 10.00, 60.00, 70.00 /
10015940, Fernanda Andressa Albuquerque Moraes, 11.00, 38.00, 49.00 / 10001269, Fernanda Cruz da
Costa, 10.00, 46.00, 56.00 / 10010236, Fernanda Danielle Amorim Pereira, 7.00, 24.00, 31.00 / 10008118, Fernanda de Fatima Rotschild e Souza Maximo, 9.00, 46.00, 55.00 / 10009416, Fernanda de Oliveira Silva, 11.00, 48.00, 59.00 / 10009445, Fernanda de Souza Alvarenga Rodrigues, 15.00, 70.00, 85.00 / 10016284,
Fernanda do Nascimento Dias, 8.00, 50.00, 58.00 / 10000971, Fernanda Farias Figueiredo, 13.00, 50.00,
63.00 / 10016171, Fernanda Gabriela Oliveira Gavinho, 14.00, 34.00, 48.00 / 10000985, Fernanda
Goudinho Pantoja, 8.00, 40.00, 48.00 / 10012582, Fernanda Lina Pena de Miranda Muiva, 13.00, 50.00,
63.00 / 10002399, Fernanda Paula da Silva Araujo Saraiva, 10.00, 52.00, 62.00 / 10005413, Fernanda Pires
de Albuquerque, 11.00, 48.00, 59.00 / 10005695, Fernanda Rodrigues Soares, 4.00, 34.00, 38.00 /
10011887, Fernanda Tavares Pinheiro, 10.00, 48.00, 58.00 / 10012912, Fernando Campos Nazare, 12.00,
52.00, 64.00 / 10002040, Fernando Carlos Teixeira de Rezende Junior, 7.00, 24.00, 31.00 / 10011093,
Fernando Cezar Silva de Lima, 11.00, 60.00, 71.00 / 10001296, Fernando da Silva Lima, 5.00, 34.00, 39.00
/ 10010910, Fernando de Oliveira Travassos, 15.00, 42.00, 57.00 / 10007957, Fernando dos Santos Rocha,
15.00, 58.00, 73.00 / 10016385, Fernando Fonseca Silva, 10.00, 26.00, 36.00 / 10013101, Fernando Lopes
Mendes da Silva, 9.00, 32.00, 41.00 / 10013182, Fernando Pinheiro Monteiro, 13.00, 38.00, 51.00 /
10001664, Fernando Santos Paixao, 10.00, 38.00, 48.00 / 10007984, Fernando Vinicius Cardoso Sarquis,
9.00, 44.00, 53.00 / 10009656, Filipe Andre de Abreu Barbosa, 9.00, 44.00, 53.00 / 10016702, Filipe
Oliveira Marques, 10.00, 46.00, 56.00 / 10010287, Filipe Pimentel Povoa, 11.00, 54.00, 65.00 / 10009831,
Filipe Ruan dos Santos Ribeiro, 10.00, 50.00, 60.00 / 10001331, Filipe Silva Oliveira, 7.00, 46.00, 53.00 /
10001928, Fillipe Pimentel da Paixao, 12.00, 60.00, 72.00 / 10012878, Flavia Alessandra Santos Tavares,
5.00, 44.00, 49.00 / 10011569, Flavia Augusta da Silva Paes, 9.00, 46.00, 55.00 / 10012657, Flavia Mendes
de Araujo, 11.00, 60.00, 71.00 / 10001659, Flavia Valesca Pereira de Queiroz, 11.00, 52.00, 63.00 /
10000537, Flaviano de Oliveira Pinto Junior, 6.00, 28.00, 34.00 / 10011534, Flavio Curcino da Silva, 13.00,
66.00, 79.00 / 10012104, Flavio da Silva de Moura, 8.00, 38.00, 46.00 / 10011155, Flavio Franco do Vale,
8.00, 44.00, 52.00 / 10000984, Flavio Henrique Cruz de Sousa, 11.00, 36.00, 47.00 / 10000461, Flavio
Vinicius Pereira Oliveira, 14.00, 48.00, 62.00 / 10001561, Franc Bernardo Lira Dantas, 9.00, 30.00, 39.00
/ 10000222, Franciele Cabral Rodrigues, 14.00, 48.00, 62.00 / 10012262, Franciely Milene Braga Cruz,
8.00, 30.00, 38.00 / 10002198, Francisco Alberto Ribeiro Machado, 11.00, 54.00, 65.00 / 10007870,
Francisco Carlos Rocha, 16.00, 54.00, 70.00 / 10015763, Francisco da Silva Costa, 3.00, 58.00, 61.00 /
10007353, Francisco de Assis Pereira Pinheiro, 14.00, 60.00, 74.00 / 10000700, Francisco Fabio Conde
Reis, 12.00, 52.00, 64.00 / 10001058, Francisco Gleyson de Sousa Santos, 9.00, 34.00, 43.00 / 10000555, Francisco Henrique Marques Vitorino de Oliveira, 12.00, 66.00, 78.00 / 10000061, Francisco Hugo Bezerra Dantas, 9.00, 42.00, 51.00 / 10011674, Francisco Jean Guimaraes Teixeira, 7.00, 44.00, 51.00 / 10016471, Francisco Lucas de Sousa Araujo, 7.00, 40.00, 47.00 / 10000197, Francisco Milton Alves da Costa Junior, 5.00, 44.00, 49.00 / 10002839, Francisco Nascimento Silva, 10.00, 58.00, 68.00 / 10009755, Francisco
Pantoja Neto, 11.00, 58.00, 69.00 / 10002070, Francisco Silva do Nascimento, 7.00, 56.00, 63.00 /
10002193, Francisco Silva Lima, 9.00, 52.00, 61.00 / 10016762, Francisco Tiago Pereira Lopes, 9.00,
50.00, 59.00 / 10013742, Francisco Vanderlei Coutinho da Silva, 13.00, 50.00, 63.00 / 10010918,
Francismar Macedo de Oliveira, 6.00, 56.00, 62.00 / 10007969, Francismira Oliveira da Cruz, 8.00, 20.00,
28.00 / 10001483, Francivan do Espirito Santo, 11.00, 50.00, 61.00 / 10015746, Franco Silva, 8.00, 44.00,
52.00 / 10011669, Frank Douglas da Silva de Sena, 7.00, 28.00, 35.00 / 10003035, Frank Rodrigues, 3.00,
28.00, 31.00 / 10007064, Frank Ronaldo Araujo Costa Junior, 9.00, 36.00, 45.00 / 10016736, Frankdavison
Brilhante Pixuna, 6.00, 50.00, 56.00 / 10009954, Frederico Campos e Santos, 12.00, 58.00, 70.00 /
 
10010989, Frederico de Jesus Aguiar, 18.00, 66.00, 84.00 / 10001574, Fredys Henrique Lica da Silva, 9.00,
42.00, 51.00 / 10009713, Gabriel Alex Sousa de Araujo, 8.00, 54.00, 62.00 / 10005752, Gabriel Augusto
Barros Roberto, 14.00, 60.00, 74.00 / 10009681, Gabriel Augusto Dourado dos Santos Ferreira, 8.00, 40.00,
48.00 / 10011528, Gabriel Barreiros Cavalcante, 10.00, 38.00, 48.00 / 10010939, Gabriel Barreiros da
Silva, 10.00, 52.00, 62.00 / 10010530, Gabriel Barros Cunha, 12.00, 44.00, 56.00 / 10001048, Gabriel
Botelho, 8.00, 52.00, 60.00 / 10016547, Gabriel Cayna Souto de Souza, 7.00, 38.00, 45.00 / 10000282,
Gabriel Costa de Almeida, 8.00, 32.00, 40.00 / 10003147, Gabriel da Silva Carneiro Cavalcante, 7.00,
58.00, 65.00 / 10017014, Gabriel da Silva Goncalves do Espirito Santo, 12.00, 60.00, 72.00 / 10000206,
Gabriel Danilo Silva Matos, 13.00, 48.00, 61.00 / 10000615, Gabriel Dolzany Cartagenes, 11.00, 62.00,
73.00 / 10011162, Gabriel dos Santos Fernandes, 12.00, 48.00, 60.00 / 10001167, Gabriel Evan Zeggai
Lambert Filho, 14.00, 58.00, 72.00 / 10001241, Gabriel Felipe Costa Brasileiro, 13.00, 56.00, 69.00 /
10012543, Gabriel Felipe Petry, 7.00, 54.00, 61.00 / 10016562, Gabriel Fernando dos Santos Nunes, 10.00,
44.00, 54.00 / 10010739, Gabriel Helberth Costa da Silva, 9.00, 72.00, 81.00 / 10010536, Gabriel Henrique
Barbosa Lima, 8.00, 46.00, 54.00 / 10010515, Gabriel Henrique Gama Macedo, 12.00, 54.00, 66.00 /
10010606, Gabriel Melo Gomes, 10.00, 60.00, 70.00 / 10008180, Gabriel Mendes Moura, 4.00, 30.00,
34.00 / 10013355, Gabriel Monteiro Rodrigues, 14.00, 48.00, 62.00 / 10005786, Gabriel Moraes Barreiros,
17.00, 46.00, 63.00 / 10009293, Gabriel Negrao Silva, 7.00, 38.00, 45.00 / 10010472, Gabriel Ortega Lopes
Sousa, 9.00, 40.00, 49.00 / 10005224, Gabriel Rodrigues Barata, 9.00, 46.00, 55.00 / 10002288, Gabriel
Rodrigues de Almeida, 15.00, 62.00, 77.00 / 10016078, Gabriel Targino Silva, 11.00, 54.00, 65.00 /
10000274, Gabriel Torres Lima, 10.00, 42.00, 52.00 / 10000160, Gabriel Victor dos Reis Silva, 14.00,
72.00, 86.00 / 10002093, Gabriel Wanderley dos Santos, 11.00, 48.00, 59.00 / 10013624, Gabriela
Alexandre do Espirito Santo, 8.00, 24.00, 32.00 / 10010382, Gabriela Araujo Dias, 11.00, 54.00, 65.00 /
10002080, Gabriela Brito Ferreira, 9.00, 68.00, 77.00 / 10007826, Gabriela Caroline Baars Dantas dos
Santos, 8.00, 54.00, 62.00 / 10007555, Gabriela de Almeida Silva, 10.00, 60.00, 70.00 / 10006981, Gabriela
Dias de Sousa, 10.00, 30.00, 40.00 / 10007548, Gabriela Faustino, 12.00, 62.00, 74.00 / 10016126, Gabriela
Kizam de Souza Chaves, 9.00, 42.00, 51.00 / 10016426, Gabriela Lobato Tito, 9.00, 32.00, 41.00 /
10013073, Gabriela Reis Coelho dos Santos, 10.00, 58.00, 68.00 / 10002938, Gabriela Rodrigues da Silva,
7.00, 36.00, 43.00 / 10011813, Gabriela Silva dos Santos, 14.00, 64.00, 78.00 / 10000596, Gabriela Silveira
de Barros, 4.00, 32.00, 36.00 / 10007894, Gabriella de Almeida Correa, 7.00, 30.00, 37.00 / 10010649,
Gabriella Marques da Silva, 12.00, 36.00, 48.00 / 10012991, Gabriella Pereira Araujo do Nascimento, 9.00,
24.00, 33.00 / 10000088, Gabriella Souto Negrao, 9.00, 54.00, 63.00 / 10001658, Gabrielle Andrade de
Carvalho, 9.00, 48.00, 57.00 / 10015836, Gabrielle Ganassoli, 8.00, 46.00, 54.00 / 10012287, Gabrielli
Moraes Pinto, 7.00, 26.00, 33.00 / 10000994, Gabrielly Almeida Prado Lordeiro, 13.00, 42.00, 55.00 /
10012746, Gabrielly Bezerra Lopes, 15.00, 54.00, 69.00 / 10000728, Gean Barros da Silva, 8.00, 34.00,
42.00 / 10013591, Gean di Laserna Guevara Souza Rodrigues, 11.00, 48.00, 59.00 / 10007351, Geiciane
Alves de Brito Castro, 4.00, 18.00, 22.00 / 10000906, Geize Maria Pinto da Costa, 10.00, 30.00, 40.00 /
10011893, Genesio Rodrigues de Queiroga Neto, 13.00, 54.00, 67.00 / 10010205, Genilson Arnaud da
Silva, 5.00, 48.00, 53.00 / 10016360, Genivaldo Silva dos Santos Junior, 6.00, 32.00, 38.00 / 10007393,
Geofre de Sousa Freires, 7.00, 52.00, 59.00 / 10012085, Geoliany Candida Goncalves Araujo, 9.00, 30.00,
39.00 / 10002999, George da Silva Lima, 12.00, 54.00, 66.00 / 10007125, Geovana da Silva Azevedo,
10.00, 48.00, 58.00 / 10000266, Geovana de Souza Leal, 11.00, 50.00, 61.00 / 10002038, Geovana Glenda
Moraes Souza, 8.00, 26.00, 34.00 / 10003208, Geovane de Lima Lopes, 12.00, 62.00, 74.00 / 10011097,
Geovane Fonseca Cardias, 14.00, 52.00, 66.00 / 10016059, Geovanna de Oliveira Araujo, 10.00, 58.00,
68.00 / 10013309, Geovanna Nunes Narciso, 8.00, 28.00, 36.00 / 10009947, Geovanny Ribeiro Dantas,
15.00, 66.00, 81.00 / 10009422, Geraldo Gomes Cunha, 11.00, 52.00, 63.00 / 10015748, Gerardo Marinho
Lopes Filho, 8.00, 32.00, 40.00 / 10013720, Gerson Braga de Moura, 6.00, 48.00, 54.00 / 10010407, Gerson
Carlos Santos Silva Sobrinho, 9.00, 44.00, 53.00 / 10007726, Gerson Queiroz Franco Monteiro, 17.00,
54.00, 71.00 / 10010041, Gerson Ribeiro Cavalcante Filho, 6.00, 42.00, 48.00 / 10009498, Gessica Kellem
Araujo Carneiro, 8.00, 36.00, 44.00 / 10010817, Gessica Policena Silva Abreu, 10.00, 54.00, 64.00 /
10007815, Gessica Taina dos Santos Cruz, 15.00, 72.00, 87.00 / 10001056, Gessyka Gabrielly Abreu de
Oliveira, 10.00, 36.00, 46.00 / 10009975, Gian Carlo Magela Cabral Falcao, 12.00, 52.00, 64.00 /
10010474, Gianluca Quaresma Alves, 10.00, 50.00, 60.00 / 10013238, Gil Fabio Cordeiro Lobato
 
Rodrigues, 8.00, 24.00, 32.00 / 10001395, Gilberto Leal de Azevedo Junior, 10.00, 36.00, 46.00 /
10010936, Gilde Ferran Lopes Pacheco, 6.00, 26.00, 32.00 / 10010652, Gildete Pompeu Moreira, 9.00,
34.00, 43.00 / 10005254, Gilmar Jose Bogo, 15.00, 60.00, 75.00 / 10000526, Gilmar Pereira Carvalho,
8.00, 42.00, 50.00 / 10010537, Gilson da Silva Trindade, 8.00, 50.00, 58.00 / 10002846, Gilson Nery Farias,
12.00, 52.00, 64.00 / 10006985, Gilvan Erick Marinho Morais, 10.00, 44.00, 54.00 / 10001756, Giovana
Coelho Gomes, 7.00, 26.00, 33.00 / 10012750, Giovana Edmea Pereira Azevedo, 12.00, 40.00, 52.00 /
10008182, Giovana Paoletti Monteiro da Silva, 11.00, 66.00, 77.00 / 10013531, Giovani da Silva Teixeira,
10.00, 46.00, 56.00 / 10008141, Giovani Welker de Lima Lopes, 13.00, 64.00, 77.00 / 10000790, Giovanna
Cristina Cardoso de Almeida, 11.00, 46.00, 57.00 / 10015854, Giovanna Maria Moura Rocha, 12.00, 66.00,
78.00 / 10010934, Giovanna Semblano Vieira Oliveira, 7.00, 52.00, 59.00 / 10011113, Giovanna Silva da
Silva, 11.00, 38.00, 49.00 / 10000764, Giovanni Trindade Santos, 14.00, 64.00, 78.00 / 10016855, Gisela
Souza de Souza, 8.00, 44.00, 52.00 / 10007073, Gisella Lima Ferreira, 10.00, 32.00, 42.00 / 10001373,
Giselle Rodrigues Fontoura, 8.00, 70.00, 78.00 / 10000616, Gisely Caroline da Silva Carvalho, 14.00,
54.00, 68.00 / 10009951, Gislane Cardoso Pereira, 13.00, 54.00, 67.00 / 10005648, Giulliano Eduardo
Alves dos Santos, 12.00, 64.00, 76.00 / 10006707, Glauber Fernando da Silva, 12.00, 58.00, 70.00 /
10009348, Glauber Jose Bueno, 9.00, 48.00, 57.00 / 10007311, Glaucia Izabela Silva de Sousa, 7.00, 32.00,
39.00 / 10007242, Gledson Diogenes dos Santos, 15.00, 46.00, 61.00 / 10016985, Gleidson Kleber Brandao
Nascimento, 9.00, 44.00, 53.00 / 10011425, Gleidson Vilhena da Silva, 12.00, 54.00, 66.00 / 10010180,
Glenda Glayce Pereira Rodrigues, 10.00, 32.00, 42.00 / 10009355, Glenda Gleyce Siqueira Menezes, 7.00,
24.00, 31.00 / 10011314, Glenda Karen Santos da Paixao, 10.00, 46.00, 56.00 / 10011247, Glenda Layana
Lira Moraes, 10.00, 58.00, 68.00 / 10009841, Glenda Raphaella de Sousa Nogueira, 8.00, 40.00, 48.00 /
10009704, Gleyce Matos Vieira Cambui, 4.00, 20.00, 24.00 / 10012395, Gleyce Miranda Ferreira, 6.00,
22.00, 28.00 / 10012494, Gleydson Albert Jorge Medeiros, 16.00, 60.00, 76.00 / 10001252, Gleydson
Antonio da Costa Melendez Alves, 15.00, 56.00, 71.00 / 10007955, Gothero Lucia Gomes da Silva, 6.00,
26.00, 32.00 / 10000307, Graziela Lopes de Sousa Carvalho, 14.00, 50.00, 64.00 / 10005484, Graziela Vital
Santos, 12.00, 42.00, 54.00 / 10000850, Gregorio Taumaturgo Amoury Ferreira, 4.00, 24.00, 28.00 /
10003141, Guilherme Aristides Dantas Furtado, 8.00, 34.00, 42.00 / 10002451, Guilherme Barbosa da
Silva, 12.00, 58.00, 70.00 / 10012122, Guilherme Bertipalha Vieira, 14.00, 62.00, 76.00 / 10016663,
Guilherme Castro Braga, 6.00, 44.00, 50.00 / 10010279, Guilherme da Silva, 12.00, 48.00, 60.00 /
10012505, Guilherme Henrique de Sousa Moreira Pessoa, 8.00, 44.00, 52.00 / 10010604, Guilherme
Henrique Dornellas Andrade, 10.00, 26.00, 36.00 / 10011869, Guilherme Lima Reis, 17.00, 52.00, 69.00 /
10002907, Guilherme Lima Sousa, 14.00, 42.00, 56.00 / 10016123, Guilherme Matos Oliveira, 14.00,
54.00, 68.00 / 10006716, Guilherme Moreira de Jesus Andrade, 9.00, 48.00, 57.00 / 10006717, Guilherme
Moreira Rodrigues, 11.00, 54.00, 65.00 / 10002563, Guilherme Silva Ferreira Botelho, 10.00, 66.00, 76.00
/ 10007307, Guilherme Tavares Monteiro, 10.00, 46.00, 56.00 / 10001396, Guilherme Torquato Araujo,
10.00, 60.00, 70.00 / 10012344, Guilherme Viana de Souza Marques, 9.00, 40.00, 49.00 / 10007298,
Guilherme Vieira da Silva, 8.00, 28.00, 36.00 / 10001088, Gustavo Abreu Monteiro, 4.00, 28.00, 32.00 /
10012017, Gustavo Albuquerque da Silva, 10.00, 30.00, 40.00 / 10009671, Gustavo Cesar Parreao, 11.00,
50.00, 61.00 / 10011707, Gustavo de Sousa da Silva, 13.00, 42.00, 55.00 / 10007001, Gustavo do
Nascimento Rodrigues, 11.00, 42.00, 53.00 / 10010504, Gustavo Enrique Alves dos Santos, 8.00, 24.00,
32.00 / 10000497, Gustavo Enrique Pereira Veloso, 9.00, 36.00, 45.00 / 10001232, Gustavo Garcia da
Silva, 15.00, 50.00, 65.00 / 10001218, Gustavo Goncalves Alves, 14.00, 60.00, 74.00 / 10013393, Gustavo
Henrique Soares da Silva, 10.00, 42.00, 52.00 / 10000601, Gustavo Henrique Sousa Nunes, 13.00, 54.00,
67.00 / 10000201, Gustavo Ibiapino dos Santos, 9.00, 28.00, 37.00 / 10012967, Gustavo Junot Bentes de
Sa Duarte, 7.00, 40.00, 47.00 / 10005508, Gustavo Marques Ferreira, 11.00, 60.00, 71.00 / 10012394,
Gustavo Medeiros Pereira, 10.00, 48.00, 58.00 / 10012868, Gustavo Moraes Silva, 13.00, 50.00, 63.00 /
10013251, Gustavo Prado de Lima, 12.00, 58.00, 70.00 / 10009288, Halisson Barbosa de Souza, 15.00,
62.00, 77.00 / 10003152, Haliza Reis Silva e Silva, 9.00, 40.00, 49.00 / 10000073, Handerson Luiz Pedroso
Chianca, 8.00, 42.00, 50.00 / 10000368, Haniton Pereira de Oliveira, 12.00, 68.00, 80.00 / 10016270,
Hanna Rayssa Souza do Carmo, 11.00, 38.00, 49.00 / 10016310, Harley Carvalho de Vasconcelos, 7.00,
50.00, 57.00 / 10002383, Harlison Jose Ferreira dos Santos, 8.00, 36.00, 44.00 / 10012308, Haroldo Bryan
Santana Garcia, 11.00, 38.00, 49.00 / 10000243, Hasller da Cunha Rodrigues, 13.00, 50.00, 63.00 /
 
10007424, Hayanna dos Santos Nogueira, 6.00, 42.00, 48.00 / 10010192, Hayla Conceicao Vieira Ramos,
10.00, 34.00, 44.00 / 10011172, Hayrison Cunha Souza, 10.00, 56.00, 66.00 / 10003043, Hayslan Santos
Galvao, 13.00, 68.00, 81.00 / 10007797, Heitor Calderaro Costa Vale, 12.00, 52.00, 64.00 / 10003205,
Heitor Dourado Policarpo, 13.00, 54.00, 67.00 / 10007466, Heitor Leite Franca, 15.00, 60.00, 75.00 /
10003207, Helan Stephan Brito Ferreira, 4.00, 38.00, 42.00 / 10011483, Helber Sales dos Santos, 10.00,
30.00, 40.00 / 10002350, Helbert do Espirito Santo Barbosa Junior, 11.00, 34.00, 45.00 / 10002856, Helbert
Yan Santos Viegas, 7.00, 28.00, 35.00 / 10000847, Helder Maia Palheta, 12.00, 58.00, 70.00 / 10007189,
Helen Karolinne, 12.00, 54.00, 66.00 / 10007442, Helen Lima Alves, 6.00, 22.00, 28.00 / 10001489, Helen
Maklicia Marinho da Silva, 5.00, 18.00, 23.00 / 10015838, Helen Maria Santana Tiburcio, 12.00, 36.00,
48.00 / 10001776, Helen Mirlaine Lima Bentes, 8.00, 34.00, 42.00 / 10002097, Helen Rubia Lopes
Demetrio de Moura, 12.00, 54.00, 66.00 / 10000886, Helena Rocha de Sousa, 8.00, 64.00, 72.00 /
10012754, Helenel Carvalho Filho, 14.00, 60.00, 74.00 / 10013397, Heliana Rodrigues Carvalho, 6.00,
16.00, 22.00 / 10001182, Helio Marco da Silva Franca, 7.00, 46.00, 53.00 / 10000533, Helio Thacio Pereira
de Oliveira, 8.00, 64.00, 72.00 / 10001106, Helkjunior Oliveira Freitas Melo, 8.00, 48.00, 56.00 /
10013104, Hellen Ruth da Silva Carvalho, 6.00, 36.00, 42.00 / 10002969, Hellington Miranda de Souza,
12.00, 68.00, 80.00 / 10007793, Hellton Jorge Nazare da Silva, 11.00, 36.00, 47.00 / 10013467, Heloisa da
Silva Rodrigues, 5.00, 26.00, 31.00 / 10016108, Heloise Helene Monteiro Barros, 10.00, 46.00, 56.00 /
10017121, Helton Thiago de Oliveira Gomes, 10.00, 46.00, 56.00 / 10000430, Helyson Felinto Andrade
Rabelo, 8.00, 54.00, 62.00 / 10007586, Hemilly Vitoria Saraiva de Lima, 11.00, 50.00, 61.00 / 10002761,
Hemily Marinho Moura, 9.00, 34.00, 43.00 / 10010634, Henderson Lobo da Conceicao, 11.00, 52.00, 63.00
/ 10009353, Hennan Silva Araujo, 6.00, 30.00, 36.00 / 10007098, Henrique Abreu Carvalho, 13.00, 52.00,
65.00 / 10009642, Henrique Araujo Candido, 13.00, 58.00, 71.00 / 10016493, Henrique Azevedo Santana,
12.00, 40.00, 52.00 / 10000623, Henrique Batista Silva, 10.00, 46.00, 56.00 / 10000287, Henrique Felipe
Carvalho dos Santos Milhomem, 11.00, 50.00, 61.00 / 10016355, Henrique Lucas de Macedo Nunes, 13.00,
46.00, 59.00 / 10000714, Henrique Miguel de Souza Monteiro, 13.00, 64.00, 77.00 / 10011084, Henzo
Ferreira Santos Silva, 9.00, 24.00, 33.00 / 10002710, Herbert Mariano Silva Junior, 15.00, 48.00, 63.00 /
10000589, Herbert William Machado Dias, 15.00, 52.00, 67.00 / 10012048, Hericles Leonardo da Cunha
Terra, 9.00, 50.00, 59.00 / 10002576, Herison da Luz Silva, 10.00, 46.00, 56.00 / 10013278, Herisson Melo
Santana, 14.00, 46.00, 60.00 / 10000106, Heritton Luiz Silva Ramos, 10.00, 36.00, 46.00 / 10011335,
Herllan Silva, 7.00, 40.00, 47.00 / 10011656, Herlon Samuel Carvalho Goncalves, 13.00, 44.00, 57.00 /
10008058, Hernani Fernandes de Oliveira Neto, 5.00, 46.00, 51.00 / 10015954, Hevellyn Hose Rodrigues
Aguiar, 5.00, 48.00, 53.00 / 10009950, Heyder Antonio Palheta Vieira, 10.00, 38.00, 48.00 / 10003093,
Hiago Alves de Barros, 7.00, 30.00, 37.00 / 10000418, Hiago Costa, 6.00, 36.00, 42.00 / 10001038, Hiago
Naves Freitas, 14.00, 68.00, 82.00 / 10000798, Hiago Vinicius Carreiro da Silva, 14.00, 56.00, 70.00 /
10001799, Higo Tallison Lopes Santos, 11.00, 42.00, 53.00 / 10000062, Higor Augusto Goncalves
Queiroga, 8.00, 42.00, 50.00 / 10002182, Higor da Silva Rego, 14.00, 56.00, 70.00 / 10013067, Higor Leite
de Macedo, 16.00, 58.00, 74.00 / 10005429, Higor Pereira de Miranda, 18.00, 58.00, 76.00 / 10000270,
Hilbert Maia Vilhena Fonseca, 11.00, 58.00, 69.00 / 10010903, Hildemar Fernandes da Silva, 9.00, 62.00,
71.00 / 10000814, Hildemar Fernandes Rocha Filho, 10.00, 26.00, 36.00 / 10010942, Hillary Vitoria Justino
dos Santos, 10.00, 40.00, 50.00 / 10009875, Hilton Carlos Machado Bessa Junior, 6.00, 38.00, 44.00 /
10007336, Hitallo Matheus de Sousa Costa, 9.00, 44.00, 53.00 / 10011751, Hitalo Roberto Ramos de
Carvalho, 7.00, 30.00, 37.00 / 10006734, Huanderson Cardoso Almeida, 10.00, 64.00, 74.00 / 10011024,
Hudson Raika Arruda Sousa, 10.00, 44.00, 54.00 / 10007004, Hugo Danilo Bezerra de Souza, 11.00, 34.00,
45.00 / 10007360, Hugo de Almeida Coutinho Neto, 14.00, 50.00, 64.00 / 10012865, Hugo de Oliveira
Silva Filho, 15.00, 50.00, 65.00 / 10005379, Hugo Ferreira Bringel, 10.00, 46.00, 56.00 / 10006827, Hugo
Lisboa Monteiro, 9.00, 40.00, 49.00 / 10002528, Hugo Rodrigues Cardoso, 11.00, 66.00, 77.00 / 10002226,
Hugo Yan Alves Galvao de Lima, 15.00, 62.00, 77.00 / 10011577, Hugor Meireles Bezerra Alves, 12.00,
50.00, 62.00 / 10007426, Humberto Celeste Zanata, 11.00, 40.00, 51.00 / 10011633, Hyan Caique Pinheiro
Brandao, 8.00, 56.00, 64.00 / 10013376, Iago do Vale Silva, 7.00, 28.00, 35.00 / 10005644, Iago Gomes
Meireles, 11.00, 60.00, 71.00 / 10010346, Iago Silva Nery, 12.00, 68.00, 80.00 / 10015833, Iago Valentim
Pereira Ramos, 5.00, 28.00, 33.00 / 10003127, Iam Ferreira de Morais, 6.00, 38.00, 44.00 / 10006806, Ian
Augusto Costa e Silva, 9.00, 28.00, 37.00 / 10007335, Ian de Andrade Picanco, 17.00, 76.00, 93.00 /
 
10007050, Ian Matheus Nogueira Marques, 11.00, 54.00, 65.00 / 10010251, Ian Paixao Costa, 10.00, 56.00,
66.00 / 10001139, Ian Victor Saraiva Ribeiro, 9.00, 62.00, 71.00 / 10005500, Iana Claires Seixas dos
Santos, 6.00, 40.00, 46.00 / 10008219, Ianca Caroline Rodrigues Barros, 8.00, 58.00, 66.00 / 10001310,
Iane da Silva Melo Marques Miranda, 7.00, 34.00, 41.00 / 10005588, Iara Fernandes Carvalho, 7.00, 34.00,
41.00 / 10010564, Iara Ferreira, 3.00, 30.00, 33.00 / 10005617, Iara Patricia Pamplona Nascimento, 11.00,
56.00, 67.00 / 10016298, Iasmin Melisse Rebelo Lemos, 12.00, 52.00, 64.00 / 10013077, Iasmin Nayara
Campos Mendes, 8.00, 36.00, 44.00 / 10013330, Iasmin Sioux Andre Vieira, 9.00, 40.00, 49.00 / 10009466,
Iasmyn Sousa Barreto, 11.00, 44.00, 55.00 / 10001378, Idila Cristina Duarte Bessa, 5.00, 28.00, 33.00 /
10001107, Iezio Cordeiro de Melo, 12.00, 50.00, 62.00 / 10000357, Igor Afonso Pinto Carneiro, 9.00,
34.00, 43.00 / 10007359, Igor Brito de Oliveira, 10.00, 44.00, 54.00 / 10000514, Igor da Silva Pinheiro,
8.00, 44.00, 52.00 / 10015793, Igor Felipe Franca Baena de Sa, 13.00, 34.00, 47.00 / 10000240, Igor
Gustavo Costa Espindola, 9.00, 54.00, 63.00 / 10009966, Igor Henrique Rodrigues de Souza, 8.00, 52.00,
60.00 / 10005213, Igor Hymiollan Pimenta de Moraes, 8.00, 52.00, 60.00 / 10005380, Igor Jorge da
Fonseca Costa, 12.00, 40.00, 52.00 / 10002116, Igor Magalhaes da Silva, 6.00, 44.00, 50.00 / 10002511,
Igor Mauro Oliveira Paraense, 8.00, 30.00, 38.00 / 10009978, Igor Pampolha Carvalho, 6.00, 24.00, 30.00
/ 10012496, Igor Pereira Jacob, 8.00, 30.00, 38.00 / 10005591, Igor Rafael Borges Lopes, 7.00, 54.00, 61.00
/ 10006823, Igor Ramon Oliveira Castro, 10.00, 52.00, 62.00 / 10007483, Igor Rebelo Nunes, 8.00, 20.00,
28.00 / 10000134, Igor Vinicius Domingues Vieira, 9.00, 68.00, 77.00 / 10005497, Ikaro Brenno Santos
Souza, 9.00, 52.00, 61.00 / 10013650, Ilamar Amorim dos Santos, 12.00, 54.00, 66.00 / 10003157, Ilan
Kaique Brito de Souza, 12.00, 36.00, 48.00 / 10015972, Ilguison Ivens de Souza Lima, 7.00, 28.00, 35.00
/ 10009301, Inae Vanessa da Silva Teixeira, 8.00, 26.00, 34.00 / 10001983, Inara Fernandes Tavares, 16.00,
56.00, 72.00 / 10001971, Indyanne Horranna Rodrigues Silva, 10.00, 64.00, 74.00 / 10010991, Ines Nassar
Bandeira Oliveira, 10.00, 40.00, 50.00 / 10009480, Ingra Martins Miranda, 10.00, 38.00, 48.00 / 10002505, Ingrid Aimee Albuquerque da Silva Chagas, 12.00, 56.00, 68.00 / 10016707, Ingrid Carmeline de Oliveira Rodolfi, 13.00, 46.00, 59.00 / 10015847, Ingrid da Silva Oliveira, 14.00, 46.00, 60.00 / 10016020, Ingrid
Farias Goncalves, 11.00, 38.00, 49.00 / 10011823, Ingrid Freitas dos Santos, 17.00, 74.00, 91.00 /
10016845, Ingrid Juliana Mourao Santa Brigida, 6.00, 22.00, 28.00 / 10005407, Ingrid Juliany Moura da
Silva, 5.00, 30.00, 35.00 / 10011676, Ingrid Lima Absolao, 8.00, 56.00, 64.00 / 10011987, Ingrid Pinheiro
do Nascimento, 8.00, 34.00, 42.00 / 10011349, Ingrid Rafaela da Silva Macedo, 9.00, 48.00, 57.00 /
10001654, Ingrid Rebecca David Rezende, 9.00, 64.00, 73.00 / 10012880, Ingrid Taina da Silva Sampaio,
9.00, 48.00, 57.00 / 10016445, Ingrid Tainara Teixeira de Assis, 7.00, 22.00, 29.00 / 10010220, Ingrid
Tatiana Nebai Reis da Costa, 8.00, 56.00, 64.00 / 10012380, Ingrid Valeska Souza Franco, 9.00, 34.00,
43.00 / 10010582, Ingrisson Anderson da Silva Aguiar, 8.00, 32.00, 40.00 / 10013148, Ingrith Ribeiro da
Silva, 13.00, 44.00, 57.00 / 10013403, Ionnaria Jamilla Alves dos Santos, 9.00, 40.00, 49.00 / 10002110,
Irailce dos Prazeres Gomes, 12.00, 56.00, 68.00 / 10012694, Iris Laiana dos Santos Pantoja, 15.00, 62.00,
77.00 / 10013503, Irvana Cleonice Silva Sousa, 9.00, 26.00, 35.00 / 10010541, Isaac da Costa Pontes, 8.00,
60.00, 68.00 / 10011134, Isaac Fernandes da Silva, 8.00, 18.00, 26.00 / 10000414, Isaack Barros Costa,
13.00, 48.00, 61.00 / 10013579, Isabel Batista de Castro, 6.00, 48.00, 54.00 / 10002970, Isabela Barroso
Pantoja, 9.00, 40.00, 49.00 / 10013295, Isabela Cardias Macedo, 5.00, 30.00, 35.00 / 10007215, Isabela
Carvalho Patrocinio Costa, 17.00, 48.00, 65.00 / 10007288, Isabela Lima Mesquita, 9.00, 50.00, 59.00 /
10000033, Isabela Passarini Zampieri, 8.00, 46.00, 54.00 / 10016576, Isabele Sabrina dos Santos Pimentel,
12.00, 52.00, 64.00 / 10003187, Isabella Cardozo Viana, 2.00, 30.00, 32.00 / 10012613, Isabella de Oliveira
Pereira Bechelli Silva, 7.00, 42.00, 49.00 / 10005652, Isabella Lopes Diniz Barros, 7.00, 30.00, 37.00 /
10012702, Isabelle Christine Correa da Silva Monteiro, 7.00, 24.00, 31.00 / 10000992, Isabelle Fonseca
Barbosa, 10.00, 46.00, 56.00 / 10005698, Isabelly Melo Mota, 8.00, 32.00, 40.00 / 10010505, Isac
Rodrigues Ferreira, 7.00, 50.00, 57.00 / 10016073, Isadora de Medeiros da Silva, 5.00, 40.00, 45.00 /
10005214, Isael Nascimento Silva, 9.00, 56.00, 65.00 / 10013574, Isaque Adalberto Furtado Barbosa, 6.00,
30.00, 36.00 / 10007526, Islane Aguiar Rodrigues, 2.00, 26.00, 28.00 / 10002382, Ismael Pego Chaves,
8.00, 44.00, 52.00 / 10011313, Israel Lucas Santos Sena, 12.00, 48.00, 60.00 / 10015969, Israel Pampolha
Costa, 10.00, 56.00, 66.00 / 10000089, Itacy Dias Domingues Filho, 10.00, 56.00, 66.00 / 10016913, Italo
Alberto de Oliveira Lopes, 9.00, 34.00, 43.00 / 10013413, Italo de Brito Alves, 11.00, 38.00, 49.00 /
10002331, Italo Jose Pereira da Silva, 8.00, 34.00, 42.00 / 10002402, Italo Joshua Mota dos Santos, 13.00,
 
48.00, 61.00 / 10013564, Italo Lucas de Brito, 9.00, 46.00, 55.00 / 10000863, Italo Pinho Apolaro Rego,
11.00, 40.00, 51.00 / 10007766, Italo Vaz Andreatta, 14.00, 54.00, 68.00 / 10011652, Itamara Rodrigues
Dutra, 5.00, 32.00, 37.00 / 10006733, Iuri Gilberth Vale Medina, 11.00, 42.00, 53.00 / 10000628, Ivan
Aquino de Araujo Brito, 13.00, 66.00, 79.00 / 10016386, Ivan Junior Santos Almeida, 14.00, 44.00, 58.00
/ 10017046, Ivan Lucas Abreu Guimaraes, 9.00, 24.00, 33.00 / 10001315, Ivanilson Paulo Correa Raiol
Filho, 10.00, 56.00, 66.00 / 10001944, Ives Fernandes de Oliveira, 9.00, 56.00, 65.00 / 10010455, Ivon
Cleiton Souza de Freitas, 9.00, 54.00, 63.00 / 10016695, Izabela do Nascimento Bernardo, 12.00, 36.00,
48.00 / 10002072, Izabela Fernandes Viana Santos, 15.00, 56.00, 71.00 / 10016723, Izabella Luiza
Saldanha da Cruz, 10.00, 34.00, 44.00 / 10010001, Izabelli Wanzeler da Silva, 11.00, 44.00, 55.00 /
10000579, Izan Jose da Costa Brito Junior, 13.00, 58.00, 71.00 / 10003078, Izaquel Lima Silva, 12.00,
64.00, 76.00 / 10003203, Izolda Barbosa Pinto Marinho, 6.00, 18.00, 24.00 / 10012045, Jaciara Oliveira
Souza, 3.00, 24.00, 27.00 / 10009283, Jack Luis Franca Ramos, 9.00, 66.00, 75.00 / 10007315, Jackeline
Fatima Carneiro Peretto, 5.00, 48.00, 53.00 / 10007925, Jackeline Silva dos Reis, 8.00, 54.00, 62.00 /
10000060, Jackellyne Tyelle Castro do Carmo, 10.00, 44.00, 54.00 / 10016950, Jackline dos Santos
Gouvea, 11.00, 66.00, 77.00 / 10011129, Jackmiller Jakson do Amaral Cota, 4.00, 32.00, 36.00 / 10013406,
Jackson Lima Machado Junior, 10.00, 42.00, 52.00 / 10009413, Jacquison Alberto Pereira Alves, 8.00,
30.00, 38.00 / 10001487, Jacsandro da Silva Menezes, 10.00, 48.00, 58.00 / 10011213, Jade Viana
Rodrigues Alves, 8.00, 42.00, 50.00 / 10012239, Jadeissa Barros da Silva, 6.00, 58.00, 64.00 / 10002329,
Jadiel Pontes Moreira, 11.00, 36.00, 47.00 / 10017013, Jadson Wesllen da Silva Neves, 6.00, 38.00, 44.00
/ 10010166, Jaime Rodrigues Bezerra Pinto Junior, 8.00, 26.00, 34.00 / 10008138, Jaimison dos Santos
Negidio, 6.00, 24.00, 30.00 / 10002882, Jaine Carolina Pereira Cota, 4.00, 40.00, 44.00 / 10011710, Jaine
Gonzaga de Oliveira Coelho, 8.00, 40.00, 48.00 / 10010330, Jair Lobao Barroso Junior, 11.00, 50.00, 61.00
/ 10007997, Jairo de Sa Macedo, 14.00, 70.00, 84.00 / 10001517, Jairo Lobato Goncalves Junior, 15.00,
64.00, 79.00 / 10013539, Jakelline Marinho da Silva, 9.00, 58.00, 67.00 / 10010104, Jalyne Eugenia
Assuncao de Souza, 11.00, 46.00, 57.00 / 10002199, Jamille Guimaraes Borges, 13.00, 54.00, 67.00 /
10003130, Jamille Laiane Amorim da Silva, 6.00, 46.00, 52.00 / 10012011, Jamily Aline Santos Costa,
7.00, 48.00, 55.00 / 10010848, Jammes Marcell da Costa Rodrigues, 12.00, 52.00, 64.00 / 10016570,
Jamylly Cristina Araujo de Brito, 12.00, 36.00, 48.00 / 10001054, Janaina Pereira Alves, 12.00, 56.00,
68.00 / 10007926, Janaina Vieira da Conceicao, 3.00, 26.00, 29.00 / 10012983, Janderson Abreu Barbosa,
13.00, 68.00, 81.00 / 10013328, Janderson Jesus Carvalho Tavares, 9.00, 52.00, 61.00 / 10002516, Janep
Netta Pereira Coelho e Silva, 12.00, 60.00, 72.00 / 10010988, Janiffer Silva Santos, 11.00, 40.00, 51.00 /
10001584, Janine Canon Francelino dos Santos, 11.00, 40.00, 51.00 / 10012591, Janio Vitor Ferreira Dias,
7.00, 32.00, 39.00 / 10009251, Jaquelha Guimaraes Gomes, 13.00, 52.00, 65.00 / 10012378, Jaqueline
Souza Macedo, 13.00, 70.00, 83.00 / 10007403, Jarbas Granjeira Coelho, 7.00, 42.00, 49.00 / 10002303,
Jardenia Pereira da Silva, 7.00, 32.00, 39.00 / 10012737, Jardson Silva Moreira, 8.00, 42.00, 50.00 /
10011227, Jarlisson Fidelis dos Santos Oliveira, 6.00, 46.00, 52.00 / 10001459, Jarlisson Rodrigo da Silva
Nogueira, 15.00, 58.00, 73.00 / 10011452, Jaryane Santos de Oliveira, 8.00, 42.00, 50.00 / 10012485, Jean
Carlos Esteves Brasil, 10.00, 46.00, 56.00 / 10000471, Jean Carlos Neves de Sousa, 9.00, 58.00, 67.00 /
10001335, Jean Lucas Correa Freitas, 11.00, 44.00, 55.00 / 10002725, Jean Paulo Oliveira Alencar, 9.00,
54.00, 63.00 / 10012355, Jean Pinheiro Souto, 8.00, 50.00, 58.00 / 10006875, Jean Rubens da Silva
Pinheiro, 11.00, 50.00, 61.00 / 10016027, Jeanderson Rego Soares, 9.00, 22.00, 31.00 / 10012237, Jeane
Karine Goncalves Colares, 14.00, 44.00, 58.00 / 10011272, Jecy Kelly de Sousa Castro, 10.00, 48.00, 58.00
/ 10000926, Jeferson Lima Oliveira, 7.00, 24.00, 31.00 / 10011147, Jefferson Caetano de Sousa Caetano,
10.00, 34.00, 44.00 / 10003144, Jefferson dos Santos Figueiredo, 11.00, 44.00, 55.00 / 10013164, Jefferson
Luiz Leite da Silva, 7.00, 40.00, 47.00 / 10001098, Jefferson Pereira dos Santos, 9.00, 32.00, 41.00 /
10007564, Jefferson Ribeiro Oliveira, 11.00, 30.00, 41.00 / 10010811, Jefferson Vinicios Rego Silva,
10.00, 22.00, 32.00 / 10013435, Jeffeson da Silva Oliveira, 4.00, 46.00, 50.00 / 10000260, Jeffeson Pericles
Baia Uchoa, 8.00, 32.00, 40.00 / 10011684, Jeisiane Beatriz Pinto Pessoa, 12.00, 52.00, 64.00 / 10011753,
Jemisson Correa Pimentel Cacela, 6.00, 36.00, 42.00 / 10009440, Jeneildo Ferreira Ponte, 10.00, 44.00,
54.00 / 10001037, Jenifer de Lima Viana, 8.00, 54.00, 62.00 / 10012166, Jenifer Karolayne Vaz da Silva,
6.00, 22.00, 28.00 / 10011235, Jenifer Natasha Sodre Rodrigues, 8.00, 46.00, 54.00 / 10013356, Jeniffer
Silva e Silva, 10.00, 52.00, 62.00 / 10005223, Jennifer Aline dos Passos Marques, 8.00, 42.00, 50.00 /
 
10007048, Jennifer Beatriz Brito dos Santos, 15.00, 56.00, 71.00 / 10000519, Jennifer Silva Dutra, 10.00,
40.00, 50.00 / 10011550, Jeova Aragao da Silva, 8.00, 46.00, 54.00 / 10011687, Jeovaney Araujo Ferreira,
9.00, 34.00, 43.00 / 10011334, Jeremias Imbiriba da Silva, 12.00, 66.00, 78.00 / 10002160, Jeremias
Moreno Moreira, 10.00, 30.00, 40.00 / 10005437, Jeremias Vulcao dos Santos, 5.00, 26.00, 31.00 /
10005553, Jersey Gulyt Wanbyst Ferraz, 6.00, 34.00, 40.00 / 10016999, Jessica Bruna Silva Mendes, 8.00,
38.00, 46.00 / 10002496, Jessica Camilla Ferreira Araujo, 11.00, 50.00, 61.00 / 10000298, Jessica Caroline
de Andrade Cardoso, 11.00, 58.00, 69.00 / 10001169, Jessica de Carvalho Barata, 5.00, 34.00, 39.00 /
10010904, Jessica Fonseca da Costa, 8.00, 44.00, 52.00 / 10002544, Jessica Gleciane Borges de Oliveira,
8.00, 36.00, 44.00 / 10016093, Jessica Gomes dos Santos, 8.00, 38.00, 46.00 / 10002109, Jessica Karine
Cavalcante Haussler, 5.00, 22.00, 27.00 / 10012785, Jessica Lorena Almeida dos Santos, 8.00, 22.00, 30.00
/ 10010414, Jessica Pinto de Jesus, 7.00, 42.00, 49.00 / 10012196, Jessica Santos Alencar, 8.00, 34.00,
42.00 / 10012465, Jessica Zouhair Daou, 14.00, 50.00, 64.00 / 10000273, Jessika Tallissa Garcia dos
Santos, 10.00, 28.00, 38.00 / 10011580, Jhemerson Costa Santos, 7.00, 50.00, 57.00 / 10002321, Jhennifer
Samira de Melo Lima, 15.00, 66.00, 81.00 / 10010511, Jhennifer Vitoria Almeida Moreira, 7.00, 28.00,
35.00 / 10003081, Jhon Leno da Conceicao Silva dos Prazeres, 12.00, 52.00, 64.00 / 10000004, Jhon Magno
Santos Gomes, 7.00, 30.00, 37.00 / 10001640, Jhonata dos Santos David, 10.00, 34.00, 44.00 / 10015928,
Jhonata Victor Lopes da Silva, 7.00, 52.00, 59.00 / 10007323, Jhonatam Escocio da Silva, 8.00, 30.00,
38.00 / 10010845, Jhonatan de Souza Monteiro, 8.00, 30.00, 38.00 / 10016892, Jhonatan Silva da Matta,
10.00, 50.00, 60.00 / 10001693, Jhoney Oliveira da Silva, 13.00, 58.00, 71.00 / 10012052, Jhonn Carlos
Santana de Souza, 13.00, 38.00, 51.00 / 10000751, Jhonnatan Lima Pedrosos, 11.00, 42.00, 53.00 /
10007609, Jhonny Vasconcelos da Silva, 9.00, 40.00, 49.00 / 10016144, Jhonys Benek Rodrigues de
Sarges, 9.00, 48.00, 57.00 / 10010927, Jhorthon Favacho Sanches, 9.00, 58.00, 67.00 / 10002268, Jhulia
Beatriz Costa da Silva, 14.00, 56.00, 70.00 / 10016891, Jhulia Elana Araujo de Araujo, 8.00, 28.00, 36.00
/ 10010749, Jhulio Valadares da Silva, 10.00, 38.00, 48.00 / 10009474, Jo Bill de Jesus dos Santos Pantoja, 6.00, 38.00, 44.00 / 10010215, Joab Alves da Silva, 9.00, 30.00, 39.00 / 10000314, Joab da Silva Abreu
Junior, 14.00, 46.00, 60.00 / 10007822, Joanio Cardoso da Silva, 12.00, 60.00, 72.00 / 10016658, Joanny
Maia Braga, 7.00, 30.00, 37.00 / 10002432, Joao Alves Delgado Junior, 13.00, 40.00, 53.00 / 10001047,
Joao Augusto Guimaraes Pimentel, 13.00, 56.00, 69.00 / 10012404, Joao Batista Silva Neto, 6.00, 50.00,
56.00 / 10009953, Joao Batista Siqueira Lopes, 6.00, 44.00, 50.00 / 10005338, Joao Bosco Magno Neto,
12.00, 46.00, 58.00 / 10010282, Joao Carlos Salgado Craveiro, 9.00, 34.00, 43.00 / 10001974, Joao de
Jesus Silva, 12.00, 58.00, 70.00 / 10000938, Joao de Souza Lima, 8.00, 44.00, 52.00 / 10001406, Joao
Felipe Lage de Souza, 7.00, 28.00, 35.00 / 10007141, Joao Gabriel dos Santos Teiero, 7.00, 26.00, 33.00 /
10012704, Joao Gabriel Milhomem do Carmo, 7.00, 32.00, 39.00 / 10002662, Joao Gabriel Silva
Goncalves, 8.00, 62.00, 70.00 / 10001044, Joao Guilherme Saraiva de Souza, 12.00, 48.00, 60.00 /
10010478, Joao Gustavo Pinheiro Gomes, 9.00, 40.00, 49.00 / 10007322, Joao Helio da Cunha Cavalcanti
Filho, 13.00, 68.00, 81.00 / 10010081, Joao Henrique Ferreira da Silva, 1.00, 18.00, 19.00 / 10009877, Joao
Luis Cardoso e Cardoso, 12.00, 38.00, 50.00 / 10009730, Joao Marcelo Lima de Souza, 12.00, 48.00, 60.00
/ 10010997, Joao Marcos Bonfim Leal, 11.00, 54.00, 65.00 / 10009735, Joao Markus da Silva Mota, 12.00,
56.00, 68.00 / 10009910, Joao Marlon Alves de Lima, 6.00, 38.00, 44.00 / 10000489, Joao Oswaldo da
Silva Goncalves, 15.00, 68.00, 83.00 / 10001138, Joao Otavio de Medeiros Felinto Rabelo, 13.00, 70.00,
83.00 / 10010804, Joao Otavio Fernandes Barreto, 13.00, 46.00, 59.00 / 10007383, Joao Paulo Aguiar
Almeida, 10.00, 68.00, 78.00 / 10016259, Joao Paulo da Silva Lima, 9.00, 30.00, 39.00 / 10011542, Joao
Paulo da Silva Morais Alexandre, 10.00, 56.00, 66.00 / 10007865, Joao Paulo Rosario de Oliveira, 9.00,
50.00, 59.00 / 10016244, Joao Paulo Santos Barros, 9.00, 48.00, 57.00 / 10001162, Joao Paulo Santos da
Costa, 13.00, 60.00, 73.00 / 10000424, Joao Paulo Silva da Cunha, 5.00, 18.00, 23.00 / 10010450, Joao
Pedro Borges Lindolfo, 13.00, 64.00, 77.00 / 10008184, Joao Pedro de Souza Monteiro, 9.00, 34.00, 43.00
/ 10007932, Joao Pedro Farias da Costa, 14.00, 52.00, 66.00 / 10012059, Joao Pedro Pedra Domingos,
15.00, 56.00, 71.00 / 10002787, Joao Pedro Pereira de Souza, 9.00, 62.00, 71.00 / 10010412, Joao Pedro
Ribeiro da Silva, 7.00, 30.00, 37.00 / 10007417, Joao Pedro Sampaio Mariano de Brito, 9.00, 42.00, 51.00
/ 10011320, Joao Renato Contente Barbosa Nunes de Souza, 11.00, 48.00, 59.00 / 10007404, Joao Sertorio
de Miranda Neto, 13.00, 44.00, 57.00 / 10010508, Joao Victor Costa Guimaraes, 10.00, 54.00, 64.00 /
10011634, Joao Victor de Faria Madureira, 9.00, 34.00, 43.00 / 10011510, Joao Victor dos Santos Brabo,
 
8.00, 44.00, 52.00 / 10002462, Joao Victor Fernandes Ferreira, 7.00, 28.00, 35.00 / 10001207, Joao Victor
Leao Viana, 15.00, 58.00, 73.00 / 10013192, Joao Victor Luz Vitorino, 9.00, 28.00, 37.00 / 10010255, Joao
Victor Melo Tavares, 10.00, 44.00, 54.00 / 10009864, Joao Victor Moreira Vilar, 9.00, 30.00, 39.00 /
10000811, Joao Victor Nascimento Portilho, 10.00, 50.00, 60.00 / 10007392, Joao Victor Oliveira Aguiar,
7.00, 56.00, 63.00 / 10011838, Joao Victor Piedade Soares, 8.00, 44.00, 52.00 / 10010278, Joao Victor
Serra Machado, 10.00, 46.00, 56.00 / 10002633, Joao Victor Silva de Castro, 11.00, 44.00, 55.00 /
10001452, Joao Victor Silva Lima, 6.00, 34.00, 40.00 / 10010816, Joao Victor Souza Galdino, 10.00, 32.00,
42.00 / 10013425, Joao Victor Tenorio Farias Pedroso, 13.00, 56.00, 69.00 / 10010047, Joao Vinicius Sousa
dos Santos, 15.00, 52.00, 67.00 / 10002048, Joao Vitor Alexandria Rodrigues, 15.00, 72.00, 87.00 /
10002881, Joao Vitor de Figueiredo Teixeira, 9.00, 38.00, 47.00 / 10016962, Joao Vitor Leal Chaves, 9.00,
44.00, 53.00 / 10007584, Joao Vitor Nascimento da Silva, 6.00, 32.00, 38.00 / 10016075, Joao Vitor Ramos,
4.00, 28.00, 32.00 / 10002120, Joao Vitor Saldanha da Silva, 10.00, 46.00, 56.00 / 10016837, Joao Vytor
Gomes Nascimento, 13.00, 38.00, 51.00 / 10012279, Joao Werlon Diniz Elmescany, 9.00, 62.00, 71.00 /
10012563, Joaquim Valdeci Vasconcelos Junior, 9.00, 48.00, 57.00 / 10012317, Joarley Guilherme Santana
de Souza, 9.00, 34.00, 43.00 / 10013640, Joe Harrison Anjos Rabelo, 8.00, 44.00, 52.00 / 10000286, Joelcio
Teixeira Gomes Junior, 16.00, 46.00, 62.00 / 10010022, Joelson Barata de Souza, 7.00, 40.00, 47.00 /
10012327, Joharlos Favacho Sanches, 9.00, 48.00, 57.00 / 10016191, John Kleiver Correa Quaresma,
14.00, 70.00, 84.00 / 10016000, John Pitter Mcalister Araujo Amorim, 7.00, 26.00, 33.00 / 10013747, John
Santana de Abreu, 6.00, 38.00, 44.00 / 10000633, Johnatas Andre Moraes da Silva, 10.00, 42.00, 52.00 /
10000531, Johnny Jose da Silveira Nascimento, 8.00, 48.00, 56.00 / 10000078, Johnny Weslley Silva
Mesquita, 11.00, 44.00, 55.00 / 10009456, Joice Campos Valim, 9.00, 44.00, 53.00 / 10016752, Joice
Nunes dos Anjos, 11.00, 32.00, 43.00 / 10001540, Joice Sousa Costa, 8.00, 30.00, 38.00 / 10017050,
Joicynara Nascimento, 8.00, 34.00, 42.00 / 10010307, Jonas do Nascimento Pantoja, 9.00, 46.00, 55.00 /
10000646, Jonas Jorge Mendes Abreu, 7.00, 40.00, 47.00 / 10015742, Jonas Luis Oliveira Jati, 13.00,
30.00, 43.00 / 10013258, Jonas Marinho da Silva, 13.00, 52.00, 65.00 / 10001576, Jonatas da Silva Silva,
9.00, 46.00, 55.00 / 10006856, Jonatas Rabelo Galvao Junior, 8.00, 44.00, 52.00 / 10002784, Jonatas Silva
de Lima, 12.00, 58.00, 70.00 / 10015926, Jonatha de Oliveira Silva, 12.00, 52.00, 64.00 / 10007046, Jonatha
Pereira de Castro, 6.00, 38.00, 44.00 / 10005341, Jonathan Dalton Tenorio Brandao, 5.00, 24.00, 29.00 /
10012656, Jonathan Dasio Moraes Lopes, 12.00, 48.00, 60.00 / 10000818, Jonathan dos Santos, 10.00,
60.00, 70.00 / 10010134, Jonathan Ferreira Costa, 15.00, 50.00, 65.00 / 10010963, Jonathan Lima de
Freitas, 6.00, 36.00, 42.00 / 10002863, Jonathan Matheus Oliveira Flor da Silva, 8.00, 46.00, 54.00 /
10006788, Jonathan Miranda da Silva, 9.00, 42.00, 51.00 / 10017079, Jonathan Moises de Souza Remedios,
6.00, 30.00, 36.00 / 10012905, Jonathan Moraes dos Reis, 4.00, 22.00, 26.00 / 10002953, Jonathas
Rodrigues de Souza, 14.00, 62.00, 76.00 / 10013386, Jonhatan Gabriel Oliveira da Costa, 8.00, 54.00, 62.00
/ 10010038, Jonoerondi da Silva Souza, 10.00, 60.00, 70.00 / 10012813, Jorda de Carvalho Meguins, 8.00,
40.00, 48.00 / 10002520, Jordan Bernardo dos Santos Silva, 10.00, 44.00, 54.00 / 10010028, Jordana de
Sousa Ribeiro, 9.00, 54.00, 63.00 / 10010491, Jordana Leite Geronazzo, 6.00, 26.00, 32.00 / 10012774,
Jorge dos Santos Felix Junior, 6.00, 36.00, 42.00 / 10006753, Jorge dos Santos Pereira Junior, 6.00, 30.00,
36.00 / 10016340, Jorge Junior Araujo Carneiro, 13.00, 56.00, 69.00 / 10000052, Jorge Leonardo Baite de
Carvalho, 14.00, 68.00, 82.00 / 10000170, Jorge Leonardo Neves Ribeiro, 9.00, 32.00, 41.00 / 10015861,
Jorge Lopes de Alfaia, 7.00, 26.00, 33.00 / 10002891, Jorge Lucas Lobato Mendonca Goncalves, 7.00,
40.00, 47.00 / 10013679, Jorge Lucas Pinheiro Rego Tavares, 12.00, 42.00, 54.00 / 10000387, Jorge Patrick
Lobatocardoso, 8.00, 58.00, 66.00 / 10009579, Josafa Soares Sousa, 9.00, 44.00, 53.00 / 10011492, Jose
Alberto Lobato Cardoso, 9.00, 46.00, 55.00 / 10000973, Jose Aleff Xavier Silva, 13.00, 54.00, 67.00 /
10013094, Jose Armando Santana Reis de Novais, 10.00, 42.00, 52.00 / 10016336, Jose Augusto Pereira
dos Santos Junior, 6.00, 32.00, 38.00 / 10010159, Jose Carlos Imbiriba do Nascimento, 13.00, 48.00, 61.00
/ 10015883, Jose Carlos Pires Barbosa Junior, 6.00, 40.00, 46.00 / 10005653, Jose Carlos Prazeres Sampaio,
8.00, 38.00, 46.00 / 10002456, Jose da Clay Guimaraes Ferreira, 11.00, 40.00, 51.00 / 10001958, Jose da
Luz Ribeiro dos Santos, 17.00, 68.00, 85.00 / 10005217, Jose de Sa Nogueira Neto, 12.00, 66.00, 78.00 /
10013170, Jose Divaldo Barbosa Lima Junior, 6.00, 58.00, 64.00 / 10010832, Jose Edson Gonzaga Farias,
9.00, 36.00, 45.00 / 10000552, Jose Elvis Marleyson Araujo Cavalcante, 9.00, 26.00, 35.00 / 10012039,
Jose Fellipe de Sousa Santos, 12.00, 46.00, 58.00 / 10015822, Jose Francisco Dourado Aguiar, 7.00, 42.00,
 
49.00 / 10009286, Jose Gabriel Lima de Oliveira, 13.00, 54.00, 67.00 / 10001869, Jose Guilherme Coelho
da Silva, 10.00, 50.00, 60.00 / 10010053, Jose Hector de Araujo Marques, 12.00, 36.00, 48.00 / 10007027,
Jose Ieliton do Nascimento Costa Junior, 10.00, 54.00, 64.00 / 10016929, Jose Igor Filintro Ribeiro, 13.00,
64.00, 77.00 / 10000841, Jose Jaimy Cardoso Ferreira Filho, 11.00, 40.00, 51.00 / 10005624, Jose Junior
de Sousa Martirios, 10.00, 64.00, 74.00 / 10017041, Jose Leandro Costa Paranhos, 12.00, 64.00, 76.00 /
10001155, Jose Leonardo Lira Carvalho, 11.00, 42.00, 53.00 / 10009506, Jose Leonardo Siqueira Penteado,
10.00, 38.00, 48.00 / 10008005, Jose Lucas Neves Pereira, 8.00, 46.00, 54.00 / 10001564, Jose Lucas Vieira
Guimaraes, 8.00, 56.00, 64.00 / 10013494, Jose Lucian Barbosa de Araujo, 4.00, 40.00, 44.00 / 10006868,
Jose Marcus Lima da Pedra, 6.00, 56.00, 62.00 / 10007440, Jose Mateus Figueredo Gois, 9.00, 38.00, 47.00
/ 10016383, Jose Matheus Oliveira Cordovil, 6.00, 46.00, 52.00 / 10007241, Jose Matheus Torreao de
Lima, 10.00, 36.00, 46.00 / 10006863, Jose Mauro Silva da Pedra Junior, 10.00, 64.00, 74.00 / 10016094, Jose Mayke Gomes Martins, 13.00, 62.00, 75.00 / 10010754, Jose Norberto Correa de Medeiros Junior, 6.00, 28.00, 34.00 / 10009714, Jose Odimario Dias Neto, 9.00, 56.00, 65.00 / 10001578, Jose Paulo de
Oliveira Sa, 8.00, 48.00, 56.00 / 10012047, Jose Pereira Filho, 10.00, 50.00, 60.00 / 10012953, Jose Renne
Braga de Carvalho, 7.00, 24.00, 31.00 / 10007450, Jose Ribamar Paiva de Assis Filho, 10.00, 56.00, 66.00
/ 10006978, Jose Roberto Silva Xerfan, 7.00, 32.00, 39.00 / 10001785, Jose Romario Freires da Silva, 9.00,
46.00, 55.00 / 10013018, Jose Sardinha de Oliveira Neto, 6.00, 36.00, 42.00 / 10016537, Jose Sergio Lobato
Rodrigues, 5.00, 32.00, 37.00 / 10000797, Jose Ulisses Stevenson Araujo Oliveira, 10.00, 60.00, 70.00 /
10010473, Jose Victor Charchar de Oliveira Falcao, 11.00, 48.00, 59.00 / 10009398, Jose Victor Correa
Faria, 11.00, 56.00, 67.00 / 10000091, Jose Victor Said de Oliveira, 10.00, 38.00, 48.00 / 10002799, Jose
Wellignton Sousa Santos, 11.00, 56.00, 67.00 / 10001825, Jose Willam de Matos do Carmo, 9.00, 20.00,
29.00 / 10010761, Jose Wilson de Oliveira Filho, 10.00, 54.00, 64.00 / 10001485, Joseff de Lima Evaldt,
11.00, 50.00, 61.00 / 10015840, Joselia de Paula Silva, 9.00, 44.00, 53.00 / 10003158, Josemar Junior Maia
Lopes, 15.00, 66.00, 81.00 / 10000958, Josenildo Rodrigues de Lima, 11.00, 54.00, 65.00 / 10002747,
Josiane Cebusliski Lorini, 9.00, 28.00, 37.00 / 10002190, Josias Cristiano do Espirito Santo Coelho, 10.00,
28.00, 38.00 / 10008147, Josias Galvao Santos, 9.00, 50.00, 59.00 / 10016420, Josiel Alves da Costa Junior,
4.00, 52.00, 56.00 / 10012927, Josiele Cordeiro Paranhos, 13.00, 56.00, 69.00 / 10005420, Josiely do
Socorro Maia de Sousa, 11.00, 52.00, 63.00 / 10013377, Josimara Cinthia Rodrigues Ribeiro, 15.00, 42.00,
57.00 / 10000449, Josiney Gomes Silva, 8.00, 34.00, 42.00 / 10002286, Josino Paulino Neto, 11.00, 46.00,
57.00 / 10013124, Josivaldo Felix da Silva, 10.00, 30.00, 40.00 / 10016523, Josue Cleiton Barroso de
Sousa, 11.00, 56.00, 67.00 / 10012760, Josue da Costa Alves, 9.00, 36.00, 45.00 / 10007105, Josue da Silva
Frazao, 8.00, 42.00, 50.00 / 10007057, Josue Gomes dos Prazeres Junior, 8.00, 44.00, 52.00 / 10010200,
Josue Luis Meireles Lima, 9.00, 62.00, 71.00 / 10009467, Josue Luiz Franco de Sa Pereira, 11.00, 52.00,
63.00 / 10001206, Josue Teixeira Bittencourt, 11.00, 62.00, 73.00 / 10009746, Josuel Valente Goncalves,
10.00, 28.00, 38.00 / 10016322, Josuelen da Silva e Silva, 8.00, 46.00, 54.00 / 10016195, Jouadna Nyuenne
Silva Cunha, 9.00, 36.00, 45.00 / 10016546, Joyce Barcelos Santos, 12.00, 36.00, 48.00 / 10002053, Joyce
Cristina Coelho Hughes, 5.00, 22.00, 27.00 / 10012783, Joyce Jaqueline Felizardo Rego, 12.00, 40.00,
52.00 / 10005230, Joyce Karoline Vogado dos Reis, 11.00, 54.00, 65.00 / 10016858, Joycedene Souza
Sales Barreto, 9.00, 38.00, 47.00 / 10009513, Joyldson Mendes Lopes, 7.00, 32.00, 39.00 / 10001479, Joziel
Vilarins Torres, 10.00, 62.00, 72.00 / 10013465, Juan Carlos Dutra dos Reis, 6.00, 32.00, 38.00 / 10012745, Juan Patrick Alexander Oliveira Moraes, 14.00, 46.00, 60.00 / 10010422, Juarez Augusto Ribeiro de Souza Netto, 6.00, 40.00, 46.00 / 10016416, Juarez Gadelha Vasconcelos Neto, 11.00, 48.00, 59.00 / 10008205,
Jukimah Felipe Nascimento Sena, 12.00, 56.00, 68.00 / 10016730, Julia Emilly Chaves dos Santos, 12.00,
44.00, 56.00 / 10009665, Julia Mahraia Bueno Machowski, 10.00, 26.00, 36.00 / 10016173, Julia Quaresma
Miranda, 7.00, 46.00, 53.00 / 10010231, Julia Vitoria Cordeiro da Silva, 5.00, 24.00, 29.00 / 10002676,
Juliana Camila Correa Lopes, 9.00, 24.00, 33.00 / 10001187, Juliana Campelo de Andrade, 8.00, 26.00,
34.00 / 10000411, Juliana Conceicao Lima da Costa, 10.00, 46.00, 56.00 / 10000516, Juliana Correa
Goncalves, 11.00, 56.00, 67.00 / 10012957, Juliana Costa da Silva, 13.00, 40.00, 53.00 / 10010393, Juliana
da Silva Brabo, 10.00, 64.00, 74.00 / 10001935, Juliana do Socorro Fonseca Lobato, 9.00, 44.00, 53.00 /
10012211, Juliana Espindola de Brito Angelim, 10.00, 36.00, 46.00 / 10010681, Juliana Ferreira da Silva,
9.00, 44.00, 53.00 / 10009570, Juliana Ferreira de Oliveira, 6.00, 38.00, 44.00 / 10006761, Juliana Garcia
Vilhena, 9.00, 42.00, 51.00 / 10013058, Juliana Goncalves de Araujo, 10.00, 38.00, 48.00 / 10016024,
 
Juliana Jorge de Montalvao Guedes, 9.00, 42.00, 51.00 / 10009779, Juliana Lima Martins, 12.00, 52.00,
64.00 / 10005531, Juliana Lima Souza, 7.00, 20.00, 27.00 / 10010479, Juliana Silva Carvalho Dias, 13.00,
66.00, 79.00 / 10013064, Juliana Silva Santos Anselmo, 12.00, 42.00, 54.00 / 10002013, Julie Samily
Gomes Crispim Magalhaes, 8.00, 48.00, 56.00 / 10001739, Julieane Rosado Lopes, 6.00, 28.00, 34.00 /
10010482, Julielma Rodrigues Teles, 9.00, 48.00, 57.00 / 10011468, Julio Cesar Alves Pedreiro, 10.00,
40.00, 50.00 / 10000459, Julio Cesar de Oliveira Pereira Baiano, 8.00, 36.00, 44.00 / 10012675, Julio Cesar
dos Santos Monteiro, 14.00, 48.00, 62.00 / 10013489, Julio Cesar Nogueira Maia, 4.00, 38.00, 42.00 /
10010006, Julio Cesar Piazza de Lima Fagundes, 7.00, 38.00, 45.00 / 10012141, Julio Cezar de Lima
Castro, 9.00, 50.00, 59.00 / 10007532, Julio Estacio Santana de Aquino, 14.00, 54.00, 68.00 / 10011563,
Jullia Sena Ferreira, 13.00, 68.00, 81.00 / 10007196, Julyan Guimaraes de Carvalho, 11.00, 58.00, 69.00 /
10011713, Junior Andre do Nascimento Felicio, 11.00, 64.00, 75.00 / 10010459, Junior Filho Araujo
Rodrigues, 12.00, 58.00, 70.00 / 10000301, Junior Gabriel de Sousa Martins, 15.00, 50.00, 65.00 /
10015886, Junior Jorge Brito de Moura, 11.00, 54.00, 65.00 / 10000557, Junne Vanessa de Araujo Souza,
8.00, 58.00, 66.00 / 10011703, Juvenco Canuto de Carvalho Neto, 15.00, 60.00, 75.00 / 10006741, Kadimo
de Araujo Ferreira, 14.00, 50.00, 64.00 / 10015780, Kaio Breno Portela Sampaio, 14.00, 56.00, 70.00 /
10012831, Kaio Deleon Barra Ribeiro, 13.00, 54.00, 67.00 / 10000210, Kaio Fabricio Costa Sampaio, 8.00,
46.00, 54.00 / 10001470, Kaio Oliveira Batista, 6.00, 24.00, 30.00 / 10012669, Kaio Vinicius Alves Pinto,
8.00, 26.00, 34.00 / 10010425, Kaio Wanderson Carneiro Silva, 7.00, 34.00, 41.00 / 10009588, Kaique
Campos Duarte, 11.00, 64.00, 75.00 / 10016187, Kalebe Costa Ferreira, 6.00, 20.00, 26.00 / 10013070,
Kaleu Dilon Barra Ribeiro, 11.00, 50.00, 61.00 / 10011127, Kaline Alencar Barros da Silva, 11.00, 50.00,
61.00 / 10005517, Kaliny Costa Rocha, 9.00, 38.00, 47.00 / 10011883, Kalleb Jones Francolino Reis Lima,
9.00, 30.00, 39.00 / 10002696, Kamilla de Almeida e Silva, 8.00, 46.00, 54.00 / 10012909, Kamille Layse
Teixeira Barreto, 12.00, 48.00, 60.00 / 10016266, Kamilly Amador Kzam, 9.00, 26.00, 35.00 / 10002616,
Kamylla Caroline Oliveira Dias, 9.00, 40.00, 49.00 / 10005637, Kananda de Souza Mendes, 8.00, 34.00,
42.00 / 10012513, Kananda Viviane da Silva Sousa, 6.00, 26.00, 32.00 / 10012729, Karen Cynnara Ferreira
Silva, 5.00, 18.00, 23.00 / 10005334, Karen de Kassia Jacob Alfaia, 14.00, 48.00, 62.00 / 10010380, Karen
Leticia Silva Correa, 13.00, 56.00, 69.00 / 10007151, Karen Lise Braga de Freitas, 10.00, 52.00, 62.00 /
10011163, Karen Rodrigues Teixeira, 12.00, 40.00, 52.00 / 10010587, Karen Santos da Silva, 10.00, 48.00,
58.00 / 10010894, Karina Araujo do Nascimento, 13.00, 56.00, 69.00 / 10010535, Karina Brasil dos Santos,
9.00, 34.00, 43.00 / 10000386, Karina Camila Amorim Melo, 7.00, 30.00, 37.00 / 10005443, Karina
Nascimento Gomes, 10.00, 36.00, 46.00 / 10001748, Karina Suhelen Sousa Domiciano, 9.00, 54.00, 63.00
/ 10000147, Karina Thayna Menezes Melo, 11.00, 66.00, 77.00 / 10000510, Karine da Silva Ribeiro Costa,
11.00, 40.00, 51.00 / 10012952, Karine Neves Linhares, 4.00, 28.00, 32.00 / 10009457, Karine Ramana
Alves Lima, 13.00, 44.00, 57.00 / 10007462, Kariny Vieira Capitani, 9.00, 42.00, 51.00 / 10011637,
Karison Kelton Feijo de Sousa, 8.00, 48.00, 56.00 / 10001127, Karla Santos Pinheiro, 9.00, 58.00, 67.00 /
10010985, Karleane Leite de Sousa, 8.00, 42.00, 50.00 / 10001998, Karleno de Sousa Oliveira, 10.00,
52.00, 62.00 / 10002810, Karliane da Costa Sousa, 12.00, 50.00, 62.00 / 10011604, Karliany Pinheiro
Vieira, 4.00, 30.00, 34.00 / 10007545, Karolaine Kesia Monteiro Moreira, 10.00, 48.00, 58.00 / 10000969,
Karolina Cristine Neves de Figueiredo, 8.00, 32.00, 40.00 / 10013658, Karolina dos Santos Freitas, 9.00,
38.00, 47.00 / 10015911, Karolina Kethlen da Silva Souza, 6.00, 38.00, 44.00 / 10000154, Karolina Thayna
Menezes Melo, 11.00, 56.00, 67.00 / 10001954, Karoline Beatriz Silva Leal, 8.00, 60.00, 68.00 / 10009270,
Karoline Sousa da Mota, 13.00, 62.00, 75.00 / 10009983, Karolinne Moreira Valpasso, 15.00, 62.00, 77.00
/ 10011187, Kassandra Magalhaes Barroso, 7.00, 16.00, 23.00 / 10010597, Kassia Vitalina Ferreira
Alvarenga, 7.00, 62.00, 69.00 / 10002206, Kassiano de Melo Madeiro, 9.00, 68.00, 77.00 / 10002841,
Kassio Ribeiro Reis, 8.00, 30.00, 38.00 / 10007092, Katarina da Silva Pereira, 12.00, 62.00, 74.00 /
10000420, Kathelyn Stefany Menezes Marinho, 10.00, 52.00, 62.00 / 10007898, Katia Flavia Alves da
Costa, 9.00, 50.00, 59.00 / 10010303, Katielly Batista Teixeira, 9.00, 44.00, 53.00 / 10003048, Katiuscia
Carneiro dos Santos Lauar, 12.00, 52.00, 64.00 / 10010776, Kauan Darles Marques Magalhaes, 10.00,
40.00, 50.00 / 10012700, Kauanny Monteiro de Lima, 4.00, 40.00, 44.00 / 10010068, Kayla Santos da
Silva, 7.00, 56.00, 63.00 / 10012285, Kayo Cesar Oliveira Monte, 7.00, 60.00, 67.00 / 10015968, Kayse da
Silva Sa, 9.00, 44.00, 53.00 / 10000679, Kedilla Senna da Silva Ramos, 10.00, 46.00, 56.00 / 10007191,
Keitiane Bispo Rodrigues Roque, 12.00, 32.00, 44.00 / 10015960, Kellem Karoline de Souza Paixao, 11.00,
 
28.00, 39.00 / 10001873, Kelme Pereira Medeiros, 12.00, 50.00, 62.00 / 10009732, Kelson Natanael de
Sousa Almeida, 9.00, 50.00, 59.00 / 10001103, Kelvim Rodrigues dos Santos, 9.00, 56.00, 65.00 /
10016992, Kelvyn Carlos da Silva Mendes, 10.00, 52.00, 62.00 / 10009572, Kenia Kerle Lima da Silva,
9.00, 56.00, 65.00 / 10015779, Kennedy Anderson Ponte Angelim, 14.00, 60.00, 74.00 / 10002720,
Kennedy Sousa da Silva, 10.00, 22.00, 32.00 / 10002294, Kennety Crisostomo Prata da Silva, 8.00, 34.00,
42.00 / 10000353, Kerolen Cardoso Moraes, 11.00, 48.00, 59.00 / 10009567, Kesia Waveney Cardoso
Moreira, 5.00, 36.00, 41.00 / 10012848, Kevellin Cristina de Sousa Cordeiro, 7.00, 36.00, 43.00 /
10009455, Keven Almeida Ramos, 9.00, 44.00, 53.00 / 10002273, Kevin Antonio dos Santos Gurjao,
14.00, 56.00, 70.00 / 10002961, Kevin Eduardo da Silva Oliveira, 10.00, 46.00, 56.00 / 10012532, Kevin
Tenorio Soares Silva, 9.00, 36.00, 45.00 / 10002813, Kewin William Soares Damasceno, 13.00, 56.00,
69.00 / 10002298, Kezia de Cassia dos Santos de Carvalho, 9.00, 46.00, 55.00 / 10012412, Khathalyn
Tenorio Soares Silva, 11.00, 54.00, 65.00 / 10007834, Khelven Ruan Caxias Figueiro, 9.00, 60.00, 69.00 /
10011133, Killdery Afffonso Farias Primo, 11.00, 62.00, 73.00 / 10010411, Kiscilla Sampaio de Amorim
Abreu, 15.00, 66.00, 81.00 / 10005277, Kleber Gemaque Cardoso, 12.00, 42.00, 54.00 / 10009521, Kleber
Gomes Souza Santos, 8.00, 42.00, 50.00 / 10015978, Kleber Wesley de Oliveira Martins, 7.00, 40.00, 47.00
/ 10011535, Klebson Arthur dos Santos Alves, 8.00, 26.00, 34.00 / 10000372, Klebson Joaquim Marinho
da Silva, 11.00, 66.00, 77.00 / 10007249, Kleyson Damaceno Santana, 9.00, 48.00, 57.00 / 10016087,
Kleyson Danilo Ramos Costa, 10.00, 60.00, 70.00 / 10005387, Kleyton Correa Vieira, 6.00, 38.00, 44.00 /
10010366, Klicia Waleria Leite, 13.00, 58.00, 71.00 / 10001594, Klinsmann Gomes da Silva, 8.00, 50.00,
58.00 / 10009987, Klynger de Azevedo Miranda e Silva, 13.00, 60.00, 73.00 / 10016908, Laelson Cruz
Colaco Neto, 15.00, 46.00, 61.00 / 10012472, Laene Maisa Ferreira Oliveira, 14.00, 42.00, 56.00 /
10012893, Laercio Rodolfo Moreno da Silva Alves, 7.00, 46.00, 53.00 / 10001080, Laiane Barbosa Costa,
7.00, 40.00, 47.00 / 10010242, Laiane Sobral dos Santos, 10.00, 50.00, 60.00 / 10001204, Lailany Alves
da Silva, 7.00, 32.00, 39.00 / 10001217, Lailson Silva Diogenes, 16.00, 54.00, 70.00 / 10010082, Lailton
da Costa Coelho, 7.00, 56.00, 63.00 / 10002623, Laine Lima da Silva, 9.00, 52.00, 61.00 / 10013382, Lais
Aguiar Leite, 13.00, 50.00, 63.00 / 10007875, Lais Correa Feitosa, 7.00, 50.00, 57.00 / 10000817, Lais
Sodre Oliveira, 9.00, 42.00, 51.00 / 10011056, Laisa Ferreira de Souza, 10.00, 38.00, 48.00 / 10000830,
Laiz Belem Costa, 8.00, 42.00, 50.00 / 10012120, Laiza Patricia Lima Tapajos, 8.00, 36.00, 44.00 /
10013111, Lana Araujo de Castro, 6.00, 28.00, 34.00 / 10002369, Lana Barbara da Silva Lameira, 10.00,
48.00, 58.00 / 10011095, Lana Thais Santos de Oliveira, 12.00, 36.00, 48.00 / 10002277, Lanna Cristal
Castro dos Santos, 13.00, 62.00, 75.00 / 10007041, Lanne Crystina Altman Ferreira Lima, 12.00, 48.00,
60.00 / 10002756, Lara Reijane Coelho Silva Araujo, 12.00, 56.00, 68.00 / 10007770, Lara Steffany
Guimaraes Goltara, 7.00, 42.00, 49.00 / 10016210, Larise da Silva Cardoso, 11.00, 68.00, 79.00 /
10007503, Larissa Araujo Fortunato, 9.00, 30.00, 39.00 / 10011002, Larissa Brito Pardauil, 10.00, 54.00,
64.00 / 10011454, Larissa Carmen de Almeida Ferreira, 4.00, 28.00, 32.00 / 10010849, Larissa Catete
Sampaio, 11.00, 44.00, 55.00 / 10007405, Larissa Chaves de Siquerira, 9.00, 52.00, 61.00 / 10015868,
Larissa Conde de Souza, 15.00, 54.00, 69.00 / 10012453, Larissa da Frota Andrade, 9.00, 34.00, 43.00 /
10001501, Larissa da Silva Martins, 6.00, 36.00, 42.00 / 10007668, Larissa Daniella Pinheiro Biloia, 11.00,
28.00, 39.00 / 10007634, Larissa de Lima Santana da Silva, 11.00, 38.00, 49.00 / 10016724, Larissa de
Sousa Silva, 8.00, 38.00, 46.00 / 10009674, Larissa de Souza Tolosa, 9.00, 34.00, 43.00 / 10002847, Larissa
do Amaral Cypriano, 15.00, 62.00, 77.00 / 10000885, Larissa Fagundes Alves, 11.00, 54.00, 65.00 /
10000279, Larissa Gemaque de Azevedo, 10.00, 64.00, 74.00 / 10001599, Larissa Gomes Cruz, 8.00,
46.00, 54.00 / 10011582, Larissa Lassance Grandidier, 12.00, 54.00, 66.00 / 10000919, Larissa Neves
Santos, 13.00, 66.00, 79.00 / 10015895, Larissa Paiva Lopes, 10.00, 60.00, 70.00 / 10012707, Larissa Pinto
Ponte, 7.00, 28.00, 35.00 / 10013594, Larissa Silva Cunha, 9.00, 30.00, 39.00 / 10009290, Larissa Souza
Paiva, 7.00, 32.00, 39.00 / 10011161, Larissa Tavares Esquerdo, 12.00, 28.00, 40.00 / 10002573, Larissa
Vasconcelos Almeida, 7.00, 36.00, 43.00 / 10013171, Larisse Gaia do Nascimento Ferreira, 14.00, 64.00,
78.00 / 10001802, Laryssa Beatriz Batista Fonseca, 9.00, 30.00, 39.00 / 10000232, Laryssa Lorrany dos
Santos Lisboa, 5.00, 42.00, 47.00 / 10006986, Laura Angelo Santos, 7.00, 28.00, 35.00 / 10006738, Laura
Cardinali Nazare, 11.00, 30.00, 41.00 / 10000122, Laura Cecilia Kuhn, 14.00, 30.00, 44.00 / 10009369,
Laura Gabrielle Leite Alves, 9.00, 42.00, 51.00 / 10013631, Laura Geovana Meireles da Silva, 11.00, 52.00,
63.00 / 10009518, Laura Maria Cardoso Pereira, 10.00, 46.00, 56.00 / 10001831, Lauro Alan Sousa e Sousa
 
Junior, 8.00, 36.00, 44.00 / 10017107, Lauro Vagner Oliveira da Silva, 9.00, 52.00, 61.00 / 10007497,
Lavinha Batista Lopes, 11.00, 52.00, 63.00 / 10002517, Layana Pinheiro Aguiar, 15.00, 66.00, 81.00 /
10010585, Layanne Freitas Cavalcante, 12.00, 58.00, 70.00 / 10012431, Layany Kelly Silva Oliveira,
12.00, 36.00, 48.00 / 10013021, Layce Leal Peniche, 12.00, 50.00, 62.00 / 10007825, Layla de Sousa
Santos, 8.00, 28.00, 36.00 / 10000331, Layna Claudia Camara Loureiro, 12.00, 48.00, 60.00 / 10016132,
Layna Roberta Moraes Moreira, 12.00, 66.00, 78.00 / 10005448, Lays de Miranda de Sousa, 7.00, 22.00,
29.00 / 10009809, Lays Feitosa Vilhena, 7.00, 38.00, 45.00 / 10006860, Lays Santos Bovo, 7.00, 30.00,
37.00 / 10011800, Laysa de Souza Amorim, 12.00, 44.00, 56.00 / 10012292, Leandreson Moura Diniz,
9.00, 34.00, 43.00 / 10001372, Leandro Costa Cunha, 2.00, 36.00, 38.00 / 10010451, Leandro Kedson de
Jesus da Costa, 11.00, 50.00, 61.00 / 10002092, Leandro Meireles da Silva, 11.00, 50.00, 61.00 / 10011592,
Leandro Silva Espindola, 8.00, 38.00, 46.00 / 10002058, Leandro Soares de Lima, 9.00, 48.00, 57.00 /
10009762, Leandro Wagner Leite da Costa, 13.00, 62.00, 75.00 / 10010209, Leiany de Sousa Goncalves,
15.00, 54.00, 69.00 / 10001300, Leila Patricia Miranda dos Santos, 7.00, 36.00, 43.00 / 10016484, Lenice
Brito da Silva, 8.00, 30.00, 38.00 / 10010684, Lenilson da Silva Almeida, 11.00, 38.00, 49.00 / 10016865,
Lennoel Soares Silva, 12.00, 54.00, 66.00 / 10011636, Lenora Thomaz Santiago Santos, 12.00, 40.00, 52.00
/ 10012792, Leo Felipe Borges Santos, 5.00, 20.00, 25.00 / 10013190, Leoan Kardec Azevedo Soares, 7.00,
36.00, 43.00 / 10001136, Leomilson Cordeiro Bandeira, 11.00, 44.00, 55.00 / 10013178, Leon Kardec
Azevedo Soares, 13.00, 64.00, 77.00 / 10010532, Leonam de Jesus Balieiro Mendes, 4.00, 18.00, 22.00 /
10016633, Leonan Ferreira Sodre, 7.00, 38.00, 45.00 / 10006820, Leonan Wander Ferreira de Oliveira,
15.00, 66.00, 81.00 / 10000917, Leonardo Barbosa Clemente dos Santos, 9.00, 28.00, 37.00 / 10011325,
Leonardo Barros Alves, 8.00, 36.00, 44.00 / 10006936, Leonardo Brito da Silva Leal, 10.00, 60.00, 70.00
/ 10011960, Leonardo de Sousa, 10.00, 68.00, 78.00 / 10000064, Leonardo Felipe Nascimento Costa, 12.00,
54.00, 66.00 / 10012046, Leonardo Fernando Oliveira da Silva, 9.00, 34.00, 43.00 / 10001109, Leonardo
Gusmao Kalif Maia, 13.00, 58.00, 71.00 / 10007024, Leonardo Jose da Silveira Costa, 16.00, 68.00, 84.00
/ 10010406, Leonardo Nobre Lopes, 11.00, 42.00, 53.00 / 10010671, Leonardo Noronha Grangense, 9.00,
38.00, 47.00 / 10005262, Leonardo Rayron da Cruz Silva, 8.00, 42.00, 50.00 / 10007118, Leonardo
Rodrigues do Espirito Santo, 10.00, 44.00, 54.00 / 10001699, Leonardo Santos do Nascimento, 11.00,
48.00, 59.00 / 10003146, Leonardo Viana Maia Lopes, 5.00, 44.00, 49.00 / 10013078, Leonardo Viegas
Rodrigues, 8.00, 34.00, 42.00 / 10005222, Leonardo Vieira Tavares, 15.00, 36.00, 51.00 / 10015977, Leony
Kemper Rodrigues de Souza, 8.00, 32.00, 40.00 / 10010477, Lerci Antonio dos Santos Junior, 13.00, 66.00,
79.00 / 10008125, Leticia Alves Dutra, 14.00, 72.00, 86.00 / 10000567, Leticia Ananda Bastos Basso,
13.00, 42.00, 55.00 / 10013319, Leticia Azevedo Leal, 7.00, 42.00, 49.00 / 10005663, Leticia Barros da
Costa, 8.00, 48.00, 56.00 / 10002098, Leticia Carine de Jesus Damasceno da Silva, 8.00, 36.00, 44.00 /
10010281, Leticia Carolina Sena Ramos, 9.00, 32.00, 41.00 / 10009780, Leticia Chagas Righini, 6.00,
32.00, 38.00 / 10001957, Leticia Coelho Guedes, 9.00, 42.00, 51.00 / 10011262, Leticia de Souza
Virgolino, 12.00, 50.00, 62.00 / 10013009, Leticia Fernanda Pinheiro Biloia, 6.00, 36.00, 42.00 / 10001629,
Leticia Jordana dos Santos Vasconcelos, 12.00, 38.00, 50.00 / 10001211, Leticia Karoline Santiago
Marreira, 6.00, 30.00, 36.00 / 10013744, Leticia Pereira Costa, 11.00, 40.00, 51.00 / 10016368, Leticia
Riely Cohen da Silva, 9.00, 40.00, 49.00 / 10016421, Leticia Rodrigues da Cunha Ramos, 6.00, 32.00,
38.00 / 10000436, Leticia Silva das Chagas, 7.00, 32.00, 39.00 / 10015913, Leticia Silva de Menezes,
11.00, 48.00, 59.00 / 10001230, Leticia Soares Santa Brigida, 12.00, 44.00, 56.00 / 10015772, Leticia
Vitoria Nascimento Magalhaes, 12.00, 54.00, 66.00 / 10000772, Levy da Silva Baia, 8.00, 50.00, 58.00 /
10011200, Liciane de Souza Vale, 16.00, 62.00, 78.00 / 10009974, Lidiane Santos da Conceicao, 10.00,
54.00, 64.00 / 10016549, Lidiani da Silva Santos, 11.00, 40.00, 51.00 / 10013201, Liedson Valente Moraes,
11.00, 52.00, 63.00 / 10007727, Ligia Rafaela Ribeiro Lopes, 10.00, 48.00, 58.00 / 10013452, Lilian Brena
da Silva Fayal, 8.00, 34.00, 42.00 / 10002278, Lilianne Sathie Guimaraes Kimura de Sousa, 11.00, 52.00,
63.00 / 10006789, Lilliane Rodrigues Barbosa, 7.00, 24.00, 31.00 / 10002738, Lindaine Silva Sampaio,
7.00, 20.00, 27.00 / 10002248, Lindberg Leite Gomes, 9.00, 32.00, 41.00 / 10012124, Lindemberg Ramos
da Silva Santos, 7.00, 34.00, 41.00 / 10000856, Linerio Silva do Espirito Santo, 11.00, 52.00, 63.00 /
10011336, Lino Victor da Gama Rodrigues Araujo, 9.00, 46.00, 55.00 / 10007534, Liorrane Nunes dos
Santos, 6.00, 58.00, 64.00 / 10013562, Livia Caetano Rocha, 13.00, 44.00, 57.00 / 10000914, Livia dos
Santos Sousa, 11.00, 34.00, 45.00 / 10012971, Livia Sampaio de Aviz, 8.00, 42.00, 50.00 / 10012590,
 
Lizandra da Silva Souza, 10.00, 44.00, 54.00 / 10000757, Loenny da Silva Maia, 8.00, 26.00, 34.00 /
10012517, Lohanny Louise Viana Gomes da Silva, 9.00, 46.00, 55.00 / 10006704, Lohany Maria Ribeiro
e Silva, 17.00, 64.00, 81.00 / 10011798, Lorena Agnes Pena Santos, 10.00, 28.00, 38.00 / 10000225, Lorena
dos Santos Silva, 10.00, 52.00, 62.00 / 10016599, Lorena Ferreira Fontes, 7.00, 58.00, 65.00 / 10011191,
Lorena Lima de Araujo, 10.00, 48.00, 58.00 / 10011299, Lorena Marla Rabelo Rodrigues, 7.00, 42.00,
49.00 / 10012786, Lorena Nunes Pinheiro, 9.00, 52.00, 61.00 / 10016912, Lorena Rabelo Foicinha, 7.00,
36.00, 43.00 / 10011280, Lorena Rayssa Silva Cavalcante, 9.00, 50.00, 59.00 / 10009546, Lorena Santos
Mourao, 10.00, 56.00, 66.00 / 10001301, Lorena Zena Nascimento, 8.00, 28.00, 36.00 / 10012026, Lorenna
Gomes Nascimento, 11.00, 54.00, 65.00 / 10007757, Loriana Saraiva Trindade, 7.00, 28.00, 35.00 /
10012215, Lothar Matheus Rocha Alves, 9.00, 52.00, 61.00 / 10000609, Louise Tavares Ferreira, 6.00,
36.00, 42.00 / 10012553, Louranny Lua Oliveira Pinheiro Silva, 8.00, 38.00, 46.00 / 10012361, Lua Lima
Vilas Boas, 11.00, 50.00, 61.00 / 10001076, Lua Pina Lima, 11.00, 34.00, 45.00 / 10016101, Luan Augusto
Soares Alves, 8.00, 30.00, 38.00 / 10002565, Luan Camara Brito, 11.00, 58.00, 69.00 / 10010764, Luan
Carlos Pereira Sousa, 6.00, 26.00, 32.00 / 10005597, Luan Castilho Rodrigues, 7.00, 34.00, 41.00 /
10012588, Luan Dener dos Prazeres Menezes, 12.00, 56.00, 68.00 / 10003206, Luan dos Santos Costa,
7.00, 36.00, 43.00 / 10010493, Luan Gabriel Monteiro dos Santos, 8.00, 42.00, 50.00 / 10011789, Luan
Nogueira de Lima, 10.00, 42.00, 52.00 / 10010755, Luan Silva Lima Lopes, 10.00, 44.00, 54.00 / 10002603,
Luan Wander Ferreira Oliveira, 13.00, 64.00, 77.00 / 10007671, Luana Alves Santiago, 7.00, 34.00, 41.00
/ 10012202, Luana Ayalla Silva de Araujo, 10.00, 56.00, 66.00 / 10011088, Luana da Silva Barbosa, 5.00,
54.00, 59.00 / 10002299, Luana Dias dos Santos Quixabeira, 10.00, 48.00, 58.00 / 10001571, Luana
Kerolline Carvalho Chaves, 7.00, 48.00, 55.00 / 10009246, Luana Kethlen Braga de Abreu, 6.00, 26.00,
32.00 / 10011159, Luana Patricia Santos de Macedo, 8.00, 48.00, 56.00 / 10007539, Luana Pereira e Silva,
10.00, 30.00, 40.00 / 10001668, Luana Pinheiro Silva, 13.00, 50.00, 63.00 / 10007999, Luana Rayssa
Pinheiro Costa, 7.00, 20.00, 27.00 / 10001940, Luana Silva Medeiros Pontes, 8.00, 56.00, 64.00 /
10001545, Luana Sipiao Oliveira, 8.00, 40.00, 48.00 / 10009554, Luana Siqueira Machado, 8.00, 56.00,
64.00 / 10010263, Luana Sousa Oliveira, 8.00, 36.00, 44.00 / 10011971, Luanderson Oliveira Duarte, 9.00,
44.00, 53.00 / 10000155, Luane Teixeira Rodrigues, 11.00, 50.00, 61.00 / 10016103, Luanne Fabiannie
Soares Alves, 10.00, 28.00, 38.00 / 10000689, Luany Jordana Ribeiro de Oliveira, 8.00, 32.00, 40.00 /
10001281, Luany Waleria Martins Canellas Magalhaes, 9.00, 48.00, 57.00 / 10010239, Luara Clicia
Pinheiro da Silva, 8.00, 38.00, 46.00 / 10002789, Luara Vitoria Costa Araujo, 13.00, 68.00, 81.00 /
10002944, Lucas Alamar da Silva, 9.00, 34.00, 43.00 / 10010394, Lucas Alexandre Pereira Pacheco, 8.00,
52.00, 60.00 / 10016257, Lucas Almada de Sousa Martins, 13.00, 64.00, 77.00 / 10012038, Lucas Amarante
Lucena, 11.00, 44.00, 55.00 / 10009399, Lucas Baia Almeida, 14.00, 50.00, 64.00 / 10012913, Lucas
Barbosa Melo, 8.00, 36.00, 44.00 / 10012930, Lucas Bellard Pereira Mariuba, 8.00, 56.00, 64.00 /
10001128, Lucas Braga Vidal, 10.00, 26.00, 36.00 / 10016628, Lucas Brito de Lima, 10.00, 32.00, 42.00 /
10009871, Lucas Brito Sousa, 9.00, 50.00, 59.00 / 10015845, Lucas Caldeira Silva, 5.00, 46.00, 51.00 /
10012791, Lucas Carneiro Maia, 5.00, 34.00, 39.00 / 10013514, Lucas Carvalho Barbosa, 12.00, 44.00,
56.00 / 10011500, Lucas Carvalho Silva, 14.00, 68.00, 82.00 / 10009330, Lucas Cruz da Silva, 10.00,
40.00, 50.00 / 10001734, Lucas da Conceicao Santos, 18.00, 64.00, 82.00 / 10013138, Lucas da Silva Alves,
7.00, 50.00, 57.00 / 10002312, Lucas da Silva Batista, 11.00, 22.00, 33.00 / 10010808, Lucas da Silva
Moraes, 11.00, 50.00, 61.00 / 10009907, Lucas Dantas Ribeiro, 7.00, 40.00, 47.00 / 10012382, Lucas de
Almeida Oliveira, 10.00, 48.00, 58.00 / 10000192, Lucas de Araujo Nascimento, 8.00, 38.00, 46.00 /
10003171, Lucas de Nadal, 9.00, 46.00, 55.00 / 10007731, Lucas de Sousa Castro, 8.00, 34.00, 42.00 /
10001706, Lucas de Sousa Veras, 13.00, 54.00, 67.00 / 10012193, Lucas de Sousa Vinuto, 10.00, 56.00,
66.00 / 10010891, Lucas Dhemetrios Vieira Peixe, 12.00, 48.00, 60.00 / 10007192, Lucas do Espirito Santo
Martins, 7.00, 34.00, 41.00 / 10013626, Lucas do Lago Alves Costa, 9.00, 30.00, 39.00 / 10001757, Lucas
do Nascimento Gois, 13.00, 66.00, 79.00 / 10013578, Lucas dos Santos Brindeiro, 5.00, 30.00, 35.00 /
10001519, Lucas dos Santos Ferreira Bispo, 12.00, 52.00, 64.00 / 10011100, Lucas Dutra Dias, 9.00, 52.00,
61.00 / 10012441, Lucas Eduardo Rebelo Pinho, 10.00, 42.00, 52.00 / 10016014, Lucas Evangelista Santos
do Vale, 4.00, 30.00, 34.00 / 10013439, Lucas Evilazio Correia Silva, 9.00, 40.00, 49.00 / 10016410, Lucas
Farineli Rosa, 8.00, 48.00, 56.00 / 10011244, Lucas Felipe Muniz dos Santos, 11.00, 32.00, 43.00 /
10010168, Lucas Fernandes Duarte Santos, 11.00, 32.00, 43.00 / 10001521, Lucas Filipe da Purificacao
 
Braga, 10.00, 44.00, 54.00 / 10007959, Lucas Fonseca Guedes Abreu, 10.00, 44.00, 54.00 / 10010730,
Lucas Gabriel Mota da Silva, 7.00, 30.00, 37.00 / 10000161, Lucas Gregorio Xavier de Paiva, 6.00, 20.00,
26.00 / 10000929, Lucas Henrique Vieira de Abreu, 8.00, 58.00, 66.00 / 10013314, Lucas Kalleb da Costa
Correa, 17.00, 62.00, 79.00 / 10006701, Lucas Lancelote Muniz Garcia, 8.00, 52.00, 60.00 / 10001614,
Lucas Lelis Melo Mendes, 11.00, 52.00, 63.00 / 10007285, Lucas Lima de Souza, 11.00, 64.00, 75.00 /
10010438, Lucas Lisboa da Silva Cruz, 10.00, 32.00, 42.00 / 10016268, Lucas Luyd Correa Nascimento
dos Santos, 12.00, 44.00, 56.00 / 10002797, Lucas Marcel dos Reis Cruz, 14.00, 62.00, 76.00 / 10000511,
Lucas Martins Batistela, 13.00, 52.00, 65.00 / 10012721, Lucas Mateus Oliveira Moreira, 14.00, 66.00,
80.00 / 10005649, Lucas Matheus Cardoso de Lima, 9.00, 42.00, 51.00 / 10001039, Lucas Matheus Prata
de Oliveira, 14.00, 44.00, 58.00 / 10002924, Lucas Miclos Soares, 7.00, 60.00, 67.00 / 10010085, Lucas
Monteiro Figueira, 6.00, 38.00, 44.00 / 10016717, Lucas Monteiro Goncalves, 9.00, 36.00, 45.00 /
10007400, Lucas Neves Sousa, 10.00, 56.00, 66.00 / 10001967, Lucas Nunes Pereira, 9.00, 42.00, 51.00 /
10003119, Lucas Oliveira da Silva, 7.00, 42.00, 49.00 / 10003018, Lucas Pagehu Lopes Locatelli da Silva,
7.00, 44.00, 51.00 / 10002363, Lucas Pereira Alves, 13.00, 52.00, 65.00 / 10000995, Lucas Pereira Palheta,
8.00, 36.00, 44.00 / 10000990, Lucas Pereira Sousa, 9.00, 30.00, 39.00 / 10016437, Lucas Pinto do Carmo,
6.00, 42.00, 48.00 / 10011781, Lucas Rafael Silva Moreno, 7.00, 48.00, 55.00 / 10001131, Lucas Ramos
Soares, 10.00, 58.00, 68.00 / 10000036, Lucas Ribeiro Herculano, 10.00, 40.00, 50.00 / 10000162, Lucas Ronaldo Claudiano do Nascimento Ferreira de Lima, 8.00, 48.00, 56.00 / 10005513, Lucas Rufino da Cunha, 6.00, 50.00, 56.00 / 10010301, Lucas Santos do Nascimento, 7.00, 32.00, 39.00 / 10007142, Lucas
Silva Ferreira, 8.00, 46.00, 54.00 / 10000481, Lucas Silva Gouveia, 8.00, 44.00, 52.00 / 10017028, Lucas
Sousa Lobato, 13.00, 44.00, 57.00 / 10002816, Lucas Sousa Silva, 10.00, 48.00, 58.00 / 10009404, Lucas
Sucupira Farias, 7.00, 46.00, 53.00 / 10010132, Lucas Taborda do Nascimento, 8.00, 68.00, 76.00 /
10006809, Lucas Tadeu da Silva Torres, 10.00, 28.00, 38.00 / 10011897, Lucas Victor Lira Costa, 14.00,
58.00, 72.00 / 10002733, Lucas Victor Ribeiro Lopes, 7.00, 60.00, 67.00 / 10010174, Lucas Vinicius
Batista Sousa, 12.00, 28.00, 40.00 / 10006853, Lucas Vinicius do Nascimento Silva, 6.00, 30.00, 36.00 /
10001955, Lucas Vinicius Goncalves Cardoso Oliveira, 14.00, 38.00, 52.00 / 10002684, Lucas Wanderley
Fonseca Ramos, 10.00, 60.00, 70.00 / 10016012, Lucas Willott Pereira, 11.00, 22.00, 33.00 / 10000578,
Lucas Yan de Oliveira Alves, 15.00, 44.00, 59.00 / 10002450, Luciana Araujo dos Santos Mendes, 9.00,
44.00, 53.00 / 10010731, Luciana Azevedo do Nascimento, 12.00, 46.00, 58.00 / 10012866, Luciana
Histerlinoi Costa Martins, 11.00, 38.00, 49.00 / 10006995, Luciane Marques Vasconcelos, 8.00, 38.00,
46.00 / 10000058, Lucianna Fabricia Tavares Nascimento, 14.00, 50.00, 64.00 / 10011586, Luciano
Cordeiro Amarante Oliveira, 8.00, 28.00, 36.00 / 10001857, Luciano Costa Mendonca, 5.00, 40.00, 45.00
/ 10001362, Luciano da Silva Machado, 6.00, 32.00, 38.00 / 10011900, Luciano Silva Figueiredo Santos,
14.00, 60.00, 74.00 / 10009296, Luciano Silva Monteiro, 11.00, 30.00, 41.00 / 10016047, Lucilia Rodrigues
Barros Luz, 10.00, 50.00, 60.00 / 10015805, Lucio Andre Miranda Parreao Santana, 15.00, 50.00, 65.00 /
10013093, Lucivaldo Batista Mota, 11.00, 42.00, 53.00 / 10000832, Ludmilla Karras Barreto Nogueira,
8.00, 18.00, 26.00 / 10005394, Ludmilla Sapucaia Cantanhede Cordeiro, 8.00, 38.00, 46.00 / 10015844,
Luidgi Oishi Silva, 9.00, 34.00, 43.00 / 10010890, Luis Eduardo Anaice Lopes, 11.00, 66.00, 77.00 /
10010920, Luis Eduardo Correa Assuncao, 13.00, 58.00, 71.00 / 10009872, Luis Eduardo Silva de Sousa,
12.00, 52.00, 64.00 / 10015944, Luis Felipe Araujo Pereira, 10.00, 44.00, 54.00 / 10013473, Luis Felipe de
Freitas Rossas Novaes, 12.00, 60.00, 72.00 / 10012246, Luis Felipe dos Santos Oliveira, 5.00, 34.00, 39.00
/ 10000335, Luis Felipe Silva Fernandes, 9.00, 54.00, 63.00 / 10011776, Luis Fernando Lima Beckman,
7.00, 44.00, 51.00 / 10001064, Luis Fernando Rodrigues Monteiro, 8.00, 56.00, 64.00 / 10000241, Luis
Filipe Silva dos Santos, 9.00, 40.00, 49.00 / 10005372, Luis Henrique Pereira Tabosa, 8.00, 44.00, 52.00 /
10001993, Luis Henrique Santa Brigida Cardoso, 5.00, 22.00, 27.00 / 10008223, Luis Lima Filho, 11.00,
50.00, 61.00 / 10005747, Luis Matheus Uchoa do Nascimento Silva, 10.00, 46.00, 56.00 / 10011714, Luis
Miguel de Souza Santos, 6.00, 44.00, 50.00 / 10010884, Luis Miguel Pimenta Albuquerque, 8.00, 46.00,
54.00 / 10011010, Luis Otavio dos Santos Teixeira, 15.00, 56.00, 71.00 / 10000252, Luis Paulo Dantas
Lopes, 14.00, 58.00, 72.00 / 10010747, Luis Paulo Silva Pereira, 14.00, 40.00, 54.00 / 10002413, Luis
Ricardo Miranda de Sousa, 6.00, 52.00, 58.00 / 10007689, Luis Richard da Cruz Marques, 4.00, 32.00,
36.00 / 10001142, Luis Vicente Pereira do Nascimento Junior, 9.00, 38.00, 47.00 / 10000124, Luis Victor
Santos Quaresma, 11.00, 44.00, 55.00 / 10012417, Luis Vitor da Silva Albuquerque, 11.00, 62.00, 73.00 /
 
10011075, Luiz Antonio Cabral Moreira, 7.00, 34.00, 41.00 / 10007913, Luiz Augusto de Almeida da Silva,
6.00, 38.00, 44.00 / 10011504, Luiz Augusto Evaristo da Silva Filho, 7.00, 34.00, 41.00 / 10001702, Luiz
Carlos Barroso de Souza, 8.00, 52.00, 60.00 / 10000291, Luiz Carlos de Carvalho Neto, 8.00, 42.00, 50.00
/ 10001941, Luiz Carlos Santos Carmo, 9.00, 46.00, 55.00 / 10016048, Luiz Carlos Soares da Silva, 9.00,
46.00, 55.00 / 10010351, Luiz Cezar Ferreira Virgolino, 9.00, 44.00, 53.00 / 10002149, Luiz Davi de Souza
Fontes, 6.00, 48.00, 54.00 / 10002959, Luiz Diogo Monteiro Pinheiro, 7.00, 46.00, 53.00 / 10016580, Luiz
Eduardo Cunha Lisboa, 11.00, 54.00, 65.00 / 10012666, Luiz Eduardo Machado dos Santos, 7.00, 44.00,
51.00 / 10000722, Luiz Eduardo Pereira de Carvalho, 12.00, 66.00, 78.00 / 10007154, Luiz Felipe de
Miranda Souza, 12.00, 46.00, 58.00 / 10001324, Luiz Felipe Lima de Miranda, 11.00, 50.00, 61.00 /
10010247, Luiz Fernando Azulay Soares, 11.00, 56.00, 67.00 / 10012511, Luiz Fernando do Rosario de
Freitas, 10.00, 40.00, 50.00 / 10013580, Luiz Fernando Lobato Araujo Filho, 12.00, 42.00, 54.00 /
10011588, Luiz Guilherme Matias Rodrigues, 11.00, 42.00, 53.00 / 10011003, Luiz Henrique Adam Alves,
8.00, 36.00, 44.00 / 10007219, Luiz Henrique Costa Arruda, 13.00, 30.00, 43.00 / 10016525, Luiz Henrique
Silva da Costa, 4.00, 44.00, 48.00 / 10015734, Luiz Ivan Naiff da Silva Junior, 7.00, 38.00, 45.00 /
10002158, Luiz Otavio de Jesus Santana Junior, 9.00, 46.00, 55.00 / 10012356, Luiz Paulo Amaral
Goncalves, 7.00, 26.00, 33.00 / 10011497, Luiz Paulo Araujo Lima, 6.00, 28.00, 34.00 / 10001829, Luiz
Ricardo Duarte de Souza, 9.00, 44.00, 53.00 / 10001719, Luiza Ariadna Nascimento dos Santos, 8.00,
40.00, 48.00 / 10007978, Luiza Caroline Vasconcelos Vallinoto, 8.00, 28.00, 36.00 / 10001482, Luiza
Cristina Maia Dias Fernandes, 9.00, 44.00, 53.00 / 10000660, Luiza do Socorro Vieira Campos, 15.00,
54.00, 69.00 / 10016640, Luiza Gabriella Moreira Rodrigues, 12.00, 38.00, 50.00 / 10012098, Luiza Maria
Dias Pureza, 12.00, 48.00, 60.00 / 10001867, Luiza Rebelo Fernandes, 6.00, 30.00, 36.00 / 10008135, Luiza
Teles de Moraes Jaccoud, 9.00, 56.00, 65.00 / 10007828, Luka Grandal de Almeida, 11.00, 48.00, 59.00 /
10012897, Lukas Batista Sarmanho, 9.00, 54.00, 63.00 / 10001291, Luysa Thalia Batista Ribeiro, 10.00,
64.00, 74.00 / 10000055, Luzivaldo da Silva Santos, 7.00, 62.00, 69.00 / 10003042, Luzivan Lopes
Almeida, 12.00, 60.00, 72.00 / 10010238, Lyandro Pinheiro da Cunha, 9.00, 40.00, 49.00 / 10003039,
Lyvian Souza Santos, 13.00, 44.00, 57.00 / 10016464, Madson Gustavo Lima de Oliveira, 5.00, 36.00,
41.00 / 10000542, Madson Yan Araujo Rolim, 13.00, 52.00, 65.00 / 10000788, Magno Azevedo Santos,
10.00, 40.00, 50.00 / 10010852, Magno Carneiro Parente, 13.00, 58.00, 71.00 / 10013339, Magno Gilberto
Lopes Araujo, 7.00, 24.00, 31.00 / 10000237, Magno Jose Reis dos Santos Filho, 14.00, 66.00, 80.00 /
10012416, Maiane Feitosa Pereira, 7.00, 20.00, 27.00 / 10012159, Maiara Cristina Oliveira de Mesquita,
6.00, 28.00, 34.00 / 10002132, Maiara Martins de Almeida, 5.00, 34.00, 39.00 / 10002592, Maiara Sousa
Moraes, 12.00, 54.00, 66.00 / 10016133, Maicky Deivson Feitosa do Nascimento, 15.00, 54.00, 69.00 /
10011321, Maico Anderson da Silva Farias, 6.00, 56.00, 62.00 / 10000934, Maicon Galante, 9.00, 56.00,
65.00 / 10000762, Maikon Rigor Apoliano Aguiar, 6.00, 48.00, 54.00 / 10002893, Mairla Wellen da Silva
Cunha, 5.00, 22.00, 27.00 / 10000603, Maisa Miranda Carvalho, 4.00, 30.00, 34.00 / 10015713, Maisa
Nava Alves, 12.00, 38.00, 50.00 / 10011428, Maiter de Oliveira Silva, 8.00, 34.00, 42.00 / 10001670,
Manoel Frank Melo Goncalves, 10.00, 46.00, 56.00 / 10015984, Manoel Jose Rodrigues Neto, 11.00, 54.00,
65.00 / 10000802, Manoel Juarez de Sousa Weiss, 10.00, 62.00, 72.00 / 10001897, Manoel Mario Santos
Nery, 10.00, 42.00, 52.00 / 10012478, Manoel Ubiratan Lemos Lima, 10.00, 52.00, 62.00 / 10016565,
Manoel Vale de Araujo Junior, 11.00, 48.00, 59.00 / 10013155, Manoel Vicente da Conceicao Figueiredo, 9.00, 34.00, 43.00 / 10007598, Manoel Victor Soares de Leao, 7.00, 28.00, 35.00 / 10009257, Manoela
Caroline Alves Matos, 12.00, 56.00, 68.00 / 10002597, Manoela Ferreira Moreira, 9.00, 30.00, 39.00 /
10007813, Manuela da Silva Rodrigues, 13.00, 40.00, 53.00 / 10002365, Manuela Karine Gaspar de
Miranda, 8.00, 48.00, 56.00 / 10005238, Manuela Silva de Menezes, 17.00, 60.00, 77.00 / 10015787,
Manuella Muriel Coelho, 6.00, 24.00, 30.00 / 10011576, Marcela Ariel de Miranda Varela, 10.00, 26.00,
36.00 / 10001428, Marcela Correa Dias, 7.00, 48.00, 55.00 / 10001280, Marcela Larissa Batista Soares,
10.00, 22.00, 32.00 / 10001085, Marcela Renata Garcia Conceicao, 11.00, 40.00, 51.00 / 10000508,
Marcela Samia Silva de Lima, 8.00, 40.00, 48.00 / 10008159, Marcela Valeria Siqueira Silva, 6.00, 32.00,
38.00 / 10000560, Marcelle Brito Macario, 10.00, 38.00, 48.00 / 10000979, Marcellia Sousa Cavalcante,
14.00, 58.00, 72.00 / 10008115, Marcelo Amaral Hernandes, 8.00, 38.00, 46.00 / 10001839, Marcelo
Augusto Alencar dos Santos, 14.00, 44.00, 58.00 / 10012100, Marcelo Augusto Carvalho Rodrigues, 7.00,
38.00, 45.00 / 10010843, Marcelo Charles Lameira Costa Junior, 7.00, 46.00, 53.00 / 10013264, Marcelo
 
Chucre dos Reis, 10.00, 58.00, 68.00 / 10002837, Marcelo de Carvalho Lacerda, 13.00, 70.00, 83.00 /
10000999, Marcelo Eduardo Goncalves de Oliveira, 7.00, 52.00, 59.00 / 10009343, Marcelo Furtado
Pantoja, 8.00, 26.00, 34.00 / 10012261, Marcelo Igor da Silva Passos, 6.00, 34.00, 40.00 / 10002186,
Marcelo Melo Martins, 10.00, 32.00, 42.00 / 10011342, Marcelo Nazareno Luz de Lima Filho, 8.00, 34.00,
42.00 / 10015903, Marcia Caroline Lobo da Silva, 6.00, 28.00, 34.00 / 10011420, Marcia Isabela Souza
Risuenho, 16.00, 58.00, 74.00 / 10013300, Marcia Kaline Meireles Dias, 7.00, 34.00, 41.00 / 10012803, Marcia Lucia Kaila Viana da Silva, 10.00, 48.00, 58.00 / 10009942, Marcia Valeria Pereira da Conceicao, 10.00, 40.00, 50.00 / 10007582, Marciane Cruz do Nascimento, 10.00, 56.00, 66.00 / 10010264, Marciel
de Sousa Ferreira, 9.00, 36.00, 45.00 / 10016910, Marciele Alves de Sousa, 11.00, 32.00, 43.00 / 10013050,
Marcio Augusto Monte Bezerra, 14.00, 54.00, 68.00 / 10006857, Marcio Braga da Costa Junior, 8.00,
36.00, 44.00 / 10011220, Marcio Ferreira dos Santos, 9.00, 48.00, 57.00 / 10007418, Marcio Guimaraes da
Silva Junior, 9.00, 40.00, 49.00 / 10013495, Marcio Matheus Santos da Rocha, 7.00, 32.00, 39.00 /
10002631, Marcio Ronald Lima Fernandes, 11.00, 68.00, 79.00 / 10011077, Marcio Tulio Faria Bicalho,
13.00, 54.00, 67.00 / 10010121, Marcius Vinicius da Silva, 9.00, 46.00, 55.00 / 10012762, Marclei de
Oliveira, 9.00, 52.00, 61.00 / 10002019, Marco Aurelio Goes de Queiros, 9.00, 38.00, 47.00 / 10016573,
Marco Jose Andrade Cruz Filho, 9.00, 30.00, 39.00 / 10012489, Marco Leandro Oliveira Reis, 9.00, 42.00,
51.00 / 10012444, Marcos Adriano Pereira Nunes, 12.00, 74.00, 86.00 / 10007056, Marcos Alexandre
Araujo de Almeida, 8.00, 40.00, 48.00 / 10016325, Marcos Alves dos Santos, 11.00, 54.00, 65.00 /
10012007, Marcos Antonio Bezerra de Sa Ribeiro, 8.00, 26.00, 34.00 / 10017074, Marcos Augusto
Nascimento de Macedo, 7.00, 58.00, 65.00 / 10011764, Marcos Aurelio da Silva Fontes, 11.00, 50.00,
61.00 / 10005775, Marcos Aurelio Lopes de Oliveira Jorge, 17.00, 64.00, 81.00 / 10010806, Marcos David
Oliveira de Lima, 8.00, 54.00, 62.00 / 10006724, Marcos de Sousa Lima, 8.00, 52.00, 60.00 / 10003022,
Marcos Dias Leao, 17.00, 66.00, 83.00 / 10012659, Marcos Fernandes da Silva Junior, 7.00, 52.00, 59.00
/ 10010679, Marcos Franklin Barbosa da Silva, 10.00, 58.00, 68.00 / 10000422, Marcos Freire da Silva,
11.00, 42.00, 53.00 / 10008106, Marcos Henrique Melo Martins, 11.00, 34.00, 45.00 / 10015731, Marcos
Matheus Rodrigues Sousa, 11.00, 46.00, 57.00 / 10013372, Marcos Natha de Jesus Silva Everton, 8.00,
42.00, 50.00 / 10007314, Marcos Paulo Barros Ribeiro, 10.00, 34.00, 44.00 / 10013532, Marcos Paulo dos
Santos Moreno, 13.00, 62.00, 75.00 / 10011367, Marcos Paulo Marques Freitas, 8.00, 44.00, 52.00 /
10010774, Marcos Paulo Vilhena Barros Junior, 12.00, 46.00, 58.00 / 10005253, Marcos Saulo Rodrigues
Silva, 11.00, 48.00, 59.00 / 10016961, Marcos Sebastiao de Jesus Pinheiro, 8.00, 56.00, 64.00 / 10012233,
Marcos Venicios Paiva da Silva, 9.00, 46.00, 55.00 / 10011146, Marcos Vinicius Correa de Souza, 11.00,
52.00, 63.00 / 10013666, Marcos Vinicius da Costa Xavier, 7.00, 24.00, 31.00 / 10010711, Marcos Vinicius
da Silva Oliveira, 8.00, 28.00, 36.00 / 10013694, Marcos Vinicius dos Santos Paz, 11.00, 38.00, 49.00 /
10011053, Marcos Vinicius Galvao da Encarnacao, 9.00, 40.00, 49.00 / 10005383, Marcos Vinicius
Martins Batista, 13.00, 60.00, 73.00 / 10001174, Marcos Vinicius Pinheiro da Silva, 7.00, 34.00, 41.00 /
10010624, Marcos Vinicius Pinto Aguiar, 11.00, 50.00, 61.00 / 10001014, Marcos Zequias Amaro de Sousa
Mendes, 8.00, 48.00, 56.00 / 10010198, Marcus Andrade Costa, 12.00, 60.00, 72.00 / 10002362, Marcus
Vinicius Alves da Silva, 15.00, 54.00, 69.00 / 10011374, Marcus Vinicius Anaice Lopes, 14.00, 62.00,
76.00 / 10012043, Marcus Vinicius Barile Martins, 11.00, 46.00, 57.00 / 10009927, Marcus Vinicius de
Jesus Sousa, 17.00, 58.00, 75.00 / 10012457, Marcus Vinicius de Medeiros Barros, 8.00, 62.00, 70.00 /
10009346, Marcus Vinicius Silva Ferreira, 9.00, 34.00, 43.00 / 10011025, Marcus Vinicius Teixeira de
Oliveira Duarte, 5.00, 42.00, 47.00 / 10009880, Marden Ribeiro Pelerano, 7.00, 20.00, 27.00 / 10016646,
Maressa Cristina de Alfaia Pinheiro, 3.00, 24.00, 27.00 / 10005709, Maria Alice Ferreira da Silva, 8.00,
54.00, 62.00 / 10010171, Maria Antonia de Sousa, 9.00, 36.00, 45.00 / 10011065, Maria Beatriz Lopes
Rodrigues, 8.00, 34.00, 42.00 / 10012826, Maria do Rosario Pacifico Ribeiro, 9.00, 40.00, 49.00 /
10009434, Maria Eduarda Assis Covre, 14.00, 46.00, 60.00 / 10002992, Maria Eduarda Bastos Gomes,
6.00, 36.00, 42.00 / 10008017, Maria Eduarda de Sa Martins, 7.00, 30.00, 37.00 / 10011177, Maria Eduarda
dos Passos Goncalves, 11.00, 40.00, 51.00 / 10005417, Maria Eduarda Maceno de Lima, 8.00, 36.00, 44.00
/ 10008039, Maria Eliza Nazario de Souza, 8.00, 26.00, 34.00 / 10007198, Maria Graziela Monteiro do
Nascimento, 11.00, 38.00, 49.00 / 10009491, Maria Jhuliana Morais Barbosa, 9.00, 38.00, 47.00 /
10016693, Maria Karoline Moreira do Nascimento, 9.00, 62.00, 71.00 / 10012990, Maria Leticia Lima
Santos, 10.00, 36.00, 46.00 / 10002034, Maria Lucia Rodrigues da Costa, 6.00, 30.00, 36.00 / 10000454,
 
Maria Luiza Alves de Oliveira, 10.00, 54.00, 64.00 / 10013000, Maria Luiza dos Santos Pereira, 6.00,
26.00, 32.00 / 10012094, Maria Madalena Santos Silva, 8.00, 20.00, 28.00 / 10015857, Maria Monica Silva
dos Santos, 8.00, 40.00, 48.00 / 10005774, Maria Quiteria Miranda Nascimento da Silva, 10.00, 44.00,
54.00 / 10005578, Maria Raquel Neco Fernandes, 6.00, 42.00, 48.00 / 10007693, Maria Shelcy Souza
Lopes, 8.00, 54.00, 62.00 / 10011176, Maria Veronika Guedes da Silva, 10.00, 40.00, 50.00 / 10001389,
Maria Vitoria Leao Porto, 5.00, 40.00, 45.00 / 10007361, Maria Yasmin da Silva Gouvea, 9.00, 36.00,
45.00 / 10013267, Mariana Bandeira Teixeira, 11.00, 58.00, 69.00 / 10010854, Mariana Costa de Souza,
12.00, 44.00, 56.00 / 10005639, Mariana de Souza Pacheco, 9.00, 30.00, 39.00 / 10010234, Marielle de
Carvalho Andrade, 10.00, 38.00, 48.00 / 10009392, Marielle Negrao Ferreira, 5.00, 22.00, 27.00 /
10016792, Marielli de Queiroz e Souto, 5.00, 32.00, 37.00 / 10017045, Marilia Barbery Teixeira, 7.00,
34.00, 41.00 / 10010181, Mariluce Mendes Ribeiro, 7.00, 48.00, 55.00 / 10011181, Marilvany Jussara
Tapajos Cardoso, 15.00, 54.00, 69.00 / 10009593, Marilya Braga Costa, 8.00, 36.00, 44.00 / 10000677,
Marina da Silva Brasil, 12.00, 40.00, 52.00 / 10016377, Mario de Menezes Moreira Junior, 6.00, 52.00,
58.00 / 10007130, Mario dos Santos Brito Neto, 9.00, 50.00, 59.00 / 10002540, Mario Fernandes Maues,
14.00, 50.00, 64.00 / 10012954, Mario Henrique Ferreira da Silva Filho, 10.00, 54.00, 64.00 / 10002244,
Mario Nickson de Araujo Caetano, 7.00, 40.00, 47.00 / 10001413, Mario Willian Rodrigues de Sousa, 7.00,
52.00, 59.00 / 10015799, Marlen Torres Teixeira, 9.00, 36.00, 45.00 / 10016288, Marli de Cassia Rego
Correa, 8.00, 22.00, 30.00 / 10000897, Marliany de Cassia Silva da Silva, 3.00, 26.00, 29.00 / 10005246, Marlison Vitor dos Santos Batista, 15.00, 54.00, 69.00 / 10016225, Marlisson Quinzeiro Marinho Cruz, 9.00, 60.00, 69.00 / 10000989, Marllon Danillo Furtado da Silva, 10.00, 48.00, 58.00 / 10005543, Marlon
Bruno Alves, 3.00, 26.00, 29.00 / 10005784, Marlon Fernandes de Oliveira Filho, 8.00, 54.00, 62.00 /
10007321, Marlon Morais Ferreira, 8.00, 34.00, 42.00 / 10016664, Marlus Williams de Souza Santos,
10.00, 52.00, 62.00 / 10008162, Marluvia Roberta Coutinho de Oliveira, 6.00, 34.00, 40.00 / 10009543,
Mary Anne da Silva Birto, 15.00, 44.00, 59.00 / 10002431, Maryelle Rodrigues Oliveira, 10.00, 32.00,
42.00 / 10002929, Mateus Adriano Jardim Cavalcante, 12.00, 50.00, 62.00 / 10002952, Mateus Calebe da
Silva Rabelo, 10.00, 58.00, 68.00 / 10005382, Mateus Casemiro Araujo, 13.00, 48.00, 61.00 / 10013436,
Mateus Chaves de Sousa, 10.00, 50.00, 60.00 / 10013734, Mateus da Costa Gomes, 5.00, 28.00, 33.00 /
10010707, Mateus da Costa Rodrigues, 12.00, 38.00, 50.00 / 10012399, Mateus Gabriel Silva de Vilhena,
11.00, 30.00, 41.00 / 10009262, Mateus Juan Barreto da Costa, 5.00, 38.00, 43.00 / 10002108, Mateus Leite
Ferreira, 11.00, 58.00, 69.00 / 10016389, Mateus Luiz Silva Burcaos de Oliveira, 7.00, 46.00, 53.00 /
10007479, Mateus Moreira Nobre, 9.00, 34.00, 43.00 / 10005236, Mateus Nalbert de Oliveira da Rocha,
10.00, 54.00, 64.00 / 10005633, Mateus Parente da Silva, 9.00, 50.00, 59.00 / 10001912, Mateus Pereira
da Silva, 9.00, 30.00, 39.00 / 10007681, Mateus Rafael de Souza Angelim de Lima, 8.00, 48.00, 56.00 /
10011205, Mateus Soeiro da Costa, 13.00, 64.00, 77.00 / 10000547, Mateus Souza Santos, 8.00, 28.00,
36.00 / 10000207, Matheus Alencar de Sousa, 10.00, 52.00, 62.00 / 10005239, Matheus Alencar Oliveira,
7.00, 38.00, 45.00 / 10010685, Matheus Andrade Santana, 14.00, 66.00, 80.00 / 10007867, Matheus Bellard
Pereira Mariuba, 9.00, 48.00, 57.00 / 10013629, Matheus da Silva Franco, 14.00, 60.00, 74.00 / 10007253,
Matheus da Silva Pinheiro, 10.00, 60.00, 70.00 / 10005260, Matheus da Silva Santa Brigida, 7.00, 36.00,
43.00 / 10009943, Matheus Dantas Lima Santiago, 9.00, 46.00, 55.00 / 10011435, Matheus Davi Araujo
Porto, 7.00, 38.00, 45.00 / 10007810, Matheus de Lima Silva, 11.00, 48.00, 59.00 / 10006812, Matheus de
Oliveira Lima, 15.00, 50.00, 65.00 / 10010953, Matheus Defensor Norat, 14.00, 44.00, 58.00 / 10008126,
Matheus dos Santos Pereira, 8.00, 36.00, 44.00 / 10000013, Matheus Emyr Nogueira Portela, 6.00, 28.00,
34.00 / 10010965, Matheus Farias Santos, 7.00, 36.00, 43.00 / 10010257, Matheus Feitosa da Silva, 11.00,
62.00, 73.00 / 10011495, Matheus Felipe Lima de Oliveira, 8.00, 38.00, 46.00 / 10012409, Matheus Felipe
Lopes Santos, 12.00, 60.00, 72.00 / 10001268, Matheus Felipe Pedrosa Gomes, 10.00, 46.00, 56.00 /
10000412, Matheus Fernandes Maues, 10.00, 58.00, 68.00 / 10016485, Matheus Ferreira da Silva, 10.00,
48.00, 58.00 / 10002384, Matheus Franco Lopes, 18.00, 66.00, 84.00 / 10010108, Matheus Henrich Nunes
Alves de Menezes, 12.00, 64.00, 76.00 / 10007183, Matheus Henrique Cordeiro Matos, 9.00, 24.00, 33.00
/ 10009327, Matheus Henrique Cutrim de Miranda, 9.00, 36.00, 45.00 / 10000759, Matheus Henrique de
Lima Fonseca, 12.00, 52.00, 64.00 / 10010748, Matheus Henrique Ribeiro Miranda, 9.00, 34.00, 43.00 /
10007695, Matheus Henrique Soares Costa, 7.00, 50.00, 57.00 / 10005231, Matheus Henrique Souza
Bitencourt, 13.00, 58.00, 71.00 / 10002006, Matheus Jose Maia de Souza Martins Lima, 14.00, 70.00, 84.00
 
/ 10002170, Matheus Kizan Oliveira Cunha, 7.00, 46.00, 53.00 / 10007713, Matheus Lopes da Silva Sousa,
7.00, 32.00, 39.00 / 10007527, Matheus Lopes de Araujo, 7.00, 40.00, 47.00 / 10013340, Matheus Macedos
Marinho, 9.00, 30.00, 39.00 / 10007083, Matheus Malhao Hertzog, 14.00, 60.00, 74.00 / 10010430,
Matheus Marinho Moura, 9.00, 58.00, 67.00 / 10008206, Matheus Montao Medeiros, 11.00, 40.00, 51.00 /
10006918, Matheus Nascimento Pinheiro de Miranda, 10.00, 48.00, 58.00 / 10012784, Matheus Oliveira
de Sousa, 9.00, 44.00, 53.00 / 10016167, Matheus Oliveira Martins, 13.00, 66.00, 79.00 / 10000251,
Matheus Pereira do Santos, 11.00, 56.00, 67.00 / 10013033, Matheus Pereira Monteiro Batista, 12.00,
50.00, 62.00 / 10013024, Matheus Phelipe de Freitas Bastos, 10.00, 38.00, 48.00 / 10010225, Matheus
Pinheiro Flor de Lima, 8.00, 16.00, 24.00 / 10002470, Matheus Quaresma de Almeida, 9.00, 48.00, 57.00
/ 10009263, Matheus Queiros Pereira, 8.00, 28.00, 36.00 / 10010364, Matheus Ribeiro Soares, 12.00, 62.00,
74.00 / 10001133, Matheus Rodrigo Freitas de Castro Costa, 13.00, 64.00, 77.00 / 10006898, Matheus
Rodrigues Lima, 5.00, 24.00, 29.00 / 10001321, Matheus Santana Gomes, 7.00, 34.00, 41.00 / 10007578, Matheus Vinicius Soares de Almeida, 9.00, 46.00, 55.00 / 10000494, Matheus Wanderson de Souza Barbosa, 6.00, 34.00, 40.00 / 10012740, Matheus Williams Santos de Leao, 8.00, 42.00, 50.00 / 10000716,
Mathews Cardoso de Almeida, 9.00, 48.00, 57.00 / 10000484, Matias Costa Bittencourth, 14.00, 68.00,
82.00 / 10016414, Mattheus Monteiro Costa Silva, 11.00, 38.00, 49.00 / 10001385, Maura Marcelino Silva
Assis, 5.00, 34.00, 39.00 / 10002169, Mauricio Barbosa da Silva, 11.00, 52.00, 63.00 / 10009664, Mauricio
Correa dos Santos, 8.00, 56.00, 64.00 / 10007897, Mauricio Farias de Lemos, 9.00, 30.00, 39.00 /
10011625, Mauricio Henrique Oliveira Rego, 7.00, 42.00, 49.00 / 10012022, Mauricio Kaue Saraiva
Santos, 16.00, 54.00, 70.00 / 10010799, Mauricio Mendes Cabral, 9.00, 28.00, 37.00 / 10007606, Mauricio
Santana da Silva, 8.00, 28.00, 36.00 / 10002993, Maurileide Costa da Cruz, 9.00, 38.00, 47.00 / 10000081,
Mauro Cesar Ferreira Rocha, 5.00, 58.00, 63.00 / 10000133, Mauro Monteiro Ferreira, 12.00, 64.00, 76.00
/ 10002635, Mauro Pedro Alves Junior, 9.00, 52.00, 61.00 / 10001473, Mauro Rafael Machado Rodrigues,
9.00, 36.00, 45.00 / 10011774, Max Alexandre Ferreira Guedes, 7.00, 54.00, 61.00 / 10002728, Max
Andresson Teixeira Gouveia, 11.00, 48.00, 59.00 / 10013231, Max de Souza Batista, 8.00, 42.00, 50.00 /
10001266, Max Marques Moura, 13.00, 68.00, 81.00 / 10001114, Max Muller Silva de Sousa, 13.00, 72.00,
85.00 / 10012864, Max Oliveira de Sousa, 8.00, 40.00, 48.00 / 10007767, Max Roberto Guimaraes, 13.00,
44.00, 57.00 / 10001586, Max Vinicius Carvalho Freitas, 10.00, 46.00, 56.00 / 10014713, Max Weyler
Paraense Baia, 10.00, 60.00, 70.00 / 10011250, Maxsuel dos Santos Souza, 13.00, 56.00, 69.00 / 10010670,
Maxsuel Ferreira da Silva, 8.00, 32.00, 40.00 / 10012402, Maxweel Ribeiro da Silva, 10.00, 46.00, 56.00 /
10012343, Maxwell Lima de Oliveira, 9.00, 32.00, 41.00 / 10013553, Mayane Lucia Braga David Pereira,
11.00, 44.00, 55.00 / 10002455, Mayara da Silva Martins, 9.00, 32.00, 41.00 / 10001851, Mayara Martina
dos Santos Sa, 7.00, 38.00, 45.00 / 10001939, Mayara Moraes Moura, 6.00, 28.00, 34.00 / 10005205,
Mayara Silva de Souza, 11.00, 34.00, 45.00 / 10011043, Mayara Vieira de Sa, 7.00, 40.00, 47.00 /
10011312, Mayarah Cristina Souza da Silva, 8.00, 30.00, 38.00 / 10010381, Maycon David Trindade de
Figueiredo, 13.00, 58.00, 71.00 / 10000263, Maycon Douglas Benjamim de Souza, 10.00, 52.00, 62.00 /
10013669, Maycon Douglas Fernandes de Sousa, 6.00, 42.00, 48.00 / 10010736, Maycon Douglas Pantoja
Bitencourt, 9.00, 56.00, 65.00 / 10017110, Maycon Oliveira dos Santos, 11.00, 58.00, 69.00 / 10016751,
Maycon Roberto de Lima Maximo, 6.00, 26.00, 32.00 / 10012400, Mayda Silva Araujo, 10.00, 46.00, 56.00
/ 10005446, Mayellen Barros Santos, 9.00, 60.00, 69.00 / 10007619, Maykelle Silva dos Santos, 10.00,
28.00, 38.00 / 10001503, Maykon Jhonny Vieira Carvalho, 12.00, 38.00, 50.00 / 10005467, Mayla
Fernandes Varejao Souto, 8.00, 36.00, 44.00 / 10007946, Mayla Lais Moita Fonseca, 10.00, 54.00, 64.00 /
10001880, Mayllan Alberth Dias Lopes, 11.00, 56.00, 67.00 / 10005405, Mayron da Silva Matos, 11.00,
42.00, 53.00 / 10007275, Maysa Dias da Silva, 7.00, 42.00, 49.00 / 10009687, Maysa Gemaque Vieira,
8.00, 44.00, 52.00 / 10011323, Mayza Araujo Correa, 10.00, 52.00, 62.00 / 10011107, Mel Lana Santana
da Silva, 7.00, 30.00, 37.00 / 10012901, Melina Cabral Alvarez Olher Medina, 15.00, 68.00, 83.00 /
10015956, Melissa Ferreira de Melo Pita, 11.00, 36.00, 47.00 / 10000140, Melissa Franca Cordeiro, 8.00,
30.00, 38.00 / 10016165, Melissa Paula Alhadef Feijao de Oliveira, 7.00, 34.00, 41.00 / 10011348, Melky
Andre Costa Duarte Leite, 7.00, 30.00, 37.00 / 10000883, Melquizedeque Oliveira Lopes, 8.00, 36.00,
44.00 / 10011544, Messias Carlos de Carvalho Dantas, 10.00, 34.00, 44.00 / 10011030, Messias Sousa de
Almeida, 6.00, 44.00, 50.00 / 10007655, Meuk Jhonson Alves Goncalves, 7.00, 46.00, 53.00 / 10005525,
Micael Felipe dos Reis Silva, 7.00, 30.00, 37.00 / 10011361, Micaela dos Santos Souza, 11.00, 46.00, 57.00
 
/ 10010862, Michael Douglas Lima Santos, 10.00, 54.00, 64.00 / 10002291, Michael Pereira da Silva,
12.00, 46.00, 58.00 / 10012670, Michel Amazonas Cotta Junior, 10.00, 64.00, 74.00 / 10016049, Michel
Simplicio de Sousa, 12.00, 62.00, 74.00 / 10010513, Michelle Caroline Carvalho da Silva Teixeira, 14.00,
56.00, 70.00 / 10001316, Michelly Daylanne Lima de Araujo, 4.00, 40.00, 44.00 / 10012421, Michelly
Silva Sandes, 11.00, 40.00, 51.00 / 10010050, Michely Bianca dos Santos Fiel, 4.00, 30.00, 34.00 /
10016098, Mickaely de Lima Gomes, 9.00, 48.00, 57.00 / 10002716, Miguel Anailton Lima da Silva, 10.00,
40.00, 50.00 / 10010480, Miguel Bezerra de Araujo Neto, 8.00, 46.00, 54.00 / 10000804, Miguel Emanoel
Ferreira Moraes, 5.00, 30.00, 35.00 / 10003045, Mik Roberth de Souza Guimaraes, 7.00, 50.00, 57.00 /
10007464, Mika Elle do Nascimento Pinto, 10.00, 46.00, 56.00 / 10016353, Mikaella Silva dos Santos,
8.00, 34.00, 42.00 / 10011035, Milena de Oliveira Fonseca, 16.00, 54.00, 70.00 / 10013326, Milena Pereira
da Silva, 5.00, 24.00, 29.00 / 10010463, Milena Silva Leal, 9.00, 38.00, 47.00 / 10002770, Milene Castro
de Vilhena, 6.00, 40.00, 46.00 / 10007891, Milina Maria Silva Vieira, 4.00, 24.00, 28.00 / 10011731, Milla
Juliana Costa Goncalves, 11.00, 44.00, 55.00 / 10002768, Millena Jayne Costa Lopes, 15.00, 60.00, 75.00
/ 10012611, Millene Antonia Moraes Santos, 4.00, 34.00, 38.00 / 10006921, Miller Eduardo Mendes
Moraes, 10.00, 52.00, 62.00 / 10011752, Milson Gabriel de Matos Dias, 10.00, 60.00, 70.00 / 10001209,
Milson Nascimento Araujo, 11.00, 52.00, 63.00 / 10005320, Milton Jose da Silva Neto, 13.00, 58.00, 71.00
/ 10000419, Minael Pereira Lagoia, 10.00, 58.00, 68.00 / 10007406, Mirelly Britto Pires, 12.00, 44.00,
56.00 / 10010310, Miriam Lorena Braga Rente, 12.00, 30.00, 42.00 / 10001486, Mirian de Oliveira Ribeiro,
12.00, 48.00, 60.00 / 10009494, Mirlen Sousa de Sousa, 4.00, 24.00, 28.00 / 10000469, Misael Nascimento
Medeiros, 3.00, 24.00, 27.00 / 10009615, Misael Pinheiro Oliveira, 6.00, 28.00, 34.00 / 10000978, Mislav
de Sousa Santos, 8.00, 40.00, 48.00 / 10016017, Mizael Lima Belem, 11.00, 58.00, 69.00 / 10012147,
Moabe Roberto Oliveira de Freitas, 7.00, 38.00, 45.00 / 10002628, Moises Cosmo Medrade, 13.00, 60.00,
73.00 / 10016287, Moises Dutra de Lima Junior, 14.00, 50.00, 64.00 / 10007872, Monic Fonseca Furtado,
10.00, 34.00, 44.00 / 10013409, Monica Maria Hecke Araujo, 13.00, 64.00, 77.00 / 10012433, Monick
Laise Peixoto da Silva, 9.00, 46.00, 55.00 / 10016394, Monique Blandina da Silva Pinheiro, 7.00, 18.00,
25.00 / 10007931, Monique Kevia Correa Oliveira, 6.00, 40.00, 46.00 / 10009483, Mozaniel Aquino
Pinheiro Filho, 5.00, 32.00, 37.00 / 10010241, Murillo Henryk Barros de Oliveira, 12.00, 48.00, 60.00 /
10009862, Murilo Abraao Alves Silva, 11.00, 50.00, 61.00 / 10016031, Murilo Macedo Sarmanho, 7.00,
40.00, 47.00 / 10005505, Mykael Lima Melo, 14.00, 60.00, 74.00 / 10011737, Mylena Rossato Marques,
14.00, 48.00, 62.00 / 10013388, Myrlen da Macena Nogueira, 10.00, 40.00, 50.00 / 10005462, Naandro
Abner Silva Costa, 5.00, 38.00, 43.00 / 10010850, Naane Adria Pereira Lima, 8.00, 34.00, 42.00 /
10007611, Nadson de Souza Martins, 14.00, 52.00, 66.00 / 10010607, Nadson Sousa Lima, 9.00, 38.00,
47.00 / 10011571, Naely dos Santos Moreira, 11.00, 38.00, 49.00 / 10013378, Naila Cristina Silva Alves,
9.00, 30.00, 39.00 / 10009432, Naillson Sousa Ferreira, 12.00, 52.00, 64.00 / 10012253, Naina Barbosa
Feio, 13.00, 58.00, 71.00 / 10005592, Naine Sobrinho Sampaio, 14.00, 54.00, 68.00 / 10013653, Naldyellen
do Socorro Vieira Souza, 11.00, 44.00, 55.00 / 10012802, Naslo Enrique Sousa Pereira, 8.00, 38.00, 46.00
/ 10000316, Natacha Pamela Martins Mendes, 12.00, 58.00, 70.00 / 10007232, Natali Alexia Leite Teixeira,
15.00, 54.00, 69.00 / 10007823, Natalia Arruda Ribeiro, 11.00, 58.00, 69.00 / 10013726, Natalia Barroso
Oliveira, 6.00, 30.00, 36.00 / 10009945, Natalia Defensor Norat, 10.00, 44.00, 54.00 / 10000593, Natalia
do Rosario Moraes, 2.00, 24.00, 26.00 / 10001018, Natalia Ferreira Mesquita, 8.00, 44.00, 52.00 /
10001391, Natalia Lopes dos Santos, 11.00, 66.00, 77.00 / 10010763, Natalia Maria Rodrigues Braga,
12.00, 56.00, 68.00 / 10009520, Natalia Pereira Silva, 11.00, 46.00, 57.00 / 10012339, Natalia Ribeiro
Gomes, 12.00, 50.00, 62.00 / 10010542, Natalya Silva Oliveira, 8.00, 42.00, 50.00 / 10011693, Natan
Andrade Evangelista, 12.00, 60.00, 72.00 / 10000365, Natanael Rodrigues Damasceno, 10.00, 40.00, 50.00
/ 10013270, Natasha Paes Barbosa, 10.00, 48.00, 58.00 / 10006882, Natasha Samanta Briglia Guerra, 16.00,
48.00, 64.00 / 10017034, Natha Gustavo dos Santos Oliveira, 8.00, 40.00, 48.00 / 10009849, Nathalia
Amanda Brito Barbosa, 15.00, 52.00, 67.00 / 10011168, Nathalia Amaral Celso, 10.00, 42.00, 52.00 /
10012148, Nathalia Jacome Viana, 10.00, 56.00, 66.00 / 10013506, Nathalia Rayanne Pereira Quadros,
5.00, 48.00, 53.00 / 10007628, Nathalia Santos Leao, 5.00, 20.00, 25.00 / 10000921, Nathalia Silva Torres,
12.00, 36.00, 48.00 / 10009636, Nathaly Amanajas de Souza, 6.00, 36.00, 42.00 / 10012824, Nathan da
Silva Martins Lopes, 9.00, 34.00, 43.00 / 10001754, Nathielle Santos da Silva, 9.00, 46.00, 55.00 /
10000187, Nayara Alves de Jesus, 10.00, 50.00, 60.00 / 10010506, Nayara Andreza Monteiro Matos, 8.00,
 
56.00, 64.00 / 10000505, Nayara Cristina Menezes de Lima Santos, 14.00, 66.00, 80.00 / 10012944, Nayara
Cruz Lima, 6.00, 44.00, 50.00 / 10012894, Nayla Rayanne Oliveira Marques, 7.00, 56.00, 63.00 /
10002918, Neemias Ferreira dos Santos, 9.00, 50.00, 59.00 / 10013153, Nei Luis Tavares Barbosa, 13.00,
52.00, 65.00 / 10011390, Neide Franca Gouveia, 9.00, 70.00, 79.00 / 10012641, Neilson Manoel da Silva
Teixeira, 5.00, 28.00, 33.00 / 10011879, Nelson Bogea Nunes de Souza, 12.00, 56.00, 68.00 / 10008158, Nelson Luis da Conceicao Figueiredo, 10.00, 38.00, 48.00 / 10010637, Neudson de Jesus da Silva Junior, 14.00, 44.00, 58.00 / 10011018, Neylon Wendril Sousa Costa, 7.00, 36.00, 43.00 / 10013725, Nichollas
Yohan Teixeira Alves da Costa, 7.00, 26.00, 33.00 / 10011941, Nicolas Robson Favacho Marques, 12.00,
32.00, 44.00 / 10015810, Nicole Ferreira Alfaia, 11.00, 54.00, 65.00 / 10001497, Nicole Lima Galucio,
9.00, 44.00, 53.00 / 10011727, Nicolle Larissa da Silva Abreu, 10.00, 36.00, 46.00 / 10011330, Nielson
Antonio Caxias Marques, 8.00, 24.00, 32.00 / 10011911, Nildo Alves Madeiro, 13.00, 40.00, 53.00 /
10000794, Nilmara Azevedo de Lima, 12.00, 30.00, 42.00 / 10005226, Nilson Cartagenes Sousa Filho,
7.00, 32.00, 39.00 / 10013715, Nilson Markes Cardoso Rodrigues, 11.00, 54.00, 65.00 / 10002889, Nilton
Jorge Imbiriba de Araujo, 14.00, 46.00, 60.00 / 10005369, Nilza Pinheiro Antunes, 5.00, 38.00, 43.00 /
10002003, Nonato Goes Coelho, 11.00, 44.00, 55.00 / 10002302, Odailson Junior Silva de Oliveira, 10.00,
50.00, 60.00 / 10000781, Odilene da Silva Santos, 11.00, 46.00, 57.00 / 10016743, Odilon Lobo Pereira,
7.00, 40.00, 47.00 / 10002535, Odilon Vitor Oliveira Luz Aragao, 13.00, 50.00, 63.00 / 10016867, Odorico
Allan Guedes Ferreira, 9.00, 34.00, 43.00 / 10011780, Orisleida dos Santos Passaranuque, 9.00, 46.00,
55.00 / 10013099, Orlando Rennan Rodrigues da Silva, 11.00, 56.00, 67.00 / 10013637, Osailton Junior
Morais Costa, 10.00, 40.00, 50.00 / 10011829, Oseas dos Santos Lima, 9.00, 44.00, 53.00 / 10012312,
Osmar da Silva Neves, 11.00, 46.00, 57.00 / 10013076, Otanniel Ferreira Santos, 10.00, 36.00, 46.00 /
10012632, Otaviano Alves da Silva Neto, 13.00, 52.00, 65.00 / 10012205, Otavio Costa Garcia, 15.00,
28.00, 43.00 / 10010186, Otavio Ferreira Alves, 8.00, 28.00, 36.00 / 10001279, Otavio Matias Xavier,
12.00, 50.00, 62.00 / 10001933, Otavio Michel Pinheiro dos Santos, 7.00, 40.00, 47.00 / 10012362, Otniel
de Souza Lima, 12.00, 60.00, 72.00 / 10010966, Pablo de Souza Jesus, 13.00, 46.00, 59.00 / 10001593,
Pablo Fernando Francisco Reis, 15.00, 56.00, 71.00 / 10011506, Pablo Henrique Maciel Leite, 10.00, 56.00,
66.00 / 10003032, Pablo Roberto Santos da Costa, 8.00, 32.00, 40.00 / 10006728, Pablo Ryan Fernandes
Sirqueira, 6.00, 24.00, 30.00 / 10007575, Pablo Simoes Ferreira Cortes, 7.00, 32.00, 39.00 / 10009913,
Pablo Victor Alves Sousa, 7.00, 38.00, 45.00 / 10011011, Pablo Wdson de Araujo Chaves, 9.00, 60.00,
69.00 / 10010745, Pablo Weslley Esquerdo Vieira, 11.00, 56.00, 67.00 / 10001392, Pablo Willians Santos
Rodrigues, 3.00, 24.00, 27.00 / 10005370, Paloma de Souza Rodrigues Batista, 13.00, 64.00, 77.00 /
10012676, Paloma Pereira Paixao, 9.00, 28.00, 37.00 / 10000079, Pamela Andara Lemos Barreira, 13.00,
60.00, 73.00 / 10013283, Pamela Dandara Pinheiro do Nascimento, 10.00, 42.00, 52.00 / 10002449, Pamela
Ketheleen Sousa Barros, 11.00, 50.00, 61.00 / 10011148, Pamela Rafaela Bezerra Lima, 7.00, 22.00, 29.00
/ 10011149, Pamela Raquel Viana de Oliveira, 12.00, 70.00, 82.00 / 10007884, Pamela Thayanne Dias
Guimaraes, 11.00, 44.00, 55.00 / 10012744, Pamella Cristina Martins Castro, 11.00, 46.00, 57.00 /
10012422, Paola Araujo Tavares, 7.00, 42.00, 49.00 / 10016802, Paola Lameira Vieira, 14.00, 52.00, 66.00
/ 10000512, Paola Leao Delgado, 12.00, 56.00, 68.00 / 10003079, Paolla Xaianny Coelho Sousa, 8.00,
22.00, 30.00 / 10002240, Paolo Ferreira Veloso, 12.00, 54.00, 66.00 / 10008120, Patricia Gabriele Palhano
Souza, 14.00, 52.00, 66.00 / 10002177, Patricia Monteiro de Amorim, 15.00, 76.00, 91.00 / 10012363,
Patricia Paiva Costa, 8.00, 44.00, 52.00 / 10002931, Patricia Silva Bruzelo, 4.00, 30.00, 34.00 / 10000666,
Patricia Taveira Tavares, 15.00, 52.00, 67.00 / 10008083, Patrick Amorim Silva, 7.00, 38.00, 45.00 /
10012272, Patrick Araujo Barros, 12.00, 56.00, 68.00 / 10011657, Patrick da Silva Torres, 7.00, 34.00,
41.00 / 10000545, Patrick Evangelista Neto, 10.00, 60.00, 70.00 / 10010227, Patrick Jackson Amaral
Pereira, 8.00, 34.00, 42.00 / 10009868, Patrick Luis Mendes dos Santos, 10.00, 34.00, 44.00 / 10015792,
Patrick Pinho Dias, 14.00, 60.00, 74.00 / 10011839, Patrik Alves Pereira, 8.00, 48.00, 56.00 / 10003161,
Paula Caroline Vonlohrmann Barra Cruz, 11.00, 46.00, 57.00 / 10013691, Paula Castro dos Santos, 8.00,
40.00, 48.00 / 10016932, Paula Cleiceani Ferreira Baia, 6.00, 30.00, 36.00 / 10012351, Paula Daniela
Nascimento de Morais, 8.00, 30.00, 38.00 / 10016833, Paula Freitas de Santana, 10.00, 46.00, 56.00 /
10000768, Paula Janaina Azevedo de Oliveira, 11.00, 46.00, 57.00 / 10012197, Paula Veronica Monteiro
Barbosa, 7.00, 24.00, 31.00 / 10002368, Paulo Alexandre Duarte Costa, 10.00, 58.00, 68.00 / 10015866,
Paulo Anderson Dias Boucao, 11.00, 50.00, 61.00 / 10001075, Paulo Andre Pantoja, 10.00, 56.00, 66.00 /
 
10016460, Paulo Antonio Cardoso de Souza, 14.00, 50.00, 64.00 / 10000604, Paulo Arthur Sobreira
Ribeiro, 8.00, 34.00, 42.00 / 10013379, Paulo Cesar da Silva Cunha, 12.00, 44.00, 56.00 / 10007263, Paulo
Cesar Pereira Farias, 14.00, 54.00, 68.00 / 10010724, Paulo Cesar Reboucas da Silva, 9.00, 54.00, 63.00 /
10008109, Paulo Christian de Almeida Bittencourt, 8.00, 46.00, 54.00 / 10001895, Paulo de Jesus Pinheiro,
13.00, 60.00, 73.00 / 10005460, Paulo de Tarso Avelar Fernandes, 14.00, 58.00, 72.00 / 10011329, Paulo
de Tarso Nogueira Araujo, 8.00, 48.00, 56.00 / 10011785, Paulo Fernando Dias Barros, 5.00, 34.00, 39.00
/ 10009295, Paulo Gabriel Pinheiro Gonçalves Ribeiro, 9.00, 44.00, 53.00 / 10005621, Paulo Henrique
Alves Muller, 14.00, 56.00, 70.00 / 10001526, Paulo Henrique do Carmo Silva, 10.00, 48.00, 58.00 /
10010120, Paulo Henrique Freitas de Castro, 15.00, 70.00, 85.00 / 10010756, Paulo Henrique Pereira Brito,
10.00, 64.00, 74.00 / 10002829, Paulo Henrique Sousa Marinho, 8.00, 26.00, 34.00 / 10013502, Paulo Jairo
Muniz Martins, 12.00, 34.00, 46.00 / 10012770, Paulo Jobson Nascimento Monteiro, 12.00, 46.00, 58.00 /
10013381, Paulo Matheus Machado da Silva, 14.00, 60.00, 74.00 / 10016435, Paulo Mathias Amarante
Dias, 10.00, 36.00, 46.00 / 10010501, Paulo Rafael Martins Baia, 7.00, 44.00, 51.00 / 10011206, Paulo
Ramon Sousa Ferreira, 7.00, 36.00, 43.00 / 10001563, Paulo Ricardo Brito da Costa, 9.00, 34.00, 43.00 /
10011479, Paulo Ricardo Silva Carvalho, 6.00, 44.00, 50.00 / 10000194, Paulo Roberto de Souza Santos,
13.00, 58.00, 71.00 / 10015761, Paulo Rodrigo Marinho de Lacerda, 8.00, 38.00, 46.00 / 10000903, Paulo
Rodrigo Viana Soares, 9.00, 38.00, 47.00 / 10003083, Paulo Rodrigues Girao da Silva, 10.00, 46.00, 56.00
/ 10011351, Paulo Sergio Correa Oliveira, 14.00, 56.00, 70.00 / 10005342, Paulo Sergio Machado Barbosa
da Silva, 10.00, 62.00, 72.00 / 10007892, Paulo Sylber do Nascimento Gusmao, 8.00, 50.00, 58.00 /
10012727, Paulo Vale Cardoso, 7.00, 56.00, 63.00 / 10000029, Paulo Victor da Costa Santos, 10.00, 28.00,
38.00 / 10007173, Paulo Victor Guimaraes de Moura, 6.00, 52.00, 58.00 / 10016311, Paulo Victor Pereira
Noronha, 10.00, 32.00, 42.00 / 10010141, Paulo Victor Silva Guerreiro, 11.00, 48.00, 59.00 / 10017005,
Paulo Victor Sousa Nunes, 7.00, 52.00, 59.00 / 10002102, Paulo Vinicius da Luz Silva, 14.00, 40.00, 54.00
/ 10002393, Paulo Vinicius de Araujo Silva, 10.00, 48.00, 58.00 / 10013550, Paulo Wallison Sales
Modesto, 8.00, 48.00, 56.00 / 10010087, Pedro Acassio Coelho Morais, 10.00, 26.00, 36.00 / 10007862, Pedro Alexandre Amorim Moreira Filho, 9.00, 40.00, 49.00 / 10007915, Pedro Antonio Pinheiro Bonatti, 10.00, 68.00, 78.00 / 10010314, Pedro Artur Leal Amorim, 8.00, 32.00, 40.00 / 10006769, Pedro da Silva
Miranda, 12.00, 60.00, 72.00 / 10005662, Pedro Emanoel Walter, 5.00, 30.00, 35.00 / 10012966, Pedro Enrique Lima Aleixo dos Santos, 6.00, 52.00, 58.00 / 10011825, Pedro Enzo Souza de Miranda Vieira, 9.00, 54.00, 63.00 / 10000614, Pedro Felipe Alves Ribeiro, 14.00, 56.00, 70.00 / 10009900, Pedro
Fernandes dos Santos Junior, 10.00, 38.00, 48.00 / 10012450, Pedro Henri Marques Xavier Gomes, 9.00,
30.00, 39.00 / 10012360, Pedro Henrique Abussafi Miranda Nogueira Vasconcelos, 8.00, 36.00, 44.00 /
10011186, Pedro Henrique Alves Neves, 10.00, 56.00, 66.00 / 10012025, Pedro Henrique Araujo de Lelis,
14.00, 58.00, 72.00 / 10001674, Pedro Henrique Araujo Monteiro, 12.00, 52.00, 64.00 / 10001130, Pedro
Henrique Carneiro Vieiria, 9.00, 62.00, 71.00 / 10002155, Pedro Henrique Carvalho das Neves, 13.00,
56.00, 69.00 / 10007887, Pedro Henrique da Silva, 12.00, 52.00, 64.00 / 10016926, Pedro Henrique da
Silva Machado, 12.00, 52.00, 64.00 / 10009492, Pedro Henrique da Silva Pacheco, 7.00, 40.00, 47.00 /
10010737, Pedro Henrique de Moraes Ericeira, 8.00, 36.00, 44.00 / 10010302, Pedro Henrique Ferreira
Cardoso, 13.00, 58.00, 71.00 / 10011124, Pedro Henrique Lima de Souza, 8.00, 32.00, 40.00 / 10001093,
Pedro Henrique Lima Silva, 11.00, 28.00, 39.00 / 10001570, Pedro Henrique Moura da Silva, 8.00, 60.00,
68.00 / 10011332, Pedro Henrique Silva da Silva, 14.00, 38.00, 52.00 / 10013158, Pedro Henrique Silva
Delgado, 10.00, 44.00, 54.00 / 10010391, Pedro Henrique Trajano da Silva, 9.00, 42.00, 51.00 / 10010629,
Pedro Henrique Trindade Costa, 10.00, 62.00, 72.00 / 10009522, Pedro Higor Almeida de Jesus, 5.00,
34.00, 39.00 / 10005616, Pedro Ivo Gomes dos Santos, 9.00, 46.00, 55.00 / 10012187, Pedro Kazutoshi,
7.00, 22.00, 29.00 / 10000453, Pedro Lucas Barbosa de Souza, 6.00, 24.00, 30.00 / 10005748, Pedro Lucas
Castro Soares, 8.00, 42.00, 50.00 / 10000135, Pedro Lucas de Oliveira Rodrigues, 15.00, 64.00, 79.00 /
10013488, Pedro Lucas Ferreira Araujo, 8.00, 34.00, 42.00 / 10009490, Pedro Lucas Lima Sanches, 9.00,
58.00, 67.00 / 10007688, Pedro Luis da Silva Gomes, 2.00, 20.00, 22.00 / 10016884, Pedro Luis Freitas de
Oliveira, 7.00, 38.00, 45.00 / 10002027, Pedro Paulo de Jesus e Silva, 11.00, 62.00, 73.00 / 10010230,
Pedro Paulo dos Santos Rabelo, 8.00, 50.00, 58.00 / 10013698, Pedro Rafael de Nazare Albino, 13.00,
28.00, 41.00 / 10013127, Pedro Rafael Veiga da Silva, 10.00, 46.00, 56.00 / 10000773, Pedro Ramon
Novais de Araujo, 12.00, 58.00, 70.00 / 10013288, Pedro Roberto dos Santos Rocha, 15.00, 28.00, 43.00 /
 
10007587, Pedro Victor de Assis Brito, 8.00, 32.00, 40.00 / 10015979, Pedro Vitor Santos Balestreri, 7.00,
32.00, 39.00 / 10011211, Pedro Weliton de Morais Torres, 11.00, 56.00, 67.00 / 10012311, Petterson dos
Reis Pedrosa, 5.00, 36.00, 41.00 / 10010045, Petterson Henrique de Souza Cordeiro, 10.00, 60.00, 70.00 /
10011073, Phablo Henrique Costa Guedes, 6.00, 22.00, 28.00 / 10010955, Phamella Nayara Dias Reis,
11.00, 52.00, 63.00 / 10005468, Phelipe Francisco Gomes dos Santos, 11.00, 58.00, 69.00 / 10009361,
Philipe Matheus Campos Ribeiro, 12.00, 50.00, 62.00 / 10017064, Phillipe Padinha Cardoso, 12.00, 48.00,
60.00 / 10010896, Poliana Lopes Teixeira, 10.00, 26.00, 36.00 / 10002308, Pollyana Enia Figueiroa Araujo,
9.00, 56.00, 65.00 / 10000102, Pollyanna dos Reis Moreira, 10.00, 62.00, 72.00 / 10012938, Polyana Correa
Tavares, 15.00, 68.00, 83.00 / 10001587, Ponciano da Silva Santos Junior, 6.00, 44.00, 50.00 / 10015992, Porfirio Alves Pacheco Neto, 10.00, 42.00, 52.00 / 10000212, Poweblo Robert Jose dos Passos Barbosa, 12.00, 60.00, 72.00 / 10007161, Priscila Bezerra Saousa, 12.00, 52.00, 64.00 / 10009590, Priscila Cardoso
Alves, 6.00, 50.00, 56.00 / 10001108, Priscila Mendes Ruiz, 9.00, 52.00, 61.00 / 10010969, Priscilla
Alvares Cascaes da Silva, 12.00, 62.00, 74.00 / 10001761, Priscilla Ketheny Gomes Farias, 13.00, 64.00,
77.00 / 10007595, Priscilla Thayse Quaresma Lins, 11.00, 46.00, 57.00 / 10000513, Priscylla Monteiro
Oliveira, 7.00, 52.00, 59.00 / 10011551, Quezia Renata Mendonca Pereira, 7.00, 30.00, 37.00 / 10002173,
Radyb Mohammed Pinheiro Salomao, 10.00, 48.00, 58.00 / 10012510, Raelson Francisco de Oliveira, 9.00,
44.00, 53.00 / 10006867, Raelton Adonai Castro, 9.00, 58.00, 67.00 / 10016423, Rafael Angelo Lima
Sampaio, 8.00, 26.00, 34.00 / 10016003, Rafael Augusto Farias Rabelo, 7.00, 40.00, 47.00 / 10000468,
Rafael Borges Araujo Barreto, 12.00, 48.00, 60.00 / 10009729, Rafael Brito Santos, 12.00, 64.00, 76.00 /
10000351, Rafael Costa de Souza, 13.00, 70.00, 83.00 / 10011281, Rafael da Silva Costa, 9.00, 20.00,
29.00 / 10003092, Rafael da Silva Rosa, 9.00, 36.00, 45.00 / 10007835, Rafael de Almeida Miranda, 10.00,
58.00, 68.00 / 10011628, Rafael de Matos Dias, 12.00, 60.00, 72.00 / 10012662, Rafael de Oliveira Ribeiro,
7.00, 46.00, 53.00 / 10010280, Rafael de Souza Mendonca, 10.00, 62.00, 72.00 / 10000304, Rafael do
Carmo Leal, 12.00, 58.00, 70.00 / 10008224, Rafael dos Santos Barbosa, 11.00, 66.00, 77.00 / 10000970,
Rafael dos Santos Reis, 8.00, 32.00, 40.00 / 10013589, Rafael Farias de Lima, 5.00, 42.00, 47.00 /
10002965, Rafael Freitas de Oliveira, 7.00, 60.00, 67.00 / 10012163, Rafael Freitas Pereira, 8.00, 46.00,
54.00 / 10000518, Rafael Maciel Andrade, 10.00, 38.00, 48.00 / 10011298, Rafael Monteiro Carneiro,
12.00, 60.00, 72.00 / 10012822, Rafael Pantoja Silva, 8.00, 32.00, 40.00 / 10012167, Rafael Pereira Castelo
Branco de Oliveira, 6.00, 46.00, 52.00 / 10011733, Rafael Pinheiro Carvalho, 14.00, 58.00, 72.00 /
10000428, Rafael Rodrigues de Andrade, 9.00, 50.00, 59.00 / 10013563, Rafael Santos Magalhaes, 10.00,
56.00, 66.00 / 10005685, Rafael Silva Pereira, 7.00, 38.00, 45.00 / 10007694, Rafael Soares Cordeireo,
8.00, 38.00, 46.00 / 10016313, Rafael Sousa dos Santos, 5.00, 30.00, 35.00 / 10000724, Rafael Viana Costa
da Silva, 10.00, 30.00, 40.00 / 10005408, Rafaela Barbosa de Almeida, 11.00, 48.00, 59.00 / 10001309,
Rafaela Batista de Sousa, 10.00, 44.00, 54.00 / 10010358, Rafaela da Silva Carvalho, 14.00, 64.00, 78.00 /
10000974, Rafaela da Silva Rodrigues, 10.00, 48.00, 58.00 / 10001345, Rafaela do Nascimento Silva, 6.00,
40.00, 46.00 / 10006911, Rafaela Luciana Freitas de Souza, 11.00, 46.00, 57.00 / 10000105, Rafaela
Martins Fontoura, 12.00, 60.00, 72.00 / 10012468, Rafaela Moreno da Silva Alves, 9.00, 62.00, 71.00 /
10015912, Rafaela Silva de Sousa, 6.00, 16.00, 22.00 / 10005562, Rafaela Soares Araujo, 4.00, 32.00,
36.00 / 10010152, Rafaela Vitoria Sampaio Pinto, 7.00, 54.00, 61.00 / 10016137, Rafaella Bonfim Lima,
7.00, 60.00, 67.00 / 10012790, Rafaella Freitas Rodrigues, 10.00, 18.00, 28.00 / 10001214, Rafaella Silva
Mendes, 6.00, 32.00, 38.00 / 10000709, Rafaelle dos Santos Alencar, 5.00, 20.00, 25.00 / 10009407,
Rafaelly Chaves de Oliveira, 9.00, 42.00, 51.00 / 10002790, Rafaiele Cristini Costa Mota, 9.00, 34.00,
43.00 / 10002445, Rafisa Costa Carvalho Silva, 12.00, 46.00, 58.00 / 10012137, Raiana Alana Souza
Varela, 5.00, 26.00, 31.00 / 10001156, Raiane da Veiga Goncalves, 11.00, 46.00, 57.00 / 10007699, Raiane
Lima da Silva, 10.00, 38.00, 48.00 / 10012571, Raiane Lima Sousa, 7.00, 46.00, 53.00 / 10003116, Raila
Regina Paiva dos Santos, 6.00, 30.00, 36.00 / 10002446, Railan Ferreira de Sousa, 8.00, 48.00, 56.00 /
10000699, Railson dos Santos Silva, 8.00, 74.00, 82.00 / 10011786, Railson Feitosa Lima, 8.00, 36.00,
44.00 / 10002888, Raimundo de Oliveira Costa Junior, 14.00, 64.00, 78.00 / 10000877, Raimundo Nonato
Costa Beleza Junior, 11.00, 76.00, 87.00 / 10007593, Raimundo Wellington Abreu Costa, 11.00, 44.00,
55.00 / 10011109, Rainilson Fernandes Monteiro Junior, 9.00, 46.00, 55.00 / 10005391, Raissa Caroline
Pereira Ferreira, 9.00, 46.00, 55.00 / 10005404, Raissa de Souza Silva, 12.00, 40.00, 52.00 / 10016817, Raissa Eduarda Oliveira Simoes, 7.00, 38.00, 45.00 / 10000141, Raissa Feitosa Guimaraes Aleixo Nunes,
 
13.00, 52.00, 65.00 / 10000339, Raissa Martins Monteiro, 10.00, 30.00, 40.00 / 10002531, Raissa Silva
Braga, 9.00, 48.00, 57.00 / 10002225, Raissy Piehtra Batista Mendonca, 12.00, 66.00, 78.00 / 10011866,
Raiza Guimaraes da Silva Rego, 10.00, 48.00, 58.00 / 10005755, Raiza Ribeiro Brazao, 6.00, 36.00, 42.00
/ 10002497, Ralf Oliveira Santos, 7.00, 42.00, 49.00 / 10010109, Ramessa da Silva Ribeiro, 10.00, 56.00,
66.00 / 10011307, Ramiles Vasconcelos de Souza, 6.00, 22.00, 28.00 / 10006979, Ramilly Souza de
Oliveira, 7.00, 36.00, 43.00 / 10013123, Ramires de Araujo Silva, 7.00, 38.00, 45.00 / 10011698, Ramon
Cruz Pereira, 16.00, 48.00, 64.00 / 10003066, Ramon da Silva Bomjardim, 10.00, 38.00, 48.00 / 10001671,
Randha Yasmin Tavares da Silva, 10.00, 36.00, 46.00 / 10007903, Raniel de Moura Carvalho, 11.00, 62.00,
73.00 / 10011886, Ranielle Nazare Lima Silva, 10.00, 54.00, 64.00 / 10013482, Raniery Policarpo Oliveira
Feitosa, 13.00, 52.00, 65.00 / 10000177, Ranyellen da Silva e Silva, 6.00, 38.00, 44.00 / 10002854, Raphael
Garces dos Santos, 8.00, 32.00, 40.00 / 10011105, Raphael Jose Barbosa Moreira, 12.00, 58.00, 70.00 /
10000535, Raphael Rangel Oliveira, 12.00, 58.00, 70.00 / 10011136, Raquel Conceicao Rodrigues de
Castro, 9.00, 42.00, 51.00 / 10007153, Raquel Steffani Gaia Cardoso, 11.00, 48.00, 59.00 / 10009252,
Raquel Teixeira do Nascimento, 10.00, 40.00, 50.00 / 10013500, Raquel Trajano Machado, 14.00, 50.00,
64.00 / 10000127, Raul Henrrique Cardoso Albuquerque Mendes, 12.00, 70.00, 82.00 / 10002769, Ray
Anderson Cruz da Silva, 13.00, 36.00, 49.00 / 10016560, Rayan Picanco Campos, 12.00, 56.00, 68.00 /
10009240, Rayana da Silva Lima, 11.00, 28.00, 39.00 / 10009462, Rayana Gomes Nascimento, 11.00,
44.00, 55.00 / 10003040, Rayana Maria Coelho Vila Nova, 10.00, 28.00, 38.00 / 10000136, Rayane de
Oliveira Souza, 7.00, 46.00, 53.00 / 10015798, Rayane Mendes de Melo, 8.00, 48.00, 56.00 / 10006755, Rayanne Carolyne Silva dos Santos Cruz, 6.00, 20.00, 26.00 / 10005241, Rayanne Cristina Sacramento Tavares, 8.00, 30.00, 38.00 / 10016782, Rayanne Vieira da Conceicao, 6.00, 32.00, 38.00 / 10012579,
Rayara Anuska Ribeiro Mascarenhas, 9.00, 32.00, 41.00 / 10007976, Raylan Keven da Costa Pessoa, 8.00,
40.00, 48.00 / 10003003, Raylane da Silva Rodrigues, 14.00, 50.00, 64.00 / 10001404, Raylson Pacheco
Leao, 9.00, 52.00, 61.00 / 10016362, Raynan da Silva Farias, 5.00, 26.00, 31.00 / 10001663, Raynara
Evelyn Alhadef da Silva Nunes, 7.00, 26.00, 33.00 / 10016734, Rayra Rafaela Pereira Lobato Leal, 13.00,
44.00, 57.00 / 10001567, Rayssa de Fatima Miranda Pantoja, 12.00, 50.00, 62.00 / 10011474, Rayssa de
Souza da Silva, 9.00, 46.00, 55.00 / 10013444, Rayssa Rodrigues Cutrim, 10.00, 40.00, 50.00 / 10001032,
Rayssa Viana Freitas, 9.00, 18.00, 27.00 / 10016903, Rayssan Airam da Silva Nunes, 9.00, 44.00, 53.00 /
10001753, Rebeca de Oliveira Caetano, 6.00, 40.00, 46.00 / 10000433, Rebeca de Paula Nunes, 14.00,
54.00, 68.00 / 10010223, Rebeca de Souza Ferreira, 14.00, 52.00, 66.00 / 10000534, Rebeca Franca de
Avelar, 10.00, 46.00, 56.00 / 10012405, Rebeca Yohana Evangelista Freitas, 12.00, 34.00, 46.00 /
10013048, Rebecca Giovanna Campos Gomes, 12.00, 44.00, 56.00 / 10002272, Rebekah Leticia Chaves
Moura, 15.00, 52.00, 67.00 / 10000362, Reinaldo Maciel Ribeiro Junior, 10.00, 70.00, 80.00 / 10001543,
Reinam Coelho Oliveira, 10.00, 48.00, 58.00 / 10012693, Reinan Mateus Barroso Barra, 12.00, 42.00,
54.00 / 10012012, Relrison Silva Feitosa, 8.00, 58.00, 66.00 / 10000019, Renan Alves Batista, 10.00, 58.00,
68.00 / 10015877, Renan Andrei Lima Cascaes, 11.00, 32.00, 43.00 / 10007592, Renan Baia Lisboa do
Nascimento, 5.00, 36.00, 41.00 / 10006988, Renan da Silva Bandeira, 11.00, 38.00, 49.00 / 10001534,
Renan Gomes Barbas, 9.00, 32.00, 41.00 / 10013548, Renan Mateus Medeiros Alves, 8.00, 54.00, 62.00 /
10001367, Renan Silva de Melo, 4.00, 54.00, 58.00 / 10000223, Renata Alexsandra Campos Batista, 10.00,
40.00, 50.00 / 10001147, Renata Beatriz dos Santos Figueira, 7.00, 40.00, 47.00 / 10007144, Renata
Cardoso e Cardoso, 8.00, 28.00, 36.00 / 10002771, Renata Carvalho, 5.00, 28.00, 33.00 / 10015725, Renata
da Silveira Aleixo, 10.00, 50.00, 60.00 / 10015823, Renata Dias Cardoso, 9.00, 32.00, 41.00 / 10012600,
Renata Goncalves da Mata Costa, 8.00, 44.00, 52.00 / 10002827, Renata Oliveira da Silva, 8.00, 54.00,
62.00 / 10010194, Renata Pereira da Silva Costa, 9.00, 44.00, 53.00 / 10009501, Renata Souza de Campos,
14.00, 44.00, 58.00 / 10009584, Renato da Silva Neris, 13.00, 60.00, 73.00 / 10007509, Renato Morais
Gando, 11.00, 54.00, 65.00 / 10016682, Renato Paniagua Sales da Silva, 10.00, 48.00, 58.00 / 10009342,
Renato Pantoja Costa, 12.00, 56.00, 68.00 / 10013586, Renato Ronaldo Lima Luna de Souza, 10.00, 40.00,
50.00 / 10001762, Renee Pantoja Aires, 8.00, 38.00, 46.00 / 10011724, Rener Felipe Silva Lins, 13.00,
60.00, 73.00 / 10009784, Renet Simas Borges, 16.00, 62.00, 78.00 / 10006989, Rennan de Campos Pantoja,
15.00, 42.00, 57.00 / 10005409, Rennan Paiva da Silva Campos, 11.00, 52.00, 63.00 / 10000311, Rennedy
Ferreira Farias, 15.00, 64.00, 79.00 / 10010094, Reyler Rafaela Brabo Ferreira, 3.00, 22.00, 25.00 /
10009816, Reyson Dcs Reis Santos, 9.00, 32.00, 41.00 / 10000536, Rhalyani Cardoso de Vasconcelos,
 
8.00, 24.00, 32.00 / 10001777, Rhanyer Pantoja Aires, 10.00, 44.00, 54.00 / 10012651, Rhoryman Costa
Pereira, 9.00, 50.00, 59.00 / 10007778, Ricardo Alves de Oliveira, 10.00, 66.00, 76.00 / 10012419, Ricardo
Antonio Amancio Pinheiro Junior, 9.00, 42.00, 51.00 / 10011215, Ricardo Costa Moraes, 10.00, 44.00,
54.00 / 10011249, Ricardo da Silva Segundo, 9.00, 50.00, 59.00 / 10011541, Ricardo de Freitas Pereira,
7.00, 40.00, 47.00 / 10002227, Ricardo Igor de Oliveira Santos, 13.00, 54.00, 67.00 / 10013333, Ricardo
Pinheiro Quadra, 11.00, 30.00, 41.00 / 10010861, Ricardo Silva Santos, 6.00, 36.00, 42.00 / 10001890,
Riceli Fernando Costa de Sousa Junior, 9.00, 40.00, 49.00 / 10012608, Richard Christi Neves Freitas, 10.00,
20.00, 30.00 / 10010063, Richard Kellory Ferreira Ribeiro, 9.00, 46.00, 55.00 / 10002861, Richard
Santurelle Lima Barros, 11.00, 48.00, 59.00 / 10010735, Richardson Pereira da Silva, 9.00, 54.00, 63.00 /
10005635, Rick Guilherme Teixeira dos Santos, 9.00, 32.00, 41.00 / 10000156, Rickson Greison da Silva
Lima, 7.00, 32.00, 39.00 / 10007310, Rillary Suane da Silva Pinho, 11.00, 56.00, 67.00 / 10002717, Rinaldo
Ribeiro de Farias, 11.00, 50.00, 61.00 / 10007849, Risomara Lima Dias de Santana, 15.00, 64.00, 79.00 /
10009606, Risonaldo Pinto de Jesus Junior, 7.00, 34.00, 41.00 / 10011229, Rita de Cassia Carvalho Reis,
7.00, 50.00, 57.00 / 10005601, Rita de Cassia Macias Lopes, 13.00, 34.00, 47.00 / 10009815, Rita
Nhandhara Quaresma de Oliveira, 11.00, 54.00, 65.00 / 10013141, Rivelino Souza da Silva, 8.00, 30.00,
38.00 / 10005757, Roanna Lucia Sousa Salgado, 16.00, 60.00, 76.00 / 10013072, Robert Anderson de
Sousa da Costa Junior, 7.00, 48.00, 55.00 / 10011816, Roberta Evelyn da Silva Lopes, 8.00, 26.00, 34.00 /
10010308, Roberta Labelly Cezar da Silva Alves, 8.00, 50.00, 58.00 / 10001498, Roberta Luzia Teles
Sousa, 10.00, 42.00, 52.00 / 10010646, Roberta Viviane Natasha Lima de Araujo, 8.00, 48.00, 56.00 /
10000561, Roberto Bruno de Oliveira Rocha, 11.00, 58.00, 69.00 / 10009828, Roberto dos Santos Dantas,
8.00, 66.00, 74.00 / 10013159, Roberto Luiz Leite Ferreira, 9.00, 26.00, 35.00 / 10008023, Roberto Mateus
de Brito dos Santos, 8.00, 28.00, 36.00 / 10007071, Roberto Soares Lobo Junior, 10.00, 42.00, 52.00 /
10001866, Roberval da Silva Ferreira, 12.00, 32.00, 44.00 / 10001072, Roberval Morais Santos, 14.00,
54.00, 68.00 / 10013056, Robinson Guimaraes Carneiro, 10.00, 52.00, 62.00 / 10005769, Robson Ataide
do Nascimento, 10.00, 38.00, 48.00 / 10003178, Robson Bruno de Jesus Santos, 10.00, 54.00, 64.00 /
10009901, Robson Fabricio Parra Sousa, 12.00, 56.00, 68.00 / 10012586, Robson Figueiredo Negrao,
14.00, 62.00, 76.00 / 10002559, Rochetauo Flaubert Silva Reis, 13.00, 58.00, 71.00 / 10002967, Rodinelson
de Lima Sanches, 14.00, 62.00, 76.00 / 10001930, Rodolfo Cavalcante Alencar, 9.00, 46.00, 55.00 /
10011048, Rodolfo Goncalves Pinheiro, 12.00, 54.00, 66.00 / 10016750, Rodolfo Goncalves Pinheiro
Filho, 13.00, 54.00, 67.00 / 10010299, Rodrigo Afonso Amazonas de Menezes, 3.00, 28.00, 31.00 /
10013120, Rodrigo Anderson Ribeiro de Vilhena, 9.00, 42.00, 51.00 / 10009242, Rodrigo Barbosa
Cardoso, 6.00, 62.00, 68.00 / 10016070, Rodrigo Barbosa de Farias, 6.00, 38.00, 44.00 / 10001129, Rodrigo
Braga Assumpcao, 10.00, 44.00, 54.00 / 10012850, Rodrigo Braga Ferreira, 10.00, 50.00, 60.00 /
10010059, Rodrigo Carvalho Brito, 12.00, 64.00, 76.00 / 10007637, Rodrigo Carvalho de Sousa, 17.00,
68.00, 85.00 / 10009525, Rodrigo Cesar Franca de Oliveira, 13.00, 44.00, 57.00 / 10012919, Rodrigo
Chaves Souza, 2.00, 16.00, 18.00 / 10009552, Rodrigo Costa Moraes da Silva, 18.00, 52.00, 70.00 /
10011863, Rodrigo da Costa Ribeiro dos Santos, 7.00, 50.00, 57.00 / 10016504, Rodrigo da Silva Sousa,
10.00, 50.00, 60.00 / 10005612, Rodrigo Evangelista dos Santos, 9.00, 34.00, 43.00 / 10002063, Rodrigo
Galvao da Silva, 17.00, 60.00, 77.00 / 10007717, Rodrigo Moraes Carneiro, 12.00, 56.00, 68.00 /
10016828, Rodrigo Moreira Melo, 8.00, 56.00, 64.00 / 10005318, Rodrigo Moura Martins Torres, 8.00,
40.00, 48.00 / 10000800, Rodrigo Otavio Sobral de Gois Rosa Dias, 13.00, 58.00, 71.00 / 10016890,
Rodrigo Pereira Martins, 9.00, 36.00, 45.00 / 10005295, Rodrigo Pinheiro Muller, 13.00, 42.00, 55.00 /
10016107, Rodrigo Soares Ferreira, 7.00, 46.00, 53.00 / 10007106, Rodrigo Soares Lopes, 5.00, 30.00,
35.00 / 10011836, Rodrigo Vieira de Araujo, 13.00, 70.00, 83.00 / 10009734, Rogenan Leal do Lago
Cabral, 10.00, 50.00, 60.00 / 10009757, Roger Deyvison Gomes Oliveira, 10.00, 38.00, 48.00 / 10009631,
Roger Willyam de Freitas Vieira, 10.00, 56.00, 66.00 / 10003168, Rogerio Cortinhas Rodrigues, 9.00,
46.00, 55.00 / 10012816, Rogerio da Costa Martins Filho, 8.00, 50.00, 58.00 / 10000285, Rogerio da Rocha
dos Santos, 5.00, 36.00, 41.00 / 10000203, Rogerio dos Anjos Araujo Filho, 13.00, 58.00, 71.00 / 10000612,
Rogerio Pereira Pereira, 11.00, 38.00, 49.00 / 10012428, Rollison Adriano Carvalho, 7.00, 20.00, 27.00 /
10013359, Romario de Paulo Lima, 13.00, 56.00, 69.00 / 10000277, Romario dos Passos de Almeida, 8.00,
40.00, 48.00 / 10000447, Romario Nogueira Silva, 7.00, 38.00, 45.00 / 10007513, Romulo Ancelmo Araujo
de Almeida, 9.00, 36.00, 45.00 / 10001789, Romulo Leao Chada, 10.00, 46.00, 56.00 / 10011076, Romulo
 
Lima Costa, 9.00, 42.00, 51.00 / 10010158, Romulo Rodrigues dos Santos, 9.00, 46.00, 55.00 / 10000663,
Romulo Rodrigues Pontes, 7.00, 50.00, 57.00 / 10007262, Ronald da Silva Picanco dos Santos, 9.00, 28.00,
37.00 / 10012935, Ronaldo Cezar Ferreira dos Santos, 6.00, 40.00, 46.00 / 10010153, Ronaldo Lima de
Sousa, 11.00, 46.00, 57.00 / 10010489, Ronan da Silva Santos, 6.00, 20.00, 26.00 / 10013215, Roniery
Lima dos Santos, 9.00, 30.00, 39.00 / 10011903, Ronildo Castor da Silva, 10.00, 60.00, 70.00 / 10001460,
Ronison Bonfim, 11.00, 66.00, 77.00 / 10013410, Ronivaldo Silva Moreira, 7.00, 26.00, 33.00 / 10010252,
Ronkallyo Silva Muniz, 13.00, 60.00, 73.00 / 10002346, Rony Castro Moraes, 14.00, 60.00, 74.00 /
10010099, Rosa Licia Rebelo Reca, 11.00, 56.00, 67.00 / 10010583, Rosangela Pereira de Araujo, 8.00,
40.00, 48.00 / 10000946, Rosangela Pereira Gomes, 10.00, 26.00, 36.00 / 10009370, Rosany dos Santos
Tenorio, 11.00, 40.00, 51.00 / 10011112, Roseane Souza da Silva, 6.00, 46.00, 52.00 / 10010018, Rosiana
de Jesus Sousa Barreto, 8.00, 42.00, 50.00 / 10000264, Rosiellen Ribeiro de Souza, 10.00, 66.00, 76.00 /
10002194, Rosilene Oliveira Frias, 11.00, 46.00, 57.00 / 10013130, Rosinaldo Camara da Silva Filho,
12.00, 36.00, 48.00 / 10011915, Rosivaldo da Silva Rosa Leal, 11.00, 50.00, 61.00 / 10007019, Ruan Felipe
Goncalves Rodrigues, 7.00, 50.00, 57.00 / 10008204, Ruan Martins da Silva, 9.00, 40.00, 49.00 / 10007276,
Ruana Moreira Prado, 9.00, 34.00, 43.00 / 10002351, Rubens Jose Garcia Pena Junior, 9.00, 34.00, 43.00
/ 10012179, Rubergio Vital Carvalho Martins, 9.00, 38.00, 47.00 / 10007409, Rudivaldo Pantoja Abreu,
8.00, 64.00, 72.00 / 10010992, Ruitemberg Feitosa Ramos, 13.00, 34.00, 47.00 / 10001513, Rute Lopes de
Castro Silva, 9.00, 54.00, 63.00 / 10016320, Ryan Fernando Ribeiro Barbosa, 9.00, 40.00, 49.00 /
10010975, Ryron do Socorro Roma Marques, 6.00, 38.00, 44.00 / 10016918, Sabrina Cristiny Ne Almeida,
5.00, 32.00, 37.00 / 10011692, Sabrina Noelle de Souza Araujo, 8.00, 30.00, 38.00 / 10001278, Sabrine da
Silva Bento, 7.00, 38.00, 45.00 / 10010519, Sabyna Gomes Dutra, 6.00, 26.00, 32.00 / 10011131, Sadraque
Resende Macedo, 10.00, 26.00, 36.00 / 10000126, Samanta Priscila Rodrigues de Carvalho, 13.00, 56.00,
69.00 / 10007890, Samara Melo da Silva, 11.00, 30.00, 41.00 / 10010101, Samara Ribeiro dos Santos,
11.00, 36.00, 47.00 / 10008244, Samaya Silva Bargaxia, 12.00, 34.00, 46.00 / 10010402, Samea de Oliveira
Silva, 10.00, 40.00, 50.00 / 10010581, Samea Regina Azevedo de Oliveira, 6.00, 44.00, 50.00 / 10001237,
Samea Vieira Galvao, 11.00, 40.00, 51.00 / 10016042, Samia Thamires Conceicao Costa, 5.00, 34.00, 39.00
/ 10005411, Samily Andreza do Vale Sousa, 12.00, 62.00, 74.00 / 10011196, Samuel Albano Santos da
Cunha, 6.00, 32.00, 38.00 / 10005608, Samuel Carlos da Luz Moura, 7.00, 32.00, 39.00 / 10016120, Samuel
Fillype Silveira Fernandes, 11.00, 52.00, 63.00 / 10013621, Samuel Gomes de Oliveira, 12.00, 48.00, 60.00
/ 10011394, Samuel Leal Nunes Vieira, 10.00, 38.00, 48.00 / 10010752, Samuel Lucas Ferreira Serpa,
10.00, 44.00, 54.00 / 10012232, Samuel Lucky Lucyano Novaes Coelho, 11.00, 66.00, 77.00 / 10011370,
Samuel Oliveira Amaral, 12.00, 56.00, 68.00 / 10016737, Samuel Pereira Barreto, 5.00, 32.00, 37.00 /
10006928, Samuel Ricardo Klen Leal, 6.00, 46.00, 52.00 / 10007089, Samuel Sandoval Cardoso Cunha,
15.00, 60.00, 75.00 / 10008233, Samy Souza Silva Fernandes, 11.00, 52.00, 63.00 / 10016909, Samya
Caroline Pereira Aragao, 11.00, 34.00, 45.00 / 10016409, Samya Julia Souza Borges, 7.00, 34.00, 41.00 /
10011166, Samya Monique Oliveira Farias, 10.00, 34.00, 44.00 / 10007079, Samya Paes Castro, 7.00,
46.00, 53.00 / 10003020, Samya Taylly Miranda Barradas, 8.00, 18.00, 26.00 / 10016815, Sanderson
Morote do Nascimento, 10.00, 54.00, 64.00 / 10001559, Sandro Correa Oliveira, 9.00, 54.00, 63.00 /
10002632, Sandro Rogerio Miglio Teixeira, 9.00, 52.00, 61.00 / 10010183, Sandy Juliana da Costa Sousa,
8.00, 56.00, 64.00 / 10007940, Sandylara Lopes Marreiros, 10.00, 34.00, 44.00 / 10011029, Sara Rosana
Marques de Souza, 16.00, 48.00, 64.00 / 10011561, Sarah Benaya Alves Moraes, 10.00, 46.00, 56.00 /
10001780, Sarah Bernadeth da Cunha Serrao, 8.00, 42.00, 50.00 / 10005551, Sarah Gomes Goncalves,
14.00, 54.00, 68.00 / 10012171, Sarah Sabrina da Silva Amaral, 8.00, 32.00, 40.00 / 10007782, Saullo
Vyctor Souza Lima Silva, 11.00, 40.00, 51.00 / 10008093, Saulo Vinicius Vinhote Dias, 10.00, 46.00, 56.00
/ 10013341, Savio Amador de Azevedo, 14.00, 34.00, 48.00 / 10013476, Savio Caian Barros da Silva, 7.00,
50.00, 57.00 / 10012437, Savio Hill Farias Santos, 10.00, 56.00, 66.00 / 10012755, Savio Miranda Pantoja,
12.00, 46.00, 58.00 / 10000625, Saymon Daniel Nery Barros, 13.00, 58.00, 71.00 / 10009725, Saynara
Raissa Paiva Brito, 8.00, 28.00, 36.00 / 10009313, Scolny Catarini Lana, 6.00, 36.00, 42.00 / 10008194,
Sebastiao Lotthas Matthews Souza Albuquerque, 11.00, 60.00, 71.00 / 10000146, Selena Dayane Aragao
Bahia, 6.00, 22.00, 28.00 / 10015990, Sergio Daniel de Abreu Brasil, 12.00, 34.00, 46.00 / 10010995,
Sergio Roberto Ramos de Oliveira, 8.00, 44.00, 52.00 / 10016254, Sergio Thiago Silva Cabral, 14.00,
50.00, 64.00 / 10013415, Shara Silva Guimaraes, 8.00, 30.00, 38.00 / 10007833, Shaya Mirella Souza Silva,
 
15.00, 52.00, 67.00 / 10000025, Sheila Wedima Barbosa Duarte, 8.00, 42.00, 50.00 / 10013035, Shirlany
Santos de Oliveira, 8.00, 26.00, 34.00 / 10002337, Shirlei Guedes Lima, 12.00, 40.00, 52.00 / 10016940,
Shirley Kauany Capitani Miranda, 11.00, 40.00, 51.00 / 10002057, Sidney Machado Ribeiro, 13.00, 60.00,
73.00 / 10005772, Sidney Silva do Rosario, 7.00, 38.00, 45.00 / 10013243, Silas Coelho Silva, 13.00, 54.00,
67.00 / 10012050, Silmar Kaeski, 10.00, 64.00, 74.00 / 10007552, Silvania Felix da Silva, 5.00, 24.00,
29.00 / 10000108, Silvestre Cardoso de Araujo Neto, 8.00, 44.00, 52.00 / 10006982, Silvia Leticia Portilho
Damasceno, 9.00, 30.00, 39.00 / 10012567, Silvio Gabriel Costa da Silva, 10.00, 48.00, 58.00 / 10000014,
Silvio Loiola Noronha, 7.00, 40.00, 47.00 / 10007366, Silvio Ricardo Dias Prado da Silva, 7.00, 26.00,
33.00 / 10011788, Simon Figueiredo Feio, 7.00, 22.00, 29.00 / 10000499, Sinak Rhayner Vieira da Cunha
Fernandes Barroso, 8.00, 42.00, 50.00 / 10016308, Sinara Renee Batista Rodrigues, 12.00, 34.00, 46.00 /
10012470, Sirney Gama da Costa, 8.00, 34.00, 42.00 / 10000910, Skarlat Alves da Silva, 9.00, 20.00, 29.00
/ 10007169, Solon Salim Bayde, 7.00, 30.00, 37.00 / 10008187, Sony Anderson Pinheiro Serrao, 12.00,
66.00, 78.00 / 10006757, Soraya Leticia de Almeida Costa, 8.00, 52.00, 60.00 / 10000038, Sosteny Joaquim
da Silva Neto, 8.00, 52.00, 60.00 / 10005555, Stefanie da Silva Oliveira, 3.00, 20.00, 23.00 / 10011660,
Stefanie Ferreira de Oliveira Leal, 8.00, 38.00, 46.00 / 10001244, Stefany Lira de Albuquerque, 10.00,
30.00, 40.00 / 10010840, Stephany Radaring dos Santos Freitas, 9.00, 30.00, 39.00 / 10009854, Suelem
Lira dos Santos, 9.00, 40.00, 49.00 / 10001035, Suelen Cristina Brasil Pinheiro, 8.00, 38.00, 46.00 /
10016608, Suelen Leal de Lima, 11.00, 52.00, 63.00 / 10013005, Suelenny do Socorro Neves dos Santos,
8.00, 28.00, 36.00 / 10001086, Suellen Dionisio Negreiros, 12.00, 48.00, 60.00 / 10010738, Suianny Lima
da Silva, 16.00, 62.00, 78.00 / 10012863, Sumaia Pereira das Chagas Santos, 11.00, 42.00, 53.00 /
10015859, Sumaya Prazeres de Campos, 12.00, 52.00, 64.00 / 10007365, Susana Ribeiro Idelfonso, 10.00,
46.00, 56.00 / 10002591, Susane Carvalho Felix, 9.00, 38.00, 47.00 / 10015777, Suzan Sara Morote do
Nascimento, 8.00, 32.00, 40.00 / 10012806, Suzane Patricia da Silva Santos, 4.00, 32.00, 36.00 / 10012219,
Suzane Silva Carneiro da Cunha, 7.00, 26.00, 33.00 / 10016356, Suzanhe do Nascimento Lopes, 5.00,
28.00, 33.00 / 10013135, Suzanny Braga Costa, 8.00, 50.00, 58.00 / 10002524, Suze Rodrigues de Souza,
8.00, 36.00, 44.00 / 10006721, Suzy Ellen Nogueira Chaves, 11.00, 48.00, 59.00 / 10011317, Tabata Analia
Mendonca Pacifico, 12.00, 50.00, 62.00 / 10007451, Tacilar Gama Calado, 6.00, 10.00, 16.00 / 10000887,
Tacyla Ingrid Silva de Moraes, 13.00, 66.00, 79.00 / 10005751, Taina Brandao Abdon, 9.00, 42.00, 51.00
/ 10009600, Taina Chaves Lopes, 10.00, 48.00, 58.00 / 10013724, Taina Cristiany Carvalho dos Santos,
8.00, 36.00, 44.00 / 10010062, Taina de Jesus Paixao Castilho, 13.00, 38.00, 51.00 / 10009666, Taina
Fernandes da Silva Guimaraes, 11.00, 44.00, 55.00 / 10015971, Taina Melo de Souza, 9.00, 32.00, 41.00 /
10016369, Taina Tamires Silva de Barros, 5.00, 30.00, 35.00 / 10013565, Tainan Fernandes Carneiro, 9.00,
48.00, 57.00 / 10015790, Tainara Helena de Assis Pereira, 8.00, 28.00, 36.00 / 10012406, Tais Fernanda
Gemaque Amaral, 9.00, 58.00, 67.00 / 10012221, Tais Oliveira Modesto Neves, 10.00, 62.00, 72.00 /
10001152, Tais Rodrigues Silva, 8.00, 34.00, 42.00 / 10015927, Tais Tariele Araujo de Souza, 9.00, 52.00,
61.00 / 10001349, Taise Campos Lobo, 7.00, 34.00, 41.00 / 10015774, Taisi Adriana Barroso Silva, 7.00,
36.00, 43.00 / 10007742, Tales Efraim Peres Falqueto, 15.00, 60.00, 75.00 / 10013656, Tales Vandre Lopes
Alho, 9.00, 40.00, 49.00 / 10000796, Talissa Colares dos Santos, 10.00, 54.00, 64.00 / 10016509, Talisson
Sodre Oliveira, 11.00, 56.00, 67.00 / 10010249, Tallita Pereira Silva, 8.00, 52.00, 60.00 / 10006873, Tallita
Pontes Pereira, 10.00, 44.00, 54.00 / 10009668, Tallyta Rodrigues Diniz, 14.00, 54.00, 68.00 / 10011795,
Tamara Correa Silva, 11.00, 42.00, 53.00 / 10007328, Tamara de Sousa Ramos, 8.00, 42.00, 50.00 /
10002814, Tamise Damasceno Pessoa, 8.00, 34.00, 42.00 / 10012835, Tania Correia dos Santos, 7.00,
36.00, 43.00 / 10002828, Tassia Cibele da Costa Paes, 9.00, 36.00, 45.00 / 10010554, Tassio Julio Aguiar
Carneiro, 16.00, 70.00, 86.00 / 10008088, Tassio Rene Lopes Furtado, 7.00, 58.00, 65.00 / 10011779,
Tatiana de Alcantara Pontes, 14.00, 50.00, 64.00 / 10009930, Tatiane Pereira, 10.00, 48.00, 58.00 /
10001313, Tatiany Fernanda de Souza Marinho, 5.00, 22.00, 27.00 / 10007194, Tatyane Conceicao da
Silva, 8.00, 36.00, 44.00 / 10002419, Tatyane Fernandes Correa, 12.00, 68.00, 80.00 / 10010267, Tavany
Correa da Silva, 6.00, 34.00, 40.00 / 10011747, Tayna Couto Barros, 5.00, 32.00, 37.00 / 10008208, Tayna
Xavier Santos Lago, 11.00, 40.00, 51.00 / 10005721, Tayua Arruda Juca da Silva, 12.00, 54.00, 66.00 /
10000070, Thabatta Geovanka Sousa Santos, 7.00, 36.00, 43.00 / 10012908, Thafnes Regina Wolff Sousa,
13.00, 52.00, 65.00 / 10011845, Thaila Kamila Vieira Leal, 7.00, 28.00, 35.00 / 10007312, Thaina Lobato
de Souza, 10.00, 34.00, 44.00 / 10000752, Thais Albernar Pessoa, 8.00, 38.00, 46.00 / 10003028, Thais
 
Araujo da Silva, 4.00, 18.00, 22.00 / 10010879, Thais dos Santos e Sousa, 14.00, 58.00, 72.00 / 10012168,
Thais dos Santos Pompeu, 4.00, 20.00, 24.00 / 10007277, Thais Farias Guerreiro dos Reis, 13.00, 58.00,
71.00 / 10010937, Thais Flavia dos Santos Cardoso, 9.00, 48.00, 57.00 / 10014716, Thais Maria Oliveira
Fernandes, 12.00, 40.00, 52.00 / 10013003, Thais Nava de Sousa, 10.00, 54.00, 64.00 / 10015897, Thais
Oliveira Colli, 8.00, 48.00, 56.00 / 10005712, Thais Renata Carvalho Costa, 10.00, 32.00, 42.00 /
10012035, Thais Resplande Martins, 8.00, 52.00, 60.00 / 10015905, Thais Santos Rodrigues, 8.00, 34.00,
42.00 / 10001768, Thais Souza Rodrigues, 9.00, 40.00, 49.00 / 10010212, Thales Augusto Teixeira Costa,
9.00, 50.00, 59.00 / 10012088, Thales Bernardo Monteiro, 13.00, 54.00, 67.00 / 10010893, Thales Menezes
de Oliveira, 8.00, 46.00, 54.00 / 10012286, Thales Renan de Almeida Teixeira, 13.00, 60.00, 73.00 /
10010867, Thalia Pamplona de Araujo Tourinho, 6.00, 48.00, 54.00 / 10012523, Thalia Pinheiro Dias, 5.00,
30.00, 35.00 / 10010864, Thaline Lorrana Bastos Pereira, 11.00, 46.00, 57.00 / 10009338, Thalita do
Carmo, 6.00, 36.00, 42.00 / 10002752, Thalles Clodoaldo Kartter Polveiro da Silva e Silva, 9.00, 54.00,
63.00 / 10010117, Thalles Vieira Mariano, 10.00, 44.00, 54.00 / 10007109, Thallison dos Santos Silva,
15.00, 66.00, 81.00 / 10002661, Thallyson Felype Cardoso dos Santos, 7.00, 58.00, 65.00 / 10005389,
Thalys Duarte da Silva, 15.00, 66.00, 81.00 / 10000765, Thalyson Vinicius Morais Barbosa, 13.00, 66.00,
79.00 / 10012945, Thalyta Brandao de Campos, 10.00, 30.00, 40.00 / 10016665, Thamires Freitas da Silva,
6.00, 36.00, 42.00 / 10011953, Thamires Silva Ribeiro, 13.00, 36.00, 49.00 / 10016006, Thammy Araujo
Pinto Batista, 12.00, 44.00, 56.00 / 10011877, Tharles Almeida da Silva, 10.00, 46.00, 56.00 / 10012794,
Tharles do Couto Alves, 7.00, 28.00, 35.00 / 10016026, Tharlis Nunes Alves, 9.00, 46.00, 55.00 /
10010469, Tharlyson Nascimento Andrade, 10.00, 48.00, 58.00 / 10007002, Thawany Camara da Silva,
9.00, 38.00, 47.00 / 10002504, Thayana Ribeiro da Silva, 12.00, 50.00, 62.00 / 10003062, Thayane
Henrique Figueiredo, 11.00, 50.00, 61.00 / 10011450, Thaylisson Rodrigues Satana, 4.00, 30.00, 34.00 /
10002156, Thaylla Macedo do Espirito Santo, 8.00, 46.00, 54.00 / 10009920, Thayna Brito Estumano, 8.00,
52.00, 60.00 / 10008191, Thayna Costa Ferreira, 13.00, 54.00, 67.00 / 10007211, Thayna Racquel Mendes
Lopes, 11.00, 52.00, 63.00 / 10011260, Thays Almeida da Trindade, 14.00, 56.00, 70.00 / 10001518, Thays
Cruz Carneiro, 7.00, 52.00, 59.00 / 10009743, Thays Hanna Gomes de Oliveira, 6.00, 34.00, 40.00 /
10010410, Thays Oliveira Goncalves, 12.00, 42.00, 54.00 / 10000032, Theo de Souza Pereira, 9.00, 58.00,
67.00 / 10013345, Theodora Luciana da Silva Gomes, 8.00, 44.00, 52.00 / 10010371, Thiago Alvino
Rodrigues Souza, 11.00, 46.00, 57.00 / 10001386, Thiago Borges Teodoro, 13.00, 54.00, 67.00 / 10011264,
Thiago Camara Barreto, 8.00, 28.00, 36.00 / 10010548, Thiago da Costa Oliveira, 11.00, 60.00, 71.00 /
10007856, Thiago Felipe Leite Padilha, 8.00, 34.00, 42.00 / 10011217, Thiago Ferreira Prazeres, 10.00,
34.00, 44.00 / 10001947, Thiago Figueiredo e Silva, 10.00, 20.00, 30.00 / 10016796, Thiago Graca Gomes,
8.00, 34.00, 42.00 / 10016760, Thiago Holanda Figueredo, 12.00, 50.00, 62.00 / 10010605, Thiago
Mangabeira Vieira, 10.00, 42.00, 52.00 / 10002313, Thiago Pereira Alves, 10.00, 30.00, 40.00 / 10001165,
Thiago Pereira de Moura, 13.00, 62.00, 75.00 / 10000131, Thiago Rendeiro do Nascimento, 10.00, 50.00,
60.00 / 10003074, Thiago Santos Pinheiro, 14.00, 56.00, 70.00 / 10016650, Thiago Sotelo de Araujo, 10.00,
64.00, 74.00 / 10005503, Thiago Sousa de Farias, 11.00, 56.00, 67.00 / 10012483, Thomas Victor Castro
Goulart, 8.00, 46.00, 54.00 / 10010218, Thyago Fellipe Fernandes da Silva, 15.00, 52.00, 67.00 / 10007669,
Thyago Henricky de Sousa Teixeira, 9.00, 34.00, 43.00 / 10010912, Tiago Benassuly de Souza, 13.00,
48.00, 61.00 / 10015881, Tiago Candido Ferreira, 8.00, 52.00, 60.00 / 10000163, Tiago de Abreu Oliveira,
5.00, 26.00, 31.00 / 10002315, Tiago de Abreu Vasconcelos, 12.00, 58.00, 70.00 / 10002912, Tiago Ferreira
Rosa, 9.00, 50.00, 59.00 / 10007165, Tiago Goes da Paixao, 11.00, 46.00, 57.00 / 10000384, Tiago
Henrique Pereira Rabelo, 14.00, 52.00, 66.00 / 10017043, Tiago Lima de Sousa, 5.00, 24.00, 29.00 /
10009721, Tiago Luis Gaia dos Santos, 9.00, 32.00, 41.00 / 10011832, Tiago Oliveira de Sena Rosa, 11.00,
48.00, 59.00 / 10010805, Tiago Ramos Dourado, 12.00, 42.00, 54.00 / 10012789, Tiago Vieira Silva, 9.00,
34.00, 43.00 / 10009836, Tifani Rebeca Monteiro Oliveira, 8.00, 44.00, 52.00 / 10000562, Tomas Almeida
Silva de Sousa, 11.00, 54.00, 65.00 / 10011945, Torquato da Silva Batista, 7.00, 48.00, 55.00 / 10016234,
Tulio Santos Pereira, 10.00, 34.00, 44.00 / 10012266, Ubiracy Jorge Correa Camargo Filho, 6.00, 30.00,
36.00 / 10000706, Ubiracy Ramos de Carvalho Junior, 15.00, 56.00, 71.00 / 10009611, Uenderson Pereira
Cruz, 7.00, 52.00, 59.00 / 10001265, Ulisses Duarte Martins, 13.00, 46.00, 59.00 / 10000075, Utiele dos
Santos Lima, 10.00, 60.00, 70.00 / 10001447, Valcinei dos Santos Martins, 9.00, 42.00, 51.00 / 10016701,
Valdenize do Espirito Santo da Luz, 6.00, 32.00, 38.00 / 10010531, Valdinei Silva Teixeira Junior, 13.00,
 
64.00, 77.00 / 10012575, Valena Rauane Carvalho Machado, 11.00, 46.00, 57.00 / 10000423, Valeria
Larissa Galvao do Prado, 11.00, 24.00, 35.00 / 10000097, Valeria Linelly Vieira Silva, 12.00, 46.00, 58.00
/ 10000080, Valeryane Franca de Souza, 8.00, 42.00, 50.00 / 10006905, Valesca Fernandes Paixao e Silva,
9.00, 44.00, 53.00 / 10003050, Valmir Caitano de Andrade Junior, 14.00, 64.00, 78.00 / 10009250, Valmir
de Oliveira Ferreira, 11.00, 58.00, 69.00 / 10001805, Valquiria Araujo de Souza, 10.00, 48.00, 58.00 /
10012418, Valteir Gomes de Oliveira, 6.00, 32.00, 38.00 / 10003107, Valter Braga dos Santos Junior,
12.00, 36.00, 48.00 / 10000144, Vancleia Silva Barbosa, 8.00, 24.00, 32.00 / 10010083, Vandenilson
Bolonha Vanderlei, 9.00, 34.00, 43.00 / 10010826, Vander Brabo Fiel, 8.00, 20.00, 28.00 / 10010796,
Vanderly da Silva Ferreira, 8.00, 34.00, 42.00 / 10012335, Vandeson da Silva, 10.00, 46.00, 56.00 /
10001669, Vando Serrao da Silva, 10.00, 44.00, 54.00 / 10013266, Vanessa Cristina do Nascimento
Aragao, 12.00, 52.00, 64.00 / 10002162, Vanessa Ferreira de Lima Barbosa, 10.00, 60.00, 70.00 /
10010870, Vanessa Ferreira de Oliveira, 10.00, 22.00, 32.00 / 10011880, Vanessa Gomes Almeida, 17.00,
60.00, 77.00 / 10013103, Vanessa Kezia Nascimento Tavares, 11.00, 52.00, 63.00 / 10000261, Vanessa
Martins Frota Vieira, 11.00, 52.00, 63.00 / 10012968, Vanessa Ribeiro Neto, 14.00, 42.00, 56.00 /
10016834, Vanessa Tamires Silva dos Santos, 6.00, 38.00, 44.00 / 10001159, Vania Lima da Silva, 11.00,
52.00, 63.00 / 10012799, Vanilson Ferreira da Costa, 8.00, 34.00, 42.00 / 10010801, Venilton Gomes da
Silva Junior, 9.00, 44.00, 53.00 / 10000873, Vicente de Paula Alves dos Santos, 10.00, 48.00, 58.00 /
10006954, Vicente Samuel Barbosa Pamplona, 12.00, 48.00, 60.00 / 10008169, Victor Akio Oliveira
Ishikawa, 8.00, 36.00, 44.00 / 10007842, Victor Augusto da Silva Galvao, 10.00, 36.00, 46.00 / 10006920,
Victor Augusto Rodrigues de Melo, 12.00, 52.00, 64.00 / 10009753, Victor Baia Furtado, 10.00, 58.00,
68.00 / 10009303, Victor Barreto da Silva, 7.00, 48.00, 55.00 / 10013203, Victor Cesar Peixoto Carneiro
do Valle, 9.00, 28.00, 37.00 / 10005750, Victor da Silva Siza, 7.00, 26.00, 33.00 / 10007812, Victor de
Aguiar Roma, 16.00, 56.00, 72.00 / 10007638, Victor de Oliveira Cirino, 10.00, 36.00, 46.00 / 10009737, Victor do Nascimento Vianna, 14.00, 54.00, 68.00 / 10001703, Victor Emanuel da Silva Amorim Souza, 8.00, 36.00, 44.00 / 10000284, Victor Fabricio de Souza Martins, 8.00, 34.00, 42.00 / 10001904, Victor
Gabriel Vieira Silva, 8.00, 32.00, 40.00 / 10012970, Victor Gustavo Reis da Silva, 11.00, 44.00, 55.00 /
10011508, Victor Henrique Marinho de Almeida, 11.00, 70.00, 81.00 / 10011591, Victor Hugo Costa Melo
de Souza, 7.00, 30.00, 37.00 / 10013588, Victor Hugo Facanha da Costa Marialva, 15.00, 44.00, 59.00 /
10001008, Victor Hugo Leite Ribeiro, 8.00, 46.00, 54.00 / 10006784, Victor Hugo Magno de Souza, 13.00,
46.00, 59.00 / 10013028, Victor Hugo Reis Colares, 12.00, 54.00, 66.00 / 10000317, Victor Igor Viana
Mendes, 12.00, 44.00, 56.00 / 10005548, Victor Leandro Menezes da Costa, 5.00, 26.00, 31.00 / 10009446,
Victor Lisboa Feio, 11.00, 42.00, 53.00 / 10001405, Victor Lopes Leite, 12.00, 58.00, 70.00 / 10010331,
Victor Lucas Nunes Mesquita, 11.00, 66.00, 77.00 / 10000312, Victor Matheus Dourado da Silva, 5.00,
34.00, 39.00 / 10002564, Victor Neves Lima, 9.00, 60.00, 69.00 / 10010834, Victor Ornelas Souza Costa,
13.00, 60.00, 73.00 / 10016869, Victor Reis de Souza, 9.00, 44.00, 53.00 / 10005487, Victor Ricardo Santos
Puga, 4.00, 36.00, 40.00 / 10007748, Victor Siqueira Miranda dos Santos, 9.00, 50.00, 59.00 / 10012570,
Victor Sousa da Silva, 7.00, 26.00, 33.00 / 10015738, Victor Zander Araujo Belfort Lisboa, 11.00, 54.00,
65.00 / 10016508, Victoria Cutrim Munhoz, 9.00, 66.00, 75.00 / 10001675, Victoria da Silva Paz, 13.00,
46.00, 59.00 / 10002950, Victoria de Jesus Botelho Portal, 10.00, 48.00, 58.00 / 10000371, Victoria
Emanuelle da Silva Barata, 9.00, 40.00, 49.00 / 10016247, Victoria Nascimento da Silva, 7.00, 40.00, 47.00
/ 10012391, Victoria Souza Ramos, 9.00, 26.00, 35.00 / 10009653, Vilidiane Morais Teixeira, 12.00, 58.00,
70.00 / 10002858, Vilmar Victor da Silva Sousa, 7.00, 54.00, 61.00 / 10012514, Vinicius Alves Rodrigues,
12.00, 60.00, 72.00 / 10011694, Vinicius Barbosa de Oliveira, 8.00, 38.00, 46.00 / 10011106, Vinicius
Borralho Serafim, 11.00, 44.00, 55.00 / 10015902, Vinicius Chaves Alves, 17.00, 62.00, 79.00 / 10001063,
Vinicius Danton Silva e Silva, 11.00, 54.00, 65.00 / 10010902, Vinicius Ferreira Tramontin, 11.00, 34.00,
45.00 / 10001384, Vinicius Fonseca da Costa, 10.00, 56.00, 66.00 / 10006727, Vinicius Jose da Silva,
13.00, 68.00, 81.00 / 10009586, Vinicius Malcher Lima, 11.00, 44.00, 55.00 / 10016519, Vinicius Mateus
Gomes Cardoso, 9.00, 22.00, 31.00 / 10001414, Vinicius Meireles dos Santos, 9.00, 54.00, 63.00 /
10016773, Vinicius Modesto Vasconcelos, 6.00, 28.00, 34.00 / 10005671, Vinicius Moura de Oliveira,
7.00, 28.00, 35.00 / 10010290, Vinicius Rodrigues Mendes de Oliveira, 14.00, 46.00, 60.00 / 10012837,
Vinicius Sales Castro, 14.00, 52.00, 66.00 / 10007053, Vinicyus Barboza Menezes, 10.00, 36.00, 46.00 /
10010442, Vitor Dantas de Macedo, 13.00, 52.00, 65.00 / 10000324, Vitor dos Santos Mano, 11.00, 44.00,
 
55.00 / 10002477, Vitor Hugo Coelho Sagawa, 7.00, 46.00, 53.00 / 10016728, Vitor Hugo Duarte das
Chagas, 13.00, 42.00, 55.00 / 10009563, Vitor Hugo Ribeiro do Rosario Murad, 7.00, 30.00, 37.00 /
10015855, Vitor Mateus Tavares Fontes, 7.00, 42.00, 49.00 / 10013234, Vitor Micael Pinheiro Lopes, 5.00,
38.00, 43.00 / 10009899, Vitor Rafael Barros Lima, 12.00, 64.00, 76.00 / 10010785, Vitor Reis Scalabrin,
6.00, 42.00, 48.00 / 10012051, Vitor Roberto Sarmento Nogueira, 9.00, 48.00, 57.00 / 10008134, Vitor
Yasser Silva Bria, 8.00, 44.00, 52.00 / 10003191, Vitoria Ainoan Angelo Policarpo, 12.00, 50.00, 62.00 /
10007563, Vitoria Aldir Lima Barros Silva, 9.00, 32.00, 41.00 / 10010775, Vitoria Bruna Soares dos
Santos, 7.00, 42.00, 49.00 / 10016683, Vitoria Colares Nobre Paixao, 9.00, 40.00, 49.00 / 10009937, Vitoria
Conceicao do Amaral Borges, 10.00, 34.00, 44.00 / 10005790, Vitoria Coutinho Brunini, 13.00, 52.00,
65.00 / 10011596, Vitoria Cristina da Costa Freitas, 6.00, 24.00, 30.00 / 10005282, Vitoria da Silva
Teixeira, 8.00, 70.00, 78.00 / 10000074, Vitoria de Lima Bezerra, 11.00, 34.00, 45.00 / 10005519, Vitoria
Lavratti Zanon Gomes de Paula, 10.00, 46.00, 56.00 / 10006892, Vitoria Leao Costa Pereira, 8.00, 24.00,
32.00 / 10012028, Vitoria Loiola de Queiroz, 13.00, 52.00, 65.00 / 10013693, Vitoria Nogueira Moreira,
11.00, 48.00, 59.00 / 10002962, Viviam Melo Bezerra, 10.00, 44.00, 54.00 / 10002680, Vivian Dayane
Souza da Silva, 12.00, 36.00, 48.00 / 10011965, Vivian Lizandra Moraes do Nascimento, 11.00, 34.00,
45.00 / 10002880, Vivian Teixeira Dezincourt, 14.00, 50.00, 64.00 / 10002946, Viviane Alves dos Santos,
8.00, 42.00, 50.00 / 10016436, Viviane Cristinne Silva da Cunha, 10.00, 38.00, 48.00 / 10005741, Viviane
Gama Dantas, 7.00, 44.00, 51.00 / 10005433, Viviane Sousa Correa, 14.00, 70.00, 84.00 / 10001590,
Volnei da Silva Lima, 9.00, 34.00, 43.00 / 10013522, Voltaire Hesketh Lopes, 8.00, 64.00, 72.00 /
10007796, Waddington Martins, 8.00, 34.00, 42.00 / 10000366, Wadson Jose de Castro, 14.00, 46.00, 60.00
/ 10009856, Wadson Lima Vieira, 11.00, 66.00, 77.00 / 10000754, Wagner Bruno Santos Leao, 8.00, 30.00,
38.00 / 10016708, Wagner da Silva Ferreira, 11.00, 38.00, 49.00 / 10009534, Wagner Fagundes dos Santos,
10.00, 54.00, 64.00 / 10007343, Wagner Mundoca dos Santos, 8.00, 46.00, 54.00 / 10001577, Wagnon
Pereira de Sousa, 12.00, 66.00, 78.00 / 10003129, Walber de Sousa Costa, 12.00, 50.00, 62.00 / 10010091,
Walder Araujo de Oliveira, 9.00, 46.00, 55.00 / 10012459, Waldir Junior dos Santos Souza, 6.00, 46.00,
52.00 / 10011835, Waldomiro Abreu da Fonseca Neto, 11.00, 56.00, 67.00 / 10000637, Waleria Braga
Martins Caridade, 5.00, 40.00, 45.00 / 10010405, Waleria Conceicao de Magalhaes, 8.00, 34.00, 42.00 /
10010841, Walkiria Fernanda Souza Fernandes Barauna, 11.00, 60.00, 71.00 / 10001579, Wallace de
Oliveira Leite, 14.00, 68.00, 82.00 / 10000795, Wallace Lucas de Abreu Costa, 8.00, 30.00, 38.00 /
10002246, Wallas Cavalcante Januario, 10.00, 30.00, 40.00 / 10010467, Wallen Bruno Carvalho Dias,
10.00, 58.00, 68.00 / 10016706, Wallery Vitoria Matos Vieira Santos, 10.00, 46.00, 56.00 / 10000842,
Wallison Costa Araujo dos Santos, 14.00, 50.00, 64.00 / 10012001, Wallison Dias Pessoa, 7.00, 32.00,
39.00 / 10001641, Walyf Lopes da Silva, 12.00, 44.00, 56.00 / 10013053, Walyson Dilson Monteiro
Oliveira, 10.00, 40.00, 50.00 / 10015916, Wandercley Monteiro Cabral, 7.00, 54.00, 61.00 / 10013445,
Wanderson Cardoso Galdino, 10.00, 34.00, 44.00 / 10009274, Wanderson Douglas Moreira Mota, 7.00,
30.00, 37.00 / 10010959, Wanderson Ferreira Pantoja, 13.00, 32.00, 45.00 / 10012751, Wanderson Ricardo
Evangelista de Queiroz, 11.00, 72.00, 83.00 / 10006923, Wanderson Santos da Silva, 9.00, 30.00, 39.00 /
10009852, Wandrew Freire Guimaraes, 8.00, 46.00, 54.00 / 10001350, Wanessa Goes de Oliveira
Goncalves, 13.00, 52.00, 65.00 / 10007372, Wanici Correa dos Anjos Bacha, 10.00, 48.00, 58.00 /
10011947, Warlei Fernando Gomes Lisboa Junior, 6.00, 28.00, 34.00 / 10011071, Warlleson Santos de
Oliveira, 8.00, 36.00, 44.00 / 10006778, Warlley Martins Noleto, 10.00, 38.00, 48.00 / 10007010,
Washington Santos Filho, 14.00, 62.00, 76.00 / 10005399, Wdson Oliveira de Souza Rodrigues, 10.00,
50.00, 60.00 / 10010901, Weider Daniel da Silva Viana, 14.00, 60.00, 74.00 / 10011998, Weidson Dias
Pessoa, 8.00, 44.00, 52.00 / 10010089, Weliton Cruz da Silva, 6.00, 18.00, 24.00 / 10001477, Welkson
Mateus Santos Albuquerque, 6.00, 28.00, 34.00 / 10005299, Wellen Patricia Ferreira de Menezes, 9.00,
58.00, 67.00 / 10000276, Wellen Silva Ferreira, 9.00, 26.00, 35.00 / 10013102, Welligton Joao Pamplona
da Costa Junior, 11.00, 46.00, 57.00 / 10002782, Welligton Marques dos Santos da Silva, 9.00, 36.00, 45.00
/ 10013119, Wellingthon Julio de Farias, 10.00, 56.00, 66.00 / 10009700, Wellington Maia da Silva, 9.00,
42.00, 51.00 / 10013184, Wellington Negrao Tavares, 9.00, 44.00, 53.00 / 10005232, Wellington Oliveira
da Silva, 10.00, 42.00, 52.00 / 10005473, Wellison Carlos, 11.00, 54.00, 65.00 / 10000083, Wellison
Smithe Alves, 9.00, 46.00, 55.00 / 10016419, Welliton Pinto Modesto, 9.00, 50.00, 59.00 / 10015880,
Wellyton Vieira Barros, 6.00, 52.00, 58.00 / 10005431, Welmyngton Barros de Castro, 12.00, 54.00, 66.00
 
/ 10003135, Welton Lima Campelo, 3.00, 22.00, 25.00 / 10007911, Wembollis da Mota Coutinho Barros,
15.00, 66.00, 81.00 / 10001472, Wemerson Santos Ferreira, 12.00, 56.00, 68.00 / 10016185, Wendel
Richard Correa da Silva, 5.00, 34.00, 39.00 / 10000227, Wendell Brendo Silva da Silva, 12.00, 54.00, 66.00
/ 10000564, Wendell Brito dos Santos, 8.00, 38.00, 46.00 / 10000085, Wendell Silva Santos, 11.00, 36.00,
47.00 / 10010898, Wenderson Aparicio Gomes de Barros, 6.00, 34.00, 40.00 / 10010177, Wenderson do
Nascimento Silva, 12.00, 56.00, 68.00 / 10011118, Wenderson Pereira Moreira, 7.00, 34.00, 41.00 /
10001422, Wenderson Ricardo Alves da Silva, 10.00, 62.00, 72.00 / 10005210, Weriqui Bezerra Araujo,
5.00, 40.00, 45.00 / 10001603, Werlison Costa Macedo, 7.00, 32.00, 39.00 / 10011857, Werner Beinson
Caldas Belo, 10.00, 46.00, 56.00 / 10000653, Werthery da Silva Cardoso, 10.00, 36.00, 46.00 / 10000509,
Werverton Douglas Rodrigues Andrade, 5.00, 34.00, 39.00 / 10001911, Wesden Richard Santos de
Mendonca, 11.00, 54.00, 65.00 / 10002125, Wesdlley Rodrigues Santos, 9.00, 54.00, 63.00 / 10005300,
Weslaine Rodrigues Pereira, 5.00, 24.00, 29.00 / 10016643, Weslane Vitoria Alves e Silva, 5.00, 24.00,
29.00 / 10013682, Weslei Silva Silva, 9.00, 40.00, 49.00 / 10013129, Wesley de Sousa Sena, 10.00, 34.00,
44.00 / 10007878, Wesley Ednaldo Batista da Silva, 12.00, 58.00, 70.00 / 10012788, Wesley Goncalves
Tavares, 8.00, 32.00, 40.00 / 10010130, Wesley Luis Macedo Xavier, 10.00, 38.00, 48.00 / 10011434,
Wesley Mendes Lima, 13.00, 54.00, 67.00 / 10005216, Wesley Ricardo Pinheiro, 10.00, 48.00, 58.00 /
10002936, Wesllen Farias dos Santos, 10.00, 46.00, 56.00 / 10012663, Weslon Mendonca Araujo, 10.00,
40.00, 50.00 / 10001495, Wesney Roberto Silva Soares, 13.00, 56.00, 69.00 / 10015876, Weverson Peres
Vieira, 7.00, 36.00, 43.00 / 10013451, Weverton Freitas Silva, 11.00, 52.00, 63.00 / 10013063, Whendel
Tayrone Rodrigues da Silva, 2.00, 32.00, 34.00 / 10011282, Wherique Costa Kreling, 5.00, 26.00, 31.00 /
10005312, Whitero Matheus Martins Vaz Pereira, 7.00, 42.00, 49.00 / 10013712, Wictor Matheus de
Albuquerque Cavalcanti, 10.00, 56.00, 66.00 / 10001092, Wigson Reis de Oliveira Guedes, 13.00, 40.00,
53.00 / 10011573, Wildemberg Costa Torres, 14.00, 62.00, 76.00 / 10002877, Wildson Ferreira de
Menezes, 10.00, 46.00, 56.00 / 10012875, Wiliam Jorge da Silva Bastos, 5.00, 30.00, 35.00 / 10010361,
Wilker Alves Gomes, 10.00, 50.00, 60.00 / 10007785, Wilkson da Cunha Lima, 4.00, 24.00, 28.00 /
10001791, Willames Rafael Silva Santos, 11.00, 54.00, 65.00 / 10016230, Willhison dos Santos Sousa,
11.00, 42.00, 53.00 / 10016172, William Racine Gouvea Lopes, 12.00, 54.00, 66.00 / 10001374, William
Ribeiro Campos, 10.00, 64.00, 74.00 / 10012577, William Victor Maciel dos Santos Cardoso, 9.00, 44.00,
53.00 / 10013739, Williams Junior Santiago Paixao, 8.00, 30.00, 38.00 / 10013721, Williams Moraes
Magalhaes, 7.00, 36.00, 43.00 / 10010208, Willian da Silva de Sousa, 7.00, 30.00, 37.00 / 10012352,
Wilmar Rodrigues da Silva Junior, 12.00, 58.00, 70.00 / 10013281, Wilmara da Silva e Silva, 8.00, 36.00,
44.00 / 10000087, Wilsara Sasha Leite Santos, 8.00, 28.00, 36.00 / 10005250, Wilson da Silva Ferreira,
9.00, 42.00, 51.00 / 10011078, Wilson Moreira Marques Neto, 11.00, 50.00, 61.00 / 10001888, Wislley
Oliveira Franca da Silva, 8.00, 48.00, 56.00 / 10016671, Wladson Luan Monteiro Borges, 8.00, 40.00,
48.00 / 10015949, Wythallo Gabriel Rodrigues Claudiano, 10.00, 50.00, 60.00 / 10007469, Yago Mota
Campelo, 6.00, 16.00, 22.00 / 10011165, Yago Williams Melo Damasceno, 5.00, 36.00, 41.00 / 10010495,
Yam Vanger Nunes Freitas Miranda, 9.00, 50.00, 59.00 / 10000888, Yan Abneer Monteiro da Costa, 13.00,
64.00, 77.00 / 10003008, Yan Eduardo Lima do Espirito Santo, 5.00, 32.00, 37.00 / 10009759, Yan Melo
dos Santos, 8.00, 30.00, 38.00 / 10002926, Yan Tamio Towata da Costa, 8.00, 44.00, 52.00 / 10010885,
Yana Dias Leal, 8.00, 34.00, 42.00 / 10001370, Yandra Teixeira Silva, 9.00, 40.00, 49.00 / 10007805, Yane
Evandra Andrade Farias, 13.00, 56.00, 69.00 / 10000015, Yanka da Costa Rodrigues, 0.00, 6.00, 6.00 /
10012558, Yanmila Isis Peroti Bentes Costa, 13.00, 46.00, 59.00 / 10001927, Yann Matheus Soares
Machado Martiniano, 7.00, 52.00, 59.00 / 10010428, Yara da Silva Reis, 15.00, 52.00, 67.00 / 10001476,
Yara Thamires Abreu Bezerra, 8.00, 42.00, 50.00 / 10001314, Yarima Ali Teixeira Araujo, 7.00, 22.00,
29.00 / 10017036, Yasmim Rodrigues Vieira, 16.00, 36.00, 52.00 / 10010163, Yasmin Cardoso Alves,
12.00, 58.00, 70.00 / 10006996, Yasmin Danielle Moraes Almeida, 14.00, 40.00, 54.00 / 10001271, Yasmin
de Jesus Silva Carvalho, 8.00, 30.00, 38.00 / 10000918, Yasmin do Socorro Gouvea de Souza, 7.00, 40.00,
47.00 / 10011851, Yasmin Jamilly Santos Neves, 11.00, 56.00, 67.00 / 10012306, Yasmin Letycia Silva do
Nascimento, 13.00, 34.00, 47.00 / 10002349, Yasmin Luana Nassar de Albuquerque, 9.00, 58.00, 67.00 /
10007630, Yasmin Monteiro Rodrigues, 8.00, 38.00, 46.00 / 10000829, Yasmin Moraes Saavedra de
Souza, 9.00, 38.00, 47.00 / 10015828, Yasmin Nazare Viana dos Reis Rodrigues Dantas, 8.00, 32.00, 40.00
/ 10012743, Yasmin Skarlat de Souza Menezes, 10.00, 32.00, 42.00 / 10000620, Yasmin Tyemi Tanaka
 
Magalhaes, 10.00, 38.00, 48.00 / 10002509, Ygo Martins Silva, 11.00, 46.00, 57.00 / 10000756, Ygor Costa
Sales de Aguiar, 12.00, 64.00, 76.00 / 10010773, Yngrid Cristina da Silva Santos, 9.00, 50.00, 59.00 /
10009857, Ytala Gabriele Ferreira Guimaraes, 7.00, 28.00, 35.00 / 10015879, Yuliana de Nazare Pereira
Mussio, 11.00, 38.00, 49.00 / 10013659, Yuri da Silva Moraes, 10.00, 40.00, 50.00 / 10005666, Yuri
Hamilton Souza Watrim, 14.00, 54.00, 68.00 / 10006792, Yuri Jose Silva da Silva, 8.00, 42.00, 50.00 /
10001692, Yuri Silva Maia, 12.00, 48.00, 60.00 / 10000581, Yvan Carrenho Lima, 6.00, 32.00, 38.00 /
10013032, Zaqueu Rodrigues de Farias, 6.00, 34.00, 40.00 / 10013597, Zazusky Zain Silveira da Silva
Nascimento, 9.00, 40.00, 49.00 / 10012301, Zylmarya Luna Maia Alencar, 11.00, 48.00, 59.00
"""
canditatos = canditatos.replace('\n', '')

canditatos_lista = canditatos.split('/')

info_candidato = []

for canditato in canditatos_lista:
    info_candidato.append(canditato.split(','))
df = pd.DataFrame(info_candidato)
df.to_excel('classificacao_cfo.xlsx', sheet_name='classificacao', index=False)
