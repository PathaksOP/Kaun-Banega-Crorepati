import random
import time

# INTRODUCTION

print(('~~~WELCOME TO KAUN BANEGA CROREPATI !~~~').center(500))
print('RULES : Questions will be displayed on your computer screen along with 4 options in which one of the options will be the correct option. \n        Type the correct option (a/b/c/d). \n        For every correct Answer you will go up a level and get more money. \n        There will be checkpoints at question 5 , 10 and 12. \n        If you answer incorrectly, you will get the money in the previous checkpoint. \n        To quit at any question and take away the money type (Q). \n        GOOD LUCK! \n')

# QUESTION BANK

Question_bank1= [
("Which Indian city is known as the Pink City?\na) Jaipur\nb) Udaipur\nc) Jodhpur\nd) Bikaner","a"),
("Who discovered penicillin?\na) Louis Pasteur\nb) Alexander Fleming\nc) Robert Koch\nd) Edward Jenner","b"),
("Which planet is known as the Red Planet?\na) Venus\nb) Mercury\nc) Mars\nd) Jupiter","c"),
("Which river flows through Delhi?\na) Ganga\nb) Narmada\nc) Godavari\nd) Yamuna","d"),

("Which Mughal emperor built the Taj Mahal?\na) Shah Jahan\nb) Akbar\nc) Babur\nd) Aurangzeb","a"),
("Which gas do plants absorb during photosynthesis?\na) Oxygen\nb) Carbon dioxide\nc) Nitrogen\nd) Hydrogen","b"),
("Which continent is the largest?\na) Africa\nb) Europe\nc) Asia\nd) Antarctica","c"),
("Which country is famous for the Eiffel Tower?\na) Italy\nb) Spain\nc) Germany\nd) France","d"),

("Which sport uses a shuttlecock?\na) Badminton\nb) Tennis\nc) Cricket\nd) Hockey","a"),
("Which vitamin is obtained from sunlight?\na) Vitamin A\nb) Vitamin D\nc) Vitamin B12\nd) Vitamin C","b"),
("Which planet is closest to the Sun?\na) Venus\nb) Earth\nc) Mercury\nd) Mars","c"),
("Which monument is located in Agra?\na) Red Fort\nb) Qutub Minar\nc) Gateway of India\nd) Taj Mahal","d"),

("Which Indian state has Mumbai as its capital?\na) Maharashtra\nb) Gujarat\nc) Rajasthan\nd) Goa","a"),
("Which bird is the national bird of India?\na) Sparrow\nb) Peacock\nc) Parrot\nd) Eagle","b"),
("Which metal is liquid at room temperature?\na) Copper\nb) Gold\nc) Mercury\nd) Iron","c"),
("Which city is known as Silicon Valley of India?\na) Hyderabad\nb) Pune\nc) Chennai\nd) Bengaluru","d"),

("Which is the fastest land animal?\na) Cheetah\nb) Lion\nc) Tiger\nd) Leopard","a"),
("Which country hosted the 2012 Olympics?\na) China\nb) UK\nc) Japan\nd) Brazil","b"),
("Which desert is located in India?\na) Sahara\nb) Gobi\nc) Thar\nd) Atacama","c"),
("Which river flows through London?\na) Seine\nb) Rhine\nc) Danube\nd) Thames","d"),

("Which organ pumps blood in the human body?\na) Heart\nb) Brain\nc) Liver\nd) Kidney","a"),
("Which scientist proposed the theory of relativity?\na) Newton\nb) Einstein\nc) Tesla\nd) Bohr","b"),
("Which country invented paper?\na) Egypt\nb) Greece\nc) China\nd) India","c"),
("Which animal is known as the King of the Jungle?\na) Tiger\nb) Leopard\nc) Elephant\nd) Lion","d"),

("Which Indian leader is called the Father of the Nation?\na) Mahatma Gandhi\nb) Jawaharlal Nehru\nc) Subhas Chandra Bose\nd) Vallabhbhai Patel","a"),
("Which instrument measures temperature?\na) Barometer\nb) Hygrometer\nc) Thermometer\nd) Altimeter","c"),
("Which ocean is the largest?\na) Pacific Ocean\nb) Atlantic Ocean\nc) Indian Ocean\nd) Arctic Ocean","a"),
("Which gas is essential for breathing?\na) Oxygen\nb) Nitrogen\nc) Carbon dioxide\nd) Helium","a"),
("Which Indian festival is known as the festival of lights?\na) Diwali\nb) Holi\nc) Eid\n d) Pongal","a"),
("Which mountain is the highest in the world?\na) Mount Everest\nb) K2\nc) Kanchenjunga\nd) Lhotse","a")
]
Question_bank2= [
("Which Indian city is known as the City of Lakes?\na) Udaipur\nb) Bhopal\nc) Srinagar\nd) Nainital","a"),
("Who invented the telephone?\na) Edison\nb) Alexander Graham Bell\nc) Tesla\nd) Marconi","b"),
("Which planet is known as Earth's twin?\na) Mars\nb) Mercury\nc) Venus\nd) Saturn","c"),
("Which Indian monument is located in Delhi?\na) Taj Mahal\nb) Charminar\nc) Gateway of India\nd) Red Fort","d"),

("Which river is the longest in India?\na) Ganga\nb) Yamuna\nc) Brahmaputra\nd) Godavari","a"),
("Which scientist discovered gravity?\na) Galileo\nb) Isaac Newton\nc) Einstein\nd) Faraday","b"),
("Which country has the Great Wall?\na) Japan\nb) Korea\nc) China\nd) Mongolia","c"),
("Which desert is the largest hot desert?\na) Thar\nb) Gobi\nc) Kalahari\nd) Sahara","d"),

("Which Indian state is famous for tea gardens?\na) Assam\nb) Gujarat\nc) Punjab\nd) Haryana","a"),
("Which gas is most abundant in Earth's atmosphere?\na) Oxygen\nb) Nitrogen\nc) Carbon dioxide\nd) Hydrogen","b"),
("Which mountain range contains Mount Everest?\na) Alps\nb) Andes\nc) Himalayas\nd) Rockies","c"),
("Which river flows through Paris?\na) Thames\nb) Rhine\nc) Danube\nd) Seine","d"),

("Which animal is the national animal of India?\na) Tiger\nb) Lion\nc) Leopard\nd) Elephant","a"),
("Which metal is mainly used in electrical wiring?\na) Aluminium\nb) Copper\nc) Iron\nd) Zinc","b"),
("Which country hosted the 2008 Olympics?\na) Japan\nb) Brazil\nc) China\nd) Greece","c"),
("Which city is famous for the Statue of Liberty?\na) Washington\nb) Chicago\nc) Boston\nd) New York","d"),

("Which organ produces insulin?\na) Pancreas\nb) Liver\nc) Kidney\nd) Stomach","a"),
("Which Indian freedom fighter founded Azad Hind Fauj?\na) Bhagat Singh\nb) Subhas Chandra Bose\nc) Gandhi\nd) Patel","b"),
("Which continent has the Amazon rainforest?\na) Africa\nb) Asia\nc) South America\nd) Australia","c"),
("Which river flows through Rome?\na) Seine\nb) Rhine\nc) Danube\nd) Tiber","d"),

("Which country is known as the Land of Rising Sun?\na) Japan\nb) China\nc) Thailand\nd) Korea","a"),
("Which vitamin prevents scurvy?\na) Vitamin A\nb) Vitamin C\nc) Vitamin D\nd) Vitamin B","b"),
("Which ocean is between Africa and Australia?\na) Pacific\nb) Atlantic\nc) Indian\n d) Arctic","c"),
("Which city hosted the first modern Olympics?\na) Paris\nb) London\nc) Rome\nd) Athens","d"),

("Which Indian state has the capital Chennai?\na) Tamil Nadu\nb) Kerala\nc) Karnataka\nd) Andhra Pradesh","a"),
("Which scientist discovered radioactivity?\na) Rutherford\nb) Henri Becquerel\nc) Einstein\nd) Curie","b"),
("Which animal is the tallest in the world?\na) Elephant\nb) Horse\nc) Giraffe\nd) Camel","c"),
("Which river is called the lifeline of Egypt?\na) Amazon\nb) Congo\nc) Niger\nd) Nile","d"),

("Which metal is used to make coins commonly?\na) Nickel\nb) Silver\nc) Aluminium\nd) Copper","a"),
("Which country is famous for tulips?\na) Belgium\nb) Netherlands\nc) Denmark\nd) Austria","b")
]
Question_bank3= [
("Which ancient Indian university was located in Bihar?\na) Nalanda\nb) Takshashila\nc) Vikramashila\nd) Vallabhi","a"),
("Who discovered the electron?\na) Rutherford\nb) J J Thomson\nc) Bohr\nd) Dalton","b"),
("Which country has the largest population in the world today?\na) USA\nb) Indonesia\nc) India\nd) Brazil","c"),
("Which river flows through Budapest?\na) Rhine\nb) Seine\nc) Volga\nd) Danube","d"),

("Which Mughal emperor built Fatehpur Sikri?\na) Akbar\nb) Babur\nc) Jahangir\nd) Aurangzeb","a"),
("Which scientist proposed the heliocentric theory?\na) Galileo\nb) Copernicus\nc) Newton\nd) Kepler","b"),
("Which metal is the best conductor of electricity?\na) Gold\nb) Copper\nc) Silver\nd) Aluminium","c"),
("Which strait separates Asia and North America?\na) Malacca\nb) Hormuz\nc) Gibraltar\nd) Bering","d"),

("Which Indian state has Kaziranga National Park?\na) Assam\nb) Meghalaya\nc) Manipur\nd) Mizoram","a"),
("Which instrument measures atmospheric pressure?\na) Thermometer\nb) Barometer\nc) Hygrometer\nd) Anemometer","b"),
("Which desert is in Mongolia and China?\na) Sahara\nb) Thar\nc) Gobi\nd) Atacama","c"),
("Which river flows through Berlin?\na) Rhine\nb) Elbe\nc) Oder\nd) Spree","d"),

("Which scientist discovered the neutron?\na) James Chadwick\nb) Rutherford\nc) Bohr\nd) Einstein","a"),
("Which Indian state has the capital Jaipur?\na) Gujarat\nb) Rajasthan\nc) Punjab\nd) Haryana","b"),
("Which planet has the largest number of moons?\na) Earth\nb) Mars\nc) Jupiter\nd) Venus","c"),
("Which city is known as the financial capital of USA?\na) Chicago\nb) Washington\nc) Los Angeles\nd) New York","d"),

("Which empire built the city of Hampi?\na) Vijayanagara\nb) Maurya\nc) Gupta\nd) Chola","a"),
("Which element has atomic number 1?\na) Helium\nb) Hydrogen\nc) Oxygen\nd) Nitrogen","b"),
("Which mountain is the second highest in the world?\na) Everest\nb) Kangchenjunga\nc) K2\nd) Lhotse","c"),
("Which river flows through Baghdad?\na) Nile\nb) Jordan\nc) Euphrates\nd) Tigris","d"),

("Which Indian king built the Brihadeeswara Temple?\na) Rajaraja Chola\nb) Ashoka\nc) Harsha\nd) Samudragupta","a"),
("Which scientist discovered X-rays?\na) Einstein\nb) Wilhelm Roentgen\nc) Curie\nd) Faraday","b"),
("Which country has the Great Barrier Reef?\na) USA\nb) Indonesia\nc) Australia\nd) Philippines","c"),
("Which river flows through Madrid?\na) Tagus\nb) Loire\nc) Po\nd) Manzanares","d"),

("Which Indian state is famous for backwaters?\na) Kerala\nb) Tamil Nadu\nc) Goa\nd) Odisha","a"),
("Which gas is used in balloons?\na) Hydrogen\nb) Helium\nc) Nitrogen\nd) Argon","b"),
("Which planet has rings most visible from Earth?\na) Jupiter\nb) Uranus\nc) Saturn\nd) Neptune","c"),
("Which river flows through Vienna?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which scientist invented the steam engine improvement?\na) James Watt\nb) Edison\nc) Tesla\nd) Newton","a"),
("Which Indian leader gave the slogan 'Jai Hind'?\na) Gandhi\nb) Subhas Chandra Bose\nc) Nehru\nd) Patel","b")
]
Question_bank4= [
("Which ancient text was written by Kautilya on statecraft?\na) Arthashastra\nb) Manusmriti\nc) Rigveda\nd) Mahabharata","a"),
("Which scientist developed the laws of planetary motion?\na) Newton\nb) Johannes Kepler\nc) Galileo\nd) Einstein","b"),
("Which country has the longest coastline in the world?\na) Russia\nb) USA\nc) Canada\nd) Australia","c"),
("Which river flows through Cairo?\na) Tigris\nb) Euphrates\nc) Congo\nd) Nile","d"),

("Which Gupta ruler is known as the Napoleon of India?\na) Samudragupta\nb) Chandragupta I\nc) Skandagupta\nd) Kumaragupta","a"),
("Which instrument measures earthquakes?\na) Barometer\nb) Seismograph\nc) Thermometer\nd) Hygrometer","b"),
("Which element has the chemical symbol Na?\na) Nitrogen\nb) Neon\nc) Sodium\nd) Nickel","c"),
("Which sea separates Europe and Africa?\na) Black Sea\nb) Baltic Sea\nc) Red Sea\nd) Mediterranean Sea","d"),

("Which Indian state has the capital Lucknow?\na) Uttar Pradesh\nb) Bihar\nc) Madhya Pradesh\nd) Uttarakhand","a"),
("Who discovered the neutron?\na) Rutherford\nb) James Chadwick\nc) Bohr\nd) Thomson","b"),
("Which planet is known for the Great Red Spot?\na) Saturn\nb) Mars\nc) Jupiter\nd) Uranus","c"),
("Which river flows through Baghdad?\na) Nile\nb) Amazon\nc) Yangtze\nd) Tigris","d"),

("Which empire built the Ajanta caves?\na) Satavahana\nb) Maurya\nc) Gupta\nd) Chola","a"),
("Which scientist formulated the electromagnetic theory?\na) Faraday\nb) James Clerk Maxwell\nc) Newton\nd) Tesla","b"),
("Which desert is the largest cold desert?\na) Sahara\nb) Arabian\nc) Antarctica\nd) Gobi","c"),
("Which river flows through Prague?\na) Rhine\nb) Danube\nc) Elbe\nd) Vltava","d"),

("Which Indian leader started the Non-Cooperation Movement?\na) Mahatma Gandhi\nb) Nehru\nc) Patel\nd) Bose","a"),
("Which metal has the highest electrical conductivity?\na) Copper\nb) Silver\nc) Gold\nd) Aluminium","b"),
("Which country has the Amazon River?\na) Peru\nb) Colombia\nc) Brazil\nd) Bolivia","c"),
("Which river flows through Budapest?\na) Rhine\nb) Seine\nc) Thames\nd) Danube","d"),

("Which Indian ruler founded the Maurya Empire?\na) Chandragupta Maurya\nb) Ashoka\nc) Bindusara\nd) Harsha","a"),
("Which scientist discovered the electron?\na) Rutherford\nb) J J Thomson\nc) Dalton\nd) Bohr","b"),
("Which planet has the shortest day?\na) Mars\nb) Venus\nc) Jupiter\nd) Mercury","c"),
("Which river flows through Rome?\na) Seine\nb) Rhine\nc) Danube\nd) Tiber","d"),

("Which Indian state has the largest coastline?\na) Gujarat\nb) Tamil Nadu\nc) Andhra Pradesh\nd) Maharashtra","a"),
("Which scientist proposed the uncertainty principle?\na) Einstein\nb) Werner Heisenberg\nc) Bohr\nd) Planck","b"),
("Which mountain is the third highest in the world?\na) Everest\nb) K2\nc) Kangchenjunga\nd) Lhotse","c"),
("Which river flows through Warsaw?\na) Rhine\nb) Danube\nc) Elbe\nd) Vistula","d"),

("Which Indian emperor built the Sanchi Stupa?\na) Ashoka\nb) Akbar\nc) Chandragupta\nd) Harsha","a"),
("Which scientist discovered radio waves?\na) Maxwell\nb) Heinrich Hertz\nc) Tesla\nd) Marconi","b")
]
Question_bank5= [
("Which ancient Indian university was destroyed by Bakhtiyar Khilji?\na) Nalanda\nb) Takshashila\nc) Vikramashila\nd) Vallabhi","a"),
("Which scientist proposed the law of universal gravitation?\na) Galileo\nb) Isaac Newton\nc) Kepler\nd) Einstein","b"),
("Which element has atomic number 92?\na) Thorium\nb) Radium\nc) Uranium\nd) Plutonium","c"),
("Which river flows through Baghdad and joins the Euphrates?\na) Jordan\nb) Nile\nc) Indus\nd) Tigris","d"),

("Which Indian king built the Brihadeeswara Temple?\na) Rajaraja Chola I\nb) Ashoka\nc) Harsha\nd) Samudragupta","a"),
("Which scientist discovered the nucleus of an atom?\na) Bohr\nb) Ernest Rutherford\nc) Dalton\nd) Thomson","b"),
("Which planet rotates on its side?\na) Neptune\nb) Saturn\nc) Uranus\nd) Mars","c"),
("Which river flows through Vienna?\na) Rhine\nb) Seine\nc) Elbe\nd) Danube","d"),

("Which Indian state has the capital Itanagar?\na) Arunachal Pradesh\nb) Nagaland\nc) Mizoram\nd) Manipur","a"),
("Which scientist discovered X-rays?\na) Einstein\nb) Wilhelm Roentgen\nc) Curie\nd) Faraday","b"),
("Which country has the most volcanoes?\na) Japan\nb) Chile\nc) Indonesia\nd) USA","c"),
("Which river flows through Kyiv?\na) Volga\nb) Rhine\nc) Danube\nd) Dnieper","d"),

("Which Mughal emperor wrote Tuzuk-i-Jahangiri?\na) Jahangir\nb) Akbar\nc) Babur\nd) Aurangzeb","a"),
("Which scientist proposed the three laws of motion?\na) Galileo\nb) Isaac Newton\nc) Einstein\nd) Tesla","b"),
("Which element is most abundant in the universe?\na) Helium\nb) Oxygen\nc) Hydrogen\nd) Carbon","c"),
("Which river flows through Belgrade?\na) Rhine\nb) Seine\nc) Elbe\nd) Danube","d"),

("Which Indian leader wrote 'Discovery of India'?\na) Jawaharlal Nehru\nb) Gandhi\nc) Patel\nd) Bose","a"),
("Which scientist developed quantum theory?\na) Einstein\nb) Max Planck\nc) Bohr\nd) Heisenberg","b"),
("Which desert is the driest place on Earth?\na) Sahara\nb) Gobi\nc) Atacama\nd) Kalahari","c"),
("Which river flows through Hamburg?\na) Rhine\nb) Danube\nc) Seine\nd) Elbe","d"),

("Which Indian state has the capital Gangtok?\na) Sikkim\nb) Assam\nc) Meghalaya\nd) Tripura","a"),
("Which scientist discovered the neutron?\na) Rutherford\nb) James Chadwick\nc) Bohr\nd) Thomson","b"),
("Which planet has the strongest gravity?\na) Earth\nb) Mars\nc) Jupiter\nd) Venus","c"),
("Which river flows through Bratislava?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which Indian ruler built Fatehpur Sikri?\na) Akbar\nb) Babur\nc) Humayun\nd) Jahangir","a"),
("Which scientist discovered electromagnetic induction?\na) Tesla\nb) Michael Faraday\nc) Maxwell\nd) Ampere","b"),
("Which mountain is the fourth highest in the world?\na) Everest\nb) K2\nc) Lhotse\nd) Makalu","c"),
("Which river flows through Khartoum?\na) Amazon\nb) Congo\nc) Niger\nd) Nile","d"),

("Which Indian king defeated Seleucus Nicator?\na) Chandragupta Maurya\nb) Ashoka\nc) Bindusara\nd) Harsha","a"),
("Which scientist discovered the proton?\na) Thomson\nb) Ernest Rutherford\nc) Bohr\nd) Chadwick","b")
]
Question_bank6= [
("Which treaty ended the First World War?\na) Treaty of Versailles\nb) Treaty of Tordesillas\nc) Treaty of Utrecht\nd) Treaty of Ghent","a"),
("Which scientist discovered penicillin?\na) Louis Pasteur\nb) Alexander Fleming\nc) Robert Koch\nd) Edward Jenner","b"),
("Which element has the highest melting point?\na) Iron\nb) Platinum\nc) Tungsten\nd) Titanium","c"),
("Which river flows through the city of Baghdad?\na) Nile\nb) Euphrates\nc) Jordan\nd) Tigris","d"),

("Which Indian state has the highest literacy rate?\na) Kerala\nb) Tamil Nadu\nc) Goa\nd) Maharashtra","a"),
("Which scientist proposed the theory of relativity?\na) Newton\nb) Albert Einstein\nc) Galileo\nd) Tesla","b"),
("Which country is the largest producer of coffee?\na) Colombia\nb) Vietnam\nc) Brazil\nd) Ethiopia","c"),
("Which river flows through the city of Budapest?\na) Rhine\nb) Seine\nc) Volga\nd) Danube","d"),

("Which ancient civilization built Machu Picchu?\na) Inca\nb) Maya\nc) Aztec\nd) Olmec","a"),
("Which scientist invented the telephone?\na) Edison\nb) Alexander Graham Bell\nc) Tesla\nd) Faraday","b"),
("Which element has atomic number 79?\na) Silver\nb) Copper\nc) Gold\nd) Zinc","c"),
("Which river flows through the city of Paris?\na) Thames\nb) Rhine\nc) Danube\nd) Seine","d"),

("Which Indian city is known as the Pink City?\na) Jaipur\nb) Jodhpur\nc) Udaipur\nd) Bikaner","a"),
("Which scientist discovered the electron?\na) Rutherford\nb) J J Thomson\nc) Bohr\nd) Dalton","b"),
("Which country has the largest rainforest?\na) Indonesia\nb) Congo\nc) Brazil\nd) Peru","c"),
("Which river flows through the city of London?\na) Seine\nb) Rhine\nc) Danube\nd) Thames","d"),

("Which Indian ruler built the Qutub Minar?\na) Qutb-ud-din Aibak\nb) Akbar\nc) Ashoka\nd) Humayun","a"),
("Which scientist discovered the neutron?\na) Rutherford\nb) James Chadwick\nc) Bohr\nd) Thomson","b"),
("Which desert is the largest in Asia?\na) Thar\nb) Arabian\nc) Gobi\nd) Kalahari","c"),
("Which river flows through the city of Cairo?\na) Congo\nb) Niger\nc) Zambezi\nd) Nile","d"),

("Which Indian state has the capital Imphal?\na) Manipur\nb) Mizoram\nc) Tripura\nd) Nagaland","a"),
("Which scientist discovered radioactivity?\na) Rutherford\nb) Henri Becquerel\nc) Curie\nd) Einstein","b"),
("Which planet has the most powerful storms?\na) Saturn\nb) Neptune\nc) Jupiter\nd) Mars","c"),
("Which river flows through the city of Rome?\na) Seine\nb) Rhine\nc) Danube\nd) Tiber","d"),

("Which Indian king built the Konark Sun Temple?\na) Narasimhadeva I\nb) Ashoka\nc) Harsha\nd) Samudragupta","a"),
("Which scientist discovered electromagnetic waves?\na) Faraday\nb) Heinrich Hertz\nc) Maxwell\nd) Tesla","b"),
("Which mountain is the fifth highest in the world?\na) Everest\nb) K2\nc) Makalu\nd) Kangchenjunga","c"),
("Which river flows through the city of Baghdad?\na) Amazon\nb) Congo\nc) Niger\nd) Tigris","d"),

("Which Indian emperor built the Sanchi Stupa?\na) Ashoka\nb) Akbar\nc) Chandragupta\nd) Harsha","a"),
("Which scientist discovered the proton?\na) Thomson\nb) Ernest Rutherford\nc) Bohr\nd) Chadwick","b")
]
Question_bank7= [
("Which Indian mathematician discovered zero independently?\na) Aryabhata\nb) Brahmagupta\nc) Bhaskara\nd) Varahamihira","a"),
("Which scientist discovered the law of electromagnetic induction?\na) Maxwell\nb) Michael Faraday\nc) Ampere\nd) Tesla","b"),
("Which country has the largest proven oil reserves?\na) Russia\nb) Iran\nc) Venezuela\nd) Iraq","c"),
("Which river flows through Khartoum?\na) Amazon\nb) Congo\nc) Niger\nd) Nile","d"),

("Which Indian empire built the Iron Pillar of Delhi?\na) Gupta Empire\nb) Maurya Empire\nc) Mughal Empire\nd) Chola Empire","a"),
("Which scientist proposed the uncertainty principle?\na) Einstein\nb) Werner Heisenberg\nc) Bohr\nd) Planck","b"),
("Which element has the highest atomic number naturally occurring?\na) Uranium\nb) Thorium\nc) Uranium\n d) Radon","c"),
("Which river flows through Vienna?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which Indian state has the largest forest cover?\na) Madhya Pradesh\nb) Arunachal Pradesh\nc) Chhattisgarh\nd) Odisha","a"),
("Which scientist proposed the quantum mechanical model of atom?\na) Rutherford\nb) Erwin Schrödinger\nc) Bohr\nd) Heisenberg","b"),
("Which ocean is the deepest?\na) Atlantic\nb) Indian\nc) Pacific\nd) Arctic","c"),
("Which river flows through Kyiv?\na) Rhine\nb) Danube\nc) Volga\nd) Dnieper","d"),

("Which Indian ruler defeated Seleucus Nicator?\na) Chandragupta Maurya\nb) Ashoka\nc) Bindusara\nd) Harsha","a"),
("Which scientist invented the alternating current system?\na) Edison\nb) Nikola Tesla\nc) Faraday\nd) Maxwell","b"),
("Which planet has the largest volcano in the solar system?\na) Venus\nb) Mercury\nc) Mars\nd) Earth","c"),
("Which river flows through Madrid?\na) Tagus\nb) Loire\nc) Po\nd) Manzanares","d"),

("Which Indian leader gave the slogan 'Do or Die'?\na) Mahatma Gandhi\nb) Nehru\nc) Patel\nd) Bose","a"),
("Which scientist discovered the structure of DNA with Watson?\na) Linus Pauling\nb) Francis Crick\nc) Darwin\nd) Mendel","b"),
("Which country has the most islands in the world?\na) Indonesia\nb) Philippines\nc) Sweden\nd) Norway","c"),
("Which river flows through Hamburg?\na) Rhine\nb) Danube\nc) Seine\nd) Elbe","d"),

("Which Indian state has the capital Dispur?\na) Assam\nb) Meghalaya\nc) Nagaland\nd) Manipur","a"),
("Which scientist developed the wave theory of light?\na) Newton\nb) Christiaan Huygens\nc) Einstein\nd) Planck","b"),
("Which desert is the coldest in the world?\na) Sahara\nb) Gobi\nc) Antarctica\nd) Atacama","c"),
("Which river flows through Bratislava?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which Indian king built the Kailasa temple at Ellora?\na) Krishna I\nb) Ashoka\nc) Harsha\nd) Pulakesin","a"),
("Which scientist discovered the neutron?\na) Rutherford\nb) James Chadwick\nc) Bohr\nd) Thomson","b"),
("Which mountain is the sixth highest in the world?\na) Everest\nb) K2\nc) Cho Oyu\nd) Makalu","c"),
("Which river flows through Baghdad?\na) Amazon\nb) Congo\nc) Niger\nd) Tigris","d"),

("Which Indian ruler founded the Maurya dynasty?\na) Chandragupta Maurya\nb) Ashoka\nc) Bindusara\nd) Harsha","a"),
("Which scientist proposed the Big Bang theory?\na) Einstein\nb) Georges Lemaître\nc) Hawking\nd) Hubble","b")
]
Question_bank8= [
("Which Indian mathematician wrote the book 'Aryabhatiya'?\na) Aryabhata\nb) Brahmagupta\nc) Bhaskara II\nd) Varahamihira","a"),
("Which scientist proposed the expanding universe theory?\na) Einstein\nb) Edwin Hubble\nc) Newton\nd) Galileo","b"),
("Which element has the highest boiling point?\na) Iron\nb) Tungsten\nc) Rhenium\nd) Osmium","c"),
("Which river flows through Baghdad before joining the Euphrates?\na) Jordan\nb) Indus\nc) Nile\nd) Tigris","d"),

("Which dynasty built the Khajuraho temples?\na) Chandela dynasty\nb) Maurya dynasty\nc) Gupta dynasty\nd) Chola dynasty","a"),
("Which scientist discovered the positron?\na) Rutherford\nb) Carl Anderson\nc) Bohr\nd) Planck","b"),
("Which country has the largest natural gas reserves?\na) USA\nb) Iran\nc) Russia\nd) Qatar","c"),
("Which river flows through the city of Prague?\na) Danube\nb) Rhine\nc) Elbe\nd) Vltava","d"),

("Which Indian state has the longest coastline?\na) Gujarat\nb) Tamil Nadu\nc) Andhra Pradesh\nd) Maharashtra","a"),
("Which scientist discovered the nucleus of the atom?\na) Dalton\nb) Ernest Rutherford\nc) Bohr\nd) Thomson","b"),
("Which mountain is the seventh highest in the world?\na) Makalu\nb) Lhotse\nc) Dhaulagiri\nd) Cho Oyu","c"),
("Which river flows through the city of Warsaw?\na) Rhine\nb) Danube\nc) Elbe\nd) Vistula","d"),

("Which Indian king built the Kailasa temple at Ellora?\na) Krishna I\nb) Ashoka\nc) Harsha\nd) Pulakesin","a"),
("Which scientist proposed the wave nature of electrons?\na) Einstein\nb) Louis de Broglie\nc) Bohr\nd) Heisenberg","b"),
("Which desert is the second largest hot desert?\na) Sahara\nb) Arabian\nc) Australian\nd) Kalahari","c"),
("Which river flows through Madrid?\na) Tagus\nb) Loire\nc) Po\nd) Manzanares","d"),

("Which Indian ruler established the Gupta Empire?\na) Chandragupta I\nb) Samudragupta\nc) Skandagupta\nd) Kumaragupta","a"),
("Which scientist developed the uncertainty principle?\na) Planck\nb) Werner Heisenberg\nc) Einstein\nd) Bohr","b"),
("Which ocean is the largest on Earth?\na) Atlantic\nb) Indian\nc) Pacific\nd) Arctic","c"),
("Which river flows through the city of Hamburg?\na) Rhine\nb) Danube\nc) Seine\nd) Elbe","d"),

("Which Indian state has the capital Aizawl?\na) Mizoram\nb) Nagaland\nc) Manipur\nd) Tripura","a"),
("Which scientist discovered cosmic microwave background radiation?\na) Hubble\nb) Arno Penzias\nc) Hawking\nd) Einstein","b"),
("Which planet has the longest day in the solar system?\na) Mercury\nb) Earth\nc) Venus\nd) Mars","c"),
("Which river flows through Bratislava?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which Indian emperor issued rock edicts across India?\na) Ashoka\nb) Akbar\nc) Harsha\nd) Chandragupta","a"),
("Which scientist proposed the Big Bang theory?\na) Einstein\nb) Georges Lemaître\nc) Hubble\nd) Hawking","b"),
("Which mountain is the eighth highest in the world?\na) Makalu\nb) Cho Oyu\nc) Manaslu\nd) Dhaulagiri","c"),
("Which river flows through Belgrade?\na) Rhine\nb) Seine\nc) Elbe\nd) Danube","d"),

("Which Indian ruler built the Sun Temple at Konark?\na) Narasimhadeva I\nb) Ashoka\nc) Samudragupta\nd) Harsha","a"),
("Which scientist discovered radio waves experimentally?\na) Maxwell\nb) Heinrich Hertz\nc) Tesla\nd) Faraday","b")
]
Question_bank9= [
("Which Indian mathematician introduced the concept of zero as a number?\na) Aryabhata\nb) Brahmagupta\nc) Bhaskara I\nd) Varahamihira","a"),
("Which scientist discovered the law of photoelectric effect?\na) Newton\nb) Albert Einstein\nc) Maxwell\nd) Planck","b"),
("Which country has the largest number of active volcanoes?\na) Japan\nb) Chile\nc) Indonesia\nd) USA","c"),
("Which river flows through the city of Kyiv?\na) Rhine\nb) Danube\nc) Volga\nd) Dnieper","d"),

("Which Indian empire built the Ajanta caves?\na) Satavahana\nb) Gupta\nc) Maurya\nd) Chola","a"),
("Which scientist developed the Bohr model of the atom?\na) Rutherford\nb) Niels Bohr\nc) Dalton\nd) Thomson","b"),
("Which planet has the most moons in the solar system?\na) Jupiter\nb) Mars\nc) Saturn\nd) Uranus","c"),
("Which river flows through the city of Vienna?\na) Rhine\nb) Seine\nc) Elbe\nd) Danube","d"),

("Which Indian state has the highest forest cover?\na) Madhya Pradesh\nb) Arunachal Pradesh\nc) Chhattisgarh\nd) Odisha","a"),
("Which scientist discovered the neutron?\na) Rutherford\nb) James Chadwick\nc) Bohr\nd) Thomson","b"),
("Which ocean trench is the deepest in the world?\na) Tonga Trench\nb) Java Trench\nc) Mariana Trench\nd) Philippine Trench","c"),
("Which river flows through the city of Budapest?\na) Rhine\nb) Seine\nc) Volga\nd) Danube","d"),

("Which Indian ruler built the Sanchi Stupa?\na) Ashoka\nb) Akbar\nc) Harsha\nd) Chandragupta","a"),
("Which scientist discovered X-rays?\na) Einstein\nb) Wilhelm Roentgen\nc) Curie\nd) Faraday","b"),
("Which mountain is the ninth highest in the world?\na) Everest\nb) K2\nc) Nanga Parbat\nd) Lhotse","c"),
("Which river flows through Baghdad?\na) Amazon\nb) Congo\nc) Niger\nd) Tigris","d"),

("Which Indian king built the Meenakshi Temple complex?\na) Tirumala Nayaka\nb) Ashoka\nc) Harsha\nd) Krishnadevaraya","a"),
("Which scientist proposed the wave theory of light?\na) Newton\nb) Christiaan Huygens\nc) Einstein\nd) Planck","b"),
("Which desert is the largest cold desert in Asia?\na) Thar\nb) Arabian\nc) Gobi\nd) Kalahari","c"),
("Which river flows through the city of Rome?\na) Seine\nb) Rhine\nc) Danube\nd) Tiber","d"),

("Which Indian state has the capital Kohima?\na) Nagaland\nb) Mizoram\nc) Manipur\nd) Tripura","a"),
("Which scientist discovered electromagnetic induction?\na) Tesla\nb) Michael Faraday\nc) Maxwell\nd) Ampere","b"),
("Which planet has the fastest rotation?\na) Earth\nb) Mars\nc) Jupiter\nd) Venus","c"),
("Which river flows through Hamburg?\na) Rhine\nb) Danube\nc) Seine\nd) Elbe","d"),

("Which Indian emperor built the Iron Pillar of Delhi?\na) Chandragupta II\nb) Ashoka\nc) Harsha\nd) Samudragupta","a"),
("Which scientist proposed the uncertainty principle?\na) Einstein\nb) Werner Heisenberg\nc) Bohr\nd) Planck","b"),
("Which mountain is the tenth highest in the world?\na) Everest\nb) K2\nc) Annapurna\nd) Kangchenjunga","c"),
("Which river flows through Bratislava?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which Indian ruler founded the Gupta dynasty?\na) Sri Gupta\nb) Samudragupta\nc) Chandragupta II\nd) Kumaragupta","a"),
("Which scientist discovered the proton?\na) Thomson\nb) Ernest Rutherford\nc) Bohr\nd) Chadwick","b")
]
Question_bank10= [
("Which Indian astronomer wrote 'Surya Siddhanta'?\na) Aryabhata\nb) Varahamihira\nc) Brahmagupta\nd) Bhaskara","a"),
("Which scientist discovered the cosmic microwave background radiation?\na) Hubble\nb) Arno Penzias\nc) Einstein\nd) Hawking","b"),
("Which element has the highest atomic number naturally occurring?\na) Radon\nb) Thorium\nc) Uranium\nd) Plutonium","c"),
("Which river flows through Khartoum?\na) Amazon\nb) Congo\nc) Niger\nd) Nile","d"),

("Which Indian king defeated Seleucus Nicator?\na) Chandragupta Maurya\nb) Ashoka\nc) Bindusara\nd) Harsha","a"),
("Which scientist proposed the Big Bang theory?\na) Einstein\nb) Georges Lemaître\nc) Hubble\nd) Hawking","b"),
("Which country has the largest desert area?\na) China\nb) USA\nc) Australia\nd) Saudi Arabia","c"),
("Which river flows through Belgrade?\na) Rhine\nb) Seine\nc) Elbe\nd) Danube","d"),

("Which Indian temple is known as the Black Pagoda?\na) Konark Sun Temple\nb) Jagannath Temple\nc) Lingaraja Temple\nd) Brihadeeswara Temple","a"),
("Which scientist developed quantum mechanics?\na) Einstein\nb) Max Planck\nc) Newton\nd) Faraday","b"),
("Which planet has the strongest gravity?\na) Earth\nb) Mars\nc) Jupiter\nd) Venus","c"),
("Which river flows through Paris?\na) Thames\nb) Rhine\nc) Danube\nd) Seine","d"),

("Which Indian leader gave the slogan 'Jai Hind'?\na) Subhas Chandra Bose\nb) Gandhi\nc) Nehru\nd) Patel","a"),
("Which scientist invented the AC electrical system?\na) Edison\nb) Nikola Tesla\nc) Faraday\nd) Maxwell","b"),
("Which ocean is the smallest?\na) Pacific\nb) Atlantic\nc) Arctic\nd) Indian","c"),
("Which river flows through Madrid?\na) Tagus\nb) Loire\nc) Po\nd) Manzanares","d"),

("Which Indian state has the capital Gangtok?\na) Sikkim\nb) Assam\nc) Meghalaya\nd) Manipur","a"),
("Which scientist proposed the atomic theory?\na) Rutherford\nb) John Dalton\nc) Bohr\nd) Thomson","b"),
("Which mountain is the eleventh highest in the world?\na) Everest\nb) K2\nc) Gasherbrum I\nd) Makalu","c"),
("Which river flows through Warsaw?\na) Rhine\nb) Danube\nc) Elbe\nd) Vistula","d"),

("Which Indian ruler built the Brihadeeswara Temple?\na) Rajaraja Chola I\nb) Ashoka\nc) Harsha\nd) Samudragupta","a"),
("Which scientist discovered the electron?\na) Rutherford\nb) J J Thomson\nc) Bohr\nd) Dalton","b"),
("Which desert is the driest in the world?\na) Sahara\nb) Gobi\nc) Atacama\nd) Arabian","c"),
("Which river flows through Vienna?\na) Rhine\nb) Elbe\nc) Seine\nd) Danube","d"),

("Which Indian empire built Hampi?\na) Vijayanagara Empire\nb) Maurya Empire\nc) Gupta Empire\nd) Chola Empire","a"),
("Which scientist proposed the wave nature of electrons?\na) Einstein\nb) Louis de Broglie\nc) Bohr\nd) Heisenberg","b"),
("Which mountain is the twelfth highest in the world?\na) Everest\nb) K2\nc) Broad Peak\nd) Lhotse","c"),
("Which river flows through Baghdad?\na) Amazon\nb) Congo\nc) Niger\nd) Tigris","d")
]
Question_bank11= [
("Which Indian city is known as the City of Lakes?\na) Udaipur\nb) Bhopal\nc) Srinagar\nd) Nainital","a"),
("Who invented the telephone?\na) Edison\nb) Alexander Graham Bell\nc) Tesla\nd) Marconi","b"),
("Which planet is known as Earth's twin?\na) Mars\nb) Mercury\nc) Venus\nd) Saturn","c"),
("Which Indian monument is located in Delhi?\na) Taj Mahal\nb) Charminar\nc) Gateway of India\nd) Red Fort","d"),

("Which river is the longest in India?\na) Ganga\nb) Yamuna\nc) Brahmaputra\nd) Godavari","a"),
("Which scientist discovered gravity?\na) Galileo\nb) Isaac Newton\nc) Einstein\nd) Faraday","b"),
("Which country has the Great Wall?\na) Japan\nb) Korea\nc) China\nd) Mongolia","c"),
("Which desert is the largest hot desert?\na) Thar\nb) Gobi\nc) Kalahari\nd) Sahara","d"),

("Which Indian state is famous for tea gardens?\na) Assam\nb) Gujarat\nc) Punjab\nd) Haryana","a"),
("Which gas is most abundant in Earth's atmosphere?\na) Oxygen\nb) Nitrogen\nc) Carbon dioxide\nd) Hydrogen","b"),
("Which mountain range contains Mount Everest?\na) Alps\nb) Andes\nc) Himalayas\nd) Rockies","c"),
("Which river flows through Paris?\na) Thames\nb) Rhine\nc) Danube\nd) Seine","d"),

("Which animal is the national animal of India?\na) Tiger\nb) Lion\nc) Leopard\nd) Elephant","a"),
("Which metal is mainly used in electrical wiring?\na) Aluminium\nb) Copper\nc) Iron\nd) Zinc","b"),
("Which country hosted the 2008 Olympics?\na) Japan\nb) Brazil\nc) China\nd) Greece","c"),
("Which city is famous for the Statue of Liberty?\na) Washington\nb) Chicago\nc) Boston\nd) New York","d"),

("Which organ produces insulin?\na) Pancreas\nb) Liver\nc) Kidney\nd) Stomach","a"),
("Which Indian freedom fighter founded Azad Hind Fauj?\na) Bhagat Singh\nb) Subhas Chandra Bose\nc) Gandhi\nd) Patel","b"),
("Which continent has the Amazon rainforest?\na) Africa\nb) Asia\nc) South America\nd) Australia","c"),
("Which river flows through Rome?\na) Seine\nb) Rhine\nc) Danube\nd) Tiber","d"),

("Which country is known as the Land of Rising Sun?\na) Japan\nb) China\nc) Thailand\nd) Korea","a"),
("Which vitamin prevents scurvy?\na) Vitamin A\nb) Vitamin C\nc) Vitamin D\nd) Vitamin B","b"),
("Which ocean is between Africa and Australia?\na) Pacific\nb) Atlantic\nc) Indian\n d) Arctic","c"),
("Which city hosted the first modern Olympics?\na) Paris\nb) London\nc) Rome\nd) Athens","d"),

("Which Indian state has the capital Chennai?\na) Tamil Nadu\nb) Kerala\nc) Karnataka\nd) Andhra Pradesh","a"),
("Which scientist discovered radioactivity?\na) Rutherford\nb) Henri Becquerel\nc) Einstein\nd) Curie","b"),
("Which animal is the tallest in the world?\na) Elephant\nb) Horse\nc) Giraffe\nd) Camel","c"),
("Which river is called the lifeline of Egypt?\na) Amazon\nb) Congo\nc) Niger\nd) Nile","d"),

("Which metal is used to make coins commonly?\na) Nickel\nb) Silver\nc) Aluminium\nd) Copper","a"),
("Which country is famous for tulips?\na) Belgium\nb) Netherlands\nc) Denmark\nd) Austria","b")
]
Question_bank12= [

("Which Indian emperor built the Grand Trunk Road between Peshawar and Kolkata?\na) Sher Shah Suri\nb) Akbar\nc) Chandragupta Maurya\nd) Ashoka","a"),

("Who discovered the nucleus of the atom?\na) J. J. Thomson\nb) Ernest Rutherford\nc) James Chadwick\nd) Niels Bohr","b"),

("Which country is the largest producer of coffee in the world?\na) Vietnam\nb) Colombia\nc) Brazil\nd) Ethiopia","c"),

("Which Indian state has the largest forest area?\na) Arunachal Pradesh\nb) Chhattisgarh\nc) Maharashtra\nd) Madhya Pradesh","d"),

("Which scientist discovered radioactivity?\na) Henri Becquerel\nb) Marie Curie\nc) Pierre Curie\nd) Ernest Rutherford","a"),

("Who developed the polio vaccine used worldwide?\na) Louis Pasteur\nb) Jonas Salk\nc) Alexander Fleming\nd) Robert Koch","b"),

("Which river is the longest in South America?\na) Paraná\nb) Orinoco\nc) Amazon\nd) Magdalena","c"),

("Which city hosted the 2012 Summer Olympics?\na) Beijing\nb) Tokyo\nc) Rio de Janeiro\nd) London","d"),

("Which Indian scientist won the Nobel Prize in Physics in 1930?\na) C. V. Raman\nb) S. N. Bose\nc) Homi Bhabha\nd) Vikram Sarabhai","a"),

("Who wrote the novel '1984'?\na) Aldous Huxley\nb) George Orwell\nc) J. R. R. Tolkien\nd) Ernest Hemingway","b"),

("Which country has the largest population in the world as of 2023?\na) USA\nb) Indonesia\nc) India\nd) China","c"),

("Which Mughal emperor commissioned the Peacock Throne?\na) Aurangzeb\nb) Akbar\nc) Jahangir\nd) Shah Jahan","d"),

("Which is the largest island in the world?\na) Greenland\nb) Madagascar\nc) Borneo\nd) New Guinea","a"),

("Who invented the electric motor?\na) Michael Faraday\nb) Nikola Tesla\nc) Thomas Edison\nd) Alessandro Volta","b"),

("Which mountain range separates Europe and Asia?\na) Alps\nb) Caucasus\nc) Ural Mountains\nd) Pyrenees","c"),

("Which Indian city is known as the 'Garden City of India'?\na) Mysuru\nb) Ooty\nc) Pune\nd) Bengaluru","d"),

("Which planet is known for having the most moons?\na) Saturn\nb) Jupiter\nc) Uranus\nd) Neptune","a"),

("Who discovered insulin?\na) Alexander Fleming\nb) Frederick Banting\nc) Louis Pasteur\nd) Robert Koch","b"),

("Which ocean is the deepest in the world?\na) Atlantic Ocean\nb) Indian Ocean\nc) Pacific Ocean\nd) Arctic Ocean","c"),

("Which Indian state has the capital city Shillong?\na) Nagaland\nb) Mizoram\nc) Tripura\nd) Meghalaya","d"),

("Which Indian freedom movement began in 1942?\na) Quit India Movement\nb) Non-Cooperation Movement\nc) Civil Disobedience Movement\nd) Swadeshi Movement","a"),

("Who wrote 'Pride and Prejudice'?\na) Emily Brontë\nb) Jane Austen\nc) Charlotte Brontë\nd) Virginia Woolf","b"),

("Which continent has the Sahara Desert?\na) Asia\nb) Australia\nc) Africa\nd) South America","c"),

("Which Indian monument is known as the 'Symbol of Love'?\na) Red Fort\nb) Qutub Minar\nc) Gateway of India\nd) Taj Mahal","d"),

("Which chemical element has the symbol 'Fe'?\na) Iron\nb) Fluorine\nc) Francium\nd) Fermium","a"),

("Who discovered the law of electromagnetic induction?\na) James Maxwell\nb) Michael Faraday\nc) Nikola Tesla\nd) Heinrich Hertz","b"),

("Which is the largest desert in the world?\na) Sahara\nb) Arabian\nc) Antarctica\nd) Gobi","c"),

("Which Indian state is known as the 'Land of Five Rivers'?\na) Haryana\nb) Himachal Pradesh\nc) Rajasthan\nd) Punjab","d"),

("Which physicist proposed the theory of relativity?\na) Albert Einstein\nb) Isaac Newton\nc) Max Planck\nd) Niels Bohr","a"),

("Who painted the Mona Lisa?\na) Michelangelo\nb) Leonardo da Vinci\nc) Pablo Picasso\nd) Vincent van Gogh","b")

]
Question_bank13= [

("Which Indian king defeated Muhammad Ghori in the First Battle of Tarain in 1191?\na) Prithviraj Chauhan\nb) Rana Sanga\nc) Maharana Pratap\nd) Harsha","a"),

("Who was the first person to travel into space?\na) Neil Armstrong\nb) Yuri Gagarin\nc) Buzz Aldrin\nd) Alan Shepard","b"),

("Which strait separates Asia and North America?\na) Strait of Gibraltar\nb) Strait of Hormuz\nc) Bering Strait\nd) Malacca Strait","c"),

("Which Indian state has the largest area?\na) Madhya Pradesh\nb) Uttar Pradesh\nc) Maharashtra\nd) Rajasthan","d"),

("Which scientist proposed the three laws of planetary motion?\na) Johannes Kepler\nb) Galileo Galilei\nc) Isaac Newton\nd) Tycho Brahe","a"),

("Who invented the steam engine used in early locomotives?\na) Thomas Newcomen\nb) James Watt\nc) George Stephenson\nd) Richard Trevithick","b"),

("Which country is the largest producer of natural rubber?\na) Indonesia\nb) Thailand\nc) Thailand\nd) Malaysia","c"),

("Which city is the capital of Canada?\na) Toronto\nb) Vancouver\nc) Montreal\nd) Ottawa","d"),

("Which Indian mathematician is known for contributions to number theory and infinite series?\na) Srinivasa Ramanujan\nb) Aryabhata\nc) Brahmagupta\nd) Bhaskara II","a"),

("Who wrote the novel 'War and Peace'?\na) Fyodor Dostoevsky\nb) Leo Tolstoy\nc) Anton Chekhov\nd) Ivan Turgenev","b"),

("Which country has the largest number of volcanoes?\na) USA\nb) Japan\nc) Indonesia\nd) Philippines","c"),

("Which Mughal emperor introduced the Mansabdari system?\na) Babur\nb) Jahangir\nc) Aurangzeb\nd) Akbar","d"),

("Which element has the chemical symbol 'Au'?\na) Gold\nb) Silver\nc) Aluminium\nd) Argon","a"),

("Who discovered the circulation of blood in the human body?\na) Hippocrates\nb) William Harvey\nc) Galen\nd) Andreas Vesalius","b"),

("Which desert is the largest cold desert in the world?\na) Gobi\nb) Patagonia\nc) Antarctica\nd) Arctic","c"),

("Which Indian city hosted the 1982 Asian Games?\na) Mumbai\nb) Kolkata\nc) Chennai\nd) New Delhi","d"),

("Which Indian freedom fighter led the Salt March in 1930?\na) Mahatma Gandhi\nb) Jawaharlal Nehru\nc) Vallabhbhai Patel\nd) Subhas Chandra Bose","a"),

("Who discovered the proton?\na) Niels Bohr\nb) Ernest Rutherford\nc) J. J. Thomson\nd) James Chadwick","b"),

("Which ocean surrounds the Maldives?\na) Pacific Ocean\nb) Atlantic Ocean\nc) Indian Ocean\nd) Arctic Ocean","c"),

("Which Indian state has the capital Panaji?\na) Kerala\nb) Karnataka\nc) Maharashtra\nd) Goa","d"),

("Which Indian classical dance form originated in Kerala?\na) Kathakali\nb) Bharatanatyam\nc) Kuchipudi\nd) Odissi","a"),

("Who painted the 'Starry Night'?\na) Pablo Picasso\nb) Vincent van Gogh\nc) Claude Monet\nd) Salvador Dalí","b"),

("Which country is known as the 'Land of a Thousand Lakes'?\na) Norway\nb) Sweden\nc) Finland\nd) Iceland","c"),

("Which monument was built by Emperor Shah Jahan in Delhi?\na) Taj Mahal\nb) Humayun's Tomb\nc) Jama Masjid\nd) Red Fort","d"),

("Which gas is used in balloons to make them float safely?\na) Helium\nb) Hydrogen\nc) Nitrogen\nd) Oxygen","a"),

("Who discovered the structure of DNA along with James Watson?\na) Francis Crick\nb) Linus Pauling\nc) Maurice Wilkins\nd) Rosalind Franklin","b"),

("Which is the largest lake in the world by surface area?\na) Lake Superior\nb) Lake Victoria\nc) Caspian Sea\nd) Lake Baikal","c"),

("Which Indian state is known as the 'Spice Garden of India'?\na) Tamil Nadu\nb) Karnataka\nc) Andhra Pradesh\nd) Kerala","d"),

("Which scientist formulated the laws of motion?\na) Isaac Newton\nb) Albert Einstein\nc) Galileo Galilei\nd) Johannes Kepler","a"),

("Who wrote the play 'Macbeth'?\na) George Bernard Shaw\nb) William Shakespeare\nc) Christopher Marlowe\nd) Oscar Wilde","b")

]
Question_bank14= [

("Which Indian emperor built the Iron Pillar of Delhi during the Gupta period?\na) Chandragupta II\nb) Samudragupta\nc) Skandagupta\nd) Kumaragupta","a"),

("Who was the first woman to go to space?\na) Sally Ride\nb) Valentina Tereshkova\nc) Kalpana Chawla\nd) Svetlana Savitskaya","b"),

("Which strait connects the Mediterranean Sea to the Atlantic Ocean?\na) Bosporus\nb) Hormuz\nc) Malacca\nd) Gibraltar","d"),

("Which Indian state shares the longest international border?\na) Punjab\nb) Assam\nc) Rajasthan\nd) West Bengal","c"),

("Which physicist developed the quantum theory of radiation?\na) Max Planck\nb) Niels Bohr\nc) Albert Einstein\nd) Werner Heisenberg","a"),

("Who wrote the famous book 'The Prince'?\na) Aristotle\nb) Niccolò Machiavelli\nc) Plato\nd) Thomas Hobbes","b"),

("Which country has the largest freshwater lake by surface area?\na) Canada\nb) Russia\nc) USA\nd) Brazil","c"),

("Which Indian monument is known as the 'Victory Tower'?\na) Charminar\nb) Qutub Minar\nc) Jama Masjid\nd) Vijay Stambh","d"),

("Which Indian mathematician calculated the value of pi accurately in ancient times?\na) Aryabhata\nb) Bhaskara II\nc) Brahmagupta\nd) Varahamihira","a"),

("Who discovered the vaccine for rabies?\na) Edward Jenner\nb) Louis Pasteur\nc) Robert Koch\nd) Alexander Fleming","b"),

("Which country has the largest number of natural lakes?\na) Finland\nb) Sweden\nc) Canada\nd) Norway","c"),

("Which Mughal emperor shifted the capital from Agra to Delhi and built Shahjahanabad?\na) Akbar\nb) Jahangir\nc) Aurangzeb\nd) Shah Jahan","d"),

("Which element has atomic number 79?\na) Gold\nb) Silver\nc) Platinum\nd) Mercury","a"),

("Who wrote the famous novel 'The Old Man and the Sea'?\na) Mark Twain\nb) Ernest Hemingway\nc) John Steinbeck\nd) F. Scott Fitzgerald","b"),

("Which is the longest river in Africa?\na) Congo\nb) Niger\nc) Nile\nd) Zambezi","c"),

("Which city hosted the 2004 Summer Olympics?\na) Sydney\nb) Beijing\nc) Athens\nd) Athens","d"),

("Which Indian leader founded the Indian National Army (INA)?\na) Subhas Chandra Bose\nb) Bhagat Singh\nc) Rajguru\nd) Lala Lajpat Rai","a"),

("Who developed the theory of general relativity?\na) Isaac Newton\nb) Albert Einstein\nc) Niels Bohr\nd) Max Planck","b"),

("Which continent has the largest desert in the world?\na) Asia\nb) Africa\nc) Antarctica\nd) Australia","c"),

("Which Indian state has the capital city Dispur?\na) Meghalaya\nb) Nagaland\nc) Mizoram\nd) Assam","d"),

("Which Indian king built the Brihadeeswara Temple at Thanjavur?\na) Rajaraja Chola I\nb) Rajendra Chola\nc) Karikala Chola\nd) Kulothunga Chola","a"),

("Who painted the famous artwork 'The Last Supper'?\na) Michelangelo\nb) Leonardo da Vinci\nc) Raphael\nd) Donatello","b"),

("Which country is the world's largest producer of rice?\na) India\nb) Indonesia\nc) China\nd) Thailand","c"),

("Which monument in India is called the 'Lotus Temple'?\na) Akshardham\nb) ISKCON Temple\nc) Birla Mandir\nd) Baháʼí House of Worship","d"),

("Which chemical element has the symbol 'K'?\na) Potassium\nb) Krypton\nc) Calcium\nd) Nickel","a"),

("Who discovered the planet Uranus?\na) Galileo\nb) William Herschel\nc) Johannes Kepler\nd) Tycho Brahe","b"),

("Which sea lies between Africa and the Arabian Peninsula?\na) Mediterranean Sea\nb) Black Sea\nc) Red Sea\nd) Caspian Sea","c"),

("Which Indian state is known as the 'Land of Festivals'?\na) Kerala\nb) Assam\nc) Nagaland\nd) Sikkim","b"),

("Which scientist is known for the discovery of electromagnetic waves?\na) Heinrich Hertz\nb) James Maxwell\nc) Nikola Tesla\nd) Michael Faraday","a"),

("Who wrote the epic poem 'Paradise Lost'?\na) William Wordsworth\nb) John Milton\nc) Geoffrey Chaucer\nd) T. S. Eliot","b")

]
Question_bank15= [

("Which Gupta ruler is associated with the title 'Vikramaditya'?\na) Chandragupta II\nb) Samudragupta\nc) Skandagupta\nd) Kumaragupta","a"),

("Who developed the uncertainty principle in quantum mechanics?\na) Max Planck\nb) Werner Heisenberg\nc) Niels Bohr\nd) Erwin Schrödinger","b"),

("Which country contains the world's largest coral reef system?\na) Indonesia\nb) Philippines\nc) Australia\nd) Fiji","c"),

("Which Indian city is home to the headquarters of the Reserve Bank of India?\na) Delhi\nb) Kolkata\nc) Chennai\nd) Mumbai","d"),

("Which scientist proposed the heliocentric model of the solar system in 1543?\na) Nicolaus Copernicus\nb) Galileo Galilei\nc) Johannes Kepler\nd) Tycho Brahe","a"),

("Who wrote the novel 'Crime and Punishment'?\na) Leo Tolstoy\nb) Fyodor Dostoevsky\nc) Anton Chekhov\nd) Ivan Turgenev","b"),

("Which country is the largest producer of coffee in the world?\na) Vietnam\nb) Colombia\nc) Brazil\nd) Ethiopia","c"),

("Which Mughal emperor built the Peacock Throne?\na) Akbar\nb) Jahangir\nc) Aurangzeb\nd) Shah Jahan","d"),

("Which Indian mathematician wrote the book 'Aryabhatiya'?\na) Aryabhata\nb) Brahmagupta\nc) Bhaskara I\nd) Varahamihira","a"),

("Who discovered penicillin in 1928?\na) Louis Pasteur\nb) Alexander Fleming\nc) Robert Koch\nd) Edward Jenner","b"),

("Which desert is the largest hot desert in the Southern Hemisphere?\na) Gobi\nb) Arabian\nc) Kalahari\nd) Atacama","c"),

("Which Indian state has the longest coastline?\na) Tamil Nadu\nb) Andhra Pradesh\nc) Kerala\nd) Gujarat","d"),

("Which physicist formulated the theory of special relativity?\na) Albert Einstein\nb) Isaac Newton\nc) Max Planck\nd) Niels Bohr","a"),

("Who composed the opera 'The Magic Flute'?\na) Beethoven\nb) Wolfgang Amadeus Mozart\nc) Bach\nd) Haydn","b"),

("Which country has the largest population in the world?\na) India\nb) USA\nc) China\nd) Indonesia","c"),

("Which Indian monument was built by Sher Shah Suri in Delhi?\na) Red Fort\nb) Humayun’s Tomb\nc) Purana Qila\nd) Qila-i-Kuhna Mosque","d"),

("Which Indian river originates from the Gangotri Glacier?\na) Ganga\nb) Yamuna\nc) Brahmaputra\nd) Godavari","a"),

("Who discovered the neutron?\na) Ernest Rutherford\nb) James Chadwick\nc) Niels Bohr\nd) Enrico Fermi","b"),

("Which continent contains the Sahara Desert?\na) Asia\nb) Europe\nc) Africa\nd) Australia","c"),

("Which Indian state has the capital city Gangtok?\na) Arunachal Pradesh\nb) Meghalaya\nc) Manipur\nd) Sikkim","d"),

("Which Indian emperor issued the famous rock edicts?\na) Ashoka\nb) Chandragupta Maurya\nc) Bindusara\nd) Harsha","a"),

("Who wrote the play 'Hamlet'?\na) Christopher Marlowe\nb) William Shakespeare\nc) Ben Jonson\nd) John Webster","b"),

("Which country is the largest exporter of crude oil?\na) Russia\nb) USA\nc) Saudi Arabia\nd) Iran","c"),

("Which monument in India is also known as 'Buland Darwaza'?\na) Taj Mahal\nb) Red Fort\nc) Jama Masjid\nd) Fatehpur Sikri Gate","d"),

("Which element has the chemical symbol 'Na'?\na) Sodium\nb) Nitrogen\nc) Nickel\nd) Neon","a"),

("Who discovered the laws of inheritance in genetics?\na) Charles Darwin\nb) Gregor Mendel\nc) Watson\nd) Crick","b"),

("Which ocean is the largest on Earth?\na) Atlantic\nb) Indian\nc) Pacific\nd) Arctic","c"),

("Which Indian state is known as the 'Land of Five Rivers'?\na) Haryana\nb) Punjab\nc) Himachal Pradesh\nd) Uttarakhand","b"),

("Which scientist is known as the father of modern chemistry?\na) Antoine Lavoisier\nb) Dmitri Mendeleev\nc) John Dalton\nd) Robert Boyle","a"),

("Who wrote the novel '1984'?\na) Aldous Huxley\nb) George Orwell\nc) Ray Bradbury\nd) H. G. Wells","b")

]
Question_bank16= [

("Which ancient Indian university was destroyed by Bakhtiyar Khilji around 1193 CE?\na) Nalanda\nb) Takshashila\nc) Vikramashila\nd) Vallabhi","a"),

("Who formulated the wave equation in quantum mechanics?\na) Max Planck\nb) Erwin Schrödinger\nc) Werner Heisenberg\nd) Paul Dirac","b"),

("Which country has the world's largest proven oil reserves?\na) Saudi Arabia\nb) Iran\nc) Venezuela\nd) Russia","c"),

("Which Indian monument was originally built by Qutb-ud-din Aibak and completed by Iltutmish?\na) Alai Darwaza\nb) Quwwat-ul-Islam Mosque\nc) Tughlaqabad Fort\nd) Qutub Minar","d"),

("Which mathematician proved Fermat's Last Theorem in 1994?\na) Andrew Wiles\nb) John Nash\nc) Terence Tao\nd) Kurt Gödel","a"),

("Who discovered the electron in 1897?\na) Ernest Rutherford\nb) J. J. Thomson\nc) Niels Bohr\nd) James Chadwick","b"),

("Which country has the largest rainforest area in the world?\na) Indonesia\nb) Congo\nc) Brazil\nd) Peru","c"),

("Which Mughal emperor commissioned the building of the Moti Masjid inside Red Fort?\na) Akbar\nb) Jahangir\nc) Shah Jahan\nd) Aurangzeb","d"),

("Which Indian mathematician developed the concept of zero as a number?\na) Brahmagupta\nb) Aryabhata\nc) Bhaskara II\nd) Varahamihira","a"),

("Who wrote the philosophical work 'Thus Spoke Zarathustra'?\na) Immanuel Kant\nb) Friedrich Nietzsche\nc) Karl Marx\nd) Arthur Schopenhauer","b"),

("Which country is the largest exporter of natural gas?\na) USA\nb) Iran\nc) Russia\nd) Qatar","c"),

("Which Indian ruler built the city of Fatehpur Sikri?\na) Babur\nb) Humayun\nc) Jahangir\nd) Akbar","d"),

("Which scientist introduced the concept of entropy in thermodynamics?\na) Rudolf Clausius\nb) James Joule\nc) Lord Kelvin\nd) Ludwig Boltzmann","a"),

("Who composed the symphony 'Eroica'?\na) Mozart\nb) Ludwig van Beethoven\nc) Bach\nd) Chopin","b"),

("Which desert is the driest place on Earth?\na) Sahara\nb) Gobi\nc) Atacama\nd) Kalahari","c"),

("Which Indian state was created in 2014 after being separated from Andhra Pradesh?\na) Jharkhand\nb) Uttarakhand\nc) Chhattisgarh\nd) Telangana","d"),

("Which Mauryan ruler converted to Buddhism after the Kalinga War?\na) Ashoka\nb) Chandragupta Maurya\nc) Bindusara\nd) Dasharatha","a"),

("Who discovered radio waves experimentally?\na) Nikola Tesla\nb) Heinrich Hertz\nc) James Maxwell\nd) Michael Faraday","b"),

("Which continent contains the Amazon River basin?\na) Africa\nb) Asia\nc) South America\nd) Australia","c"),

("Which Indian state has the capital city Kohima?\na) Manipur\nb) Mizoram\nc) Tripura\nd) Nagaland","d"),

("Which Indian scientist is known as the father of India's nuclear program?\na) Homi J. Bhabha\nb) Vikram Sarabhai\nc) A. P. J. Abdul Kalam\nd) Meghnad Saha","a"),

("Who wrote the epic poem 'The Divine Comedy'?\na) Homer\nb) Dante Alighieri\nc) Virgil\nd) Ovid","b"),

("Which country is the largest producer of lithium in the world?\na) Argentina\nb) Australia\nc) Chile\nd) Bolivia","c"),

("Which monument in India was built by Emperor Humayun's widow Haji Begum?\na) Red Fort\nb) Jama Masjid\nc) Safdarjung Tomb\nd) Humayun's Tomb","d"),

("Which element has the highest melting point among pure metals?\na) Tungsten\nb) Iron\nc) Copper\nd) Nickel","a"),

("Who developed the theory of evolution by natural selection?\na) Alfred Wallace\nb) Charles Darwin\nc) Jean Lamarck\nd) Thomas Huxley","b"),

("Which ocean trench is the deepest point on Earth?\na) Puerto Rico Trench\nb) Java Trench\nc) Mariana Trench\nd) Tonga Trench","c"),

("Which Indian state is known as the 'Land of the Thunder Dragon'?\na) Sikkim\nb) Bhutan\nc) Arunachal Pradesh\nd) Assam","b"),

("Which chemist created the periodic table in 1869?\na) Dmitri Mendeleev\nb) Antoine Lavoisier\nc) John Dalton\nd) Robert Boyle","a"),

("Who wrote the novel 'The Brothers Karamazov'?\na) Leo Tolstoy\nb) Fyodor Dostoevsky\nc) Anton Chekhov\nd) Ivan Turgenev","b")

]

