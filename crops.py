def cropss(crop_name):
    crop_d = {
        "Wheat": ["U.P., Punjab, Haryana, Rajasthan, M.P., bihar", "rabi",
                  "Sri Lanka, United Arab Emirates, Taiwan"],
        "Paddy": ["W.B., U.P., Andhra Pradesh, Punjab, T.N.", "kharif", "Bangladesh, Saudi Arabia, Iran"],
        "Barley": ["Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "rabi", "Oman, UK, Qatar, USA"],
        "Maize": ["Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "kharif",
                  "Hong Kong, United Arab Emirates, France"],
        "Bajra": ["Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "kharif",
                  "Oman, Saudi Arabia, Israel, Japan"],
        "Cotton": ["Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", "Kharif",
                   " China, Bangladesh, Egypt"],
        "Gram": ["Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka", "Kharif,Rabi",
                 "Veitnam, Spain, Myanmar"],
        "Groundnut": ["Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "kharif",
                      "Indonesia, Jordan, Iraq"],
        "Jowar": ["Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "Kharif,Rabi",
                  "Torronto, Sydney, New York"],
        "Moong": ["Rajasthan, Maharashtra, Andhra Pradesh", "rabi", "Qatar, United States, Canada"],
        "Soyabean": ["Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "kharif",
                     "Spain, Thailand, Singapore"],
        "Sugarcane": ["Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh", "kharif",
                      "Kenya, United Arab Emirates, United Kingdom"],
        "Coconut": ["Kerala, Karnataka, Andhra Pradesh Tamil Nadu", "Whole Year", "Usa,Canada,Singapore,Dubai"],
        "Chillies": ["Andhra Pradesh, Maharashtra, Karnataka, Orissa, Madhya Pradesh", "Kharif,Rabi",
                     "Usa,Sri-Lanka,Canada,Dubai"],
        "Potato": ["Madhya Pradesh, Maharashtra, Madhya Pradesh and Maharashtra", "Kharif,Rabi",
                   "China, Bangladesh,Usa"],
        "Peas": ["Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", "Kharif",
                 "Usa,Singapore,Dubai"],
        "Turmeric": ["Tamil Nadu , Orissa ,West Bengal", "kharif, Rabi", "Usa,Singapore,Dubai,Qatar,Bangladesh"],
        "Onion": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                  "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Banana": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Bean": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                 "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Black pepper": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                         "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Blackgram": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                      "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Bottle Gourd": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                         "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Brinjal": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                    "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Cabbage": ["Andhra Pradesh, Maharashtra, Karnataka, Orissa, Madhya Pradesh", "Kharif,Rabi",
                    "Usa,Sri-Lanka,Canada,Dubai"],
        "Cardamom": ["Madhya Pradesh, Maharashtra, Madhya Pradesh and Maharashtra", "Kharif,Rabi",
                     "China, Bangladesh,Usa"],
        "Carrot": ["Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", "Kharif",
                   "Usa,Singapore,Dubai"],
        "Castor seed": ["Tamil Nadu , Orissa ,West Bengal", "kharif, Rabi", "Usa,Singapore,Dubai,Qatar,Bangladesh"],
        "Cauliflower": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                        "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Colocosia": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                      "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Cowpea": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Drum Stick": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                       "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Garlic": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Ginger": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Grapes": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Guar seed": ["Andhra Pradesh, Maharashtra, Karnataka, Orissa, Madhya Pradesh", "Kharif,Rabi",
                      "Usa,Sri-Lanka,Canada,Dubai"],
        "Jute": ["Madhya Pradesh, Maharashtra, Madhya Pradesh and Maharashtra", "Kharif,Rabi",
                 "China, Bangladesh,Usa"],
        "Khesari": ["Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", "Kharif",
                    "Usa,Singapore,Dubai"],
        "Lady Finger": ["Tamil Nadu , Orissa ,West Bengal", "kharif, Rabi", "Usa,Singapore,Dubai,Qatar,Bangladesh"],
        "Lentil": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Linseed": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                    "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Mesta": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                  "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Moth": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                 "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Orange": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Papaya": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Pineapple": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                      "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Raddish": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                    "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Ragi": ["Andhra Pradesh, Maharashtra, Karnataka, Orissa, Madhya Pradesh", "Kharif,Rabi",
                 "Usa,Sri-Lanka,Canada,Dubai"],
        "Rice": ["Madhya Pradesh, Maharashtra, Madhya Pradesh and Maharashtra", "Kharif,Rabi",
                 "China, Bangladesh,Usa"],
        "Safflower": ["Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", "Kharif",
                      "Usa,Singapore,Dubai"],
        "Sannhamp": ["Tamil Nadu , Orissa ,West Bengal", "kharif, Rabi", "Usa,Singapore,Dubai,Qatar,Bangladesh"],
        "Sesamum": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                    "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Sunflower": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                      "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Sweet potato": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                         "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Tomato": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Urad": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                 "Malaysia,Sri Lanka,Singapore,Bangladesh"],
        "Varagu": ["Maharashtra,Madhya Pradesh,Karnataka,Gujarat", "Kharif ,Rabi",
                   "Malaysia,Sri Lanka,Singapore,Bangladesh"]

    }
    return crop_d[crop_name]


