from pymongo import MongoClient
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "celestial_wordforge")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Données pour le mode Vocabulaire - Mots-croisés
crossword_data = [
    {"word": "ephemeral", "definition": "Lasting for a very short time", "difficulty": 2},
    {"word": "ubiquitous", "definition": "Present, appearing, or found everywhere", "difficulty": 3},
    {"word": "serendipity", "definition": "The occurrence of events by chance in a beneficial way", "difficulty": 2},
    {"word": "eloquent", "definition": "Fluent or persuasive in speaking or writing", "difficulty": 1},
    {"word": "paradox", "definition": "A statement that contradicts itself but might be true", "difficulty": 1},
    {"word": "quintessential", "definition": "Representing the most perfect or typical example of a quality or class", "difficulty": 3},
    {"word": "ambiguous", "definition": "Open to more than one interpretation", "difficulty": 2},
    {"word": "facetious", "definition": "Treating serious issues with deliberately inappropriate humor", "difficulty": 3},
    {"word": "magnanimous", "definition": "Generous or forgiving, especially toward a rival or less powerful person", "difficulty": 2},
    {"word": "obfuscate", "definition": "Render obscure, unclear, or unintelligible", "difficulty": 3},
    {"word": "perplex", "definition": "Cause someone to feel completely baffled", "difficulty": 2},
    {"word": "ravenous", "definition": "Extremely hungry", "difficulty": 1},
    {"word": "vex", "definition": "Make someone feel annoyed or frustrated", "difficulty": 1},
    {"word": "zealot", "definition": "A person who is fanatical and uncompromising in pursuit of their ideals", "difficulty": 2},
    {"word": "jubilant", "definition": "Feeling or expressing great happiness and triumph", "difficulty": 1},
    {"word": "auspicious", "definition": "Conducive to success; favorable", "difficulty": 2},
    {"word": "cacophony", "definition": "A harsh, discordant mixture of sounds", "difficulty": 3},
    {"word": "debilitate", "definition": "Make someone weak and infirm", "difficulty": 2},
    {"word": "effervescent", "definition": "Vivacious and enthusiastic", "difficulty": 3},
    {"word": "furtive", "definition": "Attempting to avoid notice or attention, typically because of guilt", "difficulty": 2},
    {"word": "gregarious", "definition": "Fond of company; sociable", "difficulty": 1},
    {"word": "harbinger", "definition": "A person or thing that announces or signals the approach of another", "difficulty": 3},
    {"word": "innate", "definition": "Inborn; natural", "difficulty": 1},
    {"word": "juxtapose", "definition": "Place or deal with close together for contrasting effect", "difficulty": 3},
    {"word": "labyrinth", "definition": "A complicated irregular network of passages or paths", "difficulty": 2},
    {"word": "mellifluous", "definition": "Sweet or musical; pleasant to hear", "difficulty": 3},
    {"word": "nefarious", "definition": "Wicked, criminal, or villainous", "difficulty": 2},
    {"word": "oblivious", "definition": "Not aware of or concerned about what is happening around one", "difficulty": 1},
    {"word": "placate", "definition": "Make someone less angry or hostile", "difficulty": 2},
    {"word": "quagmire", "definition": "A difficult, complex, or hazardous situation", "difficulty": 3},
    {"word": "reticent", "definition": "Not revealing one's thoughts or feelings readily", "difficulty": 2},
    {"word": "scrupulous", "definition": "Diligent, thorough, and extremely attentive to details", "difficulty": 3},
    {"word": "taciturn", "definition": "Reserved or uncommunicative in speech", "difficulty": 2},
    {"word": "vindicate", "definition": "Clear someone of blame or suspicion", "difficulty": 2},
    {"word": "whimsical", "definition": "Playfully quaint or fanciful", "difficulty": 1},
    {"word": "xenophobia", "definition": "Dislike of or prejudice against people from other countries", "difficulty": 3},
    {"word": "yearn", "definition": "Have an intense feeling of longing for something", "difficulty": 1},
    {"word": "zephyr", "definition": "A soft, gentle breeze", "difficulty": 3},
    {"word": "antithesis", "definition": "A person or thing that is the direct opposite", "difficulty": 2},
    {"word": "benevolent", "definition": "Well-meaning and kindly", "difficulty": 1},
    {"word": "capitulate", "definition": "Cease to resist an opponent or an unwelcome demand", "difficulty": 2},
    {"word": "dilapidated", "definition": "In a state of disrepair or ruin due to age or neglect", "difficulty": 3},
    {"word": "eclectic", "definition": "Deriving ideas from a broad and diverse range of sources", "difficulty": 3},
    {"word": "flabbergasted", "definition": "Extremely surprised or shocked", "difficulty": 2},
    {"word": "haphazard", "definition": "Lacking any obvious principle of organization", "difficulty": 3},
    {"word": "impeccable", "definition": "In accordance with the highest standards; faultless", "difficulty": 2},
    {"word": "AREA", "definition": "Part of a place, town, or country", "difficulty": 1},
    {"word": "IDEA", "definition": "A thought, suggestion, or plan", "difficulty": 1},
    {"word": "READ", "definition": "Look at and comprehend written material", "difficulty": 1},
    {"word": "EASY", "definition": "Achieved without great effort; not difficult", "difficulty": 1},
    {"word": "LOUD", "definition": "Producing or capable of producing much noise", "difficulty": 1},
    {"word": "OPEN", "definition": "Allowing access, passage, or a view; not closed", "difficulty": 1},
    {"word": "HAPPY", "definition": "Feeling or showing pleasure or contentment", "difficulty": 1},
    {"word": "FAST", "definition": "Moving or capable of moving at high speed", "difficulty": 1},
    {"word": "COLD", "definition": "Of or at a low or relatively low temperature", "difficulty": 1},
    {"word": "GOOD", "definition": "To be desired or approved of", "difficulty": 1},
    {"word": "NEW", "definition": "Produced, introduced, or discovered recently", "difficulty": 1},
    {"word": "BIG", "definition": "Of considerable size or extent", "difficulty": 1},
    {"word": "WET", "definition": "Covered or saturated with water or another liquid", "difficulty": 1},
    {"word": "EAT", "definition": "Put food into the mouth and chew and swallow it", "difficulty": 1},
    {"word": "WALK", "definition": "Move at a regular pace by lifting and setting down each foot", "difficulty": 1},
    {"word": "TALK", "definition": "Speak in order to give information or express ideas", "difficulty": 1},
    {"word": "WORK", "definition": "Activity involving mental or physical effort", "difficulty": 1},
    {"word": "PLAY", "definition": "Engage in activity for enjoyment and recreation", "difficulty": 1},
    {"word": "CLEAN", "definition": "Free from dirt, marks, or stains", "difficulty": 1},
    {"word": "LIGHT", "definition": "The natural agent that stimulates sight", "difficulty": 1},
    {"word": "QUIET", "definition": "Making little or no noise", "difficulty": 1},
    {"word": "SOFT", "definition": "Easy to mold, cut, compress, or fold", "difficulty": 1},
    {"word": "SAFE", "definition": "Protected from or not exposed to danger or risk", "difficulty": 1},
    {"word": "TRUE", "definition": "In accordance with fact or reality", "difficulty": 1},
    {"word": "KIND", "definition": "Having or showing a friendly, generous nature", "difficulty": 1},
    {"word": "RICH", "definition": "Having a great deal of money or assets", "difficulty": 1},
    {"word": "EARLY", "definition": "Happening or done before the usual or expected time", "difficulty": 1},
    {"word": "FRESH", "definition": "Newly made or obtained; not stale", "difficulty": 1},
    {"word": "EMPTY", "definition": "Containing nothing; not filled or occupied", "difficulty": 1},
    {"word": "SIMPLE", "definition": "Easily understood or done; presenting no difficulty", "difficulty": 1},
    {"word": "ABATE", "definition": "Become less intense or widespread", "difficulty": 2},
    {"word": "ADROIT", "definition": "Clever or skillful in using the hands or mind", "difficulty": 2},
    {"word": "ALLUDE", "definition": "Suggest or call attention to indirectly; hint at", "difficulty": 2},
    {"word": "ASSUAGE", "definition": "Make (an unpleasant feeling) less intense", "difficulty": 2},
    {"word": "ASTUTE", "definition": "Accurately assessing situations or people; shrewd", "difficulty": 2},
    {"word": "BANAL", "definition": "So lacking in originality as to be obvious and boring", "difficulty": 2},
    {"word": "BELIE", "definition": "Fail to give a true notion or impression of; disguise", "difficulty": 2},
    {"word": "CANDID", "definition": "Truthful and straightforward; frank", "difficulty": 2},
    {"word": "CAJOLE", "definition": "Persuade someone to do something by coaxing or flattery", "difficulty": 2},
    {"word": "CHIDE", "definition": "Scold or rebuke", "difficulty": 2},
    {"word": "CONCISE", "definition": "Giving much information clearly and in few words; brief", "difficulty": 2},
    {"word": "CURTAIL", "definition": "Reduce in extent or quantity; impose a restriction on", "difficulty": 2},
    {"word": "DAUNT", "definition": "Make someone feel intimidated or apprehensive", "difficulty": 2},
    {"word": "DEFT", "definition": "Neatly skillful and quick in one's movements", "difficulty": 2},
    {"word": "DERIDE", "definition": "Express contempt for; ridicule", "difficulty": 2},
    {"word": "DOCILE", "definition": "Ready to accept control or instruction; submissive", "difficulty": 2},
    {"word": "ELUDE", "definition": "Evade or escape from (danger, enemy, etc.), typically skillfully", "difficulty": 2},
    {"word": "ENIGMA", "definition": "A person or thing that is mysterious, puzzling, or difficult to understand", "difficulty": 2},
    {"word": "EXALT", "definition": "Hold (someone or something) in very high regard; think or speak highly of", "difficulty": 2},
    {"word": "FORAGE", "definition": "Search widely for food or provisions", "difficulty": 2},
    {"word": "GENIAL", "definition": "Friendly and cheerful", "difficulty": 2},
    {"word": "GRIMACE", "definition": "An ugly, twisted expression indicating pain, disgust, or wry amusement", "difficulty": 2},
    {"word": "IMPEDE", "definition": "Delay or prevent (someone or something) by obstructing them; hinder", "difficulty": 2},
    {"word": "INCITE", "definition": "Encourage or stir up (violent or unlawful behavior)", "difficulty": 2},
    {"word": "INSIPID", "definition": "Lacking flavor; weak or tasteless", "difficulty": 2},
    {"word": "JADED", "definition": "Tired, bored, or lacking enthusiasm, typically after having too much of something", "difficulty": 2},
    {"word": "LAMENT", "definition": "A passionate expression of grief or sorrow", "difficulty": 2},
    {"word": "MALICE", "definition": "The intention or desire to do evil; ill will", "difficulty": 2},
    {"word": "MOROSE", "definition": "Sullen and ill-tempered", "difficulty": 2},
    {"word": "NOVICE", "definition": "A person new to or inexperienced in a field or situation", "difficulty": 2},
    {"word": "OPAQUE", "definition": "Not able to be seen through; not transparent", "difficulty": 2},
    {"word": "PIQUE", "definition": "A feeling of irritation or resentment resulting from a slight", "difficulty": 2},
    {"word": "PRAGMATIC", "definition": "Dealing with things sensibly and realistically", "difficulty": 2},
    {"word": "PROLIFIC", "definition": "Producing many works, results, or offspring; fruitful", "difficulty": 2},
    {"word": "QUASH", "definition": "Reject or void, especially by legal procedure", "difficulty": 2},
    {"word": "REFUTE", "definition": "Prove (a statement or theory) to be wrong or false", "difficulty": 2},
    {"word": "REMISS", "definition": "Lacking care or attention to duty; negligent", "difficulty": 2},
    {"word": "REVERE", "definition": "Feel deep respect or admiration for (something)", "difficulty": 2},
    {"word": "SAVVY", "definition": "Shrewdness and practical knowledge; the ability to make good judgments", "difficulty": 2},
    {"word": "SPURN", "definition": "Reject with disdain or contempt", "difficulty": 2},
    {"word": "ABERRATION", "definition": "A departure from what is normal, usual, or expected", "difficulty": 3},
    {"word": "ACRIMONIOUS", "definition": "Typically of speech or debate; angry and bitter", "difficulty": 3},
    {"word": "ALACRITY", "definition": "Brisk and cheerful readiness", "difficulty": 3},
    {"word": "ANATHEMA", "definition": "Something or someone that one vehemently dislikes", "difficulty": 3},
    {"word": "APOCRYPHAL", "definition": "Of doubtful authenticity, although widely circulated as true", "difficulty": 3},
    {"word": "ASCETIC", "definition": "Characterized by severe self-discipline and abstention", "difficulty": 3},
    {"word": "BALEFUL", "definition": "Threatening harm; menacing", "difficulty": 3},
    {"word": "BELLICOSE", "definition": "Demonstrating aggression and willingness to fight", "difficulty": 3},
    {"word": "BILK", "definition": "Obtain or withhold money from (someone) unfairly; cheat or defraud", "difficulty": 3},
    {"word": "BOMBASTIC", "definition": "High-sounding but with little meaning; inflated", "difficulty": 3},
    {"word": "COGENT", "definition": "Clear, logical, and convincing (of an argument or case)", "difficulty": 3},
    {"word": "CONTRITE", "definition": "Feeling or expressing remorse or penitence; affected by guilt", "difficulty": 3},
    {"word": "CONVIVIAL", "definition": "Friendly, lively, and enjoyable (of an atmosphere or event)", "difficulty": 3},
    {"word": "CUPIDITY", "definition": "Greed for money or possessions", "difficulty": 3},
    {"word": "DELETERIOUS", "definition": "Causing harm or damage", "difficulty": 3},
    {"word": "DIDACTIC", "definition": "Intended to teach, particularly having moral instruction as an ulterior motive", "difficulty": 3},
    {"word": "DISSEMBLE", "definition": "Conceal one's true motives, feelings, or beliefs", "difficulty": 3},
    {"word": "EBULLIENT", "definition": "Cheerful and full of energy", "difficulty": 3},
    {"word": "ENERVATE", "definition": "Cause (someone) to feel drained of energy or vitality; weaken", "difficulty": 3},
    {"word": "ERUDITE", "definition": "Having or showing great knowledge or learning", "difficulty": 3},
    {"word": "ESOTERIC", "definition": "Intended for only a small number of people with specialized knowledge", "difficulty": 3},
    {"word": "EVANESCENT", "definition": "Soon passing out of sight, memory, or existence; quickly fading", "difficulty": 3},
    {"word": "EXACERBATE", "definition": "Make (a problem, bad situation, or negative feeling) worse", "difficulty": 3},
    {"word": "EXCULPATE", "definition": "Show or declare that (someone) is not guilty of wrongdoing", "difficulty": 3},
    {"word": "EXIGENT", "definition": "Pressing; demanding", "difficulty": 3},
    {"word": "EXTOL", "definition": "Praise enthusiastically", "difficulty": 3},
    {"word": "FATUOUS", "definition": "Silly and pointless", "difficulty": 3},
    {"word": "FLAGRANT", "definition": "Conspicuously or obviously offensive", "difficulty": 3},
    {"word": "GRANDILOQUENT", "definition": "Pompous or extravagant in language, style, or manner", "difficulty": 3},
    {"word": "HEGEMONY", "definition": "Leadership or dominance, especially by one country or group", "difficulty": 3},
    {"word": "ICONOCLAST", "definition": "A person who attacks cherished beliefs or institutions", "difficulty": 3},
    {"word": "IDIOSYNCRASY", "definition": "A mode of behavior or way of thought peculiar to an individual", "difficulty": 3},
    {"word": "IGNOMINIOUS", "definition": "Deserving or causing public disgrace or shame", "difficulty": 3},
    {"word": "IMPERVIOUS", "definition": "Not allowing fluid to pass through; unable to be affected by", "difficulty": 3},
    {"word": "IMPETUOUS", "definition": "Acting or done quickly and without thought or care", "difficulty": 3},
    {"word": "INCHOATE", "definition": "Just begun and not fully formed; rudimentary", "difficulty": 3},
    {"word": "INDOLENT", "definition": "Wanting to avoid activity or exertion; lazy", "difficulty": 3},
    {"word": "INEFFABLE", "definition": "Too great or extreme to be expressed or described in words", "difficulty": 3},
    {"word": "INEXORABLE", "definition": "Impossible to stop or prevent", "difficulty": 3},
    {"word": "LACONIC", "definition": "Using very few words (of a person, speech, or style of writing)", "difficulty": 3}
]

