#!/usr/bin/python3

"""
100 simple sentences for Trakaido Lithuanian learning app.
Uses only words from the nouns.py and verbs.py wordlists.
Each sentence is practical and useful for beginners.
"""

sentences_one = [
    # Basic needs and daily activities
    {"english": "I eat bread.", "lithuanian": "Aš valgau duoną."},
    {"english": "She drinks water.", "lithuanian": "Ji geria vandenį."},
    {"english": "He sleeps in the house.", "lithuanian": "Jis miega namuose."},
    {"english": "We live in the city.", "lithuanian": "Mes gyvename mieste."},
    {"english": "You work in the hospital.", "lithuanian": "Tu dirbi ligoninėje."},
    
    # Food and eating
    {"english": "I like coffee.", "lithuanian": "Aš mėgstu kavą."},
    {"english": "They eat fish.", "lithuanian": "Jie valgo žuvį."},
    {"english": "She buys cheese.", "lithuanian": "Ji perka sūrį."},
    {"english": "He drinks beer.", "lithuanian": "Jis geria alų."},
    {"english": "We make soup.", "lithuanian": "Mes gaminame sriubą."},
    
    # Movement and travel
    {"english": "I walk to school.", "lithuanian": "Aš einu į mokyklą."},
    {"english": "She drives the car.", "lithuanian": "Ji važiuoja automobiliu."},
    {"english": "He runs in the park.", "lithuanian": "Jis bėga parke."},
    {"english": "They come home.", "lithuanian": "Jie ateina namo."},
    {"english": "We go to the store.", "lithuanian": "Mes vykstame į parduotuvę."},
    
    # Learning and knowledge
    {"english": "I read the book.", "lithuanian": "Aš skaitau knygą."},
    {"english": "She writes with the pen.", "lithuanian": "Ji rašo rašikliu."},
    {"english": "The teacher teaches the children.", "lithuanian": "Mokytojas moko vaikus."},
    {"english": "Students learn Lithuanian.", "lithuanian": "Studentai mokosi lietuvių kalbos."},
    {"english": "He knows the answer.", "lithuanian": "Jis žino atsakymą."},
    
    # Family and relationships
    {"english": "My mother cooks dinner.", "lithuanian": "Mano motina gamina vakarienę."},
    {"english": "The father works hard.", "lithuanian": "Tėvas dirba sunkiai."},
    {"english": "My brother plays games.", "lithuanian": "Mano brolis žaidžia žaidimus."},
    {"english": "The sister likes music.", "lithuanian": "Sesuo mėgsta muziką."},
    {"english": "Children play in the garden.", "lithuanian": "Vaikai žaidžia sode."},
    
    # Animals and nature
    {"english": "The dog runs fast.", "lithuanian": "Šuo bėga greitai."},
    {"english": "Cats sleep a lot.", "lithuanian": "Katės daug miega."},
    {"english": "Birds sing in the tree.", "lithuanian": "Paukščiai dainuoja medyje."},
    {"english": "The horse eats grass.", "lithuanian": "Arklys valgo žolę."},
    {"english": "We see flowers in the garden.", "lithuanian": "Mes matome gėles sode."},
    
    # Colors and descriptions
    {"english": "I like the red apple.", "lithuanian": "Aš mėgstu raudoną obuolį."},
    {"english": "She wears a blue dress.", "lithuanian": "Ji dėvi mėlyną suknelę."},
    {"english": "The green grass is beautiful.", "lithuanian": "Žalia žolė graži."},
    {"english": "He has a black car.", "lithuanian": "Jis turi juodą automobilį."},
    {"english": "We see white snow.", "lithuanian": "Mes matome baltą sniegą."},
    
    # Weather and time
    {"english": "Today is Monday.", "lithuanian": "Šiandien pirmadienis."},
    {"english": "It rains in October.", "lithuanian": "Spalį lyja."},
    {"english": "The sun shines brightly.", "lithuanian": "Saulė šviečia ryškiai."},
    {"english": "Snow falls in December.", "lithuanian": "Gruodį krenta snigas."},
    {"english": "We like warm weather.", "lithuanian": "Mes mėgstame šiltą orą."},
    
    # Clothing and appearance
    {"english": "I wear warm clothes.", "lithuanian": "Aš dėviu šiltus drabužius."},
    {"english": "She buys new shoes.", "lithuanian": "Ji perka naujus batus."},
    {"english": "He has a nice hat.", "lithuanian": "Jis turi gražią kepurę."},
    {"english": "We need winter coats.", "lithuanian": "Mums reikia žiemos paltų."},
    {"english": "They wear glasses.", "lithuanian": "Jie dėvi akinius."},
    
    # Body and health
    {"english": "My head hurts.", "lithuanian": "Man skauda galvą."},
    {"english": "She washes her hands.", "lithuanian": "Ji plauna rankas."},
    {"english": "The doctor helps people.", "lithuanian": "Gydytojas padeda žmonėms."},
    {"english": "I brush my teeth.", "lithuanian": "Aš valau dantis."},
    {"english": "He has strong muscles.", "lithuanian": "Jis turi stiprius raumenis."},
    
    # Food preparation and kitchen
    {"english": "I cook with salt.", "lithuanian": "Aš gaminu su druska."},
    {"english": "She cuts bread with a knife.", "lithuanian": "Ji kerpa duoną peiliu."},
    {"english": "We eat with a fork.", "lithuanian": "Mes valgome šakute."},
    {"english": "He drinks from a cup.", "lithuanian": "Jis geria iš puodelio."},
    {"english": "Food is on the plate.", "lithuanian": "Maistas ant lėkštės."},
    
    # Transportation
    {"english": "The bus comes at eight.", "lithuanian": "Autobusas atvažiuoja aštuoniose."},
    {"english": "I travel by train.", "lithuanian": "Aš keliiauju traukiniu."},
    {"english": "She flies in an airplane.", "lithuanian": "Ji skrenda lėktuvu."},
    {"english": "We ride bicycles.", "lithuanian": "Mes važiuojame dviračiais."},
    {"english": "The ship sails on water.", "lithuanian": "Laivas plaukia vandeniu."},
    
    # Numbers and counting
    {"english": "I have two cats.", "lithuanian": "Aš turiu dvi kates."},
    {"english": "She buys five apples.", "lithuanian": "Ji perka penkis obuolius."},
    {"english": "We see ten birds.", "lithuanian": "Mes matome dešimt paukščių."},
    {"english": "He counts to twenty.", "lithuanian": "Jis skaičiuoja iki dvidešimties."},
    {"english": "There are seven days.", "lithuanian": "Yra septynios dienos."},
    
    # Emotions and feelings
    {"english": "I am happy today.", "lithuanian": "Aš šiandien laimingas."},
    {"english": "She feels sad.", "lithuanian": "Ji jaučiasi liūdna."},
    {"english": "The child is excited.", "lithuanian": "Vaikas susijaudinęs."},
    {"english": "We are tired.", "lithuanian": "Mes pavargę."},
    {"english": "He looks worried.", "lithuanian": "Jis atrodo susirūpinęs."},
    
    # Countries and nationalities
    {"english": "I am from Lithuania.", "lithuanian": "Aš esu iš Lietuvos."},
    {"english": "She speaks German.", "lithuanian": "Ji kalba vokiškai."},
    {"english": "We visit France.", "lithuanian": "Mes lankome Prancūziją."},
    {"english": "He lives in America.", "lithuanian": "Jis gyvena Amerikoje."},
    {"english": "They come from Poland.", "lithuanian": "Jie atvyksta iš Lenkijos."},
    
    # Occupations and work
    {"english": "The nurse helps patients.", "lithuanian": "Slaugytoja padeda pacientams."},
    {"english": "A chef cooks good food.", "lithuanian": "Virėjas gamina gerą maistą."},
    {"english": "The pilot flies planes.", "lithuanian": "Pilotas skraido lėktuvais."},
    {"english": "Engineers build bridges.", "lithuanian": "Inžinieriai stato tiltus."},
    {"english": "Artists paint pictures.", "lithuanian": "Menininkai tapo paveikslus."},
    
    # Technology and modern life
    {"english": "I use my phone.", "lithuanian": "Aš naudoju telefoną."},
    {"english": "She works on computer.", "lithuanian": "Ji dirba kompiuteriu."},
    {"english": "We watch television.", "lithuanian": "Mes žiūrime televizorių."},
    {"english": "He takes photos.", "lithuanian": "Jis fotografuoja."},
    {"english": "They send emails.", "lithuanian": "Jie siunčia el. laiškus."},
    
    # Shopping and money
    {"english": "I buy bread at the store.", "lithuanian": "Aš perku duoną parduotuvėje."},
    {"english": "She pays with money.", "lithuanian": "Ji moka pinigais."},
    {"english": "We need new clothes.", "lithuanian": "Mums reikia naujų drabužių."},
    {"english": "He sells fish.", "lithuanian": "Jis parduoda žuvį."},
    {"english": "The store closes late.", "lithuanian": "Parduotuvė užsidaro vėlai."},
    
    # Hobbies and leisure
    {"english": "I like reading books.", "lithuanian": "Aš mėgstu skaityti knygas."},
    {"english": "She enjoys cooking.", "lithuanian": "Jai patinka gaminti."},
    {"english": "We play sports.", "lithuanian": "Mes sportuojame."},
    {"english": "He listens to music.", "lithuanian": "Jis klauso muzikos."},
    {"english": "They dance well.", "lithuanian": "Jie gerai šoka."},
    
    # Shapes and objects
    {"english": "The ball is round.", "lithuanian": "Kamuolys apvalus."},
    {"english": "I draw a square.", "lithuanian": "Aš piešiu kvadratą."},
    {"english": "She cuts triangles.", "lithuanian": "Ji kerpa trikampius."},
    {"english": "The box is rectangular.", "lithuanian": "Dėžė stačiakampė."},
    {"english": "We see a circle.", "lithuanian": "Mes matome apskritimą."},
    
    # Past tense examples
    {"english": "I ate breakfast.", "lithuanian": "Aš valgiau pusryčius."},
    {"english": "She worked yesterday.", "lithuanian": "Ji dirbo vakar."},
    {"english": "We lived in the country.", "lithuanian": "Mes gyvenome kaime."},
    {"english": "He bought a car.", "lithuanian": "Jis pirko automobilį."},
    {"english": "They came home late.", "lithuanian": "Jie grįžo namo vėlai."},
    
    # Future tense examples
    {"english": "I will study tomorrow.", "lithuanian": "Aš mokysiu rytoj."},
    {"english": "She will cook dinner.", "lithuanian": "Ji gamins vakarienę."},
    {"english": "We will travel to Spain.", "lithuanian": "Mes keliausime į Ispaniją."},
    {"english": "He will read the newspaper.", "lithuanian": "Jis skaitys laikraštį."},
    {"english": "They will return soon.", "lithuanian": "Jie grįš greitai."},
    
    # Complex but simple sentences
    {"english": "The red bird sings beautifully.", "lithuanian": "Raudonas paukštis gražiai dainuoja."},
    {"english": "My grandmother cooks delicious food.", "lithuanian": "Mano senelė gamina skanų maistą."},
    {"english": "The small cat sleeps quietly.", "lithuanian": "Maža katė tyliai miega."},
    {"english": "We drink hot coffee in winter.", "lithuanian": "Mes geriame karštą kavą žiemą."},
    {"english": "Children play happily in summer.", "lithuanian": "Vaikai linksmai žaidžia vasarą."}
]

def get_all_sentences():
    """
    Get all 100 sentences.
    
    Returns:
        list: List of sentence dictionaries with english and lithuanian keys
    """
    return sentences_one