def cropdes(crop_name):
    crop_des = {
        "Wheat": [
            "Wheat, any of several species of cereal grasses of the genus Triticum (family Poaceae) and their edible grains. Wheat is one of the oldest and most important of the cereal crops. Of the thousands of varieties known, the most important are common wheat Triticum aestivum, used to make bread; durum wheat"],
        "Paddy": [
            "Paddy, also called rice paddy, small, level, flooded field used to cultivate rice in southern and eastern Asia. Wet-rice cultivation is the most prevalent method of farming in the Far East, where it utilizes a small fraction of the total land yet feeds the majority of the rural population."],
        "Barley": [
            "Barley, cereal plant of the grass family Poaceae and its edible grain. Grown in a variety of environments, barley is the fourth largest grain crop globally, after wheat, rice, and corn."],
        "Maize": [
            "Maize or Indian corn (called corn in some countries) is Zea mays, a member of the grass family Poaceae. It is a cereal grain which was first grown by people in ancient Central America. Approximately 1 billion tonnes are harvested every year."],
        "Bajra": [
            "Bajra (Pennisetum glaucum) or Pearl millet is an important nutria-cereal or coarse grain cereals suitable for rainfed and dryland agriculture. It is 70-90 days duration crop best suitable for sandy, black and loamy soils with good drainage. Bajra is consumed both as grain and used for fodder purpose."],
        "Cotton": [
            "Cotton is a soft, fluffy staple fiber that grows in a boll, or protective case, around the seeds of the cotton plants of the genus Gossypium in the mallow family Malvaceae. The fiber is almost pure cellulose. The fiber is most often spun into yarn or thread and used to make a soft, breathable textile."],
        "Gram": [
            "Gram commonly known as chick pea or Bengal gram is the most important pulse crop of India. It is used for human consumption as well as for feeding to animals. Fresh green leaves are used as vegetable while straw of chickpea is an excellent fodder for cattle. The grains are also used as vegetable."],
        "Groundnut": [
            "Groundnut is raised mostly as a rainfed kharif crop, being sown from May to June, depending on the monsoon rains. It is sown as late as August or early September. As an irrigated crop it is grown to limited extent between January and March and between in May and July."],
        "Jowar": [
            "Sorghum popularly known as jowar is the most important food and fodder crop of dry land agriculture. The cereal crop is perennial in nature and possessing corn like leaves and bearing the grain in a compact cluster. Sorghum is the fifth most important cereal crop in the world after wheat, rice, maize and barley."],
        "Moong": [
            "Green gram also known as moong is one of the main pulse crop of India. It is a rich source of Protein along with fibre and iron. It can be cultivated as Kharif as well as summer crop. In Punjab, near about 5.2 thousand hectares of area is under moong cultivation with total production of 4.5 thousand tones."],
        "Soyabean": [
            "The soybean is a truly amazing and versatile crop plant. A variety of foods was developed from the soybean, ranging from soybean sprouts to steamed raw beans to roasted seeds to soy milk to soy sauce to fermented soybean paste and cake to soy flour to the commonly eaten curd called tofu."],
        "Sugarcane": [
            "Sugarcane is a major crop in many countries. It is one of the plants with the highest bioconversion efficiency. Sugarcane crop is able to efficiently fix solar energy, yielding some 55 tonnes of dry matter per hectare of land annually. After harvest, the crop produces sugar juice and bagasse, the fibrous dry matter."],
        "Coconut": [
            "Coconut is Rabi crop. Rabi crops are agriculture crops which are sown in winter. These crops are harvested in spring season in India. Soil with a minimum depth of 1.2 m and fairly good water holding capacity is preferred for coconut cultivation"],
        "Chillies": [
            "It is known as the most valuable crop of India. It is used as a principle ingredient of various curries and chutneys, also used in vegetables, spices, condiments, sauces and pickles. Pungency in chillies is due to the active constituent Capsaicin, an alkaloid."],
        "Potato": [
            "Potato is mostly grown as a rainfed crop in regions receiving a rainfall of 1200 – 2000 mm per annum. Planting is done during October – November in plains. About 3000 – 3500 kg/ha of seeds is required. Use Carbon disulphide 30 g/100 kg of seeds for breaking the dormancy and inducing sprouting of tubers.26"],
        "Peas & beans (Pulses)": [
            "It belongs to Leguminaceae family. It is a cool season crop grown throughout the world. Green pods are used for vegetable purpose and dried peas are used as pulse. In India it is cultivated in Himachal Pradesh, Madhya Pradesh, Rajasthan, Maharashtra, Punjab, Haryana, Karnataka and Bihar."],
        "Turmeric": [
            "Turmeric can be grown from sea level to 1500m in the hills, at a temperature range of 20-300C with a rainfall of 1500-2250mm per annum. It is also grown as an irrigated crop. It thrives best in a well drained sandy or clayey loam rich in humus content.light black, ashy loam and red soils to clay loams."],
        "Onion": [
            "The onion is a hardy cool-season biennial but usually grown as annual crop. The onion has narrow, hollow leaves and a base which enlarges to form a bulb. The bulb can be white, yellow, or red and require 80 to 150 days to reach harvest."],
        "Banana": [
            "Banana, basically a tropical crop, grows well in a temperature range of 15ºC – 35ºC with relative humidity of 75-85%. It prefers tropical humid lowlands and is grown from the sea level to an elevation of 2000m.Deep, rich loamy soil with pH between 6.5 – 7.5 is most preferred for banana cultivation. "],
        "Bean": [
            "The common bean (Phaseolus vulgaris L.) is a major grain legume consumed worldwide for its edible seeds and pods. It is a highly polymorphic warm-season, herbaceous annual. "],
        "Black pepper": [
            "Black pepper, Piper nigrum, is a climbing perennial plant in the family Piperaceae which is grown for its fruits.Black pepper may be vining or have bushy, wooden stems. The plant has simple, alternating leaves which are oval in shape and produces clusters, or spikes, of 50 to 150 flowers. "],
        "Blackgram": [
            " Black gram (Vigna Mungo L.), is one of the important pulses crop, grown throughout the country. The crop is resistant to adverse climatic conditions and improve the soil fertility by fixing atmospheric nitrogen in the soil."],
        "Bottle Gourd ": [
            "Bottle gourd is an important crop grown throughout in north eastern region. The plant has a trailing habit. The fruit in green stage and leaves with stem are used as vegetables.Fruit pulp is a good source of fibre free carbohydrates. "],
        "Brinjal": [
            "Brinjal or eggplant (Solanum melongena L.) is an important solanaceous crop of sub tropics and tropics. It is a versatile crop adapted to different agro-climatic regions and can be grown throughout the year.It is a perennial but grown commercially as an annual crop. "],
        "Cabbage": [
            "Cultivation of cabbage is done mainly on sandy to heavy soils rich in organic matter.Plants growing in saline soils are prone to diseases. In India, cabbage is grown in large areas having a cool and moist climate. A temperature range of 15o-21o C is considered as optimum for growth and head formation of the crop. "],
        "Cardamom": [
            " Cardamom is propagated mainly through seeds and also through suckers each consisting of atleast one old and a young aerial shoot. Seedlings are normally raised in primary and secondary nurseries. Raised beds are prepared after digging the land to a depth of 30-45cm."],
        "Carrot": [
            "Carrot is a winter season crop and if grown at 15°C to 20°C will develop a very good colour. Carrot crop needs deep loose loamy soil and pH should be ranging from 6.0 to 7.0 for higher production. "],
        "Castor seed": [
            "Castor is an important industrial non-edible oilseed crop. Castor seed contain 45-47 % non-edible oil, which is used as domestic, medicinal and industrial purposes. Castor oil is used as a lubricant in all moving parts of the machinery and particularly high speed engines and aero planes. "],
        "Cauliflower": [
            "Cauliflowers are annual plants that reach about 0.5 metre (1.5 feet) tall and bear large rounded leaves that resemble collards (Brassica oleracea, variety acephala). As desired for food, the terminal cluster forms a firm, succulent “curd,” or head, that is an immature inflorescence (cluster of flowers). "],
        "Colocosia": [
            "They are herbaceous perennial plants with a large corm on or just below the ground surface. The leaves are large to very large, 20–150 cm (7.9–59.1 in) long, with a sagittate shape. The elephant's-ear plant gets its name from the leaves, which are shaped like a large ear or shield. "],
        "Cowpea": [
            "Cowpeas are typically climbing or trailing vines that bear compound leaves with three leaflets. The white, purple, or pale-yellow flowers usually grow in pairs or threes at the ends of long stalks. The pods are long and cylindrical and can grow 20–30 cm (8–12 inches) long, depending on the cultivar "],
        "Drum Stick": [
            " Moringa oleifera is a fast-growing, evergreen, deciduous tree. It can reach a height of 10- 12 m and the trunk can reach a diameter of 45 cm.The tree has an open crown of drooping, fragile branches and the leaves build up feathery foliage of tripinnate leaves."],
        "Garlic": [
            "Garlic, Allium sativum, is a an herbaceous, annual, bulbous plant in the family Amaryllidaceae grown for its pungent, edible bulb of the same name. The stem is very short and flattened and gives way to a pseudostem, The garlic plant can possess 6–12 flat, blade-like leaves which can stretch up to 50 cm (19.7 in) long. "],
        "Ginger": [
            "Ginger is a herbaceous perennial with underground rhizomes having serial leafy shoots of 0.5 to 0.75m height; leaves sheathy, alternately arranged, linear with 15 cm long and sessile flowers borne on a spike, condensed, oblong and cylindrical with numerous scar bracts; flowers numerous yellow in colou "],
        "Grapes": [
            "Grape (Vitis sp.) belonging to Family Vitaceae is a commercially important fruit crop of India. It is a temperate crop which has got adapted to sub-tropical climate of peninsular India. The fruit contains about 20% sugar in easily digestible form besides being rich in calcium and phosphorus. "],
        "Guar seed": [
            "Guar is a drought-tolerant plant which needs moderate legume crop, which grows best in sandy soils and needs Moderate ,intermittent rainfall with lots of sunshine. below the soil surface. Plants have single stem, fine branching or basal branching and grow as high as 45-100 cm. The flowers are small, and white. "],
        "Jute": [
            "Jute is a long, soft, shiny bast fiber that can be spun into coarse, strong threads. Jute is the name of the plant or fiber used to make burlap, hessian or gunny cloth. Jute is one of the most affordable natural fibers, and second only to cotton in the amount produced and variety of uses. "],
        "Khesari": [
            "Grass pea or Lathyrus sativus or Khesai Dal grown both as food and fodder is one of the preferred legume crops in poor and arid areas for adaptation under changing climate because of its intrinsic tolerance to drought, water-logging, and salinity "],
        "Lady Finger": [
            "Lady finger or Okra or Bhendi is a flower plant grown for its edible green seed pods. Lady finger plants are cultivated in tropical, subtropical and warm regions. It is annual crop and grown about 4 meters tall. Lady's finger plants have a long and broad leaves with 4 to 5 lobes with white and yellow flower. "],
        "Lentil": [
            "Lentil, Lens culinaris, is a a bushy, annual legume in the family Fabaceae grown for its edible seeds which are cooked and eaten. The lentil plant is slender and erect or sub-erect and has branching, hairy stems. The leaves of the plant are arranged alternately and are made up of 4–7 individual oval leaflets. "],
        "Linseed": [
            "Linseed is an annual herbaceous plant and grows to a height of 30 to 120 cm. Fibre types are tall growing and less branched than the seed types. It has a well-developed fibrous root system with many lateral roots. The stem is glabrous grayish green with leaves narrow and alternate. "],
        "Mesta": [
            "Mesta is herbaceous annual plant. It is an important commercial crop after cotton and Jute. Hibiscus cannabinus and Hibiscus sabdariffa are two species commonly name as Mesta. "],
        "Moth": [
            "Phaseolus aconitifolius Jacq. Vigna aconitifolia is a drought-resistant legume, commonly grown in arid and semi-arid regions of India. It is commonly called mat bean, moth bean, matki, Turkish gram or dew bean. The pods, sprouts and protein-rich seeds of this crop are commonly consumed in India. "],
        "Orange": [
            "Mandarin orange (Citrus reticulata) is most common among citrus fruits grown in India. It occupies nearly 40% of the total area under citrus cultivation in India.Mandarin orange is propagated by seeds and also vegetatively propagated by T-budding. Seedlings are mostly transplanted in the month of July-August after commencement of monsoon. "],
        "Papaya": [
            "The papaya (from Carib via Spanish), papaw or pawpaw is the plant Carica papaya, one of the 22 accepted species in the genus Carica of the family Caricaceae. Its origin is in the tropics of the Americas, perhaps from Central America and southern Mexico.  "],
        "Pineapple": [
            " PINEAPPLE. Pineapple (Ananas comosus) is one of the commercially important fruit crops of India. Total annual world production is estimated at 14.6 million tonnes of fruits. ... Cultivation of pineapple originated in Brazil and gradually spread to other tropical parts of the world."],
        "Raddish": [
            "Radishes are grown and consumed throughout the world, being mostly eaten raw as a crunchy salad vegetable with a pungent flavor. There are numerous varieties, varying in size, flavor, color, and length of time they take to mature. Radishes owe their sharp flavor to the various chemical compounds produced by the plants, including glucosinolate, myrosinase, and isothiocyanate. "],
        "Ragi": [
            "Ragi may be grown as a hot weather crop, from May to September, using long duration varieties and as a cold season crop, from November and December, using early types. Ragi is monocropped in India under irrigation or transplantation. Ragi is chopped and weeded at intervals of 14 days or so. "],
        "Rice": [
            "Rice plant is an annual warm-season grass (monocot plant) with round culms, flat leaves and terminal panicles. Rice is normally grown as an annual plant, although in tropical areas it can survive as a perennial and can produce a ratoon crop up to 20 years. "],
        "Safflower": [
            "Safflower is an annual species in the same plant family as sunflower. This crop is adapted to dryland or irrigated cropping systems. Each seed germinates and produces a central stem that does not elongate for two to three weeks, and develops leaves near the ground in a rosette, similar to a young thistle. "],
        "Sannhamp": [
            "Sunn hemp (Crotalaria juncea L.) is a multipurpose tropical and subtropical legume grown in many countries, notably India, mainly for its high quality fibre. The crop is grown for green manure, as a soil improver and as a disease break in cereal or other crop rotations "],
        "Sesamum": [
            "Sesamum is basically a crop of warm regions of the tropics and sub-tropics. It grows in plains as well as up to an elevation of 1230 m. It requires fairly hot conditions during growth for maximum yield. A temperature of 25 to 27 ºC encourages rapid germination, initial growth and flower formation. "],
        "Sunflower": [
            "Sunflower (Helianthus annuus L.) belongs to the family Asteraceae. The Helianthus genus contains 65 different species of which 14 are annual plants. Because the sunflower has several potential markets, it is a good choice for growers on both small and large scales. "],
        "Sweet potato": [
            "Sweet potato is a highly heterozygous crop and has a chromosome number of 2n (6x) = 90, it is considered to be a natural hexaploid. Sweet potato is the second most important root crop with a world production of 103.11 million tones. Sweet potato is grown widely in tropical and sub-tropical parts of the world. "],
        "Tomato": [
            "Tomato (Lycopersicon esculentum) is an annual or short lived perennial pubescent herb and greyish green curled uneven pinnate leaves. The flowers are off white bearing fruits which are red or yellow in colour. It is a self pollinated crop. "],
        "Urad": [
            "Black gram (Vigna Mungo L.) is popularly known as “Urad”, is one of the most important pulses crop, grown across India. This crop is grown primarily for its protein-rich seeds and used as daal and as the main ingredient in breakfast snacks like dosa, idli, vada & papad "],
        "Varagu": [
            "vargu is an erect herbaceous annual which tillers profusely. Its plant grows up to a height of 45-100 centimetre. Stem is slender with distinctly swollen nodes. The roots are fibrous and shallow. "]

    }

    return crop_des