# Données pour le mode Vocabulaire - Texte à trous
gap_fill_data = [
    {
        "text": "The {1} of social media on society is both {2} and {3}.",
        "words": ["impact", "profound", "complex"],
        "definitions": [
            "The effect or influence of one thing on another",
            "Very great or intense",
            "Consisting of many different and connected parts"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} between the two countries was finally {2} after years of {3}.",
        "words": ["agreement", "signed", "negotiations"],
        "definitions": [
            "An arrangement or promise to do something, made by two or more people or groups",
            "To write your name on a document to show that you agree with its contents",
            "Official discussions between groups who are trying to reach an agreement"
        ],
        "difficulty": 2
    },
    {
        "text": "Scientists are {1} new ways to {2} renewable energy in order to {3} climate change.",
        "words": ["exploring", "harness", "combat"],
        "definitions": [
            "To investigate or examine a subject or place in order to learn about it",
            "To control and use the force or strength of something to produce power or energy",
            "To try to stop something harmful from happening or getting worse"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the mountains against the sunset created a {2} view that left us all {3}.",
        "words": ["silhouette", "breathtaking", "speechless"],
        "definitions": [
            "The dark shape and outline of someone or something visible against a lighter background",
            "Extremely impressive or beautiful",
            "Unable to speak due to strong emotion or surprise"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} café on the corner serves the most {2} coffee and has a very {3} atmosphere.",
        "words": ["quaint", "delicious", "welcoming"],
        "definitions": [
            "Attractively unusual or old-fashioned",
            "Having a very pleasant taste or smell",
            "Friendly and making you feel at home"
        ],
        "difficulty": 1
    },
    {
        "text": "Her {1} explanation of the complex theory made it {2} to understand, even for {3}.",
        "words": ["lucid", "easy", "beginners"],
        "definitions": [
            "Expressed clearly and intelligibly",
            "Achieved without great effort; presenting few difficulties",
            "People who have just started learning a skill or activity"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} forest was so {2} that we needed a map to avoid getting {3}.",
        "words": ["dense", "vast", "lost"],
        "definitions": [
            "Having parts that are closely compacted",
            "Of very great extent or quantity",
            "Unable to find one's way"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} storm caused {2} damage to the coastal town, requiring {3} efforts to rebuild.",
        "words": ["severe", "extensive", "significant"],
        "definitions": [
            "Extremely bad or serious",
            "Covering or affecting a large area",
            "Sufficiently great or important to be worthy of attention"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} pianist gave a {2} performance that left the {3} in tears.",
        "words": ["virtuoso", "moving", "audience"],
        "definitions": [
            "A person highly skilled in music or another artistic pursuit",
            "Arousing or affecting the emotions",
            "The assembled spectators or listeners at a public event"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the ancient temple remained {2} despite centuries of {3} to the elements.",
        "words": ["ruins", "impressive", "exposure"],
        "definitions": [
            "The remains of a building that has been destroyed or fallen into disrepair",
            "Evoking admiration through size, quality, or skill",
            "The state of being subject to the effects of something"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} taste of the curry was {2} by the {3} of fresh herbs added at the end.",
        "words": ["spicy", "balanced", "abundance"],
        "definitions": [
            "Having a strong, pungent flavor",
            "Being in a state of equilibrium",
            "A very large quantity of something"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of opinions in the meeting led to a {2} debate, but ultimately a {3} solution.",
        "words": ["diversity", "heated", "practical"],
        "definitions": [
            "The state of being diverse; variety",
            "Intense in feeling; passionate",
            "Concerned with actual use or practice"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} between the two cultures became {2} as they began to {3} ideas and traditions.",
        "words": ["differences", "smaller", "exchange"],
        "definitions": [
            "Points or characteristics in which people or things are dissimilar",
            "Of less than average size, extent, or degree",
            "To give something and receive something in return"
        ],
        "difficulty": 1
    },
    {
        "text": "After the long {1}, the explorers were {2} to finally {3} the hidden temple.",
        "words": ["journey", "ecstatic", "discover"],
        "definitions": [
            "An act of traveling from one place to another, especially over a long distance",
            "Feeling or expressing overwhelming happiness or joyful excitement",
            "To find something that was previously unknown"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} painting was so {2} that it appeared to {3} off the canvas.",
        "words": ["realistic", "lifelike", "jump"],
        "definitions": [
            "Representing things in a way that is accurate and true to life",
            "Looking like a real person or thing",
            "To move suddenly and quickly upward or forward"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} comedian had the {2} laughing {3} throughout the entire show.",
        "words": ["hilarious", "audience", "uncontrollably"],
        "definitions": [
            "Extremely amusing",
            "The assembled spectators or listeners at a public event",
            "In a manner that cannot be managed, directed, or stopped"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} sky at {2} was filled with {3} stars that illuminated the landscape.",
        "words": ["clear", "night", "countless"],
        "definitions": [
            "Free of anything that dims or obscures",
            "The period from sunset to sunrise",
            "Too numerous to count"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} volcano has remained {2} for centuries, but scientists still {3} it for signs of activity.",
        "words": ["dormant", "quiet", "monitor"],
        "definitions": [
            "Temporarily inactive",
            "Making little or no noise",
            "To observe and check the progress or quality of something over a period of time"
        ],
        "difficulty": 2
    },
    {
        "text": "His {1} to detail made him an {2} craftsman, producing {3} pieces of furniture.",
        "words": ["attention", "excellent", "exquisite"],
        "definitions": [
            "The notice taken of someone or something",
            "Extremely good; outstanding",
            "Extremely beautiful and delicate"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} smell of fresh bread {2} through the bakery, {3} customers from the street.",
        "words": ["enticing", "wafted", "attracting"],
        "definitions": [
            "Very attractive or tempting",
            "To move gently through the air",
            "Drawing attention or interest"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} sunset painted the sky with {2} colors, creating a {3} scene.",
        "words": ["spectacular", "vibrant", "magical"],
        "definitions": [
            "Beautiful in a dramatic and eye-catching way",
            "Full of energy and enthusiasm",
            "Wonderful in a way that seems removed from everyday life"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} on the beach was so {2} that we could build {3} sandcastles.",
        "words": ["sand", "soft", "elaborate"],
        "definitions": [
            "Loose granular substance found on beaches, deserts, and riverbeds",
            "Easy to mold, cut, compress, or fold; not hard or firm",
            "Involving many carefully arranged parts or details"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} novel was so {2} that I couldn't {3} it down until I finished reading.",
        "words": ["gripping", "compelling", "put"],
        "definitions": [
            "Having an intense or stimulating effect",
            "Evoking interest, attention, or admiration in a powerfully irresistible way",
            "To place something in a specified location"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} athlete broke the world record with an {2} display of {3} and skill.",
        "words": ["accomplished", "impressive", "strength"],
        "definitions": [
            "Highly trained or skilled in a particular activity",
            "Arousing admiration through size, quality, or skill",
            "The quality or state of being physically strong"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} melody of the song was so {2} that it continued to {3} in my head all day.",
        "words": ["catchy", "memorable", "play"],
        "definitions": [
            "Appealing and easy to remember",
            "Worth remembering or likely to be remembered",
            "To engage in activity for enjoyment and recreation"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of the ancient {2} revealed fascinating insights into a long-{3} civilization.",
        "words": ["discovery", "artifacts", "forgotten"],
        "definitions": [
            "The action or process of finding something previously unknown",
            "Objects made by a human being, typically of cultural or historical interest",
            "Not kept in mind or not thought about"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the garden was {2} with colorful flowers that {3} a sweet fragrance.",
        "words": ["landscape", "filled", "emitted"],
        "definitions": [
            "All the visible features of an area of countryside or land",
            "Having something inside or occupying a space",
            "To produce or send out something such as noise, gas, or a smell"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} architecture of the building {2} the city's skyline, making it instantly {3}.",
        "words": ["iconic", "dominated", "recognizable"],
        "definitions": [
            "Widely recognized and well-established",
            "To have a commanding influence on",
            "Able to be identified or distinguished"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} chef created a {2} dish that {3} the traditional recipe in an innovative way.",
        "words": ["talented", "delectable", "reimagined"],
        "definitions": [
            "Having a natural aptitude or skill for something",
            "Highly pleasing to the taste",
            "To rethink or recreate in a new or different way"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} documentary provided {2} insight into the {3} lives of deep-sea creatures.",
        "words": ["fascinating", "unprecedented", "mysterious"],
        "definitions": [
            "Extremely interesting",
            "Never done or known before",
            "Difficult or impossible to understand, explain, or identify"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} scent of lavender has a {2} effect, making it popular in {3} products.",
        "words": ["soothing", "calming", "relaxation"],
        "definitions": [
            "Tending to reduce pain or discomfort",
            "Making someone tranquil and quiet",
            "The state of being free from tension and anxiety"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of the water made it perfect for {2}, and we spent hours {3} in the clear lake.",
        "words": ["clarity", "swimming", "floating"],
        "definitions": [
            "The quality of being coherent and intelligible",
            "The sport or activity of propelling oneself through water using the limbs",
            "Being suspended on or in a liquid; being buoyant"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} invention {2} the industry and {3} the way people communicated.",
        "words": ["revolutionary", "transformed", "changed"],
        "definitions": [
            "Involving or causing a complete or dramatic change",
            "To make a thorough or dramatic change in the form, appearance, or character of",
            "To make or become different"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} lecture was so {2} that the students remained {3} throughout the entire presentation.",
        "words": ["engaging", "interesting", "attentive"],
        "definitions": [
            "Charming and attractive",
            "Arousing curiosity or interest",
            "Paying close attention to something"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of the expedition faced numerous {2} but remained {3} in their quest to reach the summit.",
        "words": ["members", "challenges", "determined"],
        "definitions": [
            "A person belonging to a group",
            "A task or situation that tests someone's abilities",
            "Having made a firm decision and being resolved not to change it"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of the historical {2} was carefully {3} to preserve its original features.",
        "words": ["restoration", "building", "planned"],
        "definitions": [
            "The action of returning something to a former condition",
            "A structure with a roof and walls, such as a house or factory",
            "Arranged or organized in advance"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of the artwork lies in its {2} detail and the artist's {3} use of color.",
        "words": ["beauty", "intricate", "masterful"],
        "definitions": [
            "A combination of qualities that pleases the intellect or moral sense",
            "Very complicated or detailed",
            "Performed or performed in a very skillful way"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the research findings could {2} our understanding of human {3} and lead to new treatments.",
        "words": ["implications", "revolutionize", "cognition"],
        "definitions": [
            "The conclusion that can be drawn from something although it is not explicitly stated",
            "To change something radically or fundamentally",
            "The mental action or process of acquiring knowledge and understanding through thought, experience, and the senses"
        ],
        "difficulty": 3
    },
    {
        "text": "The {1} of the old photographs {2} memories of a {3} era that had long been forgotten.",
        "words": ["discovery", "evoked", "bygone"],
        "definitions": [
            "The action of finding or learning something for the first time",
            "To bring or recall a feeling, memory, or image to the conscious mind",
            "Belonging to an earlier time or a past age"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the story was so {2} that it kept readers {3} until the very last page.",
        "words": ["plot", "captivating", "engaged"],
        "definitions": [
            "The main events of a novel or movie, devised and presented by the writer as an interrelated sequence",
            "Capable of attracting and holding interest",
            "Busy and occupied; involved"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} between different species in the ecosystem creates a {2} balance that is {3} to maintain biodiversity.",
        "words": ["interaction", "delicate", "essential"],
        "definitions": [
            "A reciprocal action or influence",
            "Very fine in texture or structure; easily damaged",
            "Absolutely necessary; extremely important"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of artificial intelligence continues to {2} at an {3} rate, transforming many industries.",
        "words": ["development", "accelerate", "unprecedented"],
        "definitions": [
            "The process of growing or causing something to grow or become larger or more advanced",
            "To increase in rate, amount, or extent",
            "Never done or known before"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} flavor of the dish was {2} by the chef's {3} blend of exotic spices.",
        "words": ["unique", "enhanced", "carefully-selected"],
        "definitions": [
            "Being the only one of its kind; unlike anything else",
            "To increase or improve the quality, value, or extent of",
            "Chosen with deliberate care and attention to detail"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} between work and personal life is {2} for maintaining good mental {3} and overall wellbeing.",
        "words": ["balance", "crucial", "health"],
        "definitions": [
            "A situation in which different elements are equal or in the correct proportions",
            "Decisive or critical, especially in the success or failure of something",
            "The state of being free from illness or injury"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} silence of the library provided the perfect {2} for students to {3} on their studies.",
        "words": ["tranquil", "environment", "concentrate"],
        "definitions": [
            "Free from disturbance; calm",
            "The surroundings or conditions in which a person, animal, or plant lives or operates",
            "To focus one's attention or mental effort on a particular object or activity"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} photography exhibition {2} viewers with its {3} portrayal of urban life.",
        "words": ["thought-provoking", "impressed", "realistic"],
        "definitions": [
            "Stimulating careful consideration or attention",
            "To affect someone strongly with a quality or feeling",
            "Representing things in a way that is accurate and true to life"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the ancient language has been {2} by linguists who {3} years studying the rare texts.",
        "words": ["complexity", "documented", "spent"],
        "definitions": [
            "The state or quality of being intricate or complicated",
            "Recorded or reported in written, photographic, or other form",
            "To pass time in a specific way"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the scientific {2} surprised even the researchers who had {3} the experiment.",
        "words": ["outcome", "experiment", "designed"],
        "definitions": [
            "The way a thing turns out; a consequence",
            "A scientific procedure undertaken to make a discovery, test a hypothesis, or demonstrate a known fact",
            "To plan and make something for a specific purpose"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of renewable energy sources is {2} increasing, which is {3} for addressing climate change.",
        "words": ["adoption", "steadily", "essential"],
        "definitions": [
            "The action or fact of adopting or being adopted",
            "In a regular, even, and continuous way",
            "Absolutely necessary; extremely important"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the historical documents {2} new light on events that had been {3} for centuries.",
        "words": ["analysis", "shed", "misunderstood"],
        "definitions": [
            "Detailed examination of the elements or structure of something",
            "To cast or emit light or understanding",
            "To fail to interpret or assess accurately"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} dancer moved with such {2} across the stage that the audience was left {3}.",
        "words": ["graceful", "elegance", "mesmerized"],
        "definitions": [
            "Displaying beauty of form or movement",
            "The quality of being graceful and stylish in appearance or manner",
            "To capture the complete attention of someone; to fascinate"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} flavor of honey depends on the {2} of flowers that the bees {3} during nectar collection.",
        "words": ["distinct", "variety", "visit"],
        "definitions": [
            "Recognizably different in nature from something else of a similar type",
            "A number or range of things of the same general class that are different or distinct in character or quality",
            "To go to see a person or place for a period of time"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of space exploration continues to {2} new technologies that {3} life on Earth.",
        "words": ["advancement", "drive", "improve"],
        "definitions": [
            "The process of promoting or developing a new idea, concept, or product",
            "To propel or move something forward",
            "To make or become better"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} between theory and practice is often {2} for students to {3} when first entering a profession.",
        "words": ["gap", "difficult", "bridge"],
        "definitions": [
            "A break or space in an otherwise continuous object",
            "Needing much effort or skill to accomplish, deal with, or understand",
            "To reduce or eliminate the distance between two things"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} performance of the orchestra {2} the audience, who gave a {3} ovation at the end.",
        "words": ["flawless", "captivated", "standing"],
        "definitions": [
            "Without any imperfections or defects; perfect",
            "To attract and hold the interest and attention of",
            "The action of standing up, especially as a mark of respect or approval"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} of the ancient city was {2} preserved beneath layers of {3} for centuries until its discovery.",
        "words": ["architecture", "remarkably", "sediment"],
        "definitions": [
            "The art or practice of designing and constructing buildings",
            "In a way that is worthy of attention because unusual or special",
            "Matter that settles to the bottom of a liquid"
        ],
        "difficulty": 3
    },
    {
        "text": "We decided to {1} the scenic route, even though it was {2}, to {3} the stunning coastal views.",
        "words": ["take", "longer", "enjoy"],
        "definitions": [
            "To adopt a particular path or course",
            "Lasting or taking a great amount of time",
            "To take pleasure or satisfaction in"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} detective used {2} reasoning to {3} the clues and {4} the perplexing case.",
        "words": ["astute", "deductive", "analyze", "solve"],
        "definitions": [
            "Having or showing an ability to accurately assess situations or people and turn this to one's advantage",
            "Based on reasoning from known principles or facts",
            "To examine methodically and in detail",
            "To find an answer to, explanation for, or means of effectively dealing with (a problem or mystery)"
        ],
        "difficulty": 3
    },
    {
        "text": "The {1} provided clear {2} on how to {3} the new software {4}.",
        "words": ["manual", "instructions", "install", "correctly"],
        "definitions": [
            "A book giving instructions or information",
            "Detailed information about how something should be done",
            "To place or fix (equipment or software) in position ready for use",
            "In a way that is accurate or true"
        ],
        "difficulty": 1
    },
    {
        "text": "Despite the {1} weather, the team {2} forward, {3} to reach the base camp before nightfall.",
        "words": ["inclement", "pressed", "determined"],
        "definitions": [
            "Unpleasantly cold or wet (referring to weather)",
            "To move forward with force or effort",
            "Having made a firm decision and being resolved not to change it"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} painting, {2} with vibrant colors, seemed to {3} the very {4} of summer.",
        "words": ["abstract", "alive", "capture", "essence"],
        "definitions": [
            "Existing in thought or as an idea but not having a physical or concrete existence",
            "Full of energy and activity",
            "To represent or record accurately in words or images",
            "The intrinsic nature or indispensable quality of something"
        ],
        "difficulty": 2
    },
    {
        "text": "Learning a new language requires {1}, {2} practice, and a willingness to {3} mistakes.",
        "words": ["patience", "consistent", "make"],
        "definitions": [
            "The capacity to accept or tolerate delay, problems, or suffering without becoming annoyed or anxious",
            "Acting or done in the same way over time, especially so as to be fair or accurate",
            "To cause something to exist or come about; bring about"
        ],
        "difficulty": 1
    },
    {
        "text": "The chef's {1} approach to cooking involved {2} traditional techniques with {3} ingredients and {4} presentation.",
        "words": ["innovative", "combining", "exotic", "modern"],
        "definitions": [
            "Featuring new methods; advanced and original",
            "Joining or merging to form a single unit or substance",
            "Originating in or characteristic of a distant foreign country",
            "Relating to the present or recent times"
        ],
        "difficulty": 2
    },
    {
        "text": "The old library, with its {1} shelves and {2} atmosphere, was a {3} place for quiet {4}.",
        "words": ["towering", "serene", "perfect", "contemplation"],
        "definitions": [
            "Extremely tall, especially in comparison with the surroundings",
            "Calm, peaceful, and untroubled; tranquil",
            "Having all the required or desirable elements, qualities, or characteristics",
            "Deep reflective thought"
        ],
        "difficulty": 2
    },
    {
        "text": "The speaker's {1} arguments {2} the audience to {3} their own {4} on the matter.",
        "words": ["persuasive", "convinced", "reconsider", "perspective"],
        "definitions": [
            "Good at convincing someone to do or believe something through reasoning or the use of temptation",
            "Completely certain about something",
            "To consider something again, especially for a possible change of decision",
            "A particular attitude toward or way of regarding something; a point of view"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} of the city's history is {2} in its diverse {3} and {4} landmarks.",
        "words": ["richness", "reflected", "architecture", "historic"],
        "definitions": [
            "The quality of having abundant resources or valuable possessions",
            "To embody or represent (something) in a faithful or appropriate way",
            "The art or practice of designing and constructing buildings",
            "Famous or important in history, or potentially so"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} astronaut shared {2} stories about the {3} experience of walking in {4}.",
        "words": ["veteran", "riveting", "surreal", "space"],
        "definitions": [
            "A person who has had long experience in a particular field",
            "Completely engrossing; compelling",
            "Having the qualities of bizarre dreams; unreal",
            "The physical universe beyond the earth's atmosphere"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} garden was a {2} mix of native plants and {3} flowers, creating a {4} ecosystem.",
        "words": ["botanical", "harmonious", "exotic", "thriving"],
        "definitions": [
            "Relating to plants",
            "Forming a pleasing or consistent whole",
            "Originating in or characteristic of a distant foreign country",
            "Growing or developing well or vigorously"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} researcher {2} dedicated her life to {3} the {4} of a rare genetic disorder.",
        "words": ["eminent", "had", "understanding", "causes"],
        "definitions": [
            "Famous and respected within a particular sphere or profession",
            "Used to indicate possession, ownership, or holding",
            "The ability to perceive the significance, explanation, or cause of something",
            "A person or thing that gives rise to an action, phenomenon, or condition"
        ],
        "difficulty": 3
    },
    {
        "text": "A {1} diet, regular {2}, and adequate {3} are {4} for maintaining good health.",
        "words": ["balanced", "exercise", "sleep", "essential"],
        "definitions": [
            "Containing a combination of elements in the correct proportions",
            "Activity requiring physical effort, carried out to sustain or improve health and fitness",
            "A condition of body and mind that typically recurs for several hours each night",
            "Absolutely necessary; extremely important"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} evidence presented during the trial left no {2} about the defendant's {3}.",
        "words": ["overwhelming", "doubt", "guilt"],
        "definitions": [
            "Very great in amount or effect",
            "A feeling of uncertainty or lack of conviction",
            "The fact of having committed a specified or implied offense or crime"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} musician could {2} play several {3} with exceptional {4}.",
        "words": ["versatile", "effortlessly", "instruments", "skill"],
        "definitions": [
            "Able to adapt or be adapted to many different functions or activities",
            "Without effort or difficulty",
            "Tools or devices, especially one used for delicate or scientific work; musical devices",
            "The ability to do something well; expertise"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} waterfall cascaded down the {2} cliff face, creating a {3} spray that {4} in the sunlight.",
        "words": ["majestic", "sheer", "fine", "glistened"],
        "definitions": [
            "Having or showing impressive beauty or dignity",
            "Perpendicular or nearly so; very steep",
            "Of very high quality; very thin or narrow",
            "To shine with a sparkling light"
        ],
        "difficulty": 2
    },
    {
        "text": "Effective {1} is {2} for resolving {3} and building strong {4}.",
        "words": ["communication", "vital", "conflicts", "relationships"],
        "definitions": [
            "The imparting or exchanging of information or news",
            "Absolutely necessary or important; essential",
            "Serious disagreements or arguments",
            "The way in which two or more people or things are connected"
        ],
        "difficulty": 1
    },
    {
        "text": "The museum exhibit {1} a {2} collection of {3} artifacts from various {4} periods.",
        "words": ["featured", "diverse", "rare", "historical"],
        "definitions": [
            "To have as a prominent attribute or aspect",
            "Showing a great deal of variety; very different",
            "Not occurring very often; uncommon",
            "Of or concerning history or past events"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} diplomat skillfully {2} the complex {3} between the two {4} nations.",
        "words": ["experienced", "navigated", "negotiations", "warring"],
        "definitions": [
            "Having gained knowledge or skill in a particular field over time",
            "To guide or direct a course through a difficult situation",
            "Discussions aimed at reaching an agreement",
            "Engaged in conflict or warfare"
        ],
        "difficulty": 3
    },
    {
        "text": "Reading {1} can {2} your vocabulary and {3} your understanding of the {4}.",
        "words": ["widely", "expand", "improve", "world"],
        "definitions": [
            "Over a large area or range; extensively",
            "To become or make larger or more extensive",
            "To make or become better",
            "The earth, together with all of its countries, peoples, and natural features"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} journalist risked {2} danger to {3} the truth behind the {4} scandal.",
        "words": ["intrepid", "personal", "uncover", "political"],
        "definitions": [
            "Fearless; adventurous",
            "Concerning one's private life, relationships, and emotions",
            "To discover (something previously secret or unknown)",
            "Relating to the government or public affairs of a country"
        ],
        "difficulty": 3
    },
    {
        "text": "The {1} aroma of coffee {2} from the café, {3} passersby to step {4}.",
        "words": ["inviting", "drifted", "tempting", "inside"],
        "definitions": [
            "Offering attraction or pleasure",
            "To be carried slowly by a current of air or water",
            "Appealing to or attracting someone, even if wrong or unwise",
            "Into or within a place or structure"
        ],
        "difficulty": 1
    },
    {
        "text": "The company's {1} to sustainability is {2} in its use of {3} materials and {4} practices.",
        "words": ["commitment", "evident", "recycled", "eco-friendly"],
        "definitions": [
            "The state or quality of being dedicated to a cause or activity",
            "Plain or obvious; clearly seen or understood",
            "Converted waste into reusable material",
            "Not harmful to the environment"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} silence of the desert at night was only {2} by the {3} chirp of crickets and the {4} wind.",
        "words": ["profound", "broken", "occasional", "whispering"],
        "definitions": [
            "Very great or intense; having deep insight or understanding",
            "Interrupted or disturbed",
            "Occurring, appearing, or done infrequently and irregularly",
            "Speaking very softly; making a soft rustling sound"
        ],
        "difficulty": 2
    },
    {
        "text": "Volunteering in the community can be a {1} experience, allowing you to {2} a positive {3} and meet new {4}.",
        "words": ["rewarding", "make", "impact", "people"],
        "definitions": [
            "Providing satisfaction; gratifying",
            "To cause something to exist or come about",
            "A marked effect or influence",
            "Human beings in general or considered collectively"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} philosopher pondered the {2} questions of existence, {3}, and the meaning of {4}.",
        "words": ["ancient", "fundamental", "consciousness", "life"],
        "definitions": [
            "Belonging to the very distant past and no longer in existence",
            "Forming a necessary base or core; of central importance",
            "The state of being aware of and responsive to one's surroundings",
            "The condition that distinguishes animals and plants from inorganic matter"
        ],
        "difficulty": 3
    },
    {
        "text": "The sudden {1} caught everyone by {2}, forcing them to seek {3} shelter from the {4} rain.",
        "words": ["downpour", "surprise", "immediate", "heavy"],
        "definitions": [
            "A heavy fall of rain",
            "An unexpected or astonishing event, fact, etc.",
            "Occurring or done at once; instant",
            "Of great density; thick or substantial"
        ],
        "difficulty": 1
    },
    {
        "text": "The startup company {1} secured {2} funding, allowing them to {3} their operations and {4} new staff.",
        "words": ["successfully", "significant", "expand", "hire"],
        "definitions": [
            "In a way that achieves the desired aim or result",
            "Sufficiently great or important to be worthy of attention; noteworthy",
            "To become or make larger or more extensive",
            "To employ someone for wages"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} tapestry depicted a {2} scene from medieval {3}, woven with {4} threads.",
        "words": ["intricate", "vivid", "folklore", "golden"],
        "definitions": [
            "Very complicated or detailed",
            "Producing powerful feelings or strong, clear images in the mind",
            "The traditional beliefs, customs, and stories of a community, passed through the generations by word of mouth",
            "Colored or shining like gold"
        ],
        "difficulty": 2
    },
    {
        "text": "Solving {1} puzzles can help to {2} cognitive function and keep your {3} sharp.",
        "words": ["complex", "improve", "mind"],
        "definitions": [
            "Consisting of many different and connected parts; not easy to analyze or understand",
            "To make or become better",
            "The element of a person that enables them to be aware of the world and their experiences, to think, and to feel"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} rescue team worked {2} through the night to {3} the hikers trapped by the {4}.",
        "words": ["dedicated", "tirelessly", "locate", "avalanche"],
        "definitions": [
            "Devoted to a task or purpose",
            "With great effort or energy; without becoming tired",
            "To discover the exact place or position of",
            "A mass of snow, ice, and rocks falling rapidly down a mountainside"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} author's latest novel received {2} reviews for its {3} plot and {4} characters.",
        "words": ["acclaimed", "rave", "compelling", "well-developed"],
        "definitions": [
            "Publicly praised; celebrated",
            "Extremely enthusiastic or positive (typically reviews)",
            "Evoking interest, attention, or admiration in a powerfully irresistible way",
            "Having a fully formed and complex personality (of a fictional character)"
        ],
        "difficulty": 2
    },
    {
        "text": "Advancements in {1} technology allow doctors to {2} diseases earlier and provide more {3} treatments.",
        "words": ["medical", "diagnose", "effective"],
        "definitions": [
            "Relating to the science or practice of medicine",
            "To identify the nature of (an illness or other problem) by examination of the symptoms",
            "Successful in producing a desired or intended result"
        ],
        "difficulty": 1
    },
    {
        "text": "The government implemented {1} measures to {2} the spread of the {3} virus and protect public {4}.",
        "words": ["strict", "curb", "contagious", "health"],
        "definitions": [
            "Demanding that rules concerning behavior are obeyed and observed",
            "To restrain or keep in check",
            "Spread from one person or organism to another by direct or indirect contact",
            "The state of being free from illness or injury"
        ],
        "difficulty": 2
    },
    {
        "text": "The {1} mountain range offered {2} hiking trails with {3} views at every {4}.",
        "words": ["rugged", "challenging", "panoramic", "turn"],
        "definitions": [
            "Having a broken, rocky, and uneven surface",
            "Testing one's abilities; demanding",
            "With a wide view surrounding the observer; sweeping",
            "A point at which a road, path, or river bends or changes direction"
        ],
        "difficulty": 2
    },
    {
        "text": "Learning to play a {1} instrument requires {2}, discipline, and a good {3} for rhythm.",
        "words": ["musical", "practice", "ear"],
        "definitions": [
            "Relating to or connected with music",
            "Repeated exercise in or performance of an activity or skill so as to acquire or maintain proficiency in it",
            "An innate ability to appreciate and remember musical tones"
        ],
        "difficulty": 1
    },
    {
        "text": "The {1} archeologist carefully {2} the fragile {3} from the ancient {4}.",
        "words": ["meticulous", "excavated", "pottery", "tomb"],
        "definitions": [
            "Showing great attention to detail; very careful and precise",
            "To make (a hole or channel) by digging; remove earth carefully to find buried remains",
            "Pots, dishes, and other articles made of earthenware or baked clay",
            "A large vault, typically an underground one, for burying the dead"
        ],
        "difficulty": 3
    },
    {
        "text": "The {1} of the rainforest is {2} by deforestation, which {3} countless species and {4} climate patterns.",
        "words": ["biodiversity", "threatened", "endangers", "disrupts"],
        "definitions": [
            "The variety of plant and animal life in the world or in a particular habitat",
            "In danger of being harmed, damaged, or destroyed",
            "To put (someone or something) at risk or in danger",
            "To interrupt the normal course or unity of"
        ],
        "difficulty": 2
    },
    {
        "text": "The small coastal village {1} its traditional {2} despite the influx of {3} and modernization.",
        "words": ["retained", "charm", "tourism"],
        "definitions": [
            "To continue to have (something); keep possession of",
            "The quality of delighting, attracting, or fascinating others",
            "The commercial organization and operation of vacations and visits to places of interest"
        ],
        "difficulty": 2
    },
    {
        "text": "The lawyer presented a {1} case, using {2} evidence and {3} arguments to {4} the jury.",
        "words": ["compelling", "factual", "logical", "persuade"],
        "definitions": [
            "Evoking interest, attention, or admiration in a powerfully irresistible way",
            "Concerned with what is actually the case rather than interpretations",
            "Characterized by or capable of clear, sound reasoning",
            "To cause (someone) to do something through reasoning or argument"
        ],
        "difficulty": 2
    },
    {
        "text": "The old {1} stood {2} on the hill, overlooking the {3} valley below.",
        "words": ["castle", "majestically", "serene"],
        "definitions": [
            "A large building, typically of the medieval period, fortified against attack",
            "With impressive beauty or scale",
            "Calm, peaceful, and untroubled"
        ],
        "difficulty": 1
    },
    {
        "text": "Ongoing {1} is needed to {2} solutions for {3} global challenges like poverty and {4}.",
        "words": ["collaboration", "develop", "complex", "inequality"],
        "definitions": [
            "The action of working with someone to produce or create something",
            "To grow or cause to grow and become more mature, advanced, or elaborate",
            "Consisting of many different and connected parts",
            "Difference in size, degree, circumstances, etc.; lack of equality"
        ],
        "difficulty": 2
    },
    {
        "text": "The chef {1} added a {2} of saffron to the dish, giving it a {3} color and {4} flavor.",
        "words": ["carefully", "pinch", "vibrant", "distinctive"],
        "definitions": [
            "With great attention",
            "A small amount of something, typically taken between the thumb and forefinger",
            "Bright and striking",
            "Characteristic of one person or thing, and so serving to distinguish it from others"
        ],
        "difficulty": 2
    }
]

# Données pour le mode Vocabulaire - Relier synonymes
synonym_data = [
    {
        "word": "begin",
        "synonym": "commence",
        "difficulty": 1
    },
    {
        "word": "strange",
        "synonym": "peculiar",
        "difficulty": 1
    },
    {
        "word": "happy",
        "synonym": "delighted",
        "difficulty": 1
    },
    {
        "word": "essential",
        "synonym": "indispensable",
        "difficulty": 2
    },
    {
        "word": "conceal",
        "synonym": "hide",
        "difficulty": 2
    },
    {
        "word": "big",
        "synonym": "large",
        "difficulty": 1
    },
    {
        "word": "small",
        "synonym": "tiny",
        "difficulty": 1
    },
    {
        "word": "fast",
        "synonym": "swift",
        "difficulty": 1
    },
    {
        "word": "sad",
        "synonym": "unhappy",
        "difficulty": 1
    },
    {
        "word": "angry",
        "synonym": "furious",
        "difficulty": 1
    },
    {
        "word": "clever",
        "synonym": "intelligent",
        "difficulty": 1
    },
    {
        "word": "beautiful",
        "synonym": "attractive",
        "difficulty": 1
    },
    {
        "word": "end",
        "synonym": "finish",
        "difficulty": 1
    },
    {
        "word": "quiet",
        "synonym": "silent",
        "difficulty": 1
    },
    {
        "word": "hard",
        "synonym": "difficult",
        "difficulty": 1
    },
    {
        "word": "simple",
        "synonym": "easy",
        "difficulty": 1
    },
    {
        "word": "rich",
        "synonym": "wealthy",
        "difficulty": 1
    },
    {
        "word": "poor",
        "synonym": "impoverished",
        "difficulty": 2
    },
    {
        "word": "brave",
        "synonym": "courageous",
        "difficulty": 1
    },
    {
        "word": "scared",
        "synonym": "afraid",
        "difficulty": 1
    },
    {
        "word": "thin",
        "synonym": "slim",
        "difficulty": 1
    },
    {
        "word": "fat",
        "synonym": "overweight",
        "difficulty": 1
    },
    {
        "word": "old",
        "synonym": "aged",
        "difficulty": 1
    },
    {
        "word": "new",
        "synonym": "modern",
        "difficulty": 1
    },
    {
        "word": "bright",
        "synonym": "luminous",
        "difficulty": 2
    },
    {
        "word": "dark",
        "synonym": "gloomy",
        "difficulty": 1
    },
    {
        "word": "wet",
        "synonym": "damp",
        "difficulty": 1
    },
    {
        "word": "dry",
        "synonym": "arid",
        "difficulty": 1
    },
    {
        "word": "loud",
        "synonym": "noisy",
        "difficulty": 1
    },
    {
        "word": "cold",
        "synonym": "chilly",
        "difficulty": 1
    },
    {
        "word": "hot",
        "synonym": "scorching",
        "difficulty": 1
    },
    {
        "word": "busy",
        "synonym": "occupied",
        "difficulty": 1
    },
    {
        "word": "lazy",
        "synonym": "idle",
        "difficulty": 1
    },
    {
        "word": "weak",
        "synonym": "feeble",
        "difficulty": 1
    },
    {
        "word": "strong",
        "synonym": "powerful",
        "difficulty": 1
    },
    {
        "word": "kind",
        "synonym": "generous",
        "difficulty": 1
    },
    {
        "word": "mean",
        "synonym": "cruel",
        "difficulty": 1
    },
    {
        "word": "true",
        "synonym": "accurate",
        "difficulty": 1
    },
    {
        "word": "false",
        "synonym": "incorrect",
        "difficulty": 1
    },
    {
        "word": "polite",
        "synonym": "courteous",
        "difficulty": 1
    },
    {
        "word": "rude",
        "synonym": "discourteous",
        "difficulty": 1
    },
    {
        "word": "funny",
        "synonym": "humorous",
        "difficulty": 1
    },
    {
        "word": "serious",
        "synonym": "grave",
        "difficulty": 1
    },
    {
        "word": "boring",
        "synonym": "tedious",
        "difficulty": 1
    },
    {
        "word": "exciting",
        "synonym": "thrilling",
        "difficulty": 1
    },
    {
        "word": "near",
        "synonym": "close",
        "difficulty": 1
    },
    {
        "word": "far",
        "synonym": "distant",
        "difficulty": 1
    },
    {
        "word": "whole",
        "synonym": "entire",
        "difficulty": 1
    },
    {
        "word": "authentic",
        "synonym": "genuine",
        "difficulty": 2
    },
    {
        "word": "obtain",
        "synonym": "acquire",
        "difficulty": 2
    },
    {
        "word": "reject",
        "synonym": "refuse",
        "difficulty": 1
    },
    {
        "word": "decrease",
        "synonym": "reduce",
        "difficulty": 1
    },
    {
        "word": "increase",
        "synonym": "expand",
        "difficulty": 1
    },
    {
        "word": "adequate",
        "synonym": "sufficient",
        "difficulty": 2
    },
    {
        "word": "enormous",
        "synonym": "immense",
        "difficulty": 2
    },
    {
        "word": "repair",
        "synonym": "fix",
        "difficulty": 1
    },
    {
        "word": "destroy",
        "synonym": "demolish",
        "difficulty": 1
    },
    {
        "word": "absurd",
        "synonym": "ridiculous",
        "difficulty": 2
    },
    {
        "word": "annual",
        "synonym": "yearly",
        "difficulty": 1
    },
    {
        "word": "fake",
        "synonym": "counterfeit",
        "difficulty": 2
    },
    {
        "word": "forbidden",
        "synonym": "prohibited",
        "difficulty": 2
    },
    {
        "word": "quick",
        "synonym": "rapid",
        "difficulty": 1
    },
    {
        "word": "risky",
        "synonym": "dangerous",
        "difficulty": 1
    },
    {
        "word": "scary",
        "synonym": "frightening",
        "difficulty": 1
    },
    {
        "word": "silly",
        "synonym": "foolish",
        "difficulty": 1
    },
    {
        "word": "odd",
        "synonym": "unusual",
        "difficulty": 1
    },
    {
        "word": "modify",
        "synonym": "change",
        "difficulty": 1
    },
    {
        "word": "remember",
        "synonym": "recall",
        "difficulty": 1
    },
    {
        "word": "achieve",
        "synonym": "accomplish",
        "difficulty": 2
    },
    {
        "word": "assist",
        "synonym": "help",
        "difficulty": 1
    },
    {
        "word": "magnificent",
        "synonym": "splendid",
        "difficulty": 2
    },
    {
        "word": "vanish",
        "synonym": "disappear",
        "difficulty": 1
    },
    {
        "word": "ancient",
        "synonym": "archaic",
        "difficulty": 2
    },
    {
        "word": "frequent",
        "synonym": "common",
        "difficulty": 1
    },
    {
        "word": "temporary",
        "synonym": "provisional",
        "difficulty": 2
    },
    {
        "word": "permanent",
        "synonym": "lasting",
        "difficulty": 1
    },
    {
        "word": "various",
        "synonym": "diverse",
        "difficulty": 2
    },
    {
        "word": "vital",
        "synonym": "crucial",
        "difficulty": 2
    },
    {
        "word": "abundant",
        "synonym": "plentiful",
        "difficulty": 2
    },
    {
        "word": "scarce",
        "synonym": "rare",
        "difficulty": 2
    },
    {
        "word": "flexible",
        "synonym": "adaptable",
        "difficulty": 2
    },
    {
        "word": "rigid",
        "synonym": "stiff",
        "difficulty": 2
    },
    {
        "word": "fragile",
        "synonym": "delicate",
        "difficulty": 2
    },
    {
        "word": "robust",
        "synonym": "sturdy",
        "difficulty": 2
    },
    {
        "word": "precise",
        "synonym": "exact",
        "difficulty": 2
    },
    {
        "word": "vague",
        "synonym": "obscure",
        "difficulty": 2
    },
    {
        "word": "ask",
        "synonym": "inquire",
        "difficulty": 1
    },
    {
        "word": "tell",
        "synonym": "narrate",
        "difficulty": 2
    },
    {
        "word": "get",
        "synonym": "receive",
        "difficulty": 1
    },
    {
        "word": "make",
        "synonym": "create",
        "difficulty": 1
    },
    {
        "word": "use",
        "synonym": "utilize",
        "difficulty": 2
    },
    {
        "word": "show",
        "synonym": "display",
        "difficulty": 1
    },
    {
        "word": "important",
        "synonym": "significant",
        "difficulty": 1
    },
    {
        "word": "different",
        "synonym": "distinct",
        "difficulty": 1
    },
    {
        "word": "explain",
        "synonym": "clarify",
        "difficulty": 2
    },
    {
        "word": "idea",
        "synonym": "concept",
        "difficulty": 1
    },
    {
        "word": "job",
        "synonym": "occupation",
        "difficulty": 1
    },
    {
        "word": "part",
        "synonym": "portion",
        "difficulty": 1
    },
    {
        "word": "place",
        "synonym": "location",
        "difficulty": 1
    },
    {
        "word": "problem",
        "synonym": "issue",
        "difficulty": 1
    },
    {
        "word": "wrong",
        "synonym": "erroneous",
        "difficulty": 2
    },
    {
        "word": "calm",
        "synonym": "serene",
        "difficulty": 2
    },
    {
        "word": "eager",
        "synonym": "keen",
        "difficulty": 1
    },
    {
        "word": "huge",
        "synonym": "vast",
        "difficulty": 1
    },
    {
        "word": "glad",
        "synonym": "pleased",
        "difficulty": 1
    },
    {
        "word": "keep",
        "synonym": "retain",
        "difficulty": 2
    },
    {
        "word": "allow",
        "synonym": "permit",
        "difficulty": 1
    },
    {
        "word": "choose",
        "synonym": "select",
        "difficulty": 1
    },
    {
        "word": "continue",
        "synonym": "persist",
        "difficulty": 2
    },
    {
        "word": "empty",
        "synonym": "vacant",
        "difficulty": 1
    },
    {
        "word": "full",
        "synonym": "replete",
        "difficulty": 2
    }
]

# Données pour le mode Grammaire - Trouver l'intrus
odd_one_out_data = [
  {
    "words": ["He plays the guitar well.", "She don't like coffee.", "They are going to the park.", "We watched a movie last night."],
    "correct_index": 1,
    "explanation": "Subject-verb agreement error: 'She' is third-person singular, so the verb should be 'doesn't'.",
    "difficulty": 1
  },
  {
    "words": ["Over the lazy dog.", "A fast runner win the race.", "The quick brown fox jumps.", "Apples are healthy."],
    "correct_index": 1,
    "explanation": "Subject-verb agreement error: 'A fast runner' is singular, so the verb should be 'wins'.",
    "difficulty": 1
  },
  {
    "words": ["He gave the book to her.", "They saw us at the store.", "Me and my friend went.", "She is taller than I am."],
    "correct_index": 2,
    "explanation": "Pronoun case error: When used as a subject, 'I' should be used instead of 'Me'. Correct: 'My friend and I went'.",
    "difficulty": 1
  },
  {
    "words": ["Walking down the street.", "Children play in the yard.", "The birds was singing loudly.", "My favorite color is blue."],
    "correct_index": 2,
    "explanation": "Subject-verb agreement error: 'birds' is plural, so the verb should be 'were'.",
    "difficulty": 1
  },
  {
    "words": ["She baked a delicious cake.", "They have finished their homework.", "He swimmed across the lake.", "I will call you later."],
    "correct_index": 2,
    "explanation": "Incorrect past tense verb form: The past tense of 'swim' is 'swam'.",
    "difficulty": 1
  },
  {
    "words": ["The dog wagged its tail.", "You're going to be late.", "Their house is big.", "Its a beautiful day."],
    "correct_index": 3,
    "explanation": "Incorrect contraction/possessive: 'It's' (with an apostrophe) is the contraction for 'it is'. 'Its' (no apostrophe) is possessive.",
    "difficulty": 1
  },
  {
    "words": ["I need more time.", "Less people attended the meeting.", "There are fewer apples.", "He has much experience."],
    "correct_index": 1,
    "explanation": "Incorrect word choice: 'Fewer' is used for countable nouns (like people), while 'less' is used for uncountable nouns.",
    "difficulty": 2
  },
  {
    "words": ["She spoke softly.", "They performed magnificently.", "He runs very quick.", "The train arrived promptly."],
    "correct_index": 2,
    "explanation": "Adverb/adjective confusion: 'Quickly' (adverb) should be used to modify the verb 'runs', not 'quick' (adjective).",
    "difficulty": 1
  },
  {
    "words": ["We have eaten dinner.", "I seen that movie.", "She wrote a long letter.", "He drove carefully."],
    "correct_index": 1,
    "explanation": "Incorrect past participle/past tense usage: The simple past tense is 'saw'. 'Seen' requires an auxiliary verb (e.g., 'have seen').",
    "difficulty": 1
  },
  {
    "words": ["Among the three friends.", "Beside the river.", "Between you and I.", "Under the table."],
    "correct_index": 2,
    "explanation": "Pronoun case error: Prepositions like 'between' require the objective case ('me'), not the subjective case ('I'). Correct: 'Between you and me'.",
    "difficulty": 2
  },
  {
    "words": ["Should have studied more.", "Could of done better.", "Might have been late.", "Would have helped if asked."],
    "correct_index": 1,
    "explanation": "Incorrect word choice: 'Could have' (or 'could've') is the correct modal construction, not 'could of'.",
    "difficulty": 1
  },
  {
    "words": ["A taller building.", "The fastest runner.", "This is the most unique design.", "A more interesting book."],
    "correct_index": 2,
    "explanation": "Incorrect modifier: 'Unique' is an absolute adjective, meaning it cannot be compared. It should be 'This design is unique' or 'This is a unique design'.",
    "difficulty": 2
  },
  {
    "words": ["She arrived later than expected.", "He is taller then me.", "More beautiful than ever.", "Older than his brother."],
    "correct_index": 1,
    "explanation": "Incorrect word choice: 'Than' is used for comparisons. 'Then' indicates time or sequence.",
    "difficulty": 1
  },
  {
    "words": ["Everyone is ready.", "Neither of the options works.", "Each of the students have a book.", "Somebody needs to help."],
    "correct_index": 2,
    "explanation": "Subject-verb agreement error: Indefinite pronouns like 'Each' are singular and take a singular verb ('has').",
    "difficulty": 2
  },
  {
    "words": ["The media is biased.", "My criteria includes experience.", "This phenomenon occurs rarely.", "The data suggests a trend."],
    "correct_index": 0,
    "explanation": "Subject-verb agreement error: 'Media' is the plural of 'medium' and traditionally takes a plural verb ('are'). While singular usage is common, 'are' is strictly more correct.",
    "difficulty": 3
  },
  {
    "words": ["The chicken lays eggs.", "He laid down for a nap.", "She set the book on the table.", "The sun rises in the east."],
    "correct_index": 1,
    "explanation": "Incorrect verb choice (lie/lay): 'Lie' (to recline) should be used. The past tense is 'lay'. 'Lay' (to put/place) has the past tense 'laid'. Correct: 'He lay down...'",
    "difficulty": 3
  },
  {
    "words": ["The music sounds good.", "I feel badly about the mistake.", "She seems happy.", "He felt strong after the workout."],
    "correct_index": 1,
    "explanation": "Adverb/adjective confusion: With linking verbs like 'feel', an adjective ('bad') is used to describe the subject's state, not an adverb ('badly').",
    "difficulty": 2
  },
  {
    "words": ["Since you asked, I'll tell you.", "The reason is because I was tired.", "Although it rained, we went out.", "He left when the movie ended."],
    "correct_index": 1,
    "explanation": "Redundancy: 'The reason is...' and '...because...' mean the same thing. Use one or the other (e.g., 'The reason is that I was tired' or 'I was tired').",
    "difficulty": 2
  },
  {
    "words": ["Regardless of the cost.", "Despite the challenges.", "Irregardless of the weather.", "Concerning your request."],
    "correct_index": 2,
    "explanation": "Non-standard word: 'Irregardless' is considered non-standard. The correct word is 'Regardless'.",
    "difficulty": 2
  },
  {
    "words": ["Who is at the door?", "Give it to whomever asks.", "Whom did you call?", "She knows who to trust."],
    "correct_index": 1,
    "explanation": "Pronoun case error: 'Whoever' should be used here as it is the subject of the verb 'asks' in the subordinate clause. 'Whomever' is used as an object.",
    "difficulty": 3
  },
  {
    "words": ["Your dinner is getting cold.", "They're planning a party.", "The team lost it's game.", "There is no reason to worry."],
    "correct_index": 2,
    "explanation": "Incorrect contraction/possessive: 'Its' (no apostrophe) is possessive. 'It's' (with an apostrophe) is the contraction for 'it is'.",
    "difficulty": 1
  },
  {
    "words": ["A number of cars.", "A large amount of people.", "A great deal of effort.", "Plenty of food."],
    "correct_index": 1,
    "explanation": "Incorrect word choice: 'Amount' is used for uncountable nouns. 'Number' should be used for countable nouns like 'people'.",
    "difficulty": 2
  },
  {
    "words": ["She performed well.", "The plan works fine.", "He did good on the test.", "They look happy together."],
    "correct_index": 2,
    "explanation": "Adverb/adjective confusion: 'Well' (adverb) should be used to modify the verb 'did', not 'good' (adjective).",
    "difficulty": 1
  },
  {
    "words": ["Be sure to lock the door.", "Let's go get some food.", "Try and finish your work.", "Come visit us soon."],
    "correct_index": 2,
    "explanation": "Incorrect idiom/construction: The standard idiom is 'Try to finish', not 'Try and finish'.",
    "difficulty": 2
  },
  {
    "words": ["Either the cat or the dogs are noisy.", "Neither the players nor the coach were happy.", "Not only the students but also the teacher is present.", "Both John and Mary have arrived."],
    "correct_index": 1,
    "explanation": "Subject-verb agreement with nor/or: The verb agrees with the noun closest to it. 'Coach' is singular, so the verb should be 'was'.",
    "difficulty": 2
  },
  {
    "words": ["It doesn't matter much.", "That's unimportant to me.", "I couldn't care less.", "I could care less."],
    "correct_index": 3,
    "explanation": "Idiom meaning error: 'I couldn't care less' means you have zero interest. 'I could care less' implies you have some level of care (and is often used mistakenly).",
    "difficulty": 2
  },
  {
    "words": ["The positive effect.", "To effect change.", "Having an affect on someone.", "Affecting the outcome."],
    "correct_index": 2,
    "explanation": "Incorrect word choice (affect/effect): 'Affect' is usually a verb (to influence). 'Effect' is usually a noun (result). Here, the noun 'effect' is needed.",
    "difficulty": 2
  },
  {
    "words": ["According to the report.", "Depending on the situation.", "Based off the results.", "Derived from the data."],
    "correct_index": 2,
    "explanation": "Incorrect preposition: The standard idiom is 'Based on', not 'Based off'.",
    "difficulty": 2
  },
  {
    "words": ["A unique opportunity.", "An hour ago.", "An historical event.", "A European country."],
    "correct_index": 2,
    "explanation": "Incorrect article: While 'h' can sometimes take 'an', if the 'h' is pronounced (as in 'historical'), 'a' is generally preferred in modern usage.",
    "difficulty": 3
  },
  {
    "words": ["The man who lives next door.", "My brother, whom is older.", "The company whose CEO resigned.", "The car that I bought."],
    "correct_index": 1,
    "explanation": "Pronoun case error: 'Who' should be used as the subject of the verb 'is' in the relative clause.",
    "difficulty": 2
  },
  {
    "words": ["If she were here, she would know.", "Had he known, he might have acted.", "If I was you, I would go.", "Were I richer, I'd travel more."],
    "correct_index": 2,
    "explanation": "Incorrect subjunctive mood: In hypothetical situations contrary to fact, 'were' is used instead of 'was' for the first and third person singular.",
    "difficulty": 2
  },
  {
    "words": ["She inferred from his tone.", "What can be inferred?", "He implied I was wrong.", "He inferred that I should leave."],
    "correct_index": 3,
    "explanation": "Incorrect word choice (imply/infer): To imply is to suggest indirectly (speaker). To infer is to deduce (listener/reader). He *implied* I should leave.",
    "difficulty": 3
  },
  {
    "words": ["Many options are available.", "We had fun.", "Alot of people agree.", "There is plenty of room."],
    "correct_index": 2,
    "explanation": "Incorrect word form: 'Alot' should be written as two words: 'a lot'.",
    "difficulty": 1
  },
  {
    "words": ["Similar to yours.", "Compared with the original.", "Different from mine.", "He differs with me on this."],
    "correct_index": 3,
    "explanation": "Incorrect preposition: While 'differs with' can mean 'disagrees with', 'differs from' (is unlike) is more common when comparing attributes. 'Disagrees with me' or 'Differs from me' would be clearer depending on intent.",
    "difficulty": 3
  },
  {
    "words": ["Apparently, it's true.", "Supposebly, he is rich.", "Undoubtedly the best.", "Probably going to rain."],
    "correct_index": 1,
    "explanation": "Misspelled/Incorrect word: The correct word is 'Supposedly'.",
    "difficulty": 2
  },
  {
    "words": ["The cat's whiskers.", "My parents' house.", "Two childrens' toys.", "Ross's car."],
    "correct_index": 2,
    "explanation": "Incorrect possessive plural: 'Children' is already plural. The possessive is formed by adding 's: 'children's'.",
    "difficulty": 1
  },
  {
    "words": ["Without warning, he left.", "All the sudden, it started raining.", "She stopped abruptly.", "Everything happened quickly."],
    "correct_index": 1,
    "explanation": "Incorrect idiom: The correct idiom is 'All of a sudden'.",
    "difficulty": 2
  },
  {
    "words": ["Finished the project on time.", "Graduated college last year.", "Entered the building.", "Discussed the problem."],
    "correct_index": 1,
    "explanation": "Missing preposition: The standard phrasing is 'Graduated *from* college'.",
    "difficulty": 2
  },
  {
    "words": ["Several interesting books.", "Many tall buildings.", "One of the best movie I've seen.", "A few good reasons."],
    "correct_index": 2,
    "explanation": "Incorrect noun number: 'One of the best' requires a plural noun following it ('movies').",
    "difficulty": 1
  },
  {
    "words": ["He hardly ever complains.", "She barely spoke.", "I didn't do nothing.", "We couldn't see anything."],
    "correct_index": 2,
    "explanation": "Double negative: 'Didn't' and 'nothing' create a double negative. Correct: 'I didn't do anything' or 'I did nothing'.",
    "difficulty": 1
  },
  {
    "words": ["Much slower now.", "More faster than before.", "Considerably heavier.", "Slightly warmer today."],
    "correct_index": 1,
    "explanation": "Double comparative: 'Faster' is already the comparative form of 'fast'. 'More' is redundant.",
    "difficulty": 1
  },
  {
    "words": ["Allow us to leave.", "He told them to wait.", "Let Jack and I go.", "She asked me to help."],
    "correct_index": 2,
    "explanation": "Pronoun case error: The verb 'Let' requires the objective case ('me'), not the subjective case ('I'). Correct: 'Let Jack and me go'.",
    "difficulty": 2
  },
  {
    "words": ["The person who called earlier.", "The house that Jack built.", "The dog what chased the cat.", "The reason why I left."],
    "correct_index": 2,
    "explanation": "Incorrect relative pronoun: 'That' or 'which' should be used for things/animals, 'who' for people. 'What' is not used this way as a relative pronoun.",
    "difficulty": 1
  },
  {
    "words": ["Tired from the journey, he rested.", "Having finished, she went home.", "Hoping you are well.", "Running quickly, the fence was jumped."],
    "correct_index": 3,
    "explanation": "Dangling modifier: The phrase 'Running quickly' seems to modify 'the fence', which is illogical. It should modify the person/animal doing the running and jumping.",
    "difficulty": 3
  },
  {
    "words": ["The primary effect was positive.", "Weather affects mood.", "The affects of the drug.", "It effected a complete change."],
    "correct_index": 2,
    "explanation": "Incorrect word choice (affect/effect): 'Effect' (noun meaning result) is needed here, not 'affects' (verb).",
    "difficulty": 2
  },
  {
    "words": ["Fewer items in the cart.", "Less traffic on the road.", "He has less worries now.", "More money, fewer problems."],
    "correct_index": 2,
    "explanation": "Incorrect word choice: 'Fewer' is used for countable nouns (like worries), while 'less' is used for uncountable nouns.",
    "difficulty": 2
  },
  {
    "words": ["The team celebrated its victory.", "Someone left his or her coat.", "Everybody forgot their keys.", "Each person has unique talents."],
    "correct_index": 2,
    "explanation": "Pronoun agreement error (traditional): 'Everybody' is singular, so traditionally it requires a singular pronoun ('his or her'). 'Their' is widely accepted in modern usage but sometimes flagged.",
    "difficulty": 2
  },
  {
    "words": ["Might have seen it.", "Could have been worse.", "Would of preferred the other.", "Should have known better."],
    "correct_index": 2,
    "explanation": "Incorrect word choice: 'Would have' (or 'would've') is the correct modal construction, not 'would of'.",
    "difficulty": 1
  },
  {
    "words": ["She sneaked out quietly.", "They hanged the picture on the wall.", "He dove into the water.", "I awoke early."],
    "correct_index": 1,
    "explanation": "Incorrect verb choice (hang/hung): 'Hung' is the past tense for hanging an object. 'Hanged' is typically reserved for executions.",
    "difficulty": 2
  },
  {
    "words": ["The dog, as well as the cats, needs feeding.", "Neither he nor they know.", "The teacher, along with the students, are going.", "Either you or I am responsible."],
    "correct_index": 2,
    "explanation": "Subject-verb agreement error: Phrases like 'along with' do not make the subject plural. The verb agrees with the main subject ('teacher'), so it should be 'is going'.",
    "difficulty": 2
  },
  {
    "words": ["She bought it for herself.", "Myself will handle it.", "He hurt himself.", "They did it themselves."],
    "correct_index": 1,
    "explanation": "Incorrect pronoun usage: Reflexive pronouns ('myself') cannot be used as the subject of a sentence. 'I' should be used.",
    "difficulty": 2
  },
  {
    "words": ["Exhausted, the hiker stopped.", "While reading, my phone rang.", "Looking out the window, the mountains were beautiful.", "To pass the exam, studying is required."],
    "correct_index": 2,
    "explanation": "Dangling modifier: It sounds like the mountains are looking out the window. Should be rephrased, e.g., 'Looking out the window, I saw the beautiful mountains.'",
    "difficulty": 3
  },
  {
    "words": ["Several phenomena were observed.", "The analysis is complete.", "A criteria for selection.", "This datum supports the theory."],
    "correct_index": 2,
    "explanation": "Incorrect number: 'Criteria' is the plural form of 'criterion'. For a single one, use 'A criterion'.",
    "difficulty": 2
  },
  {
    "words": ["Those shoes look nice.", "These books are heavy.", "I like them apples.", "That car is fast."],
    "correct_index": 2,
    "explanation": "Incorrect demonstrative adjective: 'Them' is a pronoun, not an adjective. 'Those' should be used to modify 'apples'.",
    "difficulty": 1
  },
  {
    "words": ["We went into the house.", "They arrived to the city.", "She walked towards the park.", "He flew over the ocean."],
    "correct_index": 1,
    "explanation": "Incorrect preposition: Typically, one 'arrives at' a place (like a city or building) or 'arrives in' a larger area (like a country or city). 'Arrived in' or 'Arrived at' is preferred over 'arrived to'.",
    "difficulty": 2
  },
  {
    "words": ["I eat only vegetables.", "Only I eat vegetables.", "I only eat vegetables.", "I eat vegetables only."],
    "correct_index": 2,
    "explanation": "Misplaced modifier ('only'): The placement suggests the *only* action I do is eat vegetables, which might be true but is less precise than placing 'only' directly before 'vegetables' if that's the intended meaning (that vegetables are the only food eaten). 'I eat only vegetables' is clearer for that specific meaning.",
    "difficulty": 3
  },
  {
    "words": ["The jury reached its decision.", "The staff wants a raise.", "The committee delivered their verdict.", "The audience clapped enthusiastically."],
    "correct_index": 2,
    "explanation": "Pronoun agreement (collective noun): 'Committee' is usually treated as singular (requiring 'its'), unless the members are acting individually. 'Their' implies individual actions, which might not fit the context of a single 'verdict'. 'Its' is generally safer.",
    "difficulty": 2
  },
  {
    "words": ["She knelt before the queen.", "They dealt with the problem.", "He feeled his way in the dark.", "We kept our promise."],
    "correct_index": 2,
    "explanation": "Incorrect past tense verb form: The past tense of 'feel' is 'felt'.",
    "difficulty": 1
  },
  {
    "words": ["Ascend up the stairs.", "Return back home.", "Circle around the block.", "Repeat that again."],
    "correct_index": 3,
    "explanation": "Redundancy: 'Repeat' means 'to say again', so 'again' is redundant.",
    "difficulty": 1
  },
  {
    "words": ["A one-way street.", "An university degree.", "An honest mistake.", "A useful tool."],
    "correct_index": 1,
    "explanation": "Incorrect article: 'University' starts with a consonant sound ('yoo'), so 'a' should be used instead of 'an'.",
    "difficulty": 1
  },
  {
    "words": ["My guiding principle.", "Complimenting her dress.", "The principle reason.", "A full complement of staff."],
    "correct_index": 2,
    "explanation": "Incorrect word choice (principal/principle): 'Principal' (adjective meaning main or chief) is needed here, not 'principle' (noun meaning rule or belief).",
    "difficulty": 2
  },
  {
    "words": ["Farther than I thought.", "More information is needed.", "Further down the road.", "He pushed the idea farther."],
    "correct_index": 3,
    "explanation": "Incorrect word choice (further/farther): 'Further' typically refers to metaphorical distance or extent (like pushing an idea). 'Farther' refers to physical distance. While usage blurs, 'further' is preferred here.",
    "difficulty": 3
  },
  {
    "words": ["He runs faster than I.", "They are smarter than us.", "She is taller than him.", "We work harder than them."],
    "correct_index": 0,
    "explanation": "Pronoun case error (elliptical clause): The comparison implies 'than I [run]'. 'I' (subjective case) is needed because it acts as the subject of the implied verb. 'Me' is often used colloquially but is grammatically incorrect here.",
    "difficulty": 3
  },
  {
    "words": ["She has gone home.", "He done it already.", "We were mistaken.", "They had begun eating."],
    "correct_index": 1,
    "explanation": "Incorrect past participle/past tense usage: The simple past tense is 'did'. 'Done' requires an auxiliary verb (e.g., 'has done').",
    "difficulty": 1
  },
  {
    "words": ["Take that tray to the kitchen.", "Can you bring me a drink?", "Bring this book to me.", "Take this note their."],
    "correct_index": 3,
    "explanation": "Incorrect word choice (their/there): 'There' (adverb of place) is needed, not 'their' (possessive pronoun).",
    "difficulty": 1
  },
  {
    "words": ["Scarcely enough time.", "Not hardly surprising.", "Barely visible.", "Almost finished."],
    "correct_index": 1,
    "explanation": "Double negative (implied): 'Hardly' is already negative in sense. 'Not hardly' is redundant and non-standard. Use 'Hardly surprising' or 'Not surprising'.",
    "difficulty": 2
  },
  {
    "words": ["They went altogether.", "Altogether too expensive.", "All together now!", "We were all together at the party."],
    "correct_index": 0,
    "explanation": "Incorrect word choice (altogether/all together): 'All together' (meaning in a group) is needed here. 'Altogether' means completely or entirely.",
    "difficulty": 2
  },
  {
    "words": ["Please sit here.", "The hen is setting.", "Set down and rest.", "He laid the plans on the table."],
    "correct_index": 2,
    "explanation": "Incorrect verb choice (sit/set): 'Sit' (to rest) should be used here, not 'set' (to place). Correct: 'Sit down and rest'.",
    "difficulty": 2
  },
  {
    "words": ["Whose book is this?", "Who's coming to dinner?", "The dog buried it's bone.", "It's time to leave."],
    "correct_index": 2,
    "explanation": "Incorrect contraction/possessive: 'Its' (no apostrophe) is possessive. 'It's' (with an apostrophe) is the contraction for 'it is'.",
    "difficulty": 1
  },
  {
    "words": ["The team is playing well.", "The group have decided.", "The couple holds hands.", "The family eats dinner together."],
    "correct_index": 1,
    "explanation": "Subject-verb agreement (collective noun): While 'group' can sometimes take a plural verb if members act individually ('have'), it often takes a singular verb ('has decided') when acting as a unit. Singular is generally preferred unless individuality is stressed.",
    "difficulty": 2
  },
  {
    "words": ["She invited you and me.", "Between her and him.", "Me and him saw it.", "They gave it to us."],
    "correct_index": 2,
    "explanation": "Pronoun case error: When used as part of the subject, 'I' and 'he' should be used. Correct: 'He and I saw it'.",
    "difficulty": 1
  },
  {
    "words": ["That criterion is important.", "These data suggest otherwise.", "This phenomena is rare.", "Those analyses are complex."],
    "correct_index": 2,
    "explanation": "Subject-verb agreement error: 'Phenomena' is plural (singular: phenomenon). The verb should be 'are', or the subject should be 'This phenomenon'.",
    "difficulty": 2
  },
  {
    "words": ["He acts as if he were king.", "Suppose she knew the truth.", "I wish I was taller.", "If only we had left earlier."],
    "correct_index": 2,
    "explanation": "Incorrect subjunctive mood: In hypothetical wishes contrary to fact, 'were' is traditionally used instead of 'was' for the first and third person singular.",
    "difficulty": 2
  },
  {
    "words": ["She is a student who studies hard.", "He is one of those people who complains.", "They are players who practice daily.", "It is a book that inspires."],
    "correct_index": 1,
    "explanation": "Subject-verb agreement (relative clause): The verb in the relative clause ('complains') should agree with its antecedent ('people'), which is plural. Correct: '...who complain'.",
    "difficulty": 3
  },
  {
    "words": ["Focused on the issue.", "Based on the evidence.", "Centered around the main topic.", "Revolving around the sun."],
    "correct_index": 2,
    "explanation": "Illogical phrasing: Something is 'centered on' a point, or it 'revolves around' it. 'Centered around' is geometrically problematic and considered non-standard by many.",
    "difficulty": 3
  },
  {
    "words": ["The prize will go to whoever works hardest.", "We need someone whom can be trusted.", "Ask whomever you like.", "He is the one who called."],
    "correct_index": 1,
    "explanation": "Pronoun case error: 'Who' should be used as the subject of the verb 'can be trusted' in the relative clause, not the object form 'whom'.",
    "difficulty": 3
  },
  {
    "words": ["Having finished the report, the computer was turned off.", "Tired, she went straight to bed.", "The evidence having been presented, the jury deliberated.", "Because he was late, he missed the introduction."],
    "correct_index": 0,
    "explanation": "Dangling modifier: The introductory phrase 'Having finished the report' logically refers to a person, but the subject of the main clause is 'the computer'. It sounds like the computer finished the report.",
    "difficulty": 3
  },
  {
    "words": ["The rules require that he be present.", "I suggest that she reconsider.", "It is vital that everyone understands.", "They insisted that he pays immediately."],
    "correct_index": 3,
    "explanation": "Subjunctive mood error: After verbs of demand, suggestion, necessity etc. ('insisted'), the subjunctive mood (base form of the verb, 'pay') is required in the 'that' clause, not the indicative ('pays').",
    "difficulty": 3
  },
  {
    "words": ["She likes swimming, hiking, and reading.", "To study hard and getting enough sleep are key.", "He enjoys playing chess and watching movies.", "The plan is to save money and invest wisely."],
    "correct_index": 1,
    "explanation": "Parallelism error: The elements in the list (subjects of 'are') should be in the same grammatical form. 'To study' (infinitive) and 'getting' (gerund) are not parallel. Should be 'To study... and to get...' or 'Studying... and getting...'.",
    "difficulty": 3
  },
  {
    "words": ["The number of errors was surprising.", "A number of people are waiting.", "The number of volunteers are needed.", "A large number of books were donated."],
    "correct_index": 2,
    "explanation": "Subject-verb agreement error: 'The number' is singular and takes a singular verb ('is'). 'A number' is plural and takes a plural verb ('are').",
    "difficulty": 3
  },
  {
    "words": ["The orchestra comprises seventy musicians.", "The United States consists of fifty states.", "The committee is comprised of five members.", "Fifty states compose the United States."],
    "correct_index": 2,
    "explanation": "Usage debate (comprise/compose): Traditionally, the whole 'comprises' the parts (The committee comprises five members). The parts 'compose' the whole (Five members compose the committee). 'Is comprised of' is widely used but considered incorrect by purists; 'is composed of' is preferred.",
    "difficulty": 3
  },
  {
    "words": ["He spoke quickly but clearly.", "Neither the manager nor the employees was satisfied.", "Each book and paper has been filed.", "Slow and steady wins the race."],
    "correct_index": 1,
    "explanation": "Subject-verb agreement with nor/or: The verb agrees with the noun closest to it. 'Employees' is plural, so the verb should be 'were'.",
    "difficulty": 3
  },
  {
    "words": ["Between you and me, this is confidential.", "Give the documents to whoever needs them.", "The argument was between John, Sarah, and I.", "Among the candidates, she is the most qualified."],
    "correct_index": 2,
    "explanation": "Pronoun case error: Prepositions like 'between' govern the objective case. 'I' (subjective) should be 'me' (objective). Correct: '...between John, Sarah, and me'.",
    "difficulty": 3
  },
  {
    "words": ["The reason I called is that I need help.", "He was so tired, he fell asleep.", "Being that it's late, we should leave.", "Because it was raining, the game was cancelled."],
    "correct_index": 2,
    "explanation": "Non-standard causal phrase: 'Being that' or 'Being as' are considered non-standard or informal ways to express cause. Use 'Because', 'Since', or 'As'.",
    "difficulty": 3
  },
  {
    "words": ["Try to understand my position.", "Be sure and check the locks.", "Come see us when you can.", "Go find your shoes."],
    "correct_index": 1,
    "explanation": "Incorrect idiom/construction: The standard idiom is 'Be sure to check', not 'Be sure and check'. The 'try and', 'come see', 'go find' constructions are common but sometimes considered less formal or standard than 'try to', 'come to see', 'go to find'. 'Be sure and' is less accepted.",
    "difficulty": 3
  }
]

# Données pour le mode Grammaire - Conjugaison de verbes
verb_conjugation_data = [
    # Present Simple
    {
        "sentence": "She {verb} to the store every day.",
        "verb": "go",
        "tense": "present simple",
        "correct_form": "goes",
        "difficulty": 1
    },
    {
        "sentence": "They {verb} football on weekends.",
        "verb": "play",
        "tense": "present simple",
        "correct_form": "play",
        "difficulty": 1
    },
    {
        "sentence": "He {verb} three languages fluently.",
        "verb": "speak",
        "tense": "present simple",
        "correct_form": "speaks",
        "difficulty": 1
    },
    {
        "sentence": "The sun {verb} in the east.",
        "verb": "rise",
        "tense": "present simple",
        "correct_form": "rises",
        "difficulty": 1
    },
    {
        "sentence": "My parents {verb} in London.",
        "verb": "live",
        "tense": "present simple",
        "correct_form": "live",
        "difficulty": 1
    },
    {
        "sentence": "Water {verb} at 100 degrees Celsius.",
        "verb": "boil",
        "tense": "present simple",
        "correct_form": "boils",
        "difficulty": 1
    },
    {
        "sentence": "I usually {verb} up at 7 AM.",
        "verb": "wake",
        "tense": "present simple",
        "correct_form": "wake",
        "difficulty": 1
    },
    {
        "sentence": "Does he {verb} coffee every morning?",
        "verb": "drink",
        "tense": "present simple",
        "correct_form": "drink",
        "difficulty": 1
    },
    {
        "sentence": "She {verb} TV in the evening.",
        "verb": "watch",
        "tense": "present simple",
        "correct_form": "watches",
        "difficulty": 1
    },
    {
        "sentence": "We {verb} our grandparents often.",
        "verb": "visit",
        "tense": "present simple",
        "correct_form": "visit",
        "difficulty": 1
    },
    {
        "sentence": "He does not {verb} spicy food.",
        "verb": "like",
        "tense": "present simple",
        "correct_form": "like",
        "difficulty": 1
    },
    {
        "sentence": "The Earth {verb} around the Sun.",
        "verb": "revolve",
        "tense": "present simple",
        "correct_form": "revolves",
        "difficulty": 1
    },

    # Past Simple
    {
        "sentence": "Yesterday, I {verb} to the cinema with my friends.",
        "verb": "go",
        "tense": "past simple",
        "correct_form": "went",
        "difficulty": 1
    },
    {
        "sentence": "She {verb} her homework last night.",
        "verb": "finish",
        "tense": "past simple",
        "correct_form": "finished",
        "difficulty": 1
    },
    {
        "sentence": "They {verb} a new car last month.",
        "verb": "buy",
        "tense": "past simple",
        "correct_form": "bought",
        "difficulty": 2
    },
    {
        "sentence": "We {verb} a great time at the party.",
        "verb": "have",
        "tense": "past simple",
        "correct_form": "had",
        "difficulty": 1
    },
    {
        "sentence": "The teacher {verb} us a difficult test.",
        "verb": "give",
        "tense": "past simple",
        "correct_form": "gave",
        "difficulty": 2
    },
    {
        "sentence": "He {verb} the window yesterday.",
        "verb": "break",
        "tense": "past simple",
        "correct_form": "broke",
        "difficulty": 2
    },
    {
        "sentence": "I {verb} a delicious meal for dinner.",
        "verb": "eat",
        "tense": "past simple",
        "correct_form": "ate",
        "difficulty": 2
    },
    {
        "sentence": "Did you {verb} the movie last week?",
        "verb": "see",
        "tense": "past simple",
        "correct_form": "see",
        "difficulty": 2
    },
    {
        "sentence": "They did not {verb} to the concert.",
        "verb": "go",
        "tense": "past simple",
        "correct_form": "go",
        "difficulty": 1
    },
    {
        "sentence": "She {verb} a letter to her friend.",
        "verb": "write",
        "tense": "past simple",
        "correct_form": "wrote",
        "difficulty": 2
    },
    {
        "sentence": "We {verb} in that house for five years.",
        "verb": "live",
        "tense": "past simple",
        "correct_form": "lived",
        "difficulty": 1
    },
    {
        "sentence": "The cat {verb} up the tree quickly.",
        "verb": "climb",
        "tense": "past simple",
        "correct_form": "climbed",
        "difficulty": 1
    },

    # Present Continuous
    {
        "sentence": "Look! She {verb} a beautiful dress.",
        "verb": "wear",
        "tense": "present continuous",
        "correct_form": "is wearing",
        "difficulty": 1
    },
    {
        "sentence": "They {verb} for their exam right now.",
        "verb": "study",
        "tense": "present continuous",
        "correct_form": "are studying",
        "difficulty": 1
    },
    {
        "sentence": "I {verb} to music while I work.",
        "verb": "listen",
        "tense": "present continuous",
        "correct_form": "am listening",
        "difficulty": 1
    },
    {
        "sentence": "What are you {verb} this weekend?",
        "verb": "do",
        "tense": "present continuous",
        "correct_form": "doing",
        "difficulty": 1
    },
    {
        "sentence": "The children {verb} in the garden.",
        "verb": "play",
        "tense": "present continuous",
        "correct_form": "are playing",
        "difficulty": 1
    },
    {
        "sentence": "Please be quiet, the baby {verb}.",
        "verb": "sleep",
        "tense": "present continuous",
        "correct_form": "is sleeping",
        "difficulty": 1
    },
    {
        "sentence": "He {verb} dinner at the moment.",
        "verb": "cook",
        "tense": "present continuous",
        "correct_form": "is cooking",
        "difficulty": 1
    },
    {
        "sentence": "Is it {verb} outside now?",
        "verb": "rain",
        "tense": "present continuous",
        "correct_form": "raining",
        "difficulty": 1
    },
    {
        "sentence": "We {verb} a new project this month.",
        "verb": "start",
        "tense": "present continuous",
        "correct_form": "are starting",
        "difficulty": 1
    },
    {
        "sentence": "Why are you {verb} that coat? It's not cold.",
        "verb": "wear",
        "tense": "present continuous",
        "correct_form": "wearing",
        "difficulty": 1
    },
     {
        "sentence": "She {verb} always {verb} her keys!", # Keeping this as is, special use case of present continuous for annoyance
        "verb": "lose",
        "tense": "present continuous",
        "correct_form": "is always losing",
        "difficulty": 2
    },
    {
        "sentence": "I am not {verb} well today.",
        "verb": "feel",
        "tense": "present continuous",
        "correct_form": "feeling",
        "difficulty": 1
    },

    # Past Continuous
    {
        "sentence": "They {verb} the project when the power went out.",
        "verb": "complete",
        "tense": "past continuous",
        "correct_form": "were completing",
        "difficulty": 2
    },
    {
        "sentence": "She {verb} dinner when I called.",
        "verb": "cook",
        "tense": "past continuous",
        "correct_form": "was cooking",
        "difficulty": 1
    },
    {
        "sentence": "We {verb} TV when the storm started.",
        "verb": "watch",
        "tense": "past continuous",
        "correct_form": "were watching",
        "difficulty": 1
    },
    {
        "sentence": "What were you {verb} at 8 pm last night?",
        "verb": "do",
        "tense": "past continuous",
        "correct_form": "doing",
        "difficulty": 2
    },
    {
        "sentence": "I {verb} when the phone rang.",
        "verb": "sleep",
        "tense": "past continuous",
        "correct_form": "was sleeping",
        "difficulty": 1
    },
    {
        "sentence": "The sun {verb} when I woke up.",
        "verb": "shine",
        "tense": "past continuous",
        "correct_form": "was shining",
        "difficulty": 1
    },
    {
        "sentence": "He {verb} his bike when he fell off.",
        "verb": "ride",
        "tense": "past continuous",
        "correct_form": "was riding",
        "difficulty": 1
    },
    {
        "sentence": "While they {verb}, the doorbell rang.",
        "verb": "eat",
        "tense": "past continuous",
        "correct_form": "were eating",
        "difficulty": 2
    },
    {
        "sentence": "She was not {verb} attention during the meeting.",
        "verb": "pay",
        "tense": "past continuous",
        "correct_form": "paying",
        "difficulty": 1
    },
    {
        "sentence": "Were they {verb} for the bus when the accident happened?",
        "verb": "wait",
        "tense": "past continuous",
        "correct_form": "waiting",
        "difficulty": 1
    },
    {
        "sentence": "At this time yesterday, I {verb} home.",
        "verb": "drive",
        "tense": "past continuous",
        "correct_form": "was driving",
        "difficulty": 1
    },
    {
        "sentence": "The birds {verb} sweetly in the morning.",
        "verb": "sing",
        "tense": "past continuous",
        "correct_form": "were singing",
        "difficulty": 2
    },

    # Present Perfect
    {
        "sentence": "I {verb} to Paris three times.",
        "verb": "be",
        "tense": "present perfect",
        "correct_form": "have been",
        "difficulty": 2
    },
    {
        "sentence": "She {verb} her car keys.",
        "verb": "lose",
        "tense": "present perfect",
        "correct_form": "has lost",
        "difficulty": 2
    },
    {
        "sentence": "They haven't {verb} their homework yet.",
        "verb": "finish",
        "tense": "present perfect",
        "correct_form": "finished",
        "difficulty": 2
    },
    {
        "sentence": "We {verb} here since 2010.",
        "verb": "live",
        "tense": "present perfect",
        "correct_form": "have lived",
        "difficulty": 2
    },
    {
        "sentence": "Have you ever {verb} sushi?",
        "verb": "try",
        "tense": "present perfect",
        "correct_form": "tried",
        "difficulty": 2
    },
    {
        "sentence": "He has just {verb} the email.",
        "verb": "send",
        "tense": "present perfect",
        "correct_form": "sent",
        "difficulty": 2
    },
    {
        "sentence": "Someone {verb} my bike!",
        "verb": "steal",
        "tense": "present perfect",
        "correct_form": "has stolen",
        "difficulty": 2
    },
    {
        "sentence": "I have never {verb} such a beautiful place.",
        "verb": "see",
        "tense": "present perfect",
        "correct_form": "seen",
        "difficulty": 2
    },
    {
        "sentence": "She has already {verb} that movie.",
        "verb": "watch",
        "tense": "present perfect",
        "correct_form": "watched",
        "difficulty": 2
    },
    {
        "sentence": "Has he {verb} the report yet?",
        "verb": "write",
        "tense": "present perfect",
        "correct_form": "written",
        "difficulty": 2
    },
    {
        "sentence": "They {verb} known each other for many years.",
        "verb": "know",
        "tense": "present perfect",
        "correct_form": "have known",
        "difficulty": 2
    },
    {
        "sentence": "My sister {verb} her arm.",
        "verb": "break",
        "tense": "present perfect",
        "correct_form": "has broken",
        "difficulty": 2
    },

    # Past Perfect
    {
        "sentence": "She had already {verb} dinner when I arrived.",
        "verb": "cook",
        "tense": "past perfect",
        "correct_form": "cooked",
        "difficulty": 3
    },
    {
        "sentence": "The train {verb} by the time we got to the station.",
        "verb": "leave",
        "tense": "past perfect",
        "correct_form": "had left",
        "difficulty": 3
    },
    {
        "sentence": "I had never {verb} such a beautiful sunset before.",
        "verb": "see",
        "tense": "past perfect",
        "correct_form": "seen",
        "difficulty": 3
    },
    {
        "sentence": "They {verb} to the museum before they visited the castle.",
        "verb": "go",
        "tense": "past perfect",
        "correct_form": "had gone",
        "difficulty": 3
    },
    {
        "sentence": "We {verb} the film twice before it was removed from theaters.",
        "verb": "watch",
        "tense": "past perfect",
        "correct_form": "had watched",
        "difficulty": 3
    },
    {
        "sentence": "He couldn't enter the house because he {verb} his keys.",
        "verb": "lose",
        "tense": "past perfect",
        "correct_form": "had lost",
        "difficulty": 3
    },
    {
        "sentence": "She told me she {verb} him before.",
        "verb": "meet",
        "tense": "past perfect",
        "correct_form": "had met",
        "difficulty": 3
    },
    {
        "sentence": "By the time I finished work, everyone {verb} home.",
        "verb": "go",
        "tense": "past perfect",
        "correct_form": "had gone",
        "difficulty": 3
    },
    {
        "sentence": "They had not {verb} breakfast when they left.",
        "verb": "eat",
        "tense": "past perfect",
        "correct_form": "eaten",
        "difficulty": 3
    },
    {
        "sentence": "Had you {verb} the book before you saw the movie?",
        "verb": "read",
        "tense": "past perfect",
        "correct_form": "read",
        "difficulty": 3
    },
    {
        "sentence": "I realized I {verb} a mistake.",
        "verb": "make",
        "tense": "past perfect",
        "correct_form": "had made",
        "difficulty": 3
    },
    {
        "sentence": "The flowers {verb} because nobody had watered them.",
        "verb": "die",
        "tense": "past perfect",
        "correct_form": "had died",
        "difficulty": 3
    },

    # Future Simple
    {
        "sentence": "I {verb} you tomorrow.",
        "verb": "call",
        "tense": "future simple",
        "correct_form": "will call",
        "difficulty": 1
    },
    {
        "sentence": "They {verb} to the beach next weekend.",
        "verb": "go",
        "tense": "future simple",
        "correct_form": "will go",
        "difficulty": 1
    },
    {
        "sentence": "She {verb} the exam next month.",
        "verb": "take",
        "tense": "future simple",
        "correct_form": "will take",
        "difficulty": 1
    },
    {
        "sentence": "We {verb} your invitation, thank you.",
        "verb": "accept",
        "tense": "future simple",
        "correct_form": "will accept",
        "difficulty": 1
    },
    {
        "sentence": "The concert {verb} at 8 pm tomorrow.",
        "verb": "start",
        "tense": "future simple",
        "correct_form": "will start",
        "difficulty": 1
    },
    {
        "sentence": "It looks like it {verb} soon.",
        "verb": "rain",
        "tense": "future simple",
        "correct_form": "will rain",
        "difficulty": 1
    },
    {
        "sentence": "He will probably {verb} late.",
        "verb": "be",
        "tense": "future simple",
        "correct_form": "be",
        "difficulty": 1
    },
    {
        "sentence": "I promise I won't {verb} anyone.",
        "verb": "tell",
        "tense": "future simple",
        "correct_form": "tell",
        "difficulty": 1
    },
    {
        "sentence": "Will you {verb} me with this?",
        "verb": "help",
        "tense": "future simple",
        "correct_form": "help",
        "difficulty": 1
    },
    {
        "sentence": "Don't worry, I {verb} careful.",
        "verb": "be",
        "tense": "future simple",
        "correct_form": "will be",
        "difficulty": 1
    },
    {
        "sentence": "She thinks she {verb} the competition.",
        "verb": "win",
        "tense": "future simple",
        "correct_form": "will win",
        "difficulty": 2
    },
    {
        "sentence": "We {verb} a party next Saturday.",
        "verb": "have",
        "tense": "future simple",
        "correct_form": "will have",
        "difficulty": 1
    },

    # Future Perfect
    {
        "sentence": "By next month, I {verb} here for five years.",
        "verb": "work",
        "tense": "future perfect",
        "correct_form": "will have worked",
        "difficulty": 3
    },
    {
        "sentence": "By the time you arrive, I {verb} dinner.",
        "verb": "prepare",
        "tense": "future perfect",
        "correct_form": "will have prepared",
        "difficulty": 3
    },
    {
        "sentence": "They {verb} the project before the deadline.",
        "verb": "complete",
        "tense": "future perfect",
        "correct_form": "will have completed",
        "difficulty": 3
    },
    {
        "sentence": "By next year, she {verb} from university.",
        "verb": "graduate",
        "tense": "future perfect",
        "correct_form": "will have graduated",
        "difficulty": 3
    },
    {
        "sentence": "By the end of this week, we {verb} all the exercises.",
        "verb": "finish",
        "tense": "future perfect",
        "correct_form": "will have finished",
        "difficulty": 3
    },
     {
        "sentence": "He {verb} the book by tomorrow morning.",
        "verb": "read",
        "tense": "future perfect",
        "correct_form": "will have read",
        "difficulty": 3
    },
    {
        "sentence": "By 2030, scientists {verb} a cure for the disease.",
        "verb": "find",
        "tense": "future perfect",
        "correct_form": "will have found",
        "difficulty": 3
    },
    {
        "sentence": "She won't have {verb} packing by the time the taxi comes.",
        "verb": "finish",
        "tense": "future perfect",
        "correct_form": "finished",
        "difficulty": 3
    },
    {
        "sentence": "Will they have {verb} building the bridge by next summer?",
        "verb": "finish",
        "tense": "future perfect",
        "correct_form": "finished",
        "difficulty": 3
    },
    {
        "sentence": "In five years' time, I {verb} my own company.",
        "verb": "start",
        "tense": "future perfect",
        "correct_form": "will have started",
        "difficulty": 3
    },

    # Present Perfect Continuous
    {
        "sentence": "I {verb} for three hours.",
        "verb": "study",
        "tense": "present perfect continuous",
        "correct_form": "have been studying",
        "difficulty": 3
    },
    {
        "sentence": "She {verb} all day.",
        "verb": "work",
        "tense": "present perfect continuous",
        "correct_form": "has been working",
        "difficulty": 3
    },
    {
        "sentence": "They {verb} in London since 2015.",
        "verb": "live",
        "tense": "present perfect continuous",
        "correct_form": "have been living",
        "difficulty": 3
    },
    {
        "sentence": "How long have you been {verb} English?",
        "verb": "learn",
        "tense": "present perfect continuous",
        "correct_form": "learning",
        "difficulty": 3
    },
    {
        "sentence": "It {verb} all morning.",
        "verb": "rain",
        "tense": "present perfect continuous",
        "correct_form": "has been raining",
        "difficulty": 2
    },
    {
        "sentence": "He {verb} guitar for two hours.",
        "verb": "play",
        "tense": "present perfect continuous",
        "correct_form": "has been playing",
        "difficulty": 3
    },
    {
        "sentence": "We {verb} for you for ages!",
        "verb": "wait",
        "tense": "present perfect continuous",
        "correct_form": "have been waiting",
        "difficulty": 3
    },
     {
        "sentence": "Your eyes are red. Have you been {verb}?",
        "verb": "cry",
        "tense": "present perfect continuous",
        "correct_form": "crying",
        "difficulty": 3
    },
    {
        "sentence": "I haven't been {verb} well recently.",
        "verb": "feel",
        "tense": "present perfect continuous",
        "correct_form": "feeling",
        "difficulty": 3
    },
    {
        "sentence": "She {verb} that book since yesterday.",
        "verb": "read",
        "tense": "present perfect continuous",
        "correct_form": "has been reading",
        "difficulty": 3
    },

    # Past Perfect Continuous
    {
        "sentence": "He was tired because he {verb} all night.",
        "verb": "drive",
        "tense": "past perfect continuous",
        "correct_form": "had been driving",
        "difficulty": 3
    },
    {
        "sentence": "They {verb} for only five minutes when it started to pour.",
        "verb": "walk",
        "tense": "past perfect continuous",
        "correct_form": "had been walking",
        "difficulty": 3
    },
    {
        "sentence": "She {verb} on the project for months before she finally presented it.",
        "verb": "work",
        "tense": "past perfect continuous",
        "correct_form": "had been working",
        "difficulty": 3
    },
    {
        "sentence": "How long had you been {verb} before you found a job?",
        "verb": "look",
        "tense": "past perfect continuous",
        "correct_form": "looking",
        "difficulty": 3
    },
    {
        "sentence": "I hadn't been {verb} long when you called.",
        "verb": "wait",
        "tense": "past perfect continuous",
        "correct_form": "waiting",
        "difficulty": 3
    },
    {
        "sentence": "The ground was wet because it {verb}.",
        "verb": "rain",
        "tense": "past perfect continuous",
        "correct_form": "had been raining",
        "difficulty": 3
    },
    {
        "sentence": "We {verb} about moving house for a year before we finally did.",
        "verb": "talk",
        "tense": "past perfect continuous",
        "correct_form": "had been talking",
        "difficulty": 3
    },

    # Future Continuous
    {
        "sentence": "This time tomorrow, I {verb} on a beach.",
        "verb": "lie",
        "tense": "future continuous",
        "correct_form": "will be lying",
        "difficulty": 2
    },
    {
        "sentence": "Don't call at 8 PM; we {verb} dinner then.",
        "verb": "have",
        "tense": "future continuous",
        "correct_form": "will be having",
        "difficulty": 2
    },
    {
        "sentence": "What will you be {verb} at 10 AM next Monday?",
        "verb": "do",
        "tense": "future continuous",
        "correct_form": "doing",
        "difficulty": 2
    },
    {
        "sentence": "She won't be {verb} when you arrive; she has a late meeting.",
        "verb": "sleep",
        "tense": "future continuous",
        "correct_form": "sleeping",
        "difficulty": 2
    },
    {
        "sentence": "This evening, we {verb} the match.",
        "verb": "watch",
        "tense": "future continuous",
        "correct_form": "will be watching",
        "difficulty": 2
    },
    {
        "sentence": "Will you be {verb} us at the party tonight?",
        "verb": "join",
        "tense": "future continuous",
        "correct_form": "joining",
        "difficulty": 2
    },

    # Future Perfect Continuous
    {
        "sentence": "By next June, I {verb} here for ten years.",
        "verb": "teach",
        "tense": "future perfect continuous",
        "correct_form": "will have been teaching",
        "difficulty": 3
    },
    {
        "sentence": "When he retires, he {verb} for the company for 30 years.",
        "verb": "work",
        "tense": "future perfect continuous",
        "correct_form": "will have been working",
        "difficulty": 3
    },
    {
        "sentence": "By the time the guests arrive, she {verb} for hours.",
        "verb": "cook",
        "tense": "future perfect continuous",
        "correct_form": "will have been cooking",
        "difficulty": 3
    },
    {
        "sentence": "In September, they {verb} married for 20 years.",
        "verb": "be",
        "tense": "future perfect continuous",
        "correct_form": "will have been married", # Note: 'be married' is state, continuous less common but possible
        "difficulty": 3
    },
    {
        "sentence": "How long will you have been {verb} when you finally finish your degree?",
        "verb": "study",
        "tense": "future perfect continuous",
        "correct_form": "studying",
        "difficulty": 3
    },

    # Conditionals and Modal Verbs
    {
        "sentence": "If I {verb} more time, I would visit you.",
        "verb": "have",
        "tense": "second conditional",
        "correct_form": "had",
        "difficulty": 2
    },
    {
        "sentence": "She {verb} to the party if she isn't busy.",
        "verb": "come",
        "tense": "first conditional",
        "correct_form": "will come",
        "difficulty": 2
    },
    {
        "sentence": "If I {verb} you, I would take the job.",
        "verb": "be",
        "tense": "second conditional",
        "correct_form": "were",
        "difficulty": 2
    },
    {
        "sentence": "You {verb} see a doctor.", # Rephrased from 'had better'
        "verb": "should",
        "tense": "modal verb advice",
        "correct_form": "should",
        "difficulty": 1
    },
    {
        "sentence": "If it rains tomorrow, we {verb} the picnic.",
        "verb": "cancel",
        "tense": "first conditional",
        "correct_form": "will cancel",
        "difficulty": 2
    },
    {
        "sentence": "If you {verb} ice, it melts.",
        "verb": "heat",
        "tense": "zero conditional",
        "correct_form": "heat",
        "difficulty": 1
    },
    {
        "sentence": "If she had studied harder, she {verb} the exam.",
        "verb": "pass",
        "tense": "third conditional",
        "correct_form": "would have passed",
        "difficulty": 3
    },
    {
        "sentence": "I {verb} swim when I was five.",
        "verb": "can",
        "tense": "modal verb past ability",
        "correct_form": "could",
        "difficulty": 1
    },
    {
        "sentence": "You {verb} be quiet in the library.",
        "verb": "must",
        "tense": "modal verb obligation",
        "correct_form": "must",
        "difficulty": 1
    },
    {
        "sentence": "It {verb} rain later, take an umbrella.",
        "verb": "might",
        "tense": "modal verb possibility",
        "correct_form": "might",
        "difficulty": 1
    },
    {
        "sentence": "If I {verb} known you were coming, I would have baked a cake.",
        "verb": "know",
        "tense": "third conditional",
        "correct_form": "had known",
        "difficulty": 3
    },
    {
        "sentence": "You should have {verb} me sooner!",
        "verb": "tell",
        "tense": "modal verb past criticism",
        "correct_form": "told",
        "difficulty": 3
    },
    {
        "sentence": "He can't have {verb} the meeting; he's usually punctual.",
        "verb": "forget",
        "tense": "modal verb past deduction (impossibility)",
        "correct_form": "forgotten",
        "difficulty": 3
    },
    {
        "sentence": "If water {verb} 0 degrees, it freezes.",
        "verb": "reach",
        "tense": "zero conditional",
        "correct_form": "reaches",
        "difficulty": 1
    },
    {
        "sentence": "{verb} I use your phone?",
        "verb": "may",
        "tense": "modal verb permission",
        "correct_form": "May",
        "difficulty": 1
    },
    {
        "sentence": "What would you {verb} if you found a wallet on the street?",
        "verb": "do",
        "tense": "second conditional",
        "correct_form": "do",
        "difficulty": 2
    },
    {
        "sentence": "The lights are off. They must have {verb} out.",
        "verb": "go",
        "tense": "modal verb past deduction (certainty)",
        "correct_form": "gone",
        "difficulty": 3
    },

    # Passive Voice Mix
    {
        "sentence": "English {verb} all over the world.",
        "verb": "speak",
        "tense": "present simple passive",
        "correct_form": "is spoken",
        "difficulty": 2
    },
    {
        "sentence": "The Mona Lisa {verb} by Leonardo da Vinci.",
        "verb": "paint",
        "tense": "past simple passive",
        "correct_form": "was painted",
        "difficulty": 2
    },
    {
        "sentence": "My car is being {verb} right now.",
        "verb": "repair",
        "tense": "present continuous passive",
        "correct_form": "repaired",
        "difficulty": 3
    },
    {
        "sentence": "The results will be {verb} tomorrow.",
        "verb": "announce",
        "tense": "future simple passive",
        "correct_form": "announced",
        "difficulty": 2
    },
    {
        "sentence": "The house has recently been {verb}.",
        "verb": "sell",
        "tense": "present perfect passive",
        "correct_form": "sold",
        "difficulty": 3
    },
    {
        "sentence": "This work must be {verb} by 5 pm.",
        "verb": "finish",
        "tense": "modal passive",
        "correct_form": "finished",
        "difficulty": 2
    },
    {
        "sentence": "The thief {verb} caught yesterday.",
        "verb": "catch",
        "tense": "past simple passive",
        "correct_form": "was caught",
        "difficulty": 2
    },
    {
        "sentence": "Mistakes {verb} made by everyone.",
        "verb": "make",
        "tense": "present simple passive",
        "correct_form": "are made",
        "difficulty": 2
    },
    {
        "sentence": "The project will have been {verb} by next week.",
        "verb": "complete",
        "tense": "future perfect passive",
        "correct_form": "completed",
        "difficulty": 3
    },
    {
        "sentence": "Rome was not {verb} in a day.",
        "verb": "build",
        "tense": "past simple passive",
        "correct_form": "built",
        "difficulty": 2
    }
]

# Données pour le mode Grammaire - Phrasal verbs
phrasal_verb_data = [
    {
        "verb": "look",
        "particle": "up",
        "meaning": "Search for information in a reference book or database",
        "example": "If you don't know the meaning of a word, look it up in a dictionary.",
        "difficulty": 1
    },
    {
        "verb": "give",
        "particle": "up",
        "meaning": "Stop trying to do something",
        "example": "Don't give up on your dreams, keep working hard.",
        "difficulty": 1
    },
    {
        "verb": "put",
        "particle": "off",
        "meaning": "Postpone or delay something",
        "example": "We'll have to put off the meeting until next week.",
        "difficulty": 1
    },
    {
        "verb": "break",
        "particle": "down",
        "meaning": "Stop working or functioning",
        "example": "My car broke down on the way to work this morning.",
        "difficulty": 1
    },
    {
        "verb": "turn",
        "particle": "down",
        "meaning": "Refuse an offer or request",
        "example": "She turned down the job offer because the salary was too low.",
        "difficulty": 1
    },
    {
        "verb": "come",
        "particle": "across",
        "meaning": "Find something by chance",
        "example": "I came across an old photo album while cleaning the attic.",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "along",
        "meaning": "Have a good relationship with someone",
        "example": "They get along well despite their differences.",
        "difficulty": 1
    },
    {
        "verb": "run",
        "particle": "into",
        "meaning": "Meet someone by chance",
        "example": "I ran into my old teacher at the supermarket yesterday.",
        "difficulty": 1
    },
    {
        "verb": "take",
        "particle": "off",
        "meaning": "Remove something (like clothing)",
        "example": "Take off your shoes before entering the house.",
        "difficulty": 1
    },
    {
        "verb": "make",
        "particle": "up",
        "meaning": "Invent a story or lie",
        "example": "He made up an excuse for being late to work.",
        "difficulty": 1
    },
    {
        "verb": "go",
        "particle": "through",
        "meaning": "Experience a difficult time",
        "example": "She's going through a difficult divorce right now.",
        "difficulty": 2
    },
    {
        "verb": "bring",
        "particle": "up",
        "meaning": "Mention or introduce a topic",
        "example": "I didn't want to bring up the subject of money at dinner.",
        "difficulty": 1
    },
    {
        "verb": "hold",
        "particle": "on",
        "meaning": "Wait for a short time",
        "example": "Please hold on while I check if she's available.",
        "difficulty": 1
    },
    {
        "verb": "figure",
        "particle": "out",
        "meaning": "Solve or understand something",
        "example": "It took me a while to figure out how to use the new software.",
        "difficulty": 1
    },
    {
        "verb": "carry",
        "particle": "on",
        "meaning": "Continue doing something",
        "example": "Despite the rain, they carried on with the outdoor concert.",
        "difficulty": 1
    },
    {
        "verb": "set",
        "particle": "up",
        "meaning": "Arrange or organize something",
        "example": "We need to set up a meeting with the new clients.",
        "difficulty": 1
    },
    {
        "verb": "grow",
        "particle": "up",
        "meaning": "Become an adult",
        "example": "He grew up in a small town in the countryside.",
        "difficulty": 1
    },
    {
        "verb": "call",
        "particle": "off",
        "meaning": "Cancel something that was planned",
        "example": "They had to call off the wedding due to a family emergency.",
        "difficulty": 1
    },
    {
        "verb": "work",
        "particle": "out",
        "meaning": "Exercise to improve your physical fitness",
        "example": "She works out at the gym three times a week.",
        "difficulty": 1
    },
    {
        "verb": "pick",
        "particle": "up",
        "meaning": "Collect someone or something",
        "example": "I'll pick you up at the airport tomorrow.",
        "difficulty": 1
    },
    {
        "verb": "drop",
        "particle": "by",
        "meaning": "Visit without a formal invitation",
        "example": "Feel free to drop by whenever you're in the neighborhood.",
        "difficulty": 2
    },
    {
        "verb": "cheer",
        "particle": "up",
        "meaning": "Make someone feel happier",
        "example": "I bought her flowers to cheer her up after the bad news.",
        "difficulty": 1
    },
    {
        "verb": "look",
        "particle": "after",
        "meaning": "Take care of or be responsible for someone or something",
        "example": "Could you look after my dog while I'm on vacation?",
        "difficulty": 1
    },
    {
        "verb": "check",
        "particle": "in",
        "meaning": "Register at a hotel or for a flight",
        "example": "You should check in at least two hours before your flight.",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "over",
        "meaning": "Recover from an illness, disappointment, or failure",
        "example": "It took him months to get over his ex-girlfriend.",
        "difficulty": 2
    },
    {
        "verb": "cut",
        "particle": "off",
        "meaning": "Interrupt or stop a supply or connection",
        "example": "The electricity was cut off because they didn't pay the bill.",
        "difficulty": 2
    },
    {
        "verb": "pull",
        "particle": "over",
        "meaning": "Move a vehicle to the side of the road and stop",
        "example": "The police officer asked him to pull over for speeding.",
        "difficulty": 1
    },
    {
        "verb": "put",
        "particle": "on",
        "meaning": "Get dressed in something",
        "example": "Put on a warm jacket before going outside.",
        "difficulty": 1
    },
    {
        "verb": "turn",
        "particle": "up",
        "meaning": "Arrive, especially unexpectedly",
        "example": "He turned up at the party without an invitation.",
        "difficulty": 2
    },
    {
        "verb": "wear",
        "particle": "out",
        "meaning": "Make something unusable through overuse",
        "example": "He wore out his shoes after walking for miles every day.",
        "difficulty": 2
    },
    {
        "verb": "show",
        "particle": "off",
        "meaning": "Behave in a way intended to attract attention or impress others",
        "example": "He bought an expensive car just to show off to his friends.",
        "difficulty": 1
    },
    {
        "verb": "hang",
        "particle": "out",
        "meaning": "Spend time relaxing or socializing",
        "example": "We often hang out at the local café after school.",
        "difficulty": 1
    },
    {
        "verb": "back",
        "particle": "up",
        "meaning": "Make a copy of computer data for security",
        "example": "Don't forget to back up your files before updating the system.",
        "difficulty": 2
    },
    {
        "verb": "keep",
        "particle": "up",
        "meaning": "Maintain the same level or standard",
        "example": "If you keep up this level of work, you'll get a promotion soon.",
        "difficulty": 2
    },
    {
        "verb": "take",
        "particle": "over",
        "meaning": "Assume control or responsibility",
        "example": "The assistant manager will take over while the manager is on leave.",
        "difficulty": 2
    },
    {
        "verb": "come",
        "particle": "up",
        "meaning": "Arise or occur unexpectedly",
        "example": "Something important came up, so I had to cancel our meeting.",
        "difficulty": 2
    },
    {
        "verb": "look",
        "particle": "forward to",
        "meaning": "Anticipate something with pleasure",
        "example": "I'm looking forward to seeing you next week.",
        "difficulty": 1
    },
    {
        "verb": "pay",
        "particle": "back",
        "meaning": "Return borrowed money",
        "example": "I'll pay you back as soon as I get my salary.",
        "difficulty": 1
    },
    {
        "verb": "turn",
        "particle": "on",
        "meaning": "Start a machine or device by pressing a button or moving a switch",
        "example": "Can you turn on the lights? It's getting dark.",
        "difficulty": 1
    },
    {
        "verb": "throw",
        "particle": "away",
        "meaning": "Dispose of something you no longer want",
        "example": "Don't throw away those old books; we can donate them to the library.",
        "difficulty": 1
    },
    {
        "verb": "point",
        "particle": "out",
        "meaning": "Draw attention to something",
        "example": "The teacher pointed out several mistakes in my essay.",
        "difficulty": 2
    },
    {
        "verb": "fill",
        "particle": "in",
        "meaning": "Complete a form with the required information",
        "example": "Please fill in this application form and submit it by Friday.",
        "difficulty": 1
    },
    {
        "verb": "let",
        "particle": "down",
        "meaning": "Disappoint someone by failing to do what was expected",
        "example": "I don't want to let down my parents by failing the exam.",
        "difficulty": 2
    },
    {
        "verb": "stand",
        "particle": "for",
        "meaning": "Represent or be a symbol for something",
        "example": "The letters 'UN' stand for 'United Nations'.",
        "difficulty": 2
    },
    {
        "verb": "wrap",
        "particle": "up",
        "meaning": "Complete or finish something",
        "example": "Let's wrap up this meeting; it's getting late.",
        "difficulty": 2
    },
    {
        "verb": "get",
        "particle": "by",
        "meaning": "Manage with difficulty",
        "example": "We're just getting by on one salary since my husband lost his job.",
        "difficulty": 3
    },
    {
        "verb": "break",
        "particle": "up",
        "meaning": "End a relationship",
        "example": "They broke up after dating for three years.",
        "difficulty": 1
    },
    {
        "verb": "deal",
        "particle": "with",
        "meaning": "Handle a situation or problem",
        "example": "The manager is dealing with the customer complaint right now.",
        "difficulty": 2
    },
    {
        "verb": "run",
        "particle": "out of",
        "meaning": "Have no more of something",
        "example": "We've run out of milk; I need to go to the store.",
        "difficulty": 1
    },
    {
        "verb": "give",
        "particle": "away",
        "meaning": "Reveal information accidentally",
        "example": "Her smile gave away the fact that she was hiding something.",
        "difficulty": 2
    },
    {
        "verb": "put",
        "particle": "up with",
        "meaning": "Tolerate something unpleasant",
        "example": "I don't know how you put up with all that noise from your neighbors.",
        "difficulty": 3
    },
    {
        "verb": "speak",
        "particle": "up",
        "meaning": "Talk more loudly or express your opinion with confidence",
        "example": "Could you please speak up? I can't hear you at the back.",
        "difficulty": 2
    },
    {
        "verb": "look",
        "particle": "into",
        "meaning": "Investigate or examine something",
        "example": "The police are looking into the cause of the accident.",
        "difficulty": 2
    },
    {
        "verb": "count",
        "particle": "on",
        "meaning": "Rely or depend on someone or something",
        "example": "You can count on me to help you move this weekend.",
        "difficulty": 2
    },
    {
        "verb": "come",
        "particle": "back",
        "meaning": "Return to a place",
        "example": "She came back from her vacation looking very relaxed.",
        "difficulty": 1
    },
    {
        "verb": "ask",
        "particle": "out",
        "meaning": "Invite someone on a date",
        "example": "He finally asked her out after weeks of hesitation.",
        "difficulty": 1
    },
    {
        "verb": "back",
        "particle": "down",
        "meaning": "Withdraw a claim or assertion in the face of opposition",
        "example": "She refused to back down even when they threatened her.",
        "difficulty": 2
    },
    {
        "verb": "blow",
        "particle": "up",
        "meaning": "Explode",
        "example": "The bomb could blow up at any moment.",
        "difficulty": 2
    },
    {
        "verb": "blow",
        "particle": "up",
        "meaning": "Lose one's temper suddenly",
        "example": "My dad blew up when he saw the dent in his car.",
        "difficulty": 2
    },
    {
        "verb": "break",
        "particle": "in",
        "meaning": "Enter a building forcibly, typically to steal something",
        "example": "Someone tried to break in last night, but the alarm scared them off.",
        "difficulty": 2
    },
    {
        "verb": "break",
        "particle": "out",
        "meaning": "Escape from confinement",
        "example": "Three prisoners broke out of the local jail.",
        "difficulty": 2
    },
    {
        "verb": "bring",
        "particle": "about",
        "meaning": "Cause something to happen",
        "example": "The new manager brought about significant changes in the company.",
        "difficulty": 3
    },
    {
        "verb": "bring",
        "particle": "down",
        "meaning": "Cause someone or something to fall or be removed from power",
        "example": "The scandal helped bring down the corrupt government.",
        "difficulty": 2
    },
    {
        "verb": "call",
        "particle": "for",
        "meaning": "Require or demand something",
        "example": "This recipe calls for three eggs and a cup of flour.",
        "difficulty": 2
    },
    {
        "verb": "call",
        "particle": "on",
        "meaning": "Visit someone for a short time",
        "example": "We should call on your grandmother this weekend.",
        "difficulty": 2
    },
    {
        "verb": "catch",
        "particle": "on",
        "meaning": "Understand something after a period of initial difficulty",
        "example": "He didn't catch on to the joke at first.",
        "difficulty": 2
    },
    {
        "verb": "catch",
        "particle": "up",
        "meaning": "Reach the same level or standard as someone else",
        "example": "If you miss a week of school, it's hard to catch up.",
        "difficulty": 1
    },
    {
        "verb": "check",
        "particle": "out",
        "meaning": "Settle your bill and leave a hotel",
        "example": "We need to check out of the hotel before 11 AM.",
        "difficulty": 1
    },
    {
        "verb": "clean",
        "particle": "up",
        "meaning": "Make a place tidy by removing dirt or rubbish",
        "example": "Could you please clean up your room before guests arrive?",
        "difficulty": 1
    },
    {
        "verb": "come",
        "particle": "about",
        "meaning": "Happen or occur",
        "example": "How did this strange situation come about?",
        "difficulty": 3
    },
    {
        "verb": "come",
        "particle": "down with",
        "meaning": "Start to suffer from an illness",
        "example": "I think I'm coming down with the flu.",
        "difficulty": 2
    },
    {
        "verb": "come",
        "particle": "forward",
        "meaning": "Volunteer oneself for a task or to give evidence",
        "example": "Several witnesses came forward after the appeal for information.",
        "difficulty": 2
    },
    {
        "verb": "cut",
        "particle": "back on",
        "meaning": "Reduce the amount or quantity of something, especially expenditure",
        "example": "We need to cut back on our spending this month.",
        "difficulty": 2
    },
    {
        "verb": "do",
        "particle": "over",
        "meaning": "Do something again from the beginning",
        "example": "The teacher made him do the assignment over because it was messy.",
        "difficulty": 1
    },
    {
        "verb": "drop",
        "particle": "off",
        "meaning": "Take someone or something to a particular place, usually by car",
        "example": "Can you drop me off at the station on your way to work?",
        "difficulty": 1
    },
    {
        "verb": "eat",
        "particle": "out",
        "meaning": "Eat at a restaurant instead of at home",
        "example": "We decided to eat out tonight to celebrate.",
        "difficulty": 1
    },
    {
        "verb": "fall",
        "particle": "apart",
        "meaning": "Break into pieces",
        "example": "My old boots are starting to fall apart.",
        "difficulty": 2
    },
    {
        "verb": "fall",
        "particle": "behind",
        "meaning": "Fail to keep up with work, payments, or progress",
        "example": "He fell behind with his mortgage payments after losing his job.",
        "difficulty": 2
    },
    {
        "verb": "find",
        "particle": "out",
        "meaning": "Discover a fact or piece of information",
        "example": "I need to find out what time the movie starts.",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "ahead",
        "meaning": "Make progress or become successful in one's life or career",
        "example": "She worked hard to get ahead in her field.",
        "difficulty": 2
    },
    {
        "verb": "get",
        "particle": "away",
        "meaning": "Escape from a place or person",
        "example": "The thieves managed to get away before the police arrived.",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "back",
        "meaning": "Return to a place after being away",
        "example": "What time did you get back last night?",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "off",
        "meaning": "Leave a bus, train, aircraft, or boat",
        "example": "Remember to get off at the next stop.",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "on",
        "meaning": "Enter or board a bus, train, aircraft, or boat",
        "example": "Hurry up and get on the train; it's about to leave.",
        "difficulty": 1
    },
    {
        "verb": "get",
        "particle": "through",
        "meaning": "Finish or deal with a difficult task or experience",
        "example": "It was a tough week, but we got through it.",
        "difficulty": 2
    },
    {
        "verb": "give",
        "particle": "back",
        "meaning": "Return something to its owner",
        "example": "Don't forget to give back the book you borrowed.",
        "difficulty": 1
    },
    {
        "verb": "give",
        "particle": "in",
        "meaning": "Cease fighting or arguing; admit defeat",
        "example": "After hours of negotiation, the company finally gave in to the workers' demands.",
        "difficulty": 2
    },
    {
        "verb": "go",
        "particle": "after",
        "meaning": "Pursue someone or something",
        "example": "The police went after the suspect.",
        "difficulty": 2
    },
    {
        "verb": "go",
        "particle": "ahead",
        "meaning": "Proceed or be carried out",
        "example": "'Can I start now?' 'Yes, go ahead.'",
        "difficulty": 1
    },
    {
        "verb": "go",
        "particle": "off",
        "meaning": "Begin to ring or make a noise (alarm, siren)",
        "example": "My alarm clock didn't go off this morning.",
        "difficulty": 1
    },
    {
        "verb": "go",
        "particle": "over",
        "meaning": "Review or examine something carefully",
        "example": "Let's go over the plan one more time before the meeting.",
        "difficulty": 1
    },
    {
        "verb": "grow",
        "particle": "apart",
        "meaning": "Gradually cease to have a close relationship",
        "example": "They were best friends in college but grew apart over the years.",
        "difficulty": 2
    },
    {
        "verb": "hand",
        "particle": "in",
        "meaning": "Submit work (e.g., homework, report) to a person in authority",
        "example": "Please hand in your essays by Friday.",
        "difficulty": 1
    },
    {
        "verb": "hand",
        "particle": "out",
        "meaning": "Distribute something to members of a group",
        "example": "The teacher handed out the worksheets at the beginning of the class.",
        "difficulty": 1
    },
    {
        "verb": "hang",
        "particle": "up",
        "meaning": "End a telephone conversation",
        "example": "Don't hang up! I haven't finished talking.",
        "difficulty": 1
    },
    {
        "verb": "hold",
        "particle": "back",
        "meaning": "Restrain oneself or someone else",
        "example": "She managed to hold back her tears until she was alone.",
        "difficulty": 2
    },
    {
        "verb": "keep",
        "particle": "on",
        "meaning": "Continue doing something",
        "example": "Just keep on trying; you'll succeed eventually.",
        "difficulty": 1
    },
    {
        "verb": "look",
        "particle": "down on",
        "meaning": "Regard someone with a feeling of superiority; despise",
        "example": "She tends to look down on people who are less wealthy than her.",
        "difficulty": 3
    },
    {
        "verb": "look",
        "particle": "for",
        "meaning": "Try to find someone or something",
        "example": "I'm looking for my keys; have you seen them?",
        "difficulty": 1
    },
    {
        "verb": "make",
        "particle": "out",
        "meaning": "Discern or distinguish something with difficulty",
        "example": "I could just make out a figure in the distance through the fog.",
        "difficulty": 3
    },
    {
        "verb": "mix",
        "particle": "up",
        "meaning": "Confuse two or more things or people",
        "example": "I always mix up the twins; they look so alike.",
        "difficulty": 1
    },
    {
        "verb": "pass",
        "particle": "away",
        "meaning": "Die (a polite euphemism)",
        "example": "Her grandfather passed away peacefully last night.",
        "difficulty": 2
    },
    {
        "verb": "pass",
        "particle": "out",
        "meaning": "Become unconscious; faint",
        "example": "He passed out from the heat during the parade.",
        "difficulty": 1
    },
    {
        "verb": "pay",
        "particle": "off",
        "meaning": "Finish paying money that is owed for something",
        "example": "It took them ten years to pay off their mortgage.",
        "difficulty": 2
    },
    {
        "verb": "pick",
        "particle": "out",
        "meaning": "Choose or select something from a group",
        "example": "She picked out a beautiful dress for the party.",
        "difficulty": 1
    },
    {
        "verb": "put",
        "particle": "away",
        "meaning": "Put something in its correct place; tidy",
        "example": "Please put away your toys before dinner.",
        "difficulty": 1
    },
    {
        "verb": "put",
        "particle": "down",
        "meaning": "Insult or criticize someone, making them feel foolish",
        "example": "He's always putting down his colleagues.",
        "difficulty": 2
    },
    {
        "verb": "put",
        "particle": "through",
        "meaning": "Connect someone by telephone",
        "example": "Could you put me through to the sales department, please?",
        "difficulty": 1
    },
    {
        "verb": "run",
        "particle": "away",
        "meaning": "Leave a place or person secretly and suddenly; escape",
        "example": "The teenager ran away from home after an argument.",
        "difficulty": 1
    },
    {
        "verb": "see",
        "particle": "off",
        "meaning": "Accompany someone who is leaving to their point of departure",
        "example": "We went to the airport to see her off.",
        "difficulty": 2
    },
    {
        "verb": "set",
        "particle": "off",
        "meaning": "Start a journey",
        "example": "We set off early in the morning to avoid traffic.",
        "difficulty": 1
    },
    {
        "verb": "settle",
        "particle": "down",
        "meaning": "Adopt a more stable and steady lifestyle, especially by getting married and buying a house",
        "example": "After years of travelling, they decided to settle down and start a family.",
        "difficulty": 2
    },
    {
        "verb": "stand",
        "particle": "by",
        "meaning": "Support or remain loyal to someone, especially in a difficult situation",
        "example": "She stood by her husband throughout the trial.",
        "difficulty": 2
    },
    {
        "verb": "stand",
        "particle": "out",
        "meaning": "Be very noticeable or conspicuous",
        "example": "Her bright red coat made her stand out in the crowd.",
        "difficulty": 2
    },
    {
        "verb": "take",
        "particle": "after",
        "meaning": "Resemble a parent or relative in appearance or character",
        "example": "He takes after his father with his love for music.",
        "difficulty": 2
    },
    {
        "verb": "take",
        "particle": "apart",
        "meaning": "Separate something into its constituent parts; dismantle",
        "example": "He enjoys taking apart old radios and putting them back together.",
        "difficulty": 2
    },
    {
        "verb": "take",
        "particle": "back",
        "meaning": "Withdraw or retract a statement or comment",
        "example": "I take back what I said; I didn't mean to offend you.",
        "difficulty": 2
    },
    {
        "verb": "talk",
        "particle": "over",
        "meaning": "Discuss a problem or plan thoroughly",
        "example": "We need to talk over the details before making a decision.",
        "difficulty": 1
    },
    {
        "verb": "tear",
        "particle": "up",
        "meaning": "Rip something into small pieces",
        "example": "She tore up the letter in anger.",
        "difficulty": 1
    },
    {
        "verb": "think",
        "particle": "over",
        "meaning": "Consider something carefully before making a decision",
        "example": "I need some time to think over your offer.",
        "difficulty": 2
    },
    {
        "verb": "try",
        "particle": "on",
        "meaning": "Put on an item of clothing to see if it fits or suits one",
        "example": "Can I try on these shoes in a size 7?",
        "difficulty": 1
    },
    {
        "verb": "try",
        "particle": "out",
        "meaning": "Test something to see if it is suitable or effective",
        "example": "We're going to try out the new restaurant tonight.",
        "difficulty": 1
    },
    {
        "verb": "turn",
        "particle": "into",
        "meaning": "Change or develop into something different; transform",
        "example": "The caterpillar turned into a beautiful butterfly.",
        "difficulty": 2
    },
    {
        "verb": "turn",
        "particle": "off",
        "meaning": "Stop the operation of a machine or light by pressing a button or switch",
        "example": "Please turn off the TV before you go to bed.",
        "difficulty": 1
    },
    {
        "verb": "use",
        "particle": "up",
        "meaning": "Finish the supply of something",
        "example": "We used up all the milk, so I need to buy more.",
        "difficulty": 1
    },
    {
        "verb": "wake",
        "particle": "up",
        "meaning": "Stop sleeping and become conscious",
        "example": "What time do you usually wake up in the morning?",
        "difficulty": 1
    },
    {
        "verb": "watch",
        "particle": "out",
        "meaning": "Be careful or vigilant",
        "example": "Watch out! There's a car coming.",
        "difficulty": 1
    },
    {
        "verb": "work",
        "particle": "out",
        "meaning": "Solve a problem or find a solution",
        "example": "Don't worry, we'll work something out.",
        "difficulty": 2
    },
    {
        "verb": "write",
        "particle": "down",
        "meaning": "Make a written note of something",
        "example": "Can you write down your phone number for me?",
        "difficulty": 1
    }
]

# Données pour le mode Culture - Variantes régionales
regional_variant_data = regional_variant_data = [
    # --- Original Entries (minus peephole) ---
    {
        "uk_word": "lift",
        "us_word": "elevator",
        "meaning": "A moving platform or cage for carrying people or goods between the floors of a building",
        "difficulty": 1
    },
    {
        "uk_word": "flat",
        "us_word": "apartment",
        "meaning": "A self-contained housing unit in a building",
        "difficulty": 1
    },
    {
        "uk_word": "biscuit",
        "us_word": "cookie",
        "meaning": "A small baked unleavened cake, typically crisp, flat, and sweet (UK); US biscuit is different",
        "difficulty": 1
    },
    {
        "uk_word": "autumn",
        "us_word": "fall",
        "meaning": "The third season of the year, when crops and fruits are gathered and leaves fall",
        "difficulty": 1
    },
    {
        "uk_word": "petrol",
        "us_word": "gas",
        "meaning": "A fuel for internal combustion engines",
        "difficulty": 1
    },
    {
        "uk_word": "pavement",
        "us_word": "sidewalk",
        "meaning": "A raised path for pedestrians at the side of a road",
        "difficulty": 1
    },
    {
        "uk_word": "bonnet",
        "us_word": "hood",
        "meaning": "The hinged cover over the engine of a motor vehicle",
        "difficulty": 1
    },
    {
        "uk_word": "boot",
        "us_word": "trunk",
        "meaning": "A storage compartment at the back of a car",
        "difficulty": 1
    },
    {
        "uk_word": "jumper",
        "us_word": "sweater",
        "meaning": "A knitted garment typically with long sleeves, worn over the upper body",
        "difficulty": 1
    },
    {
        "uk_word": "cinema",
        "us_word": "movie theater",
        "meaning": "A theater where films are shown for public entertainment",
        "difficulty": 1
    },
    {
        "uk_word": "queue",
        "us_word": "line",
        "meaning": "A line of people waiting for something",
        "difficulty": 1
    },
    {
        "uk_word": "mobile phone",
        "us_word": "cell phone",
        "meaning": "A portable telephone that can make and receive calls over a radio frequency",
        "difficulty": 1
    },
    {
        "uk_word": "torch",
        "us_word": "flashlight",
        "meaning": "A portable battery-powered light source",
        "difficulty": 1
    },
    {
        "uk_word": "dustbin",
        "us_word": "trash can",
        "meaning": "A container for household refuse",
        "difficulty": 1
    },
    {
        "uk_word": "holiday",
        "us_word": "vacation",
        "meaning": "An extended period of leisure and recreation, especially one spent away from home",
        "difficulty": 1
    },
    {
        "uk_word": "garden",
        "us_word": "yard",
        "meaning": "An area of ground adjoining a house (often includes lawn in US)",
        "difficulty": 1
    },
    {
        "uk_word": "underground",
        "us_word": "subway",
        "meaning": "An underground railway system",
        "difficulty": 1
    },
    {
        "uk_word": "rubber",
        "us_word": "eraser",
        "meaning": "An object used for rubbing out something written",
        "difficulty": 1
    },
    {
        "uk_word": "crisps",
        "us_word": "chips",
        "meaning": "Thin slices of potato fried until crisp and sold in packets",
        "difficulty": 1
    },
    {
        "uk_word": "chips",
        "us_word": "french fries",
        "meaning": "Long thin strips of deep-fried potato",
        "difficulty": 1
    },
    {
        "uk_word": "trousers",
        "us_word": "pants",
        "meaning": "An outer garment covering the body from the waist to the ankles, with a separate part for each leg",
        "difficulty": 1
    },
    {
        "uk_word": "waistcoat",
        "us_word": "vest",
        "meaning": "A sleeveless upper garment worn over a shirt and under a jacket",
        "difficulty": 2
    },
    {
        "uk_word": "aubergine",
        "us_word": "eggplant",
        "meaning": "A purple egg-shaped vegetable with a glossy skin",
        "difficulty": 2
    },
    {
        "uk_word": "courgette",
        "us_word": "zucchini",
        "meaning": "A small marrow, typically green in color",
        "difficulty": 2
    },
    {
        "uk_word": "plaster",
        "us_word": "band-aid",
        "meaning": "An adhesive bandage used to cover small cuts or abrasions (Band-Aid is a brand name)",
        "difficulty": 2
    },
    {
        "uk_word": "nappy",
        "us_word": "diaper",
        "meaning": "A piece of absorbent material wrapped around a baby's bottom to absorb and contain waste",
        "difficulty": 2
    },
    {
        "uk_word": "chemist",
        "us_word": "drugstore",
        "meaning": "A retail store where medicines and miscellaneous items are sold",
        "difficulty": 2
    },
    {
        "uk_word": "trainers",
        "us_word": "sneakers",
        "meaning": "Sports shoes with rubber soles",
        "difficulty": 1
    },
    {
        "uk_word": "car park",
        "us_word": "parking lot",
        "meaning": "An area or building where cars or other vehicles may be left temporarily",
        "difficulty": 1
    },
    {
        "uk_word": "ground floor",
        "us_word": "first floor",
        "meaning": "The floor of a building at or nearest ground level",
        "difficulty": 2
    },
    {
        "uk_word": "first floor",
        "us_word": "second floor",
        "meaning": "The floor above the ground floor",
        "difficulty": 2
    },
    {
        "uk_word": "solicitor",
        "us_word": "attorney",
        "meaning": "A type of lawyer who traditionally deals with legal matters outside court (though often used more broadly)",
        "difficulty": 2
    },
    {
        "uk_word": "football",
        "us_word": "soccer",
        "meaning": "A game played by two teams of eleven players with a round ball that may not be touched with the hands or arms during play",
        "difficulty": 1
    },
    {
        "uk_word": "sweets",
        "us_word": "candy",
        "meaning": "Sugary food items such as confectionery",
        "difficulty": 1
    },
    {
        "uk_word": "post",
        "us_word": "mail",
        "meaning": "The system for sending letters and parcels; letters and parcels sent",
        "difficulty": 1
    },
    {
        "uk_word": "postbox",
        "us_word": "mailbox",
        "meaning": "A box into which mail is placed to be collected for delivery",
        "difficulty": 1
    },
    {
        "uk_word": "postcode",
        "us_word": "zip code",
        "meaning": "A group of numbers or letters and numbers added to a postal address to assist in the sorting of mail",
        "difficulty": 1
    },
    {
        "uk_word": "motorway",
        "us_word": "highway",
        "meaning": "A major road for fast travel between towns and cities (US: often specifically 'freeway' or 'interstate')",
        "difficulty": 1
    },
    {
        "uk_word": "lorry",
        "us_word": "truck",
        "meaning": "A large, heavy motor vehicle used for transporting goods or materials",
        "difficulty": 1
    },
    {
        "uk_word": "full stop",
        "us_word": "period",
        "meaning": "A punctuation mark (.) used at the end of a sentence",
        "difficulty": 2
    },
    {
        "uk_word": "fortnight",
        "us_word": "two weeks",
        "meaning": "A period of two weeks",
        "difficulty": 2
    },
    {
        "uk_word": "roundabout",
        "us_word": "traffic circle",
        "meaning": "A circular junction at which traffic moves in one direction around a central island",
        "difficulty": 2
    },
    {
        "uk_word": "cooker",
        "us_word": "stove",
        "meaning": "An appliance used for cooking food, typically including an oven and hob/burners",
        "difficulty": 1
    },
    {
        "uk_word": "tap",
        "us_word": "faucet",
        "meaning": "A device by which a flow of water or gas from a pipe or container can be controlled",
        "difficulty": 1
    },
    {
        "uk_word": "dummy",
        "us_word": "pacifier",
        "meaning": "A rubber or plastic teat for a baby to suck on",
        "difficulty": 2
    },
    {
        "uk_word": "pram",
        "us_word": "baby carriage",
        "meaning": "A four-wheeled carriage for a baby, pushed by a person on foot (US stroller is lighter)",
        "difficulty": 2
    },
    {
        "uk_word": "pushchair",
        "us_word": "stroller",
        "meaning": "A light, folding chair on wheels, in which a baby or young child can be pushed along",
        "difficulty": 2
    },
    {
        "uk_word": "fringe",
        "us_word": "bangs",
        "meaning": "Hair cut straight across the forehead",
        "difficulty": 2
    },
    {
        "uk_word": "surname",
        "us_word": "last name",
        "meaning": "A hereditary name common to all members of a family",
        "difficulty": 1
    },
    {
        "uk_word": "drawing pin",
        "us_word": "thumbtack",
        "meaning": "A short pin with a broad, flat head, used for fastening papers to a board",
        "difficulty": 2
    },
    {
        "uk_word": "flyover",
        "us_word": "overpass",
        "meaning": "A bridge that carries a road or railway over another road",
        "difficulty": 2
    },
    {
        "uk_word": "white coffee",
        "us_word": "coffee with cream",
        "meaning": "Coffee with milk or cream added",
        "difficulty": 2
    },
    {
        "uk_word": "sellotape",
        "us_word": "scotch tape",
        "meaning": "A brand of clear adhesive tape (both are brand names used generically)",
        "difficulty": 2
    },
    {
        "uk_word": "cotton wool",
        "us_word": "cotton balls",
        "meaning": "Soft fluffy cotton fiber in absorbent form",
        "difficulty": 2
    },
    {
        "uk_word": "fire brigade",
        "us_word": "fire department",
        "meaning": "An organization that provides firefighters and equipment for dealing with fires",
        "difficulty": 2
    },
    {
        "uk_word": "biro",
        "us_word": "ballpoint pen",
        "meaning": "A pen with a tiny ball as its writing point (Biro is a brand name)",
        "difficulty": 3
    },
    # --- New Entries Start Here (70+ new entries) ---
    {
        "uk_word": "mince",
        "us_word": "ground meat",
        "meaning": "Meat, usually beef, finely chopped by a machine",
        "difficulty": 2
    },
    {
        "uk_word": "spring onion",
        "us_word": "scallion",
        "meaning": "A long thin green onion with a small white bulb",
        "difficulty": 2
    },
    {
        "uk_word": "coriander",
        "us_word": "cilantro",
        "meaning": "The leaves of the coriander plant used as an herb in cooking",
        "difficulty": 2
    },
    {
        "uk_word": "rocket",
        "us_word": "arugula",
        "meaning": "A salad leaf with a peppery, slightly bitter taste",
        "difficulty": 2
    },
    {
        "uk_word": "swede",
        "us_word": "rutabaga",
        "meaning": "A large, round root vegetable with yellow flesh",
        "difficulty": 3
    },
    {
        "uk_word": "ice lolly",
        "us_word": "popsicle",
        "meaning": "Flavored water or fruit juice frozen on a stick (Popsicle is a brand name)",
        "difficulty": 1
    },
    {
        "uk_word": "candy floss",
        "us_word": "cotton candy",
        "meaning": "Spun sugar served on a stick or in a bag",
        "difficulty": 1
    },
    {
        "uk_word": "jam",
        "us_word": "jelly",
        "meaning": "A fruit preserve made from fruit pulp and sugar, set firm enough to spread (US jelly is made from juice)",
        "difficulty": 1
    },
    {
        "uk_word": "jelly",
        "us_word": "jello",
        "meaning": "A fruit-flavored dessert set with gelatin (Jell-O is a brand name)",
        "difficulty": 1
    },
    {
        "uk_word": "treacle",
        "us_word": "molasses",
        "meaning": "Thick, dark syrup produced during sugar refining (especially golden syrup vs light molasses, black treacle vs dark molasses)",
        "difficulty": 2
    },
    {
        "uk_word": "maize",
        "us_word": "corn",
        "meaning": "A tall cereal grass that yields large grains, or kernels, set in rows on a cob",
        "difficulty": 1
    },
    {
        "uk_word": "pudding",
        "us_word": "dessert",
        "meaning": "The sweet course eaten at the end of a meal (general term)",
        "difficulty": 1
    },
    {
        "uk_word": "off-licence",
        "us_word": "liquor store",
        "meaning": "A shop licensed to sell alcoholic drinks for consumption off the premises",
        "difficulty": 2
    },
    {
        "uk_word": "takeaway",
        "us_word": "takeout",
        "meaning": "Cooked food bought from a shop or restaurant to be eaten elsewhere",
        "difficulty": 1
    },
    {
        "uk_word": "braces",
        "us_word": "suspenders",
        "meaning": "Straps worn over the shoulders to hold up trousers",
        "difficulty": 2
    },
    {
        "uk_word": "vest",
        "us_word": "undershirt",
        "meaning": "An undergarment worn on the upper body (sleeveless)",
        "difficulty": 2
    },
    {
        "uk_word": "tights",
        "us_word": "pantyhose",
        "meaning": "Women's thin nylon legwear covering the feet, legs, and lower torso",
        "difficulty": 1
    },
    {
        "uk_word": "dressing gown",
        "us_word": "bathrobe",
        "meaning": "A loose robe worn before dressing or after undressing, often after bathing",
        "difficulty": 1
    },
    {
        "uk_word": "polo neck",
        "us_word": "turtleneck",
        "meaning": "A high, close-fitting turnover collar on a garment, or the garment itself",
        "difficulty": 1
    },
    {
        "uk_word": "wellies",
        "us_word": "rubber boots",
        "meaning": "Waterproof boots, typically made of rubber and reaching the knee (short for Wellington boots)",
        "difficulty": 1
    },
    {
        "uk_word": "pinafore dress",
        "us_word": "jumper",
        "meaning": "A sleeveless dress typically worn over a blouse or sweater (US jumper is this dress, not a sweater)",
        "difficulty": 2
    },
    {
        "uk_word": "dungarees",
        "us_word": "overalls",
        "meaning": "Trousers with a bib held up by straps over the shoulders",
        "difficulty": 1
    },
    {
        "uk_word": "windscreen",
        "us_word": "windshield",
        "meaning": "The front window of a motor vehicle",
        "difficulty": 1
    },
    {
        "uk_word": "tyre",
        "us_word": "tire",
        "meaning": "A rubber covering fitted around a wheel's rim to form a soft contact with the road",
        "difficulty": 1
    },
    {
        "uk_word": "gear lever",
        "us_word": "gear shift",
        "meaning": "A lever used to engage or change gears in a motor vehicle",
        "difficulty": 1
    },
    {
        "uk_word": "indicator",
        "us_word": "turn signal",
        "meaning": "A flashing light on a vehicle to show that it is about to turn left or right (also US 'blinker')",
        "difficulty": 1
    },
    {
        "uk_word": "number plate",
        "us_word": "license plate",
        "meaning": "A sign affixed to the front and rear of a vehicle displaying its official registration number",
        "difficulty": 1
    },
    {
        "uk_word": "handbrake",
        "us_word": "parking brake",
        "meaning": "A brake operated by hand, used to keep a vehicle stationary",
        "difficulty": 1
    },
    {
        "uk_word": "silencer",
        "us_word": "muffler",
        "meaning": "A device fitted to the exhaust pipe of a vehicle to reduce engine noise",
        "difficulty": 2
    },
    {
        "uk_word": "zebra crossing",
        "us_word": "crosswalk",
        "meaning": "A designated place marked with broad white stripes for pedestrians to cross a road",
        "difficulty": 1
    },
    {
        "uk_word": "puncture",
        "us_word": "flat tire",
        "meaning": "A hole in a tire causing it to deflate",
        "difficulty": 1
    },
    {
        "uk_word": "carriage",
        "us_word": "car",
        "meaning": "A separate section of a train for carrying passengers",
        "difficulty": 2
    },
    {
        "uk_word": "articulated lorry",
        "us_word": "tractor-trailer",
        "meaning": "A large lorry consisting of a towing engine (tractor) and a trailer (also US 'semi-truck')",
        "difficulty": 2
    },
    {
        "uk_word": "dual carriageway",
        "us_word": "divided highway",
        "meaning": "A road consisting of two carriageways separated by a central reservation, for traffic in opposite directions",
        "difficulty": 2
    },
    {
        "uk_word": "estate car",
        "us_word": "station wagon",
        "meaning": "A car with a long body incorporating passenger seating and cargo space behind the rear seats",
        "difficulty": 2
    },
    {
        "uk_word": "saloon",
        "us_word": "sedan",
        "meaning": "A car with passenger seating and a separate boot/trunk",
        "difficulty": 2
    },
    {
        "uk_word": "rubbish",
        "us_word": "garbage",
        "meaning": "Waste material; refuse (US also 'trash')",
        "difficulty": 1
    },
    {
        "uk_word": "hoover",
        "us_word": "vacuum",
        "meaning": "A vacuum cleaner, or the action of using one (Hoover is a brand name)",
        "difficulty": 1
    },
    {
        "uk_word": "aerial",
        "us_word": "antenna",
        "meaning": "A rod, wire, or other device used to transmit or receive radio or television signals",
        "difficulty": 2
    },
    {
        "uk_word": "power point",
        "us_word": "outlet",
        "meaning": "A point in a wall where electrical appliances can be connected to the power supply (also UK 'socket')",
        "difficulty": 1
    },
    {
        "uk_word": "cash machine",
        "us_word": "ATM",
        "meaning": "Automated Teller Machine for withdrawing cash from a bank account (also UK 'cashpoint')",
        "difficulty": 1
    },
    {
        "uk_word": "bill",
        "us_word": "check",
        "meaning": "A printed statement of the money owed for goods or services (e.g., in a restaurant)",
        "difficulty": 1
    },
    {
        "uk_word": "skirting board",
        "us_word": "baseboard",
        "meaning": "A narrow wooden board running along the base of an interior wall",
        "difficulty": 2
    },
    {
        "uk_word": "wardrobe",
        "us_word": "closet",
        "meaning": "A tall cupboard or recess in which clothes may be hung or stored",
        "difficulty": 1
    },
    {
        "uk_word": "cupboard",
        "us_word": "cabinet",
        "meaning": "A recess or piece of furniture with shelves, often with doors, used for storage (esp. in kitchen)",
        "difficulty": 1
    },
    {
        "uk_word": "cutlery",
        "us_word": "silverware",
        "meaning": "Knives, forks, and spoons used for eating or serving food (US also 'flatware')",
        "difficulty": 1
    },
    {
        "uk_word": "clothes peg",
        "us_word": "clothespin",
        "meaning": "A clip, typically made of wood or plastic, for fastening clothes to a clothes line",
        "difficulty": 1
    },
    {
        "uk_word": "nought",
        "us_word": "zero",
        "meaning": "The figure 0; nothing",
        "difficulty": 1
    },
    {
        "uk_word": "anorak",
        "us_word": "parka",
        "meaning": "A waterproof jacket, typically with a hood, of a kind originally used in polar regions (US 'windbreaker' is lighter)",
        "difficulty": 2
    },
    {
        "uk_word": "barrister",
        "us_word": "trial lawyer",
        "meaning": "A lawyer entitled to practice as an advocate, particularly in the higher courts (US 'attorney' is general)",
        "difficulty": 3
    },
    {
        "uk_word": "block of flats",
        "us_word": "apartment building",
        "meaning": "A large building containing multiple flats/apartments",
        "difficulty": 1
    },
    {
        "uk_word": "caretaker",
        "us_word": "janitor",
        "meaning": "A person employed to look after a public building, such as a school or office block (US 'superintendent' for apartment buildings)",
        "difficulty": 2
    },
    {
        "uk_word": "current account",
        "us_word": "checking account",
        "meaning": "A bank account from which money may be withdrawn without notice, typically used for daily expenses",
        "difficulty": 2
    },
    {
        "uk_word": "draughts",
        "us_word": "checkers",
        "meaning": "A board game for two players using round, flat pieces on a checkered board",
        "difficulty": 1
    },
    {
        "uk_word": "engaged",
        "us_word": "busy",
        "meaning": "Currently in use (referring to a telephone line)",
        "difficulty": 1
    },
    {
        "uk_word": "film",
        "us_word": "movie",
        "meaning": "A story or event recorded by a camera as a set of moving images and shown in a cinema or on television",
        "difficulty": 1
    },
    {
        "uk_word": "head teacher",
        "us_word": "principal",
        "meaning": "The teacher in charge of a school",
        "difficulty": 1
    },
    {
        "uk_word": "hire",
        "us_word": "rent",
        "meaning": "To pay for the temporary use of something (e.g., a car, equipment)",
        "difficulty": 1
    },
    {
        "uk_word": "public convenience",
        "us_word": "restroom",
        "meaning": "A room or building containing toilets available for public use (also UK 'loo', 'toilet'; US 'bathroom')",
        "difficulty": 1
    },
    {
        "uk_word": "tin",
        "us_word": "can",
        "meaning": "A sealed cylindrical metal container for food or drink",
        "difficulty": 1
    },
    {
        "uk_word": "university",
        "us_word": "college",
        "meaning": "An institution of higher education offering degrees (US 'college' often refers to undergraduate studies or smaller institutions, 'university' for larger ones with graduate programs)",
        "difficulty": 1
    },
    {
        "uk_word": "timetable",
        "us_word": "schedule",
        "meaning": "A plan of events or tasks with intended times of commencement and completion",
        "difficulty": 1
    },
    {
        "uk_word": "staff room",
        "us_word": "teachers' lounge",
        "meaning": "A room in a school provided for teachers to use when not teaching (US 'break room' in offices)",
        "difficulty": 1
    },
    {
        "uk_word": "pupil",
        "us_word": "student",
        "meaning": "A person being taught, especially a child in school",
        "difficulty": 1
    },
    {
        "uk_word": "maths",
        "us_word": "math",
        "meaning": "Mathematics",
        "difficulty": 1
    },
    {
        "uk_word": "CV",
        "us_word": "resume",
        "meaning": "Curriculum Vitae; a summary of one's education, work experience, and qualifications",
        "difficulty": 1
    },
    {
        "uk_word": "bank holiday",
        "us_word": "public holiday",
        "meaning": "A day on which banks are officially closed, observed as a public holiday (US 'federal holiday' if designated by federal government)",
        "difficulty": 2
    },
    {
        "uk_word": "mark",
        "us_word": "grade",
        "meaning": "A figure or letter representing a score awarded to a student's work",
        "difficulty": 1
    },
    {
        "uk_word": "note",
        "us_word": "bill",
        "meaning": "A piece of paper money; banknote",
        "difficulty": 1
    },
    {
        "uk_word": "diversion",
        "us_word": "detour",
        "meaning": "An alternative route for traffic when a road is closed or blocked",
        "difficulty": 1
    },
    {
        "uk_word": "teatowel",
        "us_word": "dishtowel",
        "meaning": "A cloth for drying washed dishes, cutlery, and glasses",
        "difficulty": 1
    },
    {
        "uk_word": "letterbox",
        "us_word": "mail slot",
        "meaning": "A slot, typically in a door, through which mail is delivered",
        "difficulty": 2
    },
    {
        "uk_word": "shop",
        "us_word": "store",
        "meaning": "A place where things are sold retail",
        "difficulty": 1
    },
    {
        "uk_word": "high street",
        "us_word": "main street",
        "meaning": "The principal street of a town, typically the main shopping area",
        "difficulty": 1
    },
    {
        "uk_word": "phone box",
        "us_word": "phone booth",
        "meaning": "A public cubicle containing a telephone (also UK 'call box')",
        "difficulty": 1
    },
    {
        "uk_word": "taxi",
        "us_word": "cab",
        "meaning": "A car licensed to transport passengers in return for payment of a fare",
        "difficulty": 1
    },
    {
        "uk_word": "to let",
        "us_word": "for rent",
        "meaning": "Available for rent (sign displayed on property)",
        "difficulty": 1
    },
    {
        "uk_word": "terraced house",
        "us_word": "row house",
        "meaning": "A house built as part of a continuous row in a uniform style, sharing side walls with neighbors",
        "difficulty": 2
    }
]

# Données pour le mode Culture - Plats et nationalités
food_origin_data = [
    # Plats du Royaume-Uni (Original + Added)
    {
        "dish_name": "Sunday Roast",
        "origin_country": "United Kingdom",
        "description": "A traditional British meal consisting of roasted meat, roast potatoes, vegetables, Yorkshire pudding and gravy",
        "difficulty": 1
    },
    {
        "dish_name": "Bangers and Mash",
        "origin_country": "United Kingdom",
        "description": "A dish of sausages and mashed potatoes, usually served with onion gravy",
        "difficulty": 1
    },
    {
        "dish_name": "Shepherd's Pie",
        "origin_country": "United Kingdom",
        "description": "A meat pie with a crust of mashed potato and filled with minced lamb and vegetables",
        "difficulty": 1
    },
    {
        "dish_name": "Cottage Pie",
        "origin_country": "United Kingdom",
        "description": "Similar to Shepherd's Pie but made with minced beef instead of lamb",
        "difficulty": 2
    },
    {
        "dish_name": "Toad in the Hole",
        "origin_country": "United Kingdom",
        "description": "Sausages in Yorkshire pudding batter, typically served with onion gravy and vegetables",
        "difficulty": 2
    },
    {
        "dish_name": "Full English Breakfast",
        "origin_country": "United Kingdom",
        "description": "A breakfast meal including bacon, sausages, eggs, baked beans, toast, mushrooms, and tomatoes",
        "difficulty": 1
    },
    {
        "dish_name": "Bubble and Squeak",
        "origin_country": "United Kingdom",
        "description": "A dish made from leftover vegetables, primarily potato and cabbage, fried together until browned",
        "difficulty": 3
    },
    {
        "dish_name": "Cornish Pasty",
        "origin_country": "United Kingdom",
        "description": "A baked pastry filled with meat and vegetables, traditionally associated with Cornwall",
        "difficulty": 2
    },
    {
        "dish_name": "Spotted Dick",
        "origin_country": "United Kingdom",
        "description": "A traditional British pudding made with suet and dried fruit, usually served with custard",
        "difficulty": 3
    },
    {
        "dish_name": "Lancashire Hotpot",
        "origin_country": "United Kingdom",
        "description": "A casserole dish consisting of lamb or mutton and onion, topped with sliced potatoes",
        "difficulty": 3
    },
    {
        "dish_name": "Fish and Chips",
        "origin_country": "United Kingdom",
        "description": "Battered and deep-fried fish (commonly cod or haddock) served with thick-cut potato chips",
        "difficulty": 1
    },
    {
        "dish_name": "Haggis",
        "origin_country": "United Kingdom", # Specifically Scotland
        "description": "A savoury pudding containing sheep's pluck (heart, liver, and lungs), minced with onion, oatmeal, suet, spices, and salt, encased in the animal's stomach (or artificial casing)",
        "difficulty": 3
    },
    {
        "dish_name": "Cullen Skink",
        "origin_country": "United Kingdom", # Specifically Scotland
        "description": "A thick Scottish soup made of smoked haddock, potatoes, and onions",
        "difficulty": 2
    },
    {
        "dish_name": "Welsh Rarebit",
        "origin_country": "United Kingdom", # Specifically Wales
        "description": "A dish of melted cheese sauce served over slices of toasted bread",
        "difficulty": 1
    },
    {
        "dish_name": "Eton Mess",
        "origin_country": "United Kingdom",
        "description": "A dessert made from a mixture of broken meringue, strawberries (or other berries), and cream",
        "difficulty": 1
    },
    {
        "dish_name": "Trifle",
        "origin_country": "United Kingdom",
        "description": "A dessert made with sponge cake soaked in sherry or fruit juice, layered with custard, fruit, and whipped cream",
        "difficulty": 2
    },
    {
        "dish_name": "Scones with Clotted Cream and Jam",
        "origin_country": "United Kingdom",
        "description": "Lightly sweetened baked goods, often served with clotted cream and jam as part of a cream tea",
        "difficulty": 2
    },
    {
        "dish_name": "Victoria Sponge",
        "origin_country": "United Kingdom",
        "description": "A classic British cake made of two sponge cakes sandwiched together with jam and cream",
        "difficulty": 2
    },
    {
        "dish_name": "Sticky Toffee Pudding",
        "origin_country": "United Kingdom",
        "description": "A moist sponge cake made with finely chopped dates, covered in a toffee sauce and often served with vanilla custard or ice cream",
        "difficulty": 2
    },
    {
        "dish_name": "Mince Pies",
        "origin_country": "United Kingdom",
        "description": "Small sweet pies filled with mincemeat (a mixture of dried fruits, spices, and suet), traditionally eaten during Christmas",
        "difficulty": 2
    },
    {
        "dish_name": "Ploughman's Lunch",
        "origin_country": "United Kingdom",
        "description": "A cold meal consisting of bread, cheese, and pickles, often accompanied by butter, ham, salad, and fruit",
        "difficulty": 1
    },
    {
        "dish_name": "Black Pudding",
        "origin_country": "United Kingdom",
        "description": "A type of blood sausage, generally made from pork blood, with pork fat or beef suet, and a cereal, usually oatmeal, oat groats or barley groats",
        "difficulty": 1 # Usually bought pre-made
    },
    {
        "dish_name": "Cawl",
        "origin_country": "United Kingdom", # Specifically Wales
        "description": "A traditional Welsh soup or stew, often made with lamb or beef, potatoes, swedes, carrots and other vegetables",
        "difficulty": 2
    },
    {
        "dish_name": "Bara Brith",
        "origin_country": "United Kingdom", # Specifically Wales
        "description": "A traditional Welsh fruit loaf made with tea, dried fruits and spices",
        "difficulty": 2
    },
    {
        "dish_name": "Crumpets",
        "origin_country": "United Kingdom",
        "description": "A small, porous griddle cake typically eaten toasted and buttered",
        "difficulty": 2 # Making from scratch
    },

    # Plats des États-Unis (Original + Added)
    {
        "dish_name": "Hamburger",
        "origin_country": "United States",
        "description": "A sandwich consisting of a cooked patty of ground meat placed inside a sliced bread roll",
        "difficulty": 1
    },
    {
        "dish_name": "Buffalo Wings",
        "origin_country": "United States",
        "description": "Chicken wings coated in a spicy sauce, originated in Buffalo, New York",
        "difficulty": 1
    },
    {
        "dish_name": "Macaroni and Cheese",
        "origin_country": "United States",
        "description": "A dish of cooked macaroni pasta and a cheese sauce, commonly cheddar",
        "difficulty": 1
    },
    {
        "dish_name": "Clam Chowder",
        "origin_country": "United States",
        "description": "A thick soup containing clams and broth with diced potatoes, onions, and celery (New England style is creamy)",
        "difficulty": 2
    },
    {
        "dish_name": "Jambalaya",
        "origin_country": "United States",
        "description": "A Creole rice dish with meat (like sausage and chicken) and vegetables, originated in Louisiana",
        "difficulty": 2
    },
    {
        "dish_name": "Pulled Pork",
        "origin_country": "United States",
        "description": "A barbecue dish of shredded slow-cooked pork shoulder, popular in the Southern United States",
        "difficulty": 2
    },
    {
        "dish_name": "Pecan Pie",
        "origin_country": "United States",
        "description": "A pie with a filling of pecan nuts mixed with a custard made from corn syrup and eggs",
        "difficulty": 2
    },
    {
        "dish_name": "Pumpkin Pie",
        "origin_country": "United States",
        "description": "A traditional dessert served during Thanksgiving, made from pumpkin-based custard, baked in a pie crust",
        "difficulty": 1
    },
    {
        "dish_name": "Cornbread",
        "origin_country": "United States",
        "description": "A quick bread made with cornmeal, associated with Southern United States cuisine",
        "difficulty": 2
    },
    {
        "dish_name": "Key Lime Pie",
        "origin_country": "United States",
        "description": "A dessert pie made with key lime juice, egg yolks, and sweetened condensed milk in a pie crust, associated with Florida Keys",
        "difficulty": 2
    },
    {
        "dish_name": "Apple Pie",
        "origin_country": "United States", # Strongly associated, though origins older
        "description": "A fruit pie in which the principal filling ingredient is apples, often served with ice cream ('à la mode')",
        "difficulty": 2
    },
    {
        "dish_name": "Cheesecake (New York Style)",
        "origin_country": "United States",
        "description": "A dense, smooth cheesecake made with cream cheese, eggs, sugar, and often a graham cracker crust",
        "difficulty": 2
    },
    {
        "dish_name": "Brownies",
        "origin_country": "United States",
        "description": "A square or rectangular chocolate baked confection, ranging from fudgy to cakey in texture",
        "difficulty": 1
    },
    {
        "dish_name": "Chocolate Chip Cookies",
        "origin_country": "United States",
        "description": "Drop cookies featuring chocolate chips as the distinguishing ingredient",
        "difficulty": 1
    },
    {
        "dish_name": "S'mores",
        "origin_country": "United States",
        "description": "A campfire treat consisting of a toasted marshmallow and a layer of chocolate sandwiched between two pieces of graham cracker",
        "difficulty": 1
    },
    {
        "dish_name": "Meatloaf",
        "origin_country": "United States",
        "description": "A dish of ground meat mixed with other ingredients, formed into a loaf shape, then baked or smoked",
        "difficulty": 1
    },
    {
        "dish_name": "Coleslaw",
        "origin_country": "United States", # Popularized version
        "description": "A salad consisting primarily of finely shredded raw cabbage with a salad dressing, commonly mayonnaise-based",
        "difficulty": 1
    },
    {
        "dish_name": "Potato Salad",
        "origin_country": "United States", # Popularized versions
        "description": "A dish made from boiled potatoes, typically dressed with mayonnaise, mustard, herbs and other ingredients",
        "difficulty": 1
    },
    {
        "dish_name": "Reuben Sandwich",
        "origin_country": "United States",
        "description": "A hot sandwich composed of corned beef, Swiss cheese, sauerkraut, and Russian dressing, grilled between slices of rye bread",
        "difficulty": 1
    },
    {
        "dish_name": "Philly Cheesesteak",
        "origin_country": "United States",
        "description": "A sandwich made from thinly sliced pieces of beefsteak and melted cheese in a long hoagie roll, originating from Philadelphia",
        "difficulty": 1
    },
    {
        "dish_name": "Grits",
        "origin_country": "United States",
        "description": "A porridge made from boiled cornmeal, associated with Southern US cuisine, often served savory with butter, cheese, or shrimp",
        "difficulty": 1
    },
    {
        "dish_name": "Biscuits and Gravy",
        "origin_country": "United States",
        "description": "A popular breakfast dish in the Southern US, consisting of soft dough biscuits covered in a thick white gravy made from sausage drippings, flour, milk",
        "difficulty": 2
    },
    {
        "dish_name": "Fried Chicken (Southern Style)",
        "origin_country": "United States",
        "description": "Chicken pieces coated with seasoned flour or batter and pan-fried, deep-fried, or pressure-fried",
        "difficulty": 2
    },
    {
        "dish_name": "Lobster Roll",
        "origin_country": "United States",
        "description": "A sandwich native to New England, filled with lobster meat soaked in butter or tossed with mayonnaise, served in a hot dog-style bun",
        "difficulty": 2
    },
    {
        "dish_name": "Chili con Carne",
        "origin_country": "United States", # Strongly associated with Texas
        "description": "A spicy stew containing chili peppers, meat (usually beef), tomatoes and often kidney beans",
        "difficulty": 2
    },
    {
        "dish_name": "Chicago Deep Dish Pizza",
        "origin_country": "United States",
        "description": "Pizza baked in a deep pan, characterized by a thick crust with raised edges, topped with cheese, fillings, and tomato sauce",
        "difficulty": 3
    },
    {
        "dish_name": "Tater Tot Casserole",
        "origin_country": "United States",
        "description": "A casserole made with ground beef, condensed soup (cream of mushroom), vegetables, and topped with tater tots, popular in the Midwest",
        "difficulty": 1
    },

    # Plats du Canada (Original + Added)
    {
        "dish_name": "Butter Tarts",
        "origin_country": "Canada",
        "description": "A pastry tart filled with a semi-solid filling of butter, sugar, syrup, and egg",
        "difficulty": 2
    },
    {
        "dish_name": "Nanaimo Bars",
        "origin_country": "Canada",
        "description": "A no-bake dessert with three layers: wafer crumb base, custard icing middle, and chocolate ganache top",
        "difficulty": 2
    },
    {
        "dish_name": "Tourtière",
        "origin_country": "Canada",
        "description": "A traditional Québécois meat pie typically made with finely diced pork, veal, or beef, and spices",
        "difficulty": 3
    },
    {
        "dish_name": "Bannock",
        "origin_country": "Canada", # Indigenous / Scottish roots, adapted
        "description": "A type of flat bread developed by Indigenous peoples in Canada, often baked or fried",
        "difficulty": 3
    },
    {
        "dish_name": "Montreal Smoked Meat",
        "origin_country": "Canada",
        "description": "A type of kosher-style deli meat product made by salting and curing beef brisket with spices, typically served in a rye bread sandwich",
        "difficulty": 2 # Preparation is hard, eating is easy!
    },
    {
        "dish_name": "Poutine",
        "origin_country": "Canada",
        "description": "A dish originating from Quebec, consisting of french fries and cheese curds topped with a light brown gravy",
        "difficulty": 1
    },
    {
        "dish_name": "Split Pea Soup (Habitant style)",
        "origin_country": "Canada",
        "description": "A thick soup made from dried split peas, often flavoured with ham or bacon, a staple in Quebecois cuisine",
        "difficulty": 2
    },
    {
        "dish_name": "Saskatoon Berry Pie",
        "origin_country": "Canada",
        "description": "A pie made with Saskatoon berries, native to the Canadian Prairies, similar in appearance to blueberries but with an almond-like flavour",
        "difficulty": 2
    },
    {
        "dish_name": "BeaverTails",
        "origin_country": "Canada",
        "description": "A fried dough pastry, stretched to resemble a beaver's tail, often topped with sweet condiments like sugar, cinnamon, chocolate, or fruit",
        "difficulty": 2
    },
    {
        "dish_name": "Ketchup Chips",
        "origin_country": "Canada",
        "description": "Potato chips flavoured with a sweet and tangy ketchup seasoning, uniquely popular in Canada",
        "difficulty": 1 # To eat
    },
    {
        "dish_name": "Peameal Bacon",
        "origin_country": "Canada",
        "description": "Wet-cured, unsmoked back bacon made from trimmed lean boneless pork loin rolled in cornmeal (originally peameal)",
        "difficulty": 1 # To cook
    },
    {
        "dish_name": "Caesar Cocktail",
        "origin_country": "Canada",
        "description": "A cocktail created in Calgary, made with vodka, Clamato juice, hot sauce, and Worcestershire sauce, served in a salt-rimmed glass",
        "difficulty": 1
    },

    # Plats d'Australie (Original + Added)
    {
        "dish_name": "Vegemite on Toast",
        "origin_country": "Australia",
        "description": "Toast spread with Vegemite, a dark brown savoury paste made from leftover brewers' yeast extract",
        "difficulty": 1
    },
    {
        "dish_name": "Tim Tam",
        "origin_country": "Australia",
        "description": "A brand of chocolate biscuit consisting of two malted biscuits separated by a light chocolate filling and coated in chocolate",
        "difficulty": 1 # To eat
    },
    {
        "dish_name": "Lamington",
        "origin_country": "Australia",
        "description": "A square of sponge cake coated in chocolate sauce and rolled in desiccated coconut",
        "difficulty": 2
    },
    {
        "dish_name": "Barramundi",
        "origin_country": "Australia",
        "description": "A species of catadromous fish, often farmed and served grilled or pan-fried as a fillet with crispy skin",
        "difficulty": 2 # To cook
    },
    {
        "dish_name": "Damper",
        "origin_country": "Australia",
        "description": "A traditional Australian soda bread, historically baked in the coals of a campfire by stockmen",
        "difficulty": 3 # Traditionally
    },
    {
        "dish_name": "Pavlova",
        "origin_country": "Australia", # Origin debated with New Zealand
        "description": "A meringue-based dessert with a crisp crust and soft, light inside, usually topped with fruit and whipped cream",
        "difficulty": 3
    },
    {
        "dish_name": "Anzac Biscuits",
        "origin_country": "Australia", # Origin shared/debated with New Zealand
        "description": "Sweet biscuits made using rolled oats, flour, desiccated coconut, sugar, butter, golden syrup, baking soda and boiling water",
        "difficulty": 2
    },
    {
        "dish_name": "Fairy Bread",
        "origin_country": "Australia",
        "description": "Slices of white bread buttered and covered in sprinkles ('hundreds and thousands'), typically served at children's parties",
        "difficulty": 1
    },
    {
        "dish_name": "Sausage Sizzle",
        "origin_country": "Australia",
        "description": "Grilled sausages served on a slice of white bread, often with grilled onions and condiments, a common community fundraising event food",
        "difficulty": 1
    },
    {
        "dish_name": "Moreton Bay Bugs",
        "origin_country": "Australia",
        "description": "A species of slipper lobster found in Australian waters, often grilled or barbecued and served with garlic butter or lemon",
        "difficulty": 2 # To cook
    },
    {
        "dish_name": "Kangaroo Steak",
        "origin_country": "Australia",
        "description": "Lean meat from kangaroo, typically served grilled or pan-fried as steaks or used in stews",
        "difficulty": 2
    },
    {
        "dish_name": "Chicken Parmigiana ('Parma' or ' parmi')",
        "origin_country": "Australia", # Popularized version
        "description": "Breaded chicken schnitzel topped with tomato sauce and melted cheese, a staple pub food",
        "difficulty": 2
    },

    # Plats de Nouvelle-Zélande (Original + Added)
    {
        "dish_name": "Hangi",
        "origin_country": "New Zealand",
        "description": "A traditional Māori method of cooking food (meat and vegetables) using heated rocks buried in a pit oven",
        "difficulty": 3 # Requires special setup
    },
    {
        "dish_name": "Hokey Pokey Ice Cream",
        "origin_country": "New Zealand",
        "description": "Vanilla ice cream containing small, solid lumps of honeycomb toffee ('hokey pokey')",
        "difficulty": 1 # To eat/buy
    },
    {
        "dish_name": "Afghan Biscuit",
        "origin_country": "New Zealand",
        "description": "A traditional chocolate biscuit made with flour, butter, cornflakes, sugar and cocoa powder, topped with chocolate icing and a walnut half",
        "difficulty": 2
    },
    {
        "dish_name": "Bacon and Egg Pie",
        "origin_country": "New Zealand",
        "description": "A savory pie consisting of a pastry shell filled with bacon, eggs (often whole), and sometimes onion, peas, or cheese",
        "difficulty": 2
    },
    {
        "dish_name": "Pavlova",
        "origin_country": "New Zealand", # Origin debated with Australia
        "description": "A meringue-based dessert with a crisp crust and soft, light inside, usually topped with fruit (like kiwi) and whipped cream",
        "difficulty": 3
    },
    {
        "dish_name": "Anzac Biscuits",
        "origin_country": "New Zealand", # Origin shared/debated with Australia
        "description": "Sweet biscuits made using rolled oats, flour, desiccated coconut, sugar, butter, golden syrup, baking soda and boiling water",
        "difficulty": 2
    },
    {
        "dish_name": "Lolly Cake",
        "origin_country": "New Zealand",
        "description": "An unbaked cake or slice made with malt biscuits, butter, condensed milk, and Eskimo Lollies (or similar fruit puffs)",
        "difficulty": 1
    },
    {
        "dish_name": "Green-lipped Mussels",
        "origin_country": "New Zealand",
        "description": "A species of mussel native to New Zealand, often steamed and served with garlic, white wine, or tomato-based sauces",
        "difficulty": 2 # To cook
    },
    {
        "dish_name": "Whitebait Fritters",
        "origin_country": "New Zealand",
        "description": "Delicate fritters made by combining tiny, translucent juvenile fish (whitebait) with egg batter and frying",
        "difficulty": 2
    },
    {
        "dish_name": "Mince and Cheese Pie",
        "origin_country": "New Zealand",
        "description": "A savory pie filled with minced beef (often in gravy) and cheese, encased in pastry, an iconic Kiwi bakery item",
        "difficulty": 1 # To buy/eat
    },
    {
        "dish_name": "Cheese Rolls",
        "origin_country": "New Zealand", # Southland specialty
        "description": "Slices of white bread spread with a mixture based on cheese (often processed), rolled up, and toasted or grilled",
        "difficulty": 1
    },

    # Plats d'Irlande (Original + Added)
    {
        "dish_name": "Boxty",
        "origin_country": "Ireland",
        "description": "A traditional Irish potato pancake made with a mixture of finely grated raw potato and mashed potato, often fried",
        "difficulty": 3
    },
    {
        "dish_name": "Colcannon",
        "origin_country": "Ireland",
        "description": "A traditional dish of mashed potatoes mixed with kale or cabbage and butter or cream",
        "difficulty": 2
    },
    {
        "dish_name": "Coddle",
        "origin_country": "Ireland",
        "description": "A Dublin specialty, traditionally made from leftovers, typically a slow-cooked stew of pork sausages, bacon, potatoes, and onions",
        "difficulty": 3
    },
    {
        "dish_name": "Soda Bread",
        "origin_country": "Ireland",
        "description": "A type of quick bread in which baking soda (sodium bicarbonate) is used as a leavening agent instead of traditional yeast",
        "difficulty": 2
    },
    {
        "dish_name": "Irish Stew",
        "origin_country": "Ireland",
        "description": "A traditional stew typically made from lamb or mutton, potatoes, onions, and parsley. Carrots sometimes added.",
        "difficulty": 2
    },
    {
        "dish_name": "Full Irish Breakfast",
        "origin_country": "Ireland",
        "description": "Similar to a Full English, but often includes black and white pudding, soda bread, and potato farls alongside bacon, sausages, eggs, and tomatoes",
        "difficulty": 1
    },
    {
        "dish_name": "Barmbrack",
        "origin_country": "Ireland",
        "description": "A yeasted bread with added sultanas and raisins, often eaten toasted with butter, traditionally associated with Halloween",
        "difficulty": 2
    },
    {
        "dish_name": "Champ",
        "origin_country": "Ireland",
        "description": "An Irish dish of mashed potatoes mixed with chopped scallions (spring onions), butter, and milk",
        "difficulty": 1
    },
    {
        "dish_name": "Drisheen",
        "origin_country": "Ireland",
        "description": "A type of black pudding made from cow's, pig's or sheep's blood, milk, salt, fat and breadcrumbs or oatmeal",
        "difficulty": 2 # Finding/preparing
    },
    {
        "dish_name": "Guinness Stew",
        "origin_country": "Ireland",
        "description": "A hearty beef stew braised in Guinness beer along with root vegetables like carrots, celery, and onions",
        "difficulty": 2
    },

    # Plats de la Jamaïque (Original + Added)
    {
        "dish_name": "Ackee and Saltfish",
        "origin_country": "Jamaica",
        "description": "Jamaica's national dish made from salted codfish sautéed with boiled ackee fruit, onions, Scotch Bonnet peppers, tomatoes, and spices",
        "difficulty": 3
    },
    {
        "dish_name": "Patty",
        "origin_country": "Jamaica",
        "description": "A pastry that contains various fillings (beef, chicken, vegetable, cheese) and spices baked inside a flaky, often yellow-tinted shell",
        "difficulty": 2 # Making from scratch
    },
    {
        "dish_name": "Rice and Peas",
        "origin_country": "Jamaica",
        "description": "A staple side dish where rice is cooked with kidney beans (or gungo peas), coconut milk, scallions, thyme, and spices",
        "difficulty": 2
    },
    {
        "dish_name": "Callaloo",
        "origin_country": "Jamaica",
        "description": "A popular Caribbean dish made with leafy vegetables (callaloo, similar to spinach), steamed with onions, garlic, tomatoes, thyme, and Scotch Bonnet pepper",
        "difficulty": 2
    },
    {
        "dish_name": "Jerk Chicken/Pork",
        "origin_country": "Jamaica",
        "description": "Meat dry-rubbed or wet marinated with a hot spice mixture called Jamaican jerk spice, then traditionally smoked or grilled",
        "difficulty": 2 # Marinating and cooking
    },
    {
        "dish_name": "Festival",
        "origin_country": "Jamaica",
        "description": "Sweet fried dumplings made with cornmeal, flour, sugar, and spices, often served with jerk meats or fish",
        "difficulty": 2
    },
    {
        "dish_name": "Bammy",
        "origin_country": "Jamaica",
        "description": "A traditional flatbread made from cassava (yucca), often soaked in coconut milk and fried, served with fish or other dishes",
        "difficulty": 3 # Making from scratch
    },
    {
        "dish_name": "Mannish Water",
        "origin_country": "Jamaica",
        "description": "A goat soup traditionally made from various parts of a male goat (including head and testicles), vegetables, and ground provisions (yams, potatoes)",
        "difficulty": 3
    },
    {
        "dish_name": "Escovitch Fish",
        "origin_country": "Jamaica",
        "description": "Fried fish topped with a spicy pickled vegetable medley (onions, carrots, Scotch Bonnet peppers, pimento)",
        "difficulty": 2
    },
    {
        "dish_name": "Curry Goat",
        "origin_country": "Jamaica",
        "description": "Goat meat slow-cooked in a rich curry sauce with spices like turmeric, cumin, coriander, and Scotch Bonnet peppers",
        "difficulty": 3
    },

    # Plats de Trinidad et Tobago (Original + Added)
    {
        "dish_name": "Doubles",
        "origin_country": "Trinidad and Tobago",
        "description": "A popular street food consisting of two flat fried breads (bara) filled with curried chickpeas (channa) and topped with various chutneys and pepper sauce",
        "difficulty": 2 # Assembling
    },
    {
        "dish_name": "Crab and Callaloo",
        "origin_country": "Trinidad and Tobago",
        "description": "A thick, creamy soup made from dasheen leaves (callaloo), okra, crab meat, coconut milk, and seasonings",
        "difficulty": 3
    },
    {
        "dish_name": "Pholourie",
        "origin_country": "Trinidad and Tobago",
        "description": "Small, deep-fried balls made from a spiced split pea batter, typically served with mango or tamarind chutney",
        "difficulty": 2
    },
    {
        "dish_name": "Bake and Shark",
        "origin_country": "Trinidad and Tobago",
        "description": "A popular street food sandwich, especially from Maracas Bay, featuring fried flatbread ('bake') filled with fried shark meat and various toppings and sauces",
        "difficulty": 2
    },
    {
        "dish_name": "Pelau",
        "origin_country": "Trinidad and Tobago",
        "description": "A one-pot rice dish where meat (usually chicken or beef) is caramelized in sugar, then cooked with rice, pigeon peas, coconut milk, and vegetables",
        "difficulty": 2
    },
    {
        "dish_name": "Aloo Pie",
        "origin_country": "Trinidad and Tobago",
        "description": "A fried pastry similar to a samosa, filled with spiced mashed potatoes (aloo), often served with chutneys",
        "difficulty": 2
    },
    {
        "dish_name": "Roti (Buss Up Shut)",
        "origin_country": "Trinidad and Tobago",
        "description": "'Busted up shirt' roti is a soft, flaky flatbread torn into pieces, typically served with curried chicken, goat, channa, or vegetables",
        "difficulty": 3 # Making roti from scratch
    },

    # Plats de l'Afrique du Sud (Anglophone Context - Original + Added)
    {
        "dish_name": "Bobotie",
        "origin_country": "South Africa",
        "description": "A dish of spiced minced meat (often lamb or beef) baked with an egg-based custard topping, sometimes containing fruit like raisins or apricots",
        "difficulty": 3
    },
    {
        "dish_name": "Bunny Chow",
        "origin_country": "South Africa",
        "description": "A Durban street food consisting of a hollowed-out loaf of white bread filled with curry (chicken, mutton, bean)",
        "difficulty": 2 # Assembly
    },
    {
        "dish_name": "Boerewors",
        "origin_country": "South Africa",
        "description": "A traditional thick sausage, typically containing beef mixed with pork or lamb and spices (like coriander seed), often coiled and cooked on a 'braai' (BBQ)",
        "difficulty": 1 # To cook
    },
    {
        "dish_name": "Biltong",
        "origin_country": "South Africa",
        "description": "A form of dried, cured meat (usually beef) seasoned with vinegar, salt, sugar, coriander, and pepper",
        "difficulty": 3 # To make correctly
    },
    {
        "dish_name": "Malva Pudding",
        "origin_country": "South Africa",
        "description": "A sweet, spongy apricot pudding of Cape Dutch origin, served hot with a creamy sauce poured over it while warm",
        "difficulty": 2
    },
    {
        "dish_name": "Sosaties",
        "origin_country": "South Africa",
        "description": "Meat (often lamb or chicken) kebabs marinated in a Cape Malay curry-style sauce, typically cooked on a 'braai'",
        "difficulty": 2
    },
    {
        "dish_name": "Koeksisters",
        "origin_country": "South Africa",
        "description": "A traditional Afrikaner confectionery made of fried, plaited dough infused with syrup or honey. There's also a Cape Malay version which is spicier and coated in coconut.",
        "difficulty": 3
    },
    {
        "dish_name": "Potjiekos",
        "origin_country": "South Africa",
        "description": "Literally 'small pot food', a stew prepared outdoors in a traditional round, cast iron, three-legged pot (the potjie), slow-cooked over coals",
        "difficulty": 3 # Requires specific equipment/method
    },
    {
        "dish_name": "Chakalaka",
        "origin_country": "South Africa",
        "description": "A spicy vegetable relish typically made with onions, tomatoes, peppers, carrots, beans, and spices, often served with pap (maize porridge) or bread",
        "difficulty": 2
    },

    # Plats de Singapour (Anglophone Context - Original + Added)
    {
        "dish_name": "Hainanese Chicken Rice",
        "origin_country": "Singapore", # Adapted / Popularized
        "description": "Poached chicken served with oily rice cooked in chicken broth and garlic, accompanied by chili sauce and cucumber garnishes",
        "difficulty": 3
    },
    {
        "dish_name": "Kaya Toast",
        "origin_country": "Singapore", # Shared with Malaysia
        "description": "A popular breakfast item consisting of toast spread with kaya (a coconut and egg jam) and butter, often served with soft-boiled eggs and coffee",
        "difficulty": 1
    },
    {
        "dish_name": "Chilli Crab",
        "origin_country": "Singapore",
        "description": "Mud crabs stir-fried in a semi-thick, sweet and savoury tomato-and-chilli-based sauce, often served with fried buns (mantou)",
        "difficulty": 3
    },
    {
        "dish_name": "Laksa (Singapore/Katong Laksa)",
        "origin_country": "Singapore",
        "description": "A spicy noodle soup with a rich coconut milk-based broth, typically containing rice vermicelli, shrimp, cockles, fish cake, and bean sprouts",
        "difficulty": 3
    },
    {
        "dish_name": "Satay",
        "origin_country": "Singapore", # Regional dish, popular version here
        "description": "Seasoned, skewered and grilled meat (chicken, beef, mutton), served with a peanut sauce, cucumber, onions, and rice cakes (ketupat)",
        "difficulty": 2 # Preparation/Grilling
    },
    {
        "dish_name": "Bak Kut Teh",
        "origin_country": "Singapore", # Shared with Malaysia, distinct versions
        "description": "'Meat bone tea', a pork rib soup complexly brewed with herbs and spices (peppery Teochew style common in SG), served with rice",
        "difficulty": 3
    },
    {
        "dish_name": "Roti Prata",
        "origin_country": "Singapore", # South Indian origin, popular adaptation
        "description": "A South-Indian influenced flatbread, typically flipped and stretched thin, cooked on a griddle, served plain or with egg/onion, often with curry sauce",
        "difficulty": 2 # Flipping technique
    },
    {
        "dish_name": "Char Kway Teow",
        "origin_country": "Singapore", # Shared with Malaysia
        "description": "Stir-fried flat rice noodles with dark soy sauce, shrimp, cockles, Chinese sausage, bean sprouts, chives, and egg",
        "difficulty": 2
    },
    {
        "dish_name": "Hokkien Mee (Singapore style)",
        "origin_country": "Singapore",
        "description": "Stir-fried dish of egg noodles and rice noodles in a rich prawn and pork broth, with prawns, squid, pork belly slices, and egg",
        "difficulty": 3
    },
     {
        "dish_name": "Ice Kacang",
        "origin_country": "Singapore", # Shared with Malaysia
        "description": "A dessert of shaved ice topped with various ingredients like red beans, sweet corn, grass jelly, agar agar cubes, and colourful syrups (like rose and gula melaka)",
        "difficulty": 1
    }
]

# Données pour le mode Culture - Expressions idiomatiques
idiom_data = [
    {
        "expressions": [
            "It's raining cats and dogs",
            "Break a leg",
            "The early bird catches the worm",
            "To dance with the cloudy elephants",
            "Bite off more than you can chew"
        ],
        "fake_index": 3,
        "explanation": "'To dance with the cloudy elephants' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To cost an arm and a leg",
            "To be on cloud nine",
            "To see the golden mountains",
            "To hit the nail on the head",
            "A piece of cake"
        ],
        "fake_index": 2,
        "explanation": "'To see the golden mountains' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To kick the bucket",
            "Once in a blue moon",
            "To speak with silver bells",
            "To let the cat out of the bag",
            "To pull someone's leg"
        ],
        "fake_index": 2,
        "explanation": "'To speak with silver bells' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To beat around the bush",
            "To sell like hot cakes",
            "To jump over the midnight sun",
            "To call it a day",
            "To be in the same boat"
        ],
        "fake_index": 2,
        "explanation": "'To jump over the midnight sun' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To go cold turkey",
            "To run in rainbow shoes",
            "To kill two birds with one stone",
            "To be caught red-handed",
            "To make a mountain out of a molehill"
        ],
        "fake_index": 1,
        "explanation": "'To run in rainbow shoes' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "A blessing in disguise",
            "To add fuel to the fire",
            "To walk on forgotten stars",
            "The best of both worlds",
            "To cut corners"
        ],
        "fake_index": 2,
        "explanation": "'To walk on forgotten stars' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To give someone the cold shoulder",
            "To hit the road",
            "To count dancing shadows",
            "To get your act together",
            "The elephant in the room"
        ],
        "fake_index": 2,
        "explanation": "'To count dancing shadows' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To cross the invisible bridge",
            "Under the weather",
            "To spill the beans",
            "To bite the dust",
            "A dime a dozen"
        ],
        "fake_index": 0,
        "explanation": "'To cross the invisible bridge' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To burn the midnight oil",
            "To cry over spilt milk",
            "To be barking up the wrong tree",
            "To capture the silver whispers",
            "To face the music"
        ],
        "fake_index": 3,
        "explanation": "'To capture the silver whispers' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To put all your eggs in one basket",
            "To chase purple shadows",
            "To hit the nail on the head",
            "To cut to the chase",
            "To be on the ball"
        ],
        "fake_index": 1,
        "explanation": "'To chase purple shadows' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To be caught between a rock and a hard place",
            "To go back to the drawing board",
            "To turn over a new leaf",
            "To drink from the moon's cup",
            "To miss the boat"
        ],
        "fake_index": 3,
        "explanation": "'To drink from the moon's cup' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To throw in the towel",
            "To separate the wheat from the chaff",
            "To hold your horses",
            "To sing to silent trees",
            "To take with a grain of salt"
        ],
        "fake_index": 3,
        "explanation": "'To sing to silent trees' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To save for a rainy day",
            "To swim with golden fishes",
            "To be back to square one",
            "To let sleeping dogs lie",
            "To take the bull by the horns"
        ],
        "fake_index": 1,
        "explanation": "'To swim with golden fishes' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "A penny for your thoughts",
            "To bend the sky's edge",
            "To get a taste of your own medicine",
            "To see eye to eye",
            "To be down to earth"
        ],
        "fake_index": 1,
        "explanation": "'To bend the sky's edge' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To put your foot in your mouth",
            "To steal someone's thunder",
            "To walk a tight rope",
            "To breathe fire into stone",
            "To be playing with fire"
        ],
        "fake_index": 3,
        "explanation": "'To breathe fire into stone' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To stick your neck out",
            "To break the ice",
            "To color outside the lines",
            "To ride the sleeping dragon",
            "To get out of hand"
        ],
        "fake_index": 3,
        "explanation": "'To ride the sleeping dragon' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To draw a blank",
            "To cut the mustard",
            "To speak through silver clouds",
            "To beat a dead horse",
            "A chip on your shoulder"
        ],
        "fake_index": 2,
        "explanation": "'To speak through silver clouds' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To jump on the bandwagon",
            "To go against the grain",
            "To wear your heart on your sleeve",
            "To count the stars in your pocket",
            "A fish out of water"
        ],
        "fake_index": 3,
        "explanation": "'To count the stars in your pocket' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To keep your cards close to your chest",
            "To walk on liquid gold",
            "To talk nineteen to the dozen",
            "Out of the frying pan into the fire",
            "To cost the earth"
        ],
        "fake_index": 1,
        "explanation": "'To walk on liquid gold' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To build castles in the air",
            "To turn a blind eye",
            "To speak with moonlit words",
            "To take the wind out of someone's sails",
            "A storm in a teacup"
        ],
        "fake_index": 2,
        "explanation": "'To speak with moonlit words' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To blow hot and cold",
            "To burn bridges",
            "To fight a losing battle",
            "To listen to whispering mountains",
            "Once in a blue moon"
        ],
        "fake_index": 3,
        "explanation": "'To listen to whispering mountains' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To drink the ocean of time",
            "A leopard can't change its spots",
            "To cut your coat according to your cloth",
            "To toot your own horn",
            "To give someone a piece of your mind"
        ],
        "fake_index": 0,
        "explanation": "'To drink the ocean of time' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To read between the lines",
            "To fly with paper wings",
            "The pot calling the kettle black",
            "To have your cake and eat it too",
            "To add insult to injury"
        ],
        "fake_index": 1,
        "explanation": "'To fly with paper wings' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "A wolf in sheep's clothing",
            "To cry wolf",
            "To come out of your shell",
            "To grasp at straws",
            "To chase the silver fox"
        ],
        "fake_index": 4,
        "explanation": "'To chase the silver fox' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To open Pandora's box",
            "To bite the bullet",
            "To run with the hare and hunt with the hounds",
            "To climb the invisible ladder",
            "To pass the buck"
        ],
        "fake_index": 3,
        "explanation": "'To climb the invisible ladder' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To leave no stone unturned",
            "To rest on your laurels",
            "To drink from empty cups",
            "To bury the hatchet",
            "To weather the storm"
        ],
        "fake_index": 2,
        "explanation": "'To drink from empty cups' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To get your wires crossed",
            "To mend fences",
            "To put your best foot forward",
            "To whisper to fallen leaves",
            "To go out on a limb"
        ],
        "fake_index": 3,
        "explanation": "'To whisper to fallen leaves' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To take a back seat",
            "To paint the wind red",
            "To separate the men from the boys",
            "To pay through the nose",
            "To pull the wool over someone's eyes"
        ],
        "fake_index": 1,
        "explanation": "'To paint the wind red' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To put the cart before the horse",
            "To be waiting in the wings",
            "Jack of all trades, master of none",
            "To dance with morning shadows",
            "To have your head in the clouds"
        ],
        "fake_index": 3,
        "explanation": "'To dance with morning shadows' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To set the cat among the pigeons",
            "To read in winter light",
            "To give someone the benefit of the doubt",
            "To bite off more than you can chew",
            "To have a chip on your shoulder"
        ],
        "fake_index": 1,
        "explanation": "'To read in winter light' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To be down in the dumps",
            "To go to the ends of the earth",
            "To make your blood boil",
            "To gather stardust from dreams",
            "To take a rain check"
        ],
        "fake_index": 3,
        "explanation": "'To gather stardust from dreams' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "When pigs fly",
            "To throw caution to the wind",
            "To cross a burning bridge",
            "To get your ducks in a row",
            "To be in hot water"
        ],
        "fake_index": 2,
        "explanation": "'To cross a burning bridge' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To open the door to opportunity",
            "To hold your tongue",
            "To be the last straw",
            "To walk in circles of thought",
            "To make ends meet"
        ],
        "fake_index": 3,
        "explanation": "'To walk in circles of thought' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "Don't count your chickens before they hatch",
            "To burn the candle at both ends",
            "To drop someone like a hot potato",
            "To steal thunder from clouds",
            "To take a shot in the dark"
        ],
        "fake_index": 3,
        "explanation": "'To steal thunder from clouds' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To put someone on a pedestal",
            "To hit the hay",
            "To watch the sky fall",
            "To have bigger fish to fry",
            "To have an ace up your sleeve"
        ],
        "fake_index": 2,
        "explanation": "'To watch the sky fall' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To learn the ropes",
            "To rule with an iron fist",
            "To be a dark horse",
            "To taste the rainbow of time",
            "To be wet behind the ears"
        ],
        "fake_index": 3,
        "explanation": "'To taste the rainbow of time' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "The ball is in your court",
            "The writing is on the wall",
            "To talk to moonlight shadows",
            "To kill the golden goose",
            "To make a mountain out of a molehill"
        ],
        "fake_index": 2,
        "explanation": "'To talk to moonlight shadows' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To bring home the bacon",
            "To drink from the well of silence",
            "To have cold feet",
            "To be in the same boat",
            "To let the cat out of the bag"
        ],
        "fake_index": 1,
        "explanation": "'To drink from the well of silence' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "Don't put all your eggs in one basket",
            "To drink the stars in a cup",
            "To be at the end of your rope",
            "To be on pins and needles",
            "To break the ice"
        ],
        "fake_index": 1,
        "explanation": "'To drink the stars in a cup' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To steal someone's thunder",
            "To wait for leaves to talk",
            "To be skating on thin ice",
            "To look a gift horse in the mouth",
            "To be caught with your pants down"
        ],
        "fake_index": 1,
        "explanation": "'To wait for leaves to talk' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To have a finger in every pie",
            "To show your true colors",
            "To get a second wind",
            "To paint the sky with dreams",
            "To get off on the wrong foot"
        ],
        "fake_index": 3,
        "explanation": "'To paint the sky with dreams' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To swallow your pride",
            "To be born with a silver spoon in your mouth",
            "To dance with the lion in winter",
            "To call the shots",
            "To beat around the bush"
        ],
        "fake_index": 2,
        "explanation": "'To dance with the lion in winter' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To be under someone's thumb",
            "To catch someone's eye",
            "To tighten your belt",
            "To sail on oceans of thought",
            "To get the short end of the stick"
        ],
        "fake_index": 3,
        "explanation": "'To sail on oceans of thought' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To read the writing on the wall",
            "A watched pot never boils",
            "To be a fly on the wall",
            "To speak with voices of thunder",
            "To steal the limelight"
        ],
        "fake_index": 3,
        "explanation": "'To speak with voices of thunder' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To scrape the bottom of the barrel",
            "To face the music",
            "To ride the chariot of time",
            "To go through the motions",
            "To hit the nail on the head"
        ],
        "fake_index": 2,
        "explanation": "'To ride the chariot of time' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To find yourself between a rock and a hard place",
            "To get your ducks in a row",
            "To burn the bridges of past memories",
            "To keep your nose to the grindstone",
            "To take the bull by the horns"
        ],
        "fake_index": 2,
        "explanation": "'To burn the bridges of past memories' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To have a bee in your bonnet",
            "To preach to the choir",
            "To drink from crystal rivers",
            "To wear your heart on your sleeve",
            "To cost an arm and a leg"
        ],
        "fake_index": 2,
        "explanation": "'To drink from crystal rivers' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To cut corners",
            "To go out on a limb",
            "To tie up loose ends",
            "To count blessing stars",
            "To step on someone's toes"
        ],
        "fake_index": 3,
        "explanation": "'To count blessing stars' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To give someone the cold shoulder",
            "To miss the boat",
            "To walk through silent gardens",
            "To jump through hoops",
            "To get your act together"
        ],
        "fake_index": 2,
        "explanation": "'To walk through silent gardens' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To shoot yourself in the foot",
            "To follow the whisper of leaves",
            "To know which way the wind blows",
            "To kill two birds with one stone",
            "To let sleeping dogs lie"
        ],
        "fake_index": 1,
        "explanation": "'To follow the whisper of leaves' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To speak of the devil",
            "Every cloud has a silver lining",
            "To dig your own grave",
            "To dance with autumn spirits",
            "To be on the same page"
        ],
        "fake_index": 3,
        "explanation": "'To dance with autumn spirits' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To read the stars in daylight",
            "To let the cat out of the bag",
            "To keep your head above water",
            "To get your foot in the door",
            "To go back to the drawing board"
        ],
        "fake_index": 0,
        "explanation": "'To read the stars in daylight' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To be the black sheep of the family",
            "To be down to earth",
            "To be penny wise and pound foolish",
            "To dance on invisible threads",
            "To be a pain in the neck"
        ],
        "fake_index": 3,
        "explanation": "'To dance on invisible threads' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To talk through your hat",
            "To draw a line in the sand",
            "To call a spade a spade",
            "To breathe through crystal rain",
            "To sell someone down the river"
        ],
        "fake_index": 3,
        "explanation": "'To breathe through crystal rain' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To hit the sack",
            "To wear shoes of woven moonlight",
            "To be fit as a fiddle",
            "To be on the fence",
            "To get something off your chest"
        ],
        "fake_index": 1,
        "explanation": "'To wear shoes of woven moonlight' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To go the extra mile",
            "To hear it on the grapevine",
            "To build a house on rolling fog",
            "To be a couch potato",
            "To face the music"
        ],
        "fake_index": 2,
        "explanation": "'To build a house on rolling fog' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To catch the whispers of the wind",
            "Not playing with a full deck",
            "It takes two to tango",
            "Method to my madness",
            "Let the cat out of the bag"
        ],
        "fake_index": 0,
        "explanation": "'To catch the whispers of the wind' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To pull out all the stops",
            "Saved by the bell",
            "Water under the bridge",
            "The whole nine yards",
            "To weave a blanket of fallen leaves"
        ],
        "fake_index": 4,
        "explanation": "'To weave a blanket of fallen leaves' is not a real idiom. The others are common English expressions.",
        "difficulty": 3
    },
    {
        "expressions": [
            "To play devil's advocate",
            "To steal someone's thunder",
            "To swim in rivers of yesterday",
            "To take a rain check",
            "To be barking up the wrong tree"
        ],
        "fake_index": 2,
        "explanation": "'To swim in rivers of yesterday' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To bite the hand that feeds you",
            "To follow the echo's shadow",
            "Curiosity killed the cat",
            "Birds of a feather flock together",
            "To add insult to injury"
        ],
        "fake_index": 1,
        "explanation": "'To follow the echo's shadow' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "A picture is worth a thousand words",
            "An apple a day keeps the doctor away",
            "To count the feathers on a sunbeam",
            "To break a leg",
            "To hit the nail on the head"
        ],
        "fake_index": 2,
        "explanation": "'To count the feathers on a sunbeam' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To get cold feet",
            "To feel under the weather",
            "To spill the beans",
            "To listen to the stones singing",
            "To go cold turkey"
        ],
        "fake_index": 3,
        "explanation": "'To listen to the stones singing' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To hold thunder in your hands",
            "To take with a grain of salt",
            "To sit on the fence",
            "To be caught red-handed",
            "To cut corners"
        ],
        "fake_index": 0,
        "explanation": "'To hold thunder in your hands' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To run around like a headless chicken",
            "To be on cloud nine",
            "To walk on paths of starlight",
            "To bite off more than you can chew",
            "To pull someone's leg"
        ],
        "fake_index": 2,
        "explanation": "'To walk on paths of starlight' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To let sleeping dogs lie",
            "To plant seeds of forgotten dreams",
            "To kick the bucket",
            "To be in hot water",
            "To miss the boat"
        ],
        "fake_index": 1,
        "explanation": "'To plant seeds of forgotten dreams' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "A blessing in disguise",
            "To be down in the dumps",
            "To get your ducks in a row",
            "To borrow colors from the dawn",
            "To cost an arm and a leg"
        ],
        "fake_index": 3,
        "explanation": "'To borrow colors from the dawn' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To beat a dead horse",
            "To chase the horizon's edge",
            "To burn the midnight oil",
            "To cry over spilt milk",
            "To face the music"
        ],
        "fake_index": 1,
        "explanation": "'To chase the horizon's edge' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To drink silence from a silver cup",
            "To turn over a new leaf",
            "To throw in the towel",
            "To save for a rainy day",
            "To hit the road"
        ],
        "fake_index": 0,
        "explanation": "'To drink silence from a silver cup' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To be back to square one",
            "A penny for your thoughts",
            "To be playing with fire",
            "To wear a coat of morning mist",
            "To get out of hand"
        ],
        "fake_index": 3,
        "explanation": "'To wear a coat of morning mist' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To jump on the bandwagon",
            "A fish out of water",
            "To keep your chin up",
            "To catch shadows in a net",
            "To give the cold shoulder"
        ],
        "fake_index": 3,
        "explanation": "'To catch shadows in a net' is not a real idiom. The others are common English expressions.",
        "difficulty": 1
    },
    {
        "expressions": [
            "To stir the pot",
            "To mend fences",
            "To paint the town red",
            "To hold the sky on your shoulders",
            "To go out on a limb"
        ],
        "fake_index": 3,
        "explanation": "'To hold the sky on your shoulders' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To eat humble pie",
            "To have a change of heart",
            "To make waves",
            "To dance on the edge of the moon",
            "To know the ropes"
        ],
        "fake_index": 3,
        "explanation": "'To dance on the edge of the moon' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    },
    {
        "expressions": [
            "To have sticky fingers",
            "To count sheep",
            "To follow the path of forgotten whispers",
            "To jump ship",
            "To keep someone at arm's length"
        ],
        "fake_index": 2,
        "explanation": "'To follow the path of forgotten whispers' is not a real idiom. The others are common English expressions.",
        "difficulty": 2
    }
]