# CHECK TO START GAME

# invalid detection system:
while True:
    playing = input('DO YOU WANT TO START THE GAME, "KAUN BANEGA CROREPATI" (yes/no): ').upper().strip(' ')
    if playing in ('YES', 'NO'):
        break
    else:
        print('Invalid Input')

# Yes
if playing == 'YES':
    PLAYING = True
    print((' ~~~LETS PLAY KAUN BANEGA CROREPATI!!!~~~').center(500))

# No
else:
    PLAYING = False
    print('Thank You! Have a nice day Ahead.')


# INITIALISING VARIABLES
q_no = 0
money = 0
lifelines50_50 = 2
lifelines_Audience_poll = 2

# MONEY CALCULATOR

def money_counter(q_no):
        if q_no == 0:
            return 0
        elif q_no == 1:
            return 5000
        elif q_no == 2:
            return 10000
        elif q_no == 3:
            return 15000
        elif q_no == 4:
            return 20000
        elif q_no == 5:
            return 25000
        elif q_no == 6:
            return 50000
        elif q_no == 7:
            return 100000
        elif q_no == 8:
            return 200000
        elif q_no == 9:
            return 300000
        elif q_no == 10:
            return 500000
        elif q_no == 11:
            return 750000
        elif q_no == 12:
            return 1250000
        elif q_no == 13:
            return 2500000
        elif q_no == 14:
            return 5000000
        elif q_no == 15:
            return 10000000
        elif q_no == 16:
            return 70000000

