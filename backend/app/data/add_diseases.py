import json

new_diseases = [
  {
    "id": "tomato-septoria-leaf-spot",
    "common_name": "Septoria Leaf Spot",
    "scientific_name": "Septoria lycopersici",
    "crop": "Tomato",
    "severity": "Moderate",
    "description": "Septoria leaf spot is one of the most destructive diseases of tomato foliage. It rarely affects fruit directly but causes severe defoliation, weakening the plant and exposing fruit to sunscald.",
    "symptoms": [
      "Numerous small circular spots (3-5mm) with dark brown borders and grey-white centres",
      "Small black dots (pycnidia) visible in the centre of each spot",
      "Lower leaves affected first, disease moves upward rapidly",
      "Heavy infections cause leaves to yellow and drop",
      "Defoliation leads to fruit sunscald"
    ],
    "causes": "Caused by the fungus Septoria lycopersici. Survives on infected plant debris. Spreads by rain splash and wind. Favoured by warm temperatures (20-25C) and high humidity.",
    "treatment": {
      "organic": ["Remove and destroy all infected lower leaves immediately", "Apply copper-based fungicide every 7-10 days", "Spray neem oil solution to slow spore germination", "Mulch around plant base to prevent soil splash"],
      "chemical": ["Chlorothalonil (Daconil) spray every 7 days", "Mancozeb as a protective treatment before wet periods", "Azoxystrobin for systemic protection of new growth"],
      "prevention": ["Rotate crops — do not grow tomatoes in same spot for 2-3 years", "Water at the base of plants only", "Remove all plant debris at end of season", "Space plants 60cm apart for good air circulation"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Septoria_leaf_spot_on_tomato.jpg/640px-Septoria_leaf_spot_on_tomato.jpg",
    "tags": ["fungal", "defoliation", "common"]
  },
  {
    "id": "tomato-spider-mites",
    "common_name": "Spider Mites (Two-spotted)",
    "scientific_name": "Tetranychus urticae",
    "crop": "Tomato",
    "severity": "Moderate",
    "description": "Two-spotted spider mites are tiny arachnids that feed on the underside of tomato leaves. They build damaging populations very quickly in hot, dry weather.",
    "symptoms": [
      "Fine stippling (tiny yellow or white dots) on upper leaf surface",
      "Fine silky webbing on the underside of leaves and between stems",
      "Leaves turn bronze, yellow, then brown and die",
      "Tiny moving dots (0.5mm) visible on leaf underside — the mites themselves",
      "Severe infestations cause complete defoliation"
    ],
    "causes": "Caused by the mite Tetranychus urticae. Thrives in hot (above 27C), dry conditions. Spreads by wind, clothing, and tools. Pesticide overuse destroys natural predators, causing outbreaks.",
    "treatment": {
      "organic": ["Spray plants forcefully with water to knock mites off leaves", "Apply neem oil spray (2% solution) every 5-7 days", "Introduce predatory mites (Phytoseiulus persimilis) as biological control", "Spray insecticidal soap on leaf undersides"],
      "chemical": ["Abamectin (Agrimec) miticide — effective against all life stages", "Spiromesifen (Oberon) for resistance management", "Rotate miticides — mites develop resistance very quickly"],
      "prevention": ["Keep plants well-watered — stressed plants are more susceptible", "Avoid excessive nitrogen fertilisation", "Monitor plants weekly in hot, dry weather", "Avoid broad-spectrum insecticides that kill natural predators"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Tomato_-_under_attack_from_spider_mites.jpg/640px-Tomato_-_under_attack_from_spider_mites.jpg",
    "tags": ["mite", "pest", "hot-weather"]
  },
  {
    "id": "tomato-target-spot",
    "common_name": "Target Spot",
    "scientific_name": "Corynespora cassiicola",
    "crop": "Tomato",
    "severity": "Moderate",
    "description": "Target spot is an emerging fungal disease of tomatoes increasingly important in tropical and subtropical regions. It affects leaves, stems, and fruit.",
    "symptoms": [
      "Brown spots with concentric rings giving a bull-eye appearance",
      "Spots have yellow halos surrounding the lesion",
      "Lesions appear on leaves, stems, and fruit",
      "Dark brown fruit lesions that are slightly sunken",
      "Severe leaf infections cause yellowing and defoliation"
    ],
    "causes": "Caused by the fungus Corynespora cassiicola. Favoured by warm (20-30C), humid conditions. Spreads through airborne spores and infected plant material.",
    "treatment": {
      "organic": ["Remove infected plant material promptly", "Apply copper hydroxide spray every 7-10 days", "Improve air circulation around plants by pruning"],
      "chemical": ["Azoxystrobin (Amistar) provides good systemic control", "Boscalid + Pyraclostrobin (Pristine) for difficult infections", "Tebuconazole as an alternative mode of action"],
      "prevention": ["Use disease-free transplants from certified nurseries", "Rotate crops annually", "Avoid overhead irrigation", "Clean up all plant debris after harvest"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Tomato_target_spot.jpg/640px-Tomato_target_spot.jpg",
    "tags": ["fungal", "tropical", "emerging"]
  },
  {
    "id": "tomato-yellow-leaf-curl-virus",
    "common_name": "Yellow Leaf Curl Virus",
    "scientific_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
    "crop": "Tomato",
    "severity": "Severe",
    "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is one of the most devastating diseases of tomatoes in tropical and subtropical regions. Early infections can destroy entire crops. It is transmitted by the silverleaf whitefly.",
    "symptoms": [
      "Young leaves curl upward and inward, becoming cup-shaped",
      "Leaves turn yellow (chlorotic) between the veins",
      "Severely stunted plant growth",
      "Flowers drop before fruit forms, leading to near-zero yield",
      "Older leaves may appear leathery and thickened"
    ],
    "causes": "Caused by Tomato Yellow Leaf Curl Virus (TYLCV). Transmitted exclusively by the silverleaf whitefly (Bemisia tabaci). Spreads rapidly when whitefly populations are high.",
    "treatment": {
      "organic": ["Remove and destroy infected plants immediately", "Control whitefly using yellow sticky traps", "Apply neem oil or insecticidal soap to reduce whitefly", "Use reflective silver mulch to disorient whiteflies"],
      "chemical": ["Apply imidacloprid (Confidor) to control whitefly vectors", "Thiamethoxam (Actara) as soil drench or foliar spray", "No cure for the virus — vector control is the only strategy"],
      "prevention": ["CRITICAL: Plant TYLCV-resistant varieties (e.g., Tygress, Shanty)", "Use insect-proof netting to exclude whiteflies in nurseries", "Remove infected plants within 24 hours of detection", "Control weeds that host whiteflies around the field"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/TYLCV_symptoms.jpg/640px-TYLCV_symptoms.jpg",
    "tags": ["viral", "whitefly", "severe", "tropical"]
  },
  {
    "id": "tomato-mosaic-virus",
    "common_name": "Tomato Mosaic Virus",
    "scientific_name": "Tomato mosaic virus (ToMV)",
    "crop": "Tomato",
    "severity": "Moderate",
    "description": "Tomato mosaic virus is a highly stable plant virus that persists in soil and plant debris for years. It spreads mechanically during pruning and field operations.",
    "symptoms": [
      "Mosaic pattern of light and dark green on leaves",
      "Leaf distortion — leaves may appear fern-like or crinkled",
      "Stunted plant growth in early-infected plants",
      "Fruit may show internal browning or uneven ripening",
      "Yellow mottling on leaves"
    ],
    "causes": "Caused by Tomato mosaic virus (ToMV). Spreads through mechanical contact — infected sap on hands, tools, or clothing. No insect vector. Seed transmission can occur.",
    "treatment": {
      "organic": ["Remove and destroy infected plants — do not compost", "Wash hands thoroughly with soap between plants", "No cure — management focuses on removing infected plants"],
      "chemical": ["No effective chemical treatment exists for the virus", "Disinfect all tools with 10% bleach or 70% alcohol", "Treat seeds with trisodium phosphate (TSP) solution"],
      "prevention": ["Use certified virus-free seed and transplants", "Plant resistant varieties (Tm-2 or Tm-2^2 resistance gene)", "Disinfect all tools between plants during pruning", "Avoid smoking near plants", "Wash hands before entering the growing area"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Tomato_mosaic_virus_symptoms.jpg/640px-Tomato_mosaic_virus_symptoms.jpg",
    "tags": ["viral", "mechanical-transmission", "seed-borne"]
  },
  {
    "id": "maize-gray-leaf-spot",
    "common_name": "Gray Leaf Spot (Cercospora)",
    "scientific_name": "Cercospora zeae-maydis",
    "crop": "Maize",
    "severity": "Severe",
    "description": "Gray leaf spot (GLS) is the most yield-limiting foliar disease of maize globally. Under severe conditions it can cause 50%+ yield loss. Most destructive in humid climates with reduced tillage.",
    "symptoms": [
      "Long, narrow rectangular lesions running parallel between leaf veins",
      "Lesions initially appear as small tan spots with yellow halos",
      "Mature lesions are grey to tan, 1-6cm long, with distinct parallel edges",
      "Heavy infections cause large areas of leaf tissue to die",
      "Grey sporulation visible on lesion surface in humid conditions"
    ],
    "causes": "Caused by the fungus Cercospora zeae-maydis. Survives on infected corn residue. Spores spread by wind and splash. Favoured by warm (25-30C), humid conditions with prolonged dew periods.",
    "treatment": {
      "organic": ["Till crop residue into soil after harvest", "Improve air circulation through proper plant spacing", "Apply balanced fertilisation — especially potassium"],
      "chemical": ["Azoxystrobin + Propiconazole (Headline AMP) applied at tasselling", "Pyraclostrobin (Headline) for high-value crops", "Propiconazole (Tilt) as a cost-effective option"],
      "prevention": ["Plant GLS-resistant hybrids — most effective control measure", "Rotate crops with non-grass species (soybean, vegetables)", "Till crop debris to reduce inoculum", "Apply preventive fungicide at VT in high-risk years"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Gray_leaf_spot_corn.jpg/640px-Gray_leaf_spot_corn.jpg",
    "tags": ["fungal", "severe", "residue-borne", "global"]
  },
  {
    "id": "maize-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Zea mays",
    "crop": "Maize",
    "severity": "None",
    "description": "Your maize plant appears healthy! No signs of disease detected. Continue your current crop management practices.",
    "symptoms": ["Deep green leaves without spots or lesions", "Strong upright stalks with no discolouration", "Well-formed tassels and silks", "Cobs developing normally"],
    "causes": "No disease detected. Plant is in good condition.",
    "treatment": {
      "organic": ["Continue regular watering and fertilisation", "Scout weekly for pests and diseases"],
      "chemical": ["No treatment needed"],
      "prevention": ["Rotate crops next season", "Keep field free of weeds"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/640px-Camponotus_flavomarginatus_ant.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "potato-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Solanum tuberosum",
    "crop": "Potato",
    "severity": "None",
    "description": "Your potato plant appears healthy! No disease detected. Keep up your good management practices.",
    "symptoms": ["Lush, dark green compound leaves without spots", "Strong stems without discolouration", "Flowers present at appropriate growth stage", "Tubers forming normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Continue current watering and hilling practices", "Monitor weekly for late blight in wet weather"],
      "chemical": ["No treatment needed", "Apply preventive copper spray before expected wet periods"],
      "prevention": ["Keep hilling soil around stems", "Rotate location next season", "Harvest at full maturity"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Potato_plant.jpg/640px-Potato_plant.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "pepper-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Capsicum annuum",
    "crop": "Pepper",
    "severity": "None",
    "description": "Your pepper plant appears healthy! No disease detected.",
    "symptoms": ["Dark green, glossy leaves without spots", "Strong stems without lesions", "Flowers or developing fruit with no blemishes"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Maintain regular watering schedule", "Monitor weekly for pests and disease"],
      "chemical": ["No treatment needed"],
      "prevention": ["Avoid overhead irrigation", "Maintain good air circulation", "Rotate crops next season"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Capsicum_annuum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-027.jpg/640px-Capsicum_annuum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-027.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "apple-scab",
    "common_name": "Apple Scab",
    "scientific_name": "Venturia inaequalis",
    "crop": "Apple",
    "severity": "Severe",
    "description": "Apple scab is the most economically important disease of apples worldwide. Without management, it can cause near total crop loss in susceptible varieties during wet spring seasons.",
    "symptoms": [
      "Olive-green to brown, velvety or scab-like lesions on leaf surfaces",
      "Infected leaves may yellow and drop prematurely",
      "Dark, rough, scab-like lesions on fruit surface",
      "Fruit lesions crack and allow entry of secondary rots",
      "Severely affected fruit is unmarketable"
    ],
    "causes": "Caused by the fungus Venturia inaequalis. Overwinters in infected fallen leaves. Releases spores during spring rains when temperatures are above 6C.",
    "treatment": {
      "organic": ["Rake and destroy fallen leaves in autumn", "Apply copper or sulphur fungicide at bud break", "Apply lime sulphur spray during dormant season"],
      "chemical": ["Apply Captan from green tip stage every 7-14 days", "Myclobutanil (Rally) for post-infection curative control within 72 hours", "Trifloxystrobin (Flint) for both protective and curative activity"],
      "prevention": ["Plant resistant apple varieties (e.g., Liberty, Freedom, Redfree)", "Prune trees to open the canopy", "Use a predictive spray programme", "Mow and remove fallen leaves in autumn", "Avoid overhead irrigation during critical infection period"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Malus_pumila_Mela_arancia_rust.JPG/640px-Malus_pumila_Mela_arancia_rust.JPG",
    "tags": ["fungal", "severe", "temperate", "economic"]
  },
  {
    "id": "apple-black-rot",
    "common_name": "Black Rot",
    "scientific_name": "Botryosphaeria obtusa",
    "crop": "Apple",
    "severity": "Moderate",
    "description": "Apple black rot affects fruit, leaves, and bark. Infected fruit becomes mummified and hangs on the tree as a source of inoculum for future seasons.",
    "symptoms": [
      "Purple spots on leaves that enlarge to form frog-eye lesions with brown centres",
      "Fruit rot beginning as small purple spots, expanding to large black rot",
      "Infected fruit becomes mummified — shrivelled, black, and hard",
      "Dark, sunken cankers on limbs and trunk",
      "Cankers can girdle branches causing dieback"
    ],
    "causes": "Caused by the fungus Botryosphaeria obtusa. Survives in mummified fruit, dead bark, and cankers. Spreads by rain-splashed spores.",
    "treatment": {
      "organic": ["Remove all mummified fruit and dead wood immediately", "Apply copper fungicide sprays from pink stage", "Paint wound dressings on pruning cuts"],
      "chemical": ["Captan sprays from pink through cover", "Thiophanate-methyl for canker control", "Myclobutanil during summer months"],
      "prevention": ["Prune out all dead and cankered wood during dormancy", "Remove mummified fruit — primary inoculum source", "Avoid tree stress through proper nutrition and irrigation", "Protect trees from fire blight wounds"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Apple_black_rot.jpg/640px-Apple_black_rot.jpg",
    "tags": ["fungal", "fruit-rot", "canker"]
  },
  {
    "id": "apple-cedar-rust",
    "common_name": "Cedar Apple Rust",
    "scientific_name": "Gymnosporangium juniperi-virginianae",
    "crop": "Apple",
    "severity": "Moderate",
    "description": "Cedar apple rust requires two different host plants to complete its life cycle — apple trees and Eastern red cedar. It causes bright orange spots on apple leaves and fruit.",
    "symptoms": [
      "Bright orange-yellow spots with slightly raised centres on upper leaf surface",
      "Small tube-like structures (aecia) on the underside of leaf spots",
      "Lesions on fruit and young stems in severe infections",
      "Early defoliation in heavily infected trees",
      "Orange gelatinous horns visible on nearby juniper trees in spring"
    ],
    "causes": "Caused by the fungus Gymnosporangium juniperi-virginianae. Alternates between Eastern red cedar/juniper and apple. Spores released from cedar galls during wet spring weather infect apple.",
    "treatment": {
      "organic": ["Remove nearby Eastern red cedar trees if feasible", "Apply sulphur fungicide at petal fall stage", "Apply copper spray at bud break as preventive"],
      "chemical": ["Myclobutanil (Rally) or Trifloxystrobin from pink stage", "Apply at 7-10 day intervals from pink through 3rd cover spray", "Propiconazole as an alternative fungicide"],
      "prevention": ["Plant resistant apple varieties (e.g., Liberty, Redfree)", "Remove Eastern red cedar trees within 300m if possible", "Apply protective fungicides starting at bud break"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Cedar_apple_rust_gall.jpg/640px-Cedar_apple_rust_gall.jpg",
    "tags": ["fungal", "rust", "two-host", "temperate"]
  },
  {
    "id": "apple-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Malus domestica",
    "crop": "Apple",
    "severity": "None",
    "description": "Your apple tree appears healthy! No disease detected.",
    "symptoms": ["Dark green, glossy leaves without spots or distortion", "Clean fruit developing without blemishes", "Healthy bark without cankers"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Maintain regular pruning for good air circulation", "Monitor monthly for pests and disease"],
      "chemical": ["No treatment needed"],
      "prevention": ["Keep orchard floor clean of fallen fruit and leaves", "Prune annually during dormancy"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/640px-Red_Apple.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "grape-black-rot",
    "common_name": "Black Rot",
    "scientific_name": "Guignardia bidwellii",
    "crop": "Grape",
    "severity": "Severe",
    "description": "Grape black rot is one of the most destructive diseases of grapes in humid climates. Under favourable conditions, entire clusters can be lost. Infected berries shrivel into hard, black mummies.",
    "symptoms": [
      "Small tan spots with dark brown margins on leaves",
      "Black pimple-like structures (pycnidia) in the centre of leaf lesions",
      "Infected berries turn brown then rapidly shrivel and turn black",
      "Black mummified berries remain attached to cluster",
      "Brown elongated lesions on young shoots and tendrils"
    ],
    "causes": "Caused by the fungus Guignardia bidwellii. Overwinters in mummified berries and infected canes. Critical infection period is from bloom to 3-4 weeks after bloom.",
    "treatment": {
      "organic": ["Remove all mummified berries", "Apply copper or sulphur fungicide from bud break through 4-6 weeks post-bloom", "Remove and destroy infected clusters immediately"],
      "chemical": ["Myclobutanil (Rally) from pre-bloom through cover sprays", "Tebuconazole (Elite) for systemic curative control", "Captan as a broad-spectrum protective spray"],
      "prevention": ["Remove all mummified fruit and infected canes during winter pruning", "Train vines to improve air circulation", "Apply protective fungicide sprays from bud break"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Guignardia_bidwellii_on_grape.jpg/640px-Guignardia_bidwellii_on_grape.jpg",
    "tags": ["fungal", "severe", "fruit-rot", "temperate"]
  },
  {
    "id": "grape-esca",
    "common_name": "Esca (Black Measles)",
    "scientific_name": "Phaeoacremonium aleophilum",
    "crop": "Grape",
    "severity": "Severe",
    "description": "Esca (Black Measles) is a complex grapevine trunk disease causing chronic decline and sudden vine death. It has become increasingly important worldwide.",
    "symptoms": [
      "Interveinal yellowing (white grapes) or reddening (red grapes) in a tiger-stripe pattern",
      "Berries develop small dark spots with purple borders — the black measles symptom",
      "Internal wood shows dark streaking when canes are cut",
      "Sudden wilting and death of entire vine in hot weather (apoplexy)",
      "Annual recurrence of foliar symptoms with progressive decline"
    ],
    "causes": "Caused by a complex of wood-rotting fungi. Enters through pruning wounds. Spreads through infected planting material and pruning tools.",
    "treatment": {
      "organic": ["Paint all pruning cuts with Trichoderma wound sealant", "Remove severely affected vines and replant", "Use double pruning technique to minimise wound size"],
      "chemical": ["No fully effective curative treatment exists", "Apply wound protectant (Thiophanate-methyl) immediately after pruning", "Trunk surgery to remove infected wood"],
      "prevention": ["Prune during dry weather to reduce spore dispersal", "Apply wound protectant immediately after every pruning cut", "Disinfect pruning tools with 10% bleach between vines", "Source certified clean planting material"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Esca_on_grapevine_leaves.jpg/640px-Esca_on_grapevine_leaves.jpg",
    "tags": ["fungal", "trunk-disease", "severe", "chronic"]
  },
  {
    "id": "grape-leaf-blight",
    "common_name": "Isariopsis Leaf Blight",
    "scientific_name": "Isariopsis clavispora",
    "crop": "Grape",
    "severity": "Moderate",
    "description": "Grape leaf blight causes irregular brown lesions on leaves and defoliation. It typically appears later in the season.",
    "symptoms": [
      "Large irregular dark brown lesions on leaf margins and between veins",
      "Lesions may have a darker brown border with lighter brown interior",
      "Infected leaves turn yellow and drop prematurely",
      "Lesions on fruit stems can cause berry drop"
    ],
    "causes": "Caused by the fungus Isariopsis clavispora. Favoured by warm, humid conditions. Often occurs as a secondary disease.",
    "treatment": {
      "organic": ["Remove infected leaves to reduce inoculum", "Apply copper-based fungicide spray", "Improve canopy management to increase air flow"],
      "chemical": ["Mancozeb as protective spray", "Myclobutanil for systemic control", "Apply during routine mildew spray programme"],
      "prevention": ["Maintain open canopy through leaf removal", "Apply routine fungicide programme from bud break", "Avoid overhead irrigation"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Grapevine_leaf_blight.jpg/640px-Grapevine_leaf_blight.jpg",
    "tags": ["fungal", "defoliation", "secondary"]
  },
  {
    "id": "grape-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Vitis vinifera",
    "crop": "Grape",
    "severity": "None",
    "description": "Your grapevine appears healthy! No disease detected.",
    "symptoms": ["Bright green undistorted leaves without spots", "Clean shoot growth", "Berries developing uniformly"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Continue routine canopy management", "Monitor fortnightly for disease and pests"],
      "chemical": ["No treatment needed"],
      "prevention": ["Maintain open canopy for good air circulation", "Scout regularly throughout the growing season"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Premi%C3%A8res_Vendanges_de_l%27ann%C3%A9e_-_First_Harvest_of_the_Year_%286087949716%29.jpg/640px-Premi%C3%A8res_Vendanges_de_l%27ann%C3%A9e_-_First_Harvest_of_the_Year_%286087949716%29.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "strawberry-leaf-scorch",
    "common_name": "Leaf Scorch",
    "scientific_name": "Diplocarpon earlianum",
    "crop": "Strawberry",
    "severity": "Moderate",
    "description": "Strawberry leaf scorch weakens plants by reducing photosynthetic area. Severe infections can kill plants and reduce runner production significantly.",
    "symptoms": [
      "Small irregular purple to dark red spots on upper leaf surface",
      "Spots coalesce giving the leaf a scorched or burnt appearance",
      "Heavily infected leaves turn brown-purple and die",
      "Lesions may appear on petioles, runners, and fruit stalks",
      "Plant vigour and yield reduced in chronic infections"
    ],
    "causes": "Caused by the fungus Diplocarpon earlianum. Survives on infected plant debris. Spreads by rain splash. Favoured by wet conditions and mild temperatures (15-25C).",
    "treatment": {
      "organic": ["Remove and destroy infected leaves", "Apply copper-based fungicide every 7-10 days", "Improve drainage and air circulation around plants"],
      "chemical": ["Captan spray every 7-14 days during wet weather", "Myclobutanil for systemic control", "Pyraclostrobin for curative and protective activity"],
      "prevention": ["Plant disease-resistant varieties", "Renovate strawberry beds annually after fruiting", "Avoid overhead irrigation", "Remove all old leaves and debris after harvest"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Strawberry_leaf_scorch.jpg/640px-Strawberry_leaf_scorch.jpg",
    "tags": ["fungal", "common", "defoliation"]
  },
  {
    "id": "strawberry-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Fragaria x ananassa",
    "crop": "Strawberry",
    "severity": "None",
    "description": "Your strawberry plant appears healthy! No disease detected.",
    "symptoms": ["Dark green, undistorted leaves without spots", "Healthy runners and crowns", "Fruit developing normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Maintain regular watering", "Apply straw mulch to keep fruit clean"],
      "chemical": ["No treatment needed"],
      "prevention": ["Renovate bed annually", "Rotate planting site every 3-4 years"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/PerfectStrawberry.jpg/640px-PerfectStrawberry.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "cherry-powdery-mildew",
    "common_name": "Powdery Mildew",
    "scientific_name": "Podosphaera clandestina",
    "crop": "Cherry",
    "severity": "Moderate",
    "description": "Powdery mildew is a common and disfiguring disease of sweet and sour cherries, causing significant losses in young orchards and affecting fruit quality.",
    "symptoms": [
      "White powdery coating on leaf surfaces, shoots, and young fruit",
      "Infected leaves curl, pucker, and become distorted",
      "Affected shoots are stunted and may die back",
      "Fruit develops a rough, russeted appearance",
      "Defoliation of infected shoots late in the season"
    ],
    "causes": "Caused by the fungus Podosphaera clandestina. Thrives in warm (20-27C) conditions with high humidity at night. Does not need free water to infect.",
    "treatment": {
      "organic": ["Apply potassium bicarbonate spray — disrupts fungal cell walls", "Spray neem oil every 7 days", "Apply sulphur fungicide (not above 32C)"],
      "chemical": ["Myclobutanil (Rally) as systemic curative treatment", "Trifloxystrobin (Flint) for protective and curative activity", "Tebuconazole as alternative — rotate to prevent resistance"],
      "prevention": ["Plant resistant cherry varieties where available", "Apply preventive fungicide from pink stage of bud development", "Prune to maintain open canopy", "Avoid excessive nitrogen fertilisation"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Powdery_mildew_on_pumpkin_plant.jpg/640px-Powdery_mildew_on_pumpkin_plant.jpg",
    "tags": ["fungal", "powdery-mildew", "dry-weather"]
  },
  {
    "id": "cherry-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Prunus avium",
    "crop": "Cherry",
    "severity": "None",
    "description": "Your cherry plant appears healthy! No disease detected.",
    "symptoms": ["Deep green glossy leaves without distortion", "Healthy shoot growth", "Fruit developing normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Maintain regular monitoring", "Apply balanced fertilisation"],
      "chemical": ["No treatment needed"],
      "prevention": ["Continue regular orchard hygiene", "Prune annually for good air circulation"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Cherry_Blossoms_in_Vancouver_3.jpg/640px-Cherry_Blossoms_in_Vancouver_3.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "squash-powdery-mildew",
    "common_name": "Powdery Mildew",
    "scientific_name": "Podosphaera xanthii",
    "crop": "Squash",
    "severity": "Moderate",
    "description": "Powdery mildew is the most common disease of cucurbits (squash, pumpkin, cucumber, melon). It reduces yield and quality and causes premature senescence.",
    "symptoms": [
      "White to light grey powdery spots on upper and lower leaf surfaces",
      "Spots enlarge and merge, eventually covering the entire leaf",
      "Infected leaves yellow, brown, and die prematurely",
      "Stems and petioles may also be infected",
      "Fruit smaller due to reduced photosynthesis"
    ],
    "causes": "Caused by the fungus Podosphaera xanthii. Thrives in warm (20-30C) conditions with high humidity at night but dry days. Spreads rapidly through airborne spores.",
    "treatment": {
      "organic": ["Apply potassium bicarbonate spray (2 tbsp per litre) — very effective", "Spray neem oil every 7 days on both leaf surfaces", "Apply diluted milk spray (40% milk, 60% water)"],
      "chemical": ["Myclobutanil systemic fungicide for established infections", "Azoxystrobin for both protection and eradication", "Sulphur (avoid above 32C)"],
      "prevention": ["Plant resistant squash varieties", "Ensure adequate plant spacing", "Avoid excessive nitrogen fertilisation", "Remove and destroy infected leaves early"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Powdery_mildew_on_pumpkin_plant.jpg/640px-Powdery_mildew_on_pumpkin_plant.jpg",
    "tags": ["fungal", "powdery-mildew", "cucurbit", "common"]
  },
  {
    "id": "orange-citrus-greening",
    "common_name": "Citrus Greening (Huanglongbing)",
    "scientific_name": "Candidatus Liberibacter asiaticus",
    "crop": "Orange",
    "severity": "Severe",
    "description": "Citrus greening (Huanglongbing/HLB) is the most destructive citrus disease in the world. There is no cure. It has devastated citrus industries across Asia, Africa, and the Americas.",
    "symptoms": [
      "Asymmetric yellowing (blotchy mottle) of leaves",
      "Shoots with small, upright, yellow leaves",
      "Small, misshapen, bitter fruit that remains green at maturity",
      "Fruit drops prematurely and seeds abort",
      "Progressive dieback of branches; eventual death of tree"
    ],
    "causes": "Caused by the bacterium Candidatus Liberibacter asiaticus. Transmitted by the Asian citrus psyllid insect (Diaphorina citri). Also spreads through infected budwood.",
    "treatment": {
      "organic": ["Remove and destroy all infected trees immediately", "Control psyllid vector using organic-approved insecticides", "No cure — removal is the only management option"],
      "chemical": ["Control Asian citrus psyllid with imidacloprid soil drench", "Thiamethoxam (Actara) for vector control", "Nutritional sprays (zinc, micronutrients) can slow decline but do not cure"],
      "prevention": ["Source certified HLB-free planting material ONLY", "Install insect-proof screens in nurseries", "Monitor trees monthly for psyllid insects", "Report any suspect trees to your extension officer immediately"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Citrus_greening_disease.jpg/640px-Citrus_greening_disease.jpg",
    "tags": ["bacterial", "severe", "incurable", "psyllid", "global"]
  },
  {
    "id": "peach-bacterial-spot",
    "common_name": "Bacterial Spot",
    "scientific_name": "Xanthomonas arboricola pv. pruni",
    "crop": "Peach",
    "severity": "Moderate",
    "description": "Bacterial spot is one of the most serious diseases of peaches and nectarines, causing significant economic losses in warm, humid growing regions.",
    "symptoms": [
      "Small water-soaked spots on leaves that turn brown with purple margins and yellow halos",
      "Infected leaf spots fall out leaving a shot-hole appearance",
      "Heavily infected leaves turn yellow and drop prematurely",
      "Small circular dark water-soaked spots on fruit that become sunken and cracked",
      "Dark elongated lesions on young twigs"
    ],
    "causes": "Caused by Xanthomonas arboricola pv. pruni bacteria. Survives in infected twigs and buds. Spreads by wind-driven rain during spring.",
    "treatment": {
      "organic": ["Apply copper hydroxide sprays every 5-7 days", "Avoid working in the orchard when trees are wet", "Remove mummified fruit and infected twigs during dormant pruning"],
      "chemical": ["Copper hydroxide + Mancozeb combination during wet periods", "Oxytetracycline antibiotic spray (where permitted)", "Apply protective sprays before expected rain events"],
      "prevention": ["Plant resistant varieties (e.g., Redhaven, Reliance, Contender)", "Prune for good air circulation", "Avoid low-lying sites with poor air drainage", "Apply dormant copper spray before bud swell"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Bacterial_spot_peach_leaf.jpg/640px-Bacterial_spot_peach_leaf.jpg",
    "tags": ["bacterial", "fruit-quality", "temperate"]
  },
  {
    "id": "peach-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Prunus persica",
    "crop": "Peach",
    "severity": "None",
    "description": "Your peach tree appears healthy! No disease detected.",
    "symptoms": ["Dark green undistorted leaves without spots", "Clean shoot growth", "Fruit developing normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Maintain regular irrigation", "Monitor monthly for pests and disease"],
      "chemical": ["No treatment needed"],
      "prevention": ["Continue dormant pruning programme", "Apply dormant copper spray annually"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Autumn_Red_peaches.jpg/640px-Autumn_Red_peaches.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "soybean-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Glycine max",
    "crop": "Soybean",
    "severity": "None",
    "description": "Your soybean plant appears healthy! No disease detected.",
    "symptoms": ["Trifoliate leaves are dark green and undistorted", "Stem shows no lesions", "Pods developing normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Continue regular monitoring", "Maintain soil health"],
      "chemical": ["No treatment needed"],
      "prevention": ["Rotate with non-legume crops next season", "Use certified disease-free seed"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Soybean_plant.jpg/640px-Soybean_plant.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "raspberry-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Rubus idaeus",
    "crop": "Raspberry",
    "severity": "None",
    "description": "Your raspberry plant appears healthy! No disease detected.",
    "symptoms": ["Pinnate leaves are dark green without spots", "Canes are vigorous without lesions", "Fruit developing normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Continue regular watering and fertilisation", "Tie canes to supports for good air circulation"],
      "chemical": ["No treatment needed"],
      "prevention": ["Remove old fruited canes after harvest", "Rotate planting site every 5 years"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Big_and_tasty_raspberries_-_%28_now_21_Megapixels_%29.jpg/640px-Big_and_tasty_raspberries_-_%28_now_21_Megapixels_%29.jpg",
    "tags": ["healthy"]
  },
  {
    "id": "blueberry-healthy",
    "common_name": "Healthy Plant",
    "scientific_name": "Vaccinium corymbosum",
    "crop": "Blueberry",
    "severity": "None",
    "description": "Your blueberry plant appears healthy! No disease detected.",
    "symptoms": ["Small oval leaves are green and healthy", "Stems are reddish and vigorous", "Berries developing normally"],
    "causes": "No disease detected.",
    "treatment": {
      "organic": ["Maintain soil pH at 4.5-5.5", "Apply acidic mulch (pine bark, sawdust)", "Monitor for mummy berry and other diseases"],
      "chemical": ["No treatment needed"],
      "prevention": ["Maintain correct soil pH", "Prune annually for good air circulation"]
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Blueberries.jpg/640px-Blueberries.jpg",
    "tags": ["healthy"]
  }
]

with open("diseases.json") as f:
    existing = json.load(f)

existing_ids = {d["id"] for d in existing}
added = 0
for d in new_diseases:
    if d["id"] not in existing_ids:
        existing.append(d)
        added += 1

with open("diseases.json", "w") as f:
    json.dump(existing, f, indent=2)

print(f"Added {added} diseases. Total: {len(existing)}")