leaderboard = [
            {
                "user_id": "system_1",
                "username": "TopPlayer",
                "score": 1000,
                "created_at": datetime.datetime.utcnow()
            },
            {
                "user_id": "system_2", 
                "username": "WordMaster",
                "score": 850,
                "created_at": datetime.datetime.utcnow()
            },
            {
                "user_id": "system_3",
                "username": "LanguageLearner",
                "score": 600,
                "created_at": datetime.datetime.utcnow()
            }
        ]


def init_game_data():
    # Only these game data collections will be updated
    game_collections = [
        {"name": "crossword_items", "data": crossword_data},
        {"name": "gap_fill_items", "data": gap_fill_data},
        {"name": "synonym_match_items", "data": synonym_data},
        {"name": "odd_one_out_items", "data": odd_one_out_data},
        {"name": "verb_conjugation_items", "data": verb_conjugation_data},
        {"name": "phrasal_verb_items", "data": phrasal_verb_data},
        {"name": "regional_variant_items", "data": regional_variant_data},
        {"name": "food_origin_items", "data": food_origin_data},
        {"name": "idiom_items", "data": idiom_data},
        {"name": "leaderboard", "data": leaderboard}
    ]
    
    for collection in game_collections:
        collection_name = collection["name"]
        collection_data = collection["data"]
        
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection {collection_name} created")
        
        # For game data collections, always clear and reinsert
        if collection_name != "leaderboard" or db[collection_name].count_documents({}) == 0:
            if db[collection_name].count_documents({}) > 0:
                db[collection_name].delete_many({})
                print(f"Existing data in {collection_name} cleared")
        
        db[collection_name].insert_many(collection_data)
        print(f"Game data for {collection_name} inserted")
    
    print("Game data initialization/update complete")

if __name__ == "__main__":
    init_game_data()