def fert(crop_name):
    fert1 = {
        "Wheat": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Paddy": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Barley": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Maize":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Bajra": ["Sandy loam soils", "Nitrogen , Phosphorous , Potassium ", "80:40:40"],
        "Cotton": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Gram": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Groundnut": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Jowar":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Moong": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Soyabean": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Sugarcane": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Coconut": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Chillies": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Potato": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Peas & beans (Pulses)": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Turmeric": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Onion": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Banana": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Bean": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Black pepper": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Blackgram": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Bottle Gourd": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Brinjal": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        'Cabbage': ["Clay soil", "Liquid fert,Compost tea,Fish emulsion", "10:10:10"],
        "Cardamom": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Carrot":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Castor seed": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Cauliflower": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Colocosia": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Cowpea": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Drum Stick": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Garlic": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Ginger": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Grapes": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Guar seed": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Jute": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Khesari": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Lady Finger": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Lentil": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Linseed": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Mesta":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Moth": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Orange": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Papaya": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Pineapple":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Raddish": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Ragi": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Rice": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Safflower": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"],
        "Sannhamp": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Sesamum":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Sunflower": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Sweet potato": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Tomato":["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Urad": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "30:10:10"],
        "Varagu": ["Sandy soil","Nitrogen , Phosphorous , Potassium ", "70:60:50"]
    }

    return fert1[crop_name]