# PLAYING LOOP
while PLAYING:
    
    # QUESTION ASSIGNMENT & CORRECT LEVEL ASSIGNMENT & CORRECT OPTION ASSIGNMENT

    if q_no == 0:
        question,correct_ans = random.choice(Question_bank1)
    elif q_no == 1:
        question,correct_ans = random.choice(Question_bank2)
    elif q_no == 2:
        question,correct_ans = random.choice(Question_bank3)
    elif q_no == 3:
        question,correct_ans = random.choice(Question_bank4)
    elif q_no == 4:
        question,correct_ans = random.choice(Question_bank5)
    elif q_no == 5:
        question,correct_ans = random.choice(Question_bank6)
    elif q_no == 6:
        question,correct_ans = random.choice(Question_bank7)
    elif q_no == 7:
        question,correct_ans = random.choice(Question_bank8)
    elif q_no == 8:
        question,correct_ans = random.choice(Question_bank9)
    elif q_no == 9:
        question,correct_ans = random.choice(Question_bank10)
    elif q_no == 10:
        question,correct_ans = random.choice(Question_bank11)
    elif q_no == 11:
        question,correct_ans = random.choice(Question_bank12)
    elif q_no == 12:
        question,correct_ans = random.choice(Question_bank13)
    elif q_no == 13:
        question,correct_ans = random.choice(Question_bank14)
    elif q_no == 14:
        question,correct_ans = random.choice(Question_bank15)
    elif q_no == 15:
        question,correct_ans = random.choice(Question_bank16)
        
    
    # Question printer
    
    time.sleep(1)
    print(f'\nQ.{q_no + 1} for ₹{money_counter(q_no + 1)}: {question}')
    
    # User Answer
    start = time.time()
    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit, type (50) to use 50-50 lifeline or type (AP) to use Audience Poll: ').strip().lower()

    # ANSWER VERIFICATION
    
    # Invalid detection system:
    while True:
        if user_ans in ['a','b','c','d','q','50','ap']:
            break
        else:
            print('Invalid Input')
            user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit, type (50) to use 50-50 lifeline or type (AP) to use Audience Poll: ').strip().lower()

    # Quit
    if user_ans == 'q':
        print('You have quitted the game')
        print('You will take ₹',money,'home')
    
    # Correct
    elif user_ans == correct_ans.lower():
        q_no = q_no + 1
        
        money = money_counter(q_no)
        print('Correct Answer!')
        if q_no != 16:
            print('\n','YOU HAVE','₹', money ,'\n')
            print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
            print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
            print('Next Question: \n')
            
        else:
            print('YOU ARE THE WINNER!!!')
            print('SEVEN CRORES!!!!')
            PLAYING = False
        
    # Incorrect
    elif user_ans in ['a','b','c','d']:
        print('Wrong Answer! You lost. Better Luck Next Time.')
        if q_no>=12:
            money = 1250000
        elif q_no>=10:
            money = 500000
        elif q_no>=5:
            money = 25000
        else:
            money = 0
        print('You will take ₹',money,'home')

    # Lifeline 50-50
    elif user_ans == '50':
        if lifelines50_50 > 0:
            if q_no < 16:
                print('Lifeline Activated!')
                lifelines50_50 = lifelines50_50 - 1
                options_except_correct = ['a','b','c','d']
                options_except_correct.remove(correct_ans.lower())
                remove_options1 = random.choice(options_except_correct)
                options_except_correct.remove(remove_options1)
                remove_options2 = random.choice(options_except_correct)
                options_left = ['a','b','c','d']
                options_left.remove(remove_options1)
                options_left.remove(remove_options2)
               
                print(f'Options {remove_options1.upper()} and {remove_options2.upper()} are wrong. The correct answer is in ({options_left[0].upper()}, {options_left[1].upper()})')
                user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                while True:
                    if user_ans in ['a','b','c','d','q']:
                        break
                    else:
                        print('Invalid Input')
                        user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                # Quit
                if user_ans == 'q':
                    print('You have quitted the game')
                    print('You will take ₹',money,'home')
                

                # Correct
                elif user_ans == correct_ans.lower():
                    q_no = q_no + 1
        
                    money = money_counter(q_no)
                    print('Correct Answer!')
                    if q_no != 16:
                        print('\n','YOU HAVE','₹', money ,'\n')
                        print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                        print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                        print('Next Question: \n')
            
                    else:
                        print('YOU ARE THE WINNER!!!')
                        print('SEVEN CRORES!!!!')
                        PLAYING = False
                # Incorrect
                elif user_ans in ['a','b','c','d']:
                    print('Wrong Answer! You lost. Better Luck Next Time.')
                    if q_no>=12:
                        money = 1250000
                    elif q_no>=10:
                        money = 500000
                    elif q_no>=5:
                        money = 25000
                    else:
                        money = 0
                    print('You will take ₹',money,'home')
                    
                
            else:
                print('You cannot use a lifeline on the 7 crore question!')
                # Invalid detection system:
                while True:
                    if user_ans in ['a','b','c','d','q']:
                        break
                    elif user_ans == '50':
                        print("Sorry, you cannot use a lifeline on the 7 crore question!")
                        user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                    else:
                        print('Invalid Input')
                        user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit, type (50) to use 50-50 lifeline or type (AP) to use Audience Poll: ').strip().lower()

                # Quit
                if user_ans == 'q':
                    print('You have quitted the game')
                    print('You will take ₹',money,'home')
                    

                # Correct
                elif user_ans == correct_ans.lower():
                    q_no = q_no + 1

                    money = money_counter(q_no)
                    print('Correct Answer!')
                    if q_no != 16:
                        print('\n','YOU HAVE','₹', money ,'\n')
                        print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                        print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                        print('Next Question: \n')

                    else:
                        print('YOU ARE THE WINNER!!!')
                        print('SEVEN CRORES!!!!')
                        PLAYING = False

                # Incorrect
                elif user_ans in ['a','b','c','d']:
                    print('Wrong Answer! You lost. Better Luck Next Time.')
                    if q_no>=12:
                        money = 1250000
                    elif q_no>=10:
                        money = 500000
                    elif q_no>=5:
                        money = 25000
                    else:
                        money = 0
                    print('You will take ₹',money,'home')
                    

        elif lifelines50_50 == 0:
            # Invalid detection system:
            while True:
                if user_ans in ['a','b','c','d','q']:
                    break
                elif user_ans == '50':
                    print("Sorry, you have no 50-50 lifelines left!")
                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit or type(ap) to use Audience Poll: ').strip().lower()
                elif user_ans == 'ap':
                    if lifelines_Audience_poll > 0:
                        if q_no < 16:
                            print('Lifeline Activated!')
                            lifelines_Audience_poll = lifelines_Audience_poll - 1
                            except_correct_ans_list = ['a','b','c','d']
                            except_correct_ans_list.remove(correct_ans.lower())
                            poll_result = random.choice([correct_ans.lower()]*9 + except_correct_ans_list)
                            print(f'The audience thinks the correct answer is option {poll_result.upper()}')
                            user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                            while True:
                                if user_ans in ['a','b','c','d','q']:
                                    break
                                else:
                                    print('Invalid Input')
                                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                            # Quit
                            if user_ans == 'q':
                                print('You have quitted the game')
                                print('You will take ₹',money,'home')
                                
                            
                            # Correct
                            elif user_ans == correct_ans.lower():
                                q_no = q_no + 1
                    
                                money = money_counter(q_no)
                                print('Correct Answer!')
                                if q_no != 16:
                                    print('\n','YOU HAVE','₹', money ,'\n')
                                    print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                                    print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                                    print('Next Question: \n')
                        
                                else:
                                    print('YOU ARE THE WINNER!!!')
                                    print('SEVEN CRORES!!!!')
                                    PLAYING = False
                            
                            # Incorrect
                            elif user_ans in ['a','b','c','d']:
                            
                                print('Wrong Answer! You lost. Better Luck Next Time.')
                                if q_no>=12:
                                    money = 1250000
                                elif q_no>=10:
                                    money = 500000
                                elif q_no>=5:
                                    money = 25000
                                else:
                                    money = 0
                                print('You will take ₹',money,'home')
                                
                        
                        else:
                            print('You cannot use a lifeline on the 7 crore question!')
                            # Invalid detection system:
                            while True:
                                if user_ans in ['a','b','c','d','q']:
                                    break
                                elif user_ans == '50':
                                    print("Sorry, you cannot use a lifeline on the 7 crore question!")
                                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                                else:
                                    print('Invalid Input')
                                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit, type (50) to use 50-50 lifeline or type (AP) to use Audience Poll: ').strip().lower()
            
                            # Quit
                            if user_ans == 'q':
                                print('You have quitted the game')
                                print('You will take ₹',money,'home')
                                
            
                            # Correct
                            elif user_ans == correct_ans.lower():
                                q_no = q_no + 1
            
                                money = money_counter(q_no)
                                print('Correct Answer!')
                                if q_no != 16:
                                    print('\n','YOU HAVE','₹', money ,'\n')
                                    print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                                    print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                                    print('Next Question: \n')
            
                                else:
                                    print('YOU ARE THE WINNER!!!')
                                    print('SEVEN CRORES!!!!')
                                    PLAYING = False
            
                            # Incorrect
                            elif user_ans in ['a','b','c','d']:
                                print('Wrong Answer! You lost. Better Luck Next Time.')
                                if q_no>=12:
                                    money = 1250000
                                elif q_no>=10:
                                    money = 500000
                                elif q_no>=5:
                                    money = 25000
                                else:
                                    money = 0
                                print('You will take ₹',money,'home')
                                
            
                    elif lifelines_Audience_poll == 0:
                        # Invalid detection system:
                        while True:
                            if user_ans in ['a','b','c','d','q']:
                                break
                            elif user_ans == 'ap':
                                print("Sorry, you have no Audience Poll lifelines left!")
                                user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                            else:
                                print('Invalid Input')
                                user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                    
                        # Quit
                        if user_ans == 'q':
                            print('You have quitted the game')
                            print('You will take ₹',money,'home')
                            
                        
                        # Correct
                        elif user_ans == correct_ans.lower():
                            q_no = q_no + 1
                            
                            money = money_counter(q_no)
                            print('Correct Answer!')
                            if q_no != 16:
                                print('\n','YOU HAVE','₹', money ,'\n')
                                print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                                print(f'You have {lifelines_Audience_poll} lifeline(s) left')
                                print('Next Question: \n')
                                
                            else:
                                print('YOU ARE THE WINNER!!!')
                                print('SEVEN CRORES!!!!')
                                PLAYING = False
                            
                        # Incorrect
                        elif user_ans in ['a','b','c','d']:
                            print('Wrong Answer! You lost. Better Luck Next Time.')
                            if q_no>=12:
                                money = 1250000
                            elif q_no>=10:
                                money = 500000
                            elif q_no>=5:
                                money = 25000
                            else:
                                money = 0
                            print('You will take ₹',money,'home')
                            
                else:
                    print('Invalid Input')
                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit or type(ap) to use Audience Poll: ').strip().lower()
        
            # Quit
            if user_ans == 'q':
                print('You have quitted the game')
                print('You will take ₹',money,'home')
                
            
            # Correct
            elif user_ans == correct_ans.lower():
                q_no = q_no + 1
                
                money = money_counter(q_no)
                print('Correct Answer!')
                if q_no != 16:
                    print('\n','YOU HAVE','₹', money ,'\n')
                    print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                    print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                    print('Next Question: \n')
                    
                else:
                    print('YOU ARE THE WINNER!!!')
                    print('SEVEN CRORES!!!!')
                    PLAYING = False
                
            # Incorrect
            elif user_ans in ['a','b','c','d']:
                print('Wrong Answer! You lost. Better Luck Next Time.')
                if q_no>=12:
                    money = 1250000
                elif q_no>=10:
                    money = 500000
                elif q_no>=5:
                    money = 25000
                else:
                    money = 0
                print('You will take ₹',money,'home')
                

    # Lifeline Audience Poll
    elif user_ans == 'ap':
        if lifelines_Audience_poll > 0:
            if q_no < 16:
                print('Lifeline Activated!')
                lifelines_Audience_poll = lifelines_Audience_poll - 1
                except_correct_ans_list = ['a','b','c','d']
                except_correct_ans_list.remove(correct_ans.lower())
                poll_result = random.choice([correct_ans.lower()]*9 + except_correct_ans_list)
                print(f'The audience thinks the correct answer is option {poll_result.upper()}')
                user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                while True:
                    if user_ans in ['a','b','c','d','q']:
                        break
                    else:
                        print('Invalid Input')
                        user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                # Quit
                if user_ans == 'q':
                    print('You have quitted the game')
                    print('You will take ₹',money,'home')
                    
                
                # Correct
                elif user_ans == correct_ans.lower():
                    q_no = q_no + 1
        
                    money = money_counter(q_no)
                    print('Correct Answer!')
                    if q_no != 16:
                        print('\n','YOU HAVE','₹', money ,'\n')
                        print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                        print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                        print('Next Question: \n')
            
                    else:
                        print('YOU ARE THE WINNER!!!')
                        print('SEVEN CRORES!!!!')
                        PLAYING = False
                
                # Incorrect
                elif user_ans in ['a','b','c','d']:

                    print('Wrong Answer! You lost. Better Luck Next Time.')
                    if q_no>=12:
                        money = 1250000
                    elif q_no>=10:
                        money = 500000
                    elif q_no>=5:
                        money = 25000
                    else:
                        money = 0
                    print('You will take ₹',money,'home')
                    
            
            else:
                print('You cannot use a lifeline on the 7 crore question!')
                # Invalid detection system:
                while True:
                    if user_ans in ['a','b','c','d','q']:
                        break
                    elif user_ans == '50':
                        print("Sorry, you cannot use a lifeline on the 7 crore question!")
                        user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                    else:
                        print('Invalid Input')
                        user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit, type (50) to use 50-50 lifeline or type (AP) to use Audience Poll: ').strip().lower()

                # Quit
                if user_ans == 'q':
                    print('You have quitted the game')
                    print('You will take ₹',money,'home')
                    

                # Correct
                elif user_ans == correct_ans.lower():
                    q_no = q_no + 1

                    money = money_counter(q_no)
                    print('Correct Answer!')
                    if q_no != 16:
                        print('\n','YOU HAVE','₹', money ,'\n')
                        print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                        print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                        print('Next Question: \n')

                    else:
                        print('YOU ARE THE WINNER!!!')
                        print('SEVEN CRORES!!!!')
                        PLAYING = False

                # Incorrect
                elif user_ans in ['a','b','c','d']:
                    print('Wrong Answer! You lost. Better Luck Next Time.')
                    if q_no>=12:
                        money = 1250000
                    elif q_no>=10:
                        money = 500000
                    elif q_no>=5:
                        money = 25000
                    else:
                        money = 0
                    print('You will take ₹',money,'home')
                    

        elif lifelines_Audience_poll == 0:
            # Invalid detection system:
            while True:
                if user_ans in ['a','b','c','d','q']:
                    break
                elif user_ans == 'ap':
                    print("Sorry, you have no Audience Poll lifelines left!")
                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit or type(50) to use 50-50 lifeline: ').strip().lower()
                elif user_ans == '50':
                    if lifelines50_50 > 0:
                        if q_no < 16:
                            print('Lifeline Activated!')
                            lifelines50_50 = lifelines50_50 - 1
                            options_except_correct = ['a','b','c','d']
                            options_except_correct.remove(correct_ans.lower())
                            remove_options1 = random.choice(options_except_correct)
                            options_except_correct.remove(remove_options1)
                            remove_options2 = random.choice(options_except_correct)
                            options_left = ['a','b','c','d']
                            options_left.remove(remove_options1)
                            options_left.remove(remove_options2)
                           
                            print(f'Options {remove_options1.upper()} and {remove_options2.upper()} are wrong. The correct answer is in ({options_left[0].upper()}, {options_left[1].upper()})')
                            user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                            while True:
                                if user_ans in ['a','b','c','d','q']:
                                    break
                                else:
                                    print('Invalid Input')
                                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit : ').strip().lower()
                            # Quit
                            if user_ans == 'q':
                                print('You have quitted the game')
                                print('You will take ₹',money,'home')
                                   
            
                            # Correct
                            elif user_ans == correct_ans.lower():
                                q_no = q_no + 1
                    
                                money = money_counter(q_no)
                                print('Correct Answer!')
                                if q_no != 16:
                                    print('\n','YOU HAVE','₹', money ,'\n')
                                    print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                                    print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                                    print('Next Question: \n')
                        
                                else:
                                    print('YOU ARE THE WINNER!!!')
                                    print('SEVEN CRORES!!!!')
                                    PLAYING = False
                            # Incorrect
                            elif user_ans in ['a','b','c','d']:
                                print('Wrong Answer! You lost. Better Luck Next Time.')
                                if q_no>=12:
                                    money = 1250000
                                elif q_no>=10:
                                    money = 500000
                                elif q_no>=5:
                                    money = 25000
                                else:
                                    money = 0
                                print('You will take ₹',money,'home')
                                
                            
                        else:
                            print('You cannot use a lifeline on the 7 crore question!')
                            # Invalid detection system:
                            while True:
                                if user_ans in ['a','b','c','d','q']:
                                    break
                                elif user_ans == '50':
                                    print("Sorry, you cannot use a lifeline on the 7 crore question!")
                                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                                else:
                                    print('Invalid Input')
                                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit, type (50) to use 50-50 lifeline or type (AP) to use Audience Poll: ').strip().lower()
            
                            # Quit
                            if user_ans == 'q':
                                print('You have quitted the game')
                                print('You will take ₹',money,'home')
                                
            
                            # Correct
                            elif user_ans == correct_ans.lower():
                                q_no = q_no + 1
            
                                money = money_counter(q_no)
                                print('Correct Answer!')
                                if q_no != 16:
                                    print('\n','YOU HAVE','₹', money ,'\n')
                                    print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                                    print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                                    print('Next Question: \n')
            
                                else:
                                    print('YOU ARE THE WINNER!!!')
                                    print('SEVEN CRORES!!!!')
                                    PLAYING = False
            
                            # Incorrect
                            elif user_ans in ['a','b','c','d']:
                                print('Wrong Answer! You lost. Better Luck Next Time.')
                                if q_no>=12:
                                    money = 1250000
                                elif q_no>=10:
                                    money = 500000
                                elif q_no>=5:
                                    money = 25000
                                else:
                                    money = 0
                                print('You will take ₹',money,'home')
                                
            
                    elif lifelines50_50 == 0:
                        # Invalid detection system:
                        while True:
                            if user_ans in ['a','b','c','d','q']:
                                break
                            elif user_ans == '50':
                                print("Sorry, you have no 50-50 lifelines left!")
                                user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                            else:
                                print('Invalid Input')
                                user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit: ').strip().lower()
                    
                        # Quit
                        if user_ans == 'q':
                            print('You have quitted the game')
                            print('You will take ₹',money,'home')
                            
                        
                        # Correct
                        elif user_ans == correct_ans.lower():
                            q_no = q_no + 1
                            
                            money = money_counter(q_no)
                            print('Correct Answer!')
                            if q_no != 16:
                                print('\n','YOU HAVE','₹', money ,'\n')
                                print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                                print(f'You have {lifelines_Audience_poll} Audience Poll lifeline(s) left')
                                print('Next Question: \n')
                                
                            else:
                                print('YOU ARE THE WINNER!!!')
                                print('SEVEN CRORES!!!!')
                                PLAYING = False
                            
                        # Incorrect
                        elif user_ans in ['a','b','c','d']:
                            print('Wrong Answer! You lost. Better Luck Next Time.')
                            if q_no>=12:
                                money = 1250000
                            elif q_no>=10:
                                money = 500000
                            elif q_no>=5:
                                money = 25000
                            else:
                                money = 0
                            print('You will take ₹',money,'home')
                            

                else:
                    print('Invalid Input')
                    user_ans = input('Enter Your Answer(a/b/c/d), type(q) to Quit or type(50) to use 50-50 lifeline: ').strip().lower()
        
            # Quit
            if user_ans == 'q':
                print('You have quitted the game')
                print('You will take ₹',money,'home')
                
            
            # Correct
            elif user_ans == correct_ans.lower():
                q_no = q_no + 1
                
                money = money_counter(q_no)
                print('Correct Answer!')
                if q_no != 16:
                    print('\n','YOU HAVE','₹', money ,'\n')
                    print(f'You have {lifelines50_50} 50-50 lifeline(s) left')
                    print(f'You have {lifelines_Audience_poll} lifeline(s) left')
                    print('Next Question: \n')
                    
                else:
                    print('YOU ARE THE WINNER!!!')
                    print('SEVEN CRORES!!!!')
                    PLAYING = False
                
            # Incorrect
            elif user_ans in ['a','b','c','d']:
                print('Wrong Answer! You lost. Better Luck Next Time.')
                if q_no>=12:
                    money = 1250000
                elif q_no>=10:
                    money = 500000
                elif q_no>=5:
                    money = 25000
                else:
                    money = 0
                print('You will take ₹',money,'home')
                

    elapsed = int(time.time()) - int(start)

    if 0 <= q_no <= 5 and elapsed >= 30 :
        PLAYING = False                
        if user_ans == correct_ans :
            print('Sorry, but your Answer was too Slow! You ran out of Time.')
            q_no -= 1
            if q_no>=12:
                money = 1250000
            elif q_no>=10:
                money = 500000
            elif q_no>=5:
                money = 25000
            else:
                money = 0
                print(f'Now You will take ₹{money} home.')
            while True:
                play_again = input('Do You Want To Play Again? (yes/no): ').upper().strip(' ')
                if play_again in ('YES','NO'):
                    break
                else:
                    print('Invalid Input')
            if play_again == 'YES':
                q_no = 0
                money = 0
                lifelines50_50 = 2
                PLAYING = True
        
                print('...STARTING THE GAME AGAIN...')
            else:
                print('Thank You for Playing!')
                PLAYING = False
        if user_ans == 'q':
            print('Sorry, but you took too long to take this decision!')
            if q_no>=12:
                money = 1250000
            elif q_no>=10:
                money = 500000
            elif q_no>=5:
                money = 25000
            else:
                money = 0
                print(f'Now You will take ₹{money} home.')
        else:
            print('You took too long to answer the previous question, so you Lost anyway.')

    elif 6 <= q_no <= 10  and elapsed >= 60 :
        PLAYING = False  

        if user_ans == correct_ans :
            print('Sorry, but your Answer was too Slow! You ran out of Time.')
            q_no -= 1
            if q_no>=12:
                money = 1250000
            elif q_no>=10:
                money = 500000
            elif q_no>=5:
                money = 25000
            else:
                money = 0
                print(f'Now You will take ₹{money} home.')
            while True:
                play_again = input('Do You Want To Play Again? (yes/no): ').upper().strip(' ')
                if play_again in ('YES','NO'):
                    break
                else:
                    print('Invalid Input')
            if play_again == 'YES':
                q_no = 0
                money = 0
                lifelines50_50 = 2
                PLAYING = True
        
                print('...STARTING THE GAME AGAIN...')
            else:
                print('Thank You for Playing!')
                PLAYING = False
        if user_ans == 'q':
            print('Sorry, but you took too long to take this decision!')
            if q_no>=12:
                money = 1250000
            elif q_no>=10:
                money = 500000
            elif q_no>=5:
                money = 25000
            else:
                money = 0
                print(f'Now You will take ₹{money} home.')
        else:
            print('You took too long to answer the previous question, so you Lost anyway.')

    if user_ans != correct_ans:
        while True:
            play_again = input('Do You Want To Play Again? (yes/no): ').upper().strip(' ')
            if play_again in ('YES','NO'):
                break
            else:
                print('Invalid Input')
        if play_again == 'YES':
            q_no = 0
            money = 0
            lifelines50_50 = 2
            PLAYING = True
    
            print('...STARTING THE GAME AGAIN...')
        else:
            print('Thank You for Playing!')
            PLAYING = False

    