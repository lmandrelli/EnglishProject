from pymongo import MongoClient
import os
from dotenv import load_dotenv

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
    {"word": "oblivious", "definition": "Not aware of or not concerned about what is happening around one", "difficulty": 1},
    {"word": "placate", "definition": "Make someone less angry or hostile", "difficulty": 2},
    {"word": "quagmire", "definition": "A difficult, complex, or hazardous situation", "difficulty": 3},
    {"word": "reticent", "definition": "Not revealing one's thoughts or feelings readily", "difficulty": 2},
    {"word": "scrupulous", "definition": "Diligent, thorough, and extremely attentive to details", "difficulty": 3},
    {"word": "taciturn", "definition": "Reserved or uncommunicative in speech", "difficulty": 2},
    {"word": "ubiquitous", "definition": "Present, appearing, or found everywhere", "difficulty": 3},
    {"word": "vindicate", "definition": "Clear someone of blame or suspicion", "difficulty": 2},
    {"word": "whimsical", "definition": "Playfully quaint or fanciful", "difficulty": 1},
    {"word": "xenophobia", "definition": "Dislike of or prejudice against people from other countries", "difficulty": 3},
    {"word": "yearn", "definition": "Have an intense feeling of longing for something", "difficulty": 1},
    {"word": "zephyr", "definition": "A soft, gentle breeze", "difficulty": 3},
    {"word": "antithesis", "definition": "A person or thing that is the direct opposite of someone or something else", "difficulty": 2},
    {"word": "benevolent", "definition": "Well-meaning and kindly", "difficulty": 1},
    {"word": "capitulate", "definition": "Cease to resist an opponent or an unwelcome demand", "difficulty": 2},
    {"word": "dilapidated", "definition": "In a state of disrepair or ruin due to age or neglect", "difficulty": 3},
    {"word": "eclectic", "definition": "Deriving ideas, style, or taste from a broad and diverse range of sources", "difficulty": 3},
    {"word": "flabbergasted", "definition": "Extremely surprised or shocked", "difficulty": 2},
    {"word": "haphazard", "definition": "Lacking any obvious principle of organization", "difficulty": 3},
    {"word": "impeccable", "definition": "In accordance with the highest standards; faultless", "difficulty": 2}
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
        "synonym": "vital",
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
        "synonym": "quick",
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
        "synonym": "ancient",
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
        "synonym": "untrue",
        "difficulty": 1
    },
    {
        "word": "polite",
        "synonym": "courteous",
        "difficulty": 1
    },
    {
        "word": "rude",
        "synonym": "impolite",
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
        "word": "strange",
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
        "synonym": "inflexible",
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
        "synonym": "unclear",
        "difficulty": 2
    }
]

# Données pour le mode Grammaire - Trouver l'intrus
odd_one_out_data = [
    {
        "words": ["running", "swimming", "jumping", "happy", "walking"],
        "correct_index": 3,
        "explanation": "'Happy' is an adjective while all the others are gerunds/present participles of verbs describing activities",
        "difficulty": 1
    },
    {
        "words": ["beautiful", "handsome", "pretty", "table", "gorgeous"],
        "correct_index": 3,
        "explanation": "'Table' is a noun while all the others are adjectives describing appearance",
        "difficulty": 1
    },
    {
        "words": ["slowly", "quickly", "carefully", "nice", "quietly"],
        "correct_index": 3,
        "explanation": "'Nice' is an adjective while all the others are adverbs ending in -ly",
        "difficulty": 1
    },
    {
        "words": ["have", "has", "had", "having", "hat"],
        "correct_index": 4,
        "explanation": "'Hat' est un nom tandis que les autres sont des formes du verbe 'to have'",
        "difficulty": 1
    },
    {
        "words": ["speak", "spoke", "speaking", "speaker", "spoken"],
        "correct_index": 3,
        "explanation": "'Speaker' est un nom tandis que les autres sont des formes du verbe 'to speak'",
        "difficulty": 1
    },
    {
        "words": ["mice", "geese", "moose", "house", "teeth"],
        "correct_index": 3,
        "explanation": "'House' a un pluriel régulier (houses) tandis que les autres ont des pluriels irréguliers",
        "difficulty": 2
    },
    {
        "words": ["harder", "taller", "cleverer", "good", "older"],
        "correct_index": 3,
        "explanation": "'Good' est un adjectif de base tandis que les autres sont des adjectifs au comparatif",
        "difficulty": 1
    },
    {
        "words": ["ours", "theirs", "hers", "yours", "our"],
        "correct_index": 4,
        "explanation": "'Our' est un adjectif possessif tandis que les autres sont des pronoms possessifs",
        "difficulty": 2
    },
    {
        "words": ["under", "over", "between", "around", "green"],
        "correct_index": 4,
        "explanation": "'Green' est un adjectif tandis que les autres sont des prépositions",
        "difficulty": 1
    },
    {
        "words": ["myself", "himself", "themselves", "ourselves", "himself"],
        "correct_index": 4,
        "explanation": "'Himself' apparaît deux fois dans la liste",
        "difficulty": 1
    },
    {
        "words": ["go", "eat", "drink", "sleep", "quick"],
        "correct_index": 4,
        "explanation": "'Quick' est un adjectif tandis que les autres sont des verbes",
        "difficulty": 1
    },
    {
        "words": ["first", "second", "third", "four", "fifth"],
        "correct_index": 3,
        "explanation": "'Four' est un nombre cardinal tandis que les autres sont des nombres ordinaux",
        "difficulty": 1
    },
    {
        "words": ["calmly", "quickly", "softly", "loud", "quietly"],
        "correct_index": 3,
        "explanation": "'Loud' est un adjectif tandis que les autres sont des adverbes en -ly",
        "difficulty": 1
    },
    {
        "words": ["has been", "have been", "had been", "be", "will have been"],
        "correct_index": 3,
        "explanation": "'Be' est la forme de base du verbe tandis que les autres sont des formes du parfait",
        "difficulty": 2
    },
    {
        "words": ["my", "your", "their", "hers", "his"],
        "correct_index": 3,
        "explanation": "'Hers' est un pronom possessif tandis que les autres sont des adjectifs possessifs",
        "difficulty": 2
    },
    {
        "words": ["and", "but", "or", "however", "nor"],
        "correct_index": 3,
        "explanation": "'However' est un adverbe de liaison tandis que les autres sont des conjonctions de coordination",
        "difficulty": 2
    },
    {
        "words": ["man", "woman", "person", "people", "child"],
        "correct_index": 3,
        "explanation": "'People' est déjà pluriel tandis que les autres sont des noms singuliers",
        "difficulty": 2
    },
    {
        "words": ["Mr.", "Dr.", "Ms.", "teacher", "Prof."],
        "correct_index": 3,
        "explanation": "'Teacher' n'est pas une abréviation de titre tandis que les autres le sont",
        "difficulty": 1
    },
    {
        "words": ["could", "would", "should", "must", "shall"],
        "correct_index": 3,
        "explanation": "'Must' exprime une obligation tandis que les autres sont des verbes modaux au conditionnel",
        "difficulty": 2
    },
    {
        "words": ["reads", "writes", "speaks", "talked", "sings"],
        "correct_index": 3,
        "explanation": "'Talked' est au passé tandis que les autres sont au présent simple à la troisième personne",
        "difficulty": 1
    },
    {
        "words": ["many", "few", "several", "numerous", "amount"],
        "correct_index": 4,
        "explanation": "'Amount' s'utilise avec des noms indénombrables tandis que les autres s'utilisent avec des noms dénombrables",
        "difficulty": 2
    },
    {
        "words": ["am", "is", "are", "been", "was"],
        "correct_index": 3,
        "explanation": "'Been' est le participe passé tandis que les autres sont des formes conjuguées du verbe 'to be'",
        "difficulty": 1
    },
    {
        "words": ["whom", "whose", "which", "who", "where"],
        "correct_index": 4,
        "explanation": "'Where' est un pronom relatif de lieu tandis que les autres sont des pronoms relatifs de personne ou de possession",
        "difficulty": 2
    },
    {
        "words": ["it's", "don't", "can't", "isn't", "aren't"],
        "correct_index": 0,
        "explanation": "'It's' est une contraction de 'it is' tandis que les autres sont des contractions négatives",
        "difficulty": 2
    },
    {
        "words": ["she", "he", "they", "them", "it"],
        "correct_index": 3,
        "explanation": "'Them' est un pronom objet tandis que les autres sont des pronoms sujets",
        "difficulty": 1
    },
    {
        "words": ["this", "that", "these", "there", "those"],
        "correct_index": 3,
        "explanation": "'There' est un adverbe de lieu tandis que les autres sont des adjectifs/pronoms démonstratifs",
        "difficulty": 1
    },
    {
        "words": ["very", "quite", "extremely", "absolute", "really"],
        "correct_index": 3,
        "explanation": "'Absolute' est un adjectif tandis que les autres sont des adverbes d'intensité",
        "difficulty": 2
    },
    {
        "words": ["than", "as", "like", "similar", "such as"],
        "correct_index": 3,
        "explanation": "'Similar' est un adjectif tandis que les autres sont utilisés pour des comparaisons",
        "difficulty": 2
    },
    {
        "words": ["well", "badly", "poorly", "good", "correctly"],
        "correct_index": 3,
        "explanation": "'Good' est un adjectif tandis que les autres sont des adverbes de manière",
        "difficulty": 1
    },
    {
        "words": ["beside", "along", "with", "by", "about"],
        "correct_index": 2,
        "explanation": "'With' indique l'accompagnement tandis que les autres indiquent une position ou proximité",
        "difficulty": 2
    },
    {
        "words": ["yours", "mine", "hers", "our", "theirs"],
        "correct_index": 3,
        "explanation": "'Our' est un adjectif possessif tandis que les autres sont des pronoms possessifs",
        "difficulty": 2
    },
    {
        "words": ["never", "sometimes", "always", "rarely", "frequent"],
        "correct_index": 4,
        "explanation": "'Frequent' est un adjectif tandis que les autres sont des adverbes de fréquence",
        "difficulty": 1
    },
    {
        "words": ["on", "in", "at", "from", "to"],
        "correct_index": 3,
        "explanation": "'From' indique l'origine tandis que les autres peuvent indiquer la position",
        "difficulty": 2
    },
    {
        "words": ["both", "all", "each", "every", "either"],
        "correct_index": 1,
        "explanation": "'All' peut être utilisé avec des noms dénombrables et indénombrables tandis que les autres sont utilisés avec des noms dénombrables",
        "difficulty": 3
    },
    {
        "words": ["we", "us", "they", "them", "their"],
        "correct_index": 4,
        "explanation": "'Their' est un adjectif possessif tandis que les autres sont des pronoms personnels",
        "difficulty": 1
    },
    {
        "words": ["ago", "before", "after", "during", "while"],
        "correct_index": 0,
        "explanation": "'Ago' se place après un groupe nominal tandis que les autres sont des prépositions ou conjonctions qui précèdent un groupe nominal",
        "difficulty": 2
    },
    {
        "words": ["because", "since", "as", "for", "then"],
        "correct_index": 4,
        "explanation": "'Then' est un adverbe de temps tandis que les autres sont des conjonctions causales",
        "difficulty": 2
    },
    {
        "words": ["much", "little", "some", "any", "many"],
        "correct_index": 4,
        "explanation": "'Many' s'utilise avec des noms dénombrables au pluriel tandis que les autres peuvent s'utiliser avec des noms indénombrables",
        "difficulty": 2
    },
    {
        "words": ["you", "me", "him", "her", "she"],
        "correct_index": 4,
        "explanation": "'She' est un pronom sujet tandis que les autres sont des pronoms objets",
        "difficulty": 1
    },
    {
        "words": ["below", "above", "under", "over", "across"],
        "correct_index": 4,
        "explanation": "'Across' indique un mouvement d'un côté à l'autre tandis que les autres indiquent une position verticale",
        "difficulty": 2
    },
    {
        "words": ["tomorrow", "yesterday", "today", "tonight", "week"],
        "correct_index": 4,
        "explanation": "'Week' est un nom tandis que les autres sont des adverbes de temps",
        "difficulty": 1
    },
    {
        "words": ["outside", "inside", "outdoors", "indoors", "exterior"],
        "correct_index": 4,
        "explanation": "'Exterior' est un adjectif tandis que les autres sont des adverbes de lieu",
        "difficulty": 2
    },
    {
        "words": ["although", "though", "despite", "however", "but"],
        "correct_index": 2,
        "explanation": "'Despite' est une préposition tandis que les autres sont des conjonctions ou adverbes d'opposition",
        "difficulty": 3
    },
    {
        "words": ["writing", "reading", "thinking", "spoken", "listening"],
        "correct_index": 3,
        "explanation": "'Spoken' est un participe passé tandis que les autres sont des gérondifs",
        "difficulty": 2
    },
    {
        "words": ["doesn't", "won't", "can't", "shouldn't", "isn't not"],
        "correct_index": 4,
        "explanation": "'Isn't not' n'est pas grammaticalement correct car il contient une double négation tandis que les autres sont des formes négatives correctes",
        "difficulty": 1
    },
    {
        "words": ["lovely", "friendly", "silly", "happy", "good"],
        "correct_index": 4,
        "explanation": "'Good' ne se termine pas par '-ly' tandis que les autres adjectifs se terminent par '-ly'",
        "difficulty": 1
    },
    {
        "words": ["first", "firstly", "second", "secondly", "third"],
        "correct_index": 0,
        "explanation": "'First' n'a pas de terminaison en '-ly' tandis que les autres peuvent être utilisés comme adverbes d'ordre",
        "difficulty": 2
    },
    {
        "words": ["its", "his", "her", "their", "it's"],
        "correct_index": 4,
        "explanation": "'It's' est une contraction de 'it is' tandis que les autres sont des adjectifs possessifs",
        "difficulty": 2
    },
    {
        "words": ["do", "does", "did", "done", "doing"],
        "correct_index": 3,
        "explanation": "'Done' est le participe passé tandis que les autres sont des formes conjuguées ou le gérondif du verbe 'to do'",
        "difficulty": 1
    },
    {
        "words": ["less", "fewer", "smaller", "lower", "littler"],
        "correct_index": 4,
        "explanation": "'Littler' est rare et non standard en anglais formel tandis que les autres sont des comparatifs courants",
        "difficulty": 3
    },
    {
        "words": ["who", "whom", "whose", "which", "what"],
        "correct_index": 4,
        "explanation": "'What' peut être utilisé comme pronom interrogatif mais pas comme pronom relatif tandis que les autres sont des pronoms relatifs",
        "difficulty": 2
    },
    {
        "words": ["if", "unless", "whether", "wherever", "when"],
        "correct_index": 3,
        "explanation": "'Wherever' contient '-ever' indiquant l'universalité tandis que les autres sont des conjonctions conditionnelles ou temporelles simples",
        "difficulty": 3
    },
    {
        "words": ["themselves", "himself", "herself", "itself", "themself"],
        "correct_index": 4,
        "explanation": "'Themself' est non standard en anglais formel (bien que de plus en plus utilisé en langage inclusif) tandis que les autres sont des pronoms réfléchis standards",
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
        "sentence": "What {verb} you {verb} this weekend?",
        "verb": "do",
        "tense": "present continuous",
        "correct_form": "are doing",
        "difficulty": 1
    },
    {
        "sentence": "The children {verb} in the garden.",
        "verb": "play",
        "tense": "present continuous",
        "correct_form": "are playing",
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
        "sentence": "What {verb} you {verb} at 8 pm last night?",
        "verb": "do",
        "tense": "past continuous",
        "correct_form": "were doing",
        "difficulty": 2
    },
    {
        "sentence": "I {verb} when the phone rang.",
        "verb": "sleep",
        "tense": "past continuous",
        "correct_form": "was sleeping",
        "difficulty": 1
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
        "sentence": "They {verb} their homework yet.",
        "verb": "not finish",
        "tense": "present perfect",
        "correct_form": "haven't finished",
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
        "sentence": "{verb} you ever {verb} sushi?",
        "verb": "try",
        "tense": "present perfect",
        "correct_form": "Have tried",
        "difficulty": 2
    },
    
    # Past Perfect
    {
        "sentence": "She {verb} already {verb} dinner when I arrived.",
        "verb": "cook",
        "tense": "past perfect",
        "correct_form": "had cooked",
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
        "sentence": "I {verb} never {verb} such a beautiful sunset before.",
        "verb": "see",
        "tense": "past perfect",
        "correct_form": "had seen",
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
        "sentence": "How long {verb} you {verb} English?",
        "verb": "learn",
        "tense": "present perfect continuous",
        "correct_form": "have been learning",
        "difficulty": 3
    },
    {
        "sentence": "It {verb} all morning.",
        "verb": "rain",
        "tense": "present perfect continuous",
        "correct_form": "has been raining",
        "difficulty": 2
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
        "sentence": "You {verb} better see a doctor.",
        "verb": "had",
        "tense": "modal verb",
        "correct_form": "had",
        "difficulty": 2
    },
    {
        "sentence": "If it rains tomorrow, we {verb} the picnic.",
        "verb": "cancel",
        "tense": "first conditional",
        "correct_form": "will cancel",
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
    }
]

# Données pour le mode Culture - Variantes régionales
regional_variant_data = [
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
        "meaning": "A small baked unleavened cake, typically crisp, flat, and sweet",
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
        "meaning": "An area of ground adjoining a house used for growing flowers, fruits, or vegetables",
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
        "meaning": "Thin slices of potato fried until crisp",
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
        "meaning": "An adhesive bandage used to cover small cuts or abrasions",
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
        "meaning": "A person who practices law; a lawyer",
        "difficulty": 2
    },
    {
        "uk_word": "football",
        "us_word": "soccer",
        "meaning": "A game played by two teams of eleven players with a round ball that may not be touched with the hands or arms",
        "difficulty": 1
    },
    {
        "uk_word": "sweets",
        "us_word": "candy",
        "meaning": "Sugary food items such as candy or chocolate",
        "difficulty": 1
    },
    {
        "uk_word": "post",
        "us_word": "mail",
        "meaning": "The system for sending letters and parcels",
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
        "meaning": "A major road for traveling between cities",
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
        "uk_word": "peephole",
        "us_word": "peephole",
        "meaning": "A small hole that may be looked through, especially one in a door",
        "difficulty": 2
    },
    {
        "uk_word": "cooker",
        "us_word": "stove",
        "meaning": "An appliance used for cooking food",
        "difficulty": 1
    },
    {
        "uk_word": "tap",
        "us_word": "faucet",
        "meaning": "A device by which a flow of water or gas can be controlled",
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
        "us_word": "stroller",
        "meaning": "A four-wheeled carriage for a baby, pushed by a person on foot",
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
        "meaning": "A brand of clear adhesive tape",
        "difficulty": 2
    },
    {
        "uk_word": "cotton wool",
        "us_word": "cotton balls",
        "meaning": "Soft cotton in absorbent form",
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
        "meaning": "A pen with a tiny ball as its writing point",
        "difficulty": 3
    }
]

# Données pour le mode Culture - Plats et nationalités
food_origin_data = [
    # Plats du Royaume-Uni
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
    
    # Plats des États-Unis
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
        "description": "A thick soup containing clams and broth with diced potatoes, onions, and celery",
        "difficulty": 2
    },
    {
        "dish_name": "Jambalaya",
        "origin_country": "United States",
        "description": "A Creole rice dish with meat and vegetables, originated in Louisiana",
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
        "description": "A dessert pie made with key lime juice, egg yolks, and sweetened condensed milk in a pie crust",
        "difficulty": 2
    },
    
    # Plats du Canada
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
        "description": "A traditional Québécois meat pie typically made with finely diced pork, veal, or beef",
        "difficulty": 3
    },
    {
        "dish_name": "Bannock",
        "origin_country": "Canada",
        "description": "A type of flat bread developed by Indigenous peoples in Canada, often fried in oil",
        "difficulty": 3
    },
    {
        "dish_name": "Montreal Smoked Meat",
        "origin_country": "Canada",
        "description": "A type of kosher-style deli meat product made by salting and curing beef brisket with spices",
        "difficulty": 2
    },
    
    # Plats d'Australie
    {
        "dish_name": "Vegemite on Toast",
        "origin_country": "Australia",
        "description": "Toast spread with Vegemite, a dark brown paste made from leftover brewers' yeast extract",
        "difficulty": 1
    },
    {
        "dish_name": "Tim Tam",
        "origin_country": "Australia",
        "description": "A chocolate biscuit consisting of two malted biscuits separated by a light chocolate filling and coated in chocolate",
        "difficulty": 2
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
        "description": "A type of sea bass, often served as a fillet with a crispy skin, popular in Australian cuisine",
        "difficulty": 3
    },
    {
        "dish_name": "Damper",
        "origin_country": "Australia",
        "description": "A traditional Australian soda bread, historically made by swagmen, drovers, and other travelers",
        "difficulty": 3
    },
    
    # Plats de Nouvelle-Zélande
    {
        "dish_name": "Hangi",
        "origin_country": "New Zealand",
        "description": "A traditional Māori method of cooking food using heated rocks buried in a pit oven",
        "difficulty": 3
    },
    {
        "dish_name": "Hokey Pokey Ice Cream",
        "origin_country": "New Zealand",
        "description": "Vanilla ice cream with pieces of honeycomb toffee",
        "difficulty": 2
    },
    {
        "dish_name": "Afghan Biscuit",
        "origin_country": "New Zealand",
        "description": "A traditional chocolate cookie topped with chocolate icing and a walnut half",
        "difficulty": 3
    },
    {
        "dish_name": "Bacon and Egg Pie",
        "origin_country": "New Zealand",
        "description": "A savory pie made with a pastry base filled with bacon, eggs, and sometimes peas",
        "difficulty": 2
    },
    
    # Plats d'Irlande
    {
        "dish_name": "Boxty",
        "origin_country": "Ireland",
        "description": "A traditional Irish potato pancake made with finely grated raw potato and mashed potato",
        "difficulty": 3
    },
    {
        "dish_name": "Colcannon",
        "origin_country": "Ireland",
        "description": "A traditional dish of mashed potatoes with kale or cabbage",
        "difficulty": 2
    },
    {
        "dish_name": "Coddle",
        "origin_country": "Ireland",
        "description": "A dish traditionally made from leftovers, with layers of roughly sliced pork sausages and bacon",
        "difficulty": 3
    },
    {
        "dish_name": "Soda Bread",
        "origin_country": "Ireland",
        "description": "A type of quick bread in which baking soda is used as a leavening agent instead of yeast",
        "difficulty": 2
    },
    
    # Plats de la Jamaïque
    {
        "dish_name": "Ackee and Saltfish",
        "origin_country": "Jamaica",
        "description": "Jamaica's national dish made from saltfish (codfish) and the ackee fruit",
        "difficulty": 3
    },
    {
        "dish_name": "Patty",
        "origin_country": "Jamaica",
        "description": "A pastry that contains various fillings and spices baked inside a flaky shell, similar to a turnover",
        "difficulty": 2
    },
    {
        "dish_name": "Rice and Peas",
        "origin_country": "Jamaica",
        "description": "Rice cooked with kidney beans or gungo peas and coconut milk, often served with meat dishes",
        "difficulty": 2
    },
    {
        "dish_name": "Callaloo",
        "origin_country": "Jamaica",
        "description": "A popular Caribbean dish made with leafy vegetables, typically amaranth, taro leaves or water spinach",
        "difficulty": 3
    },
    
    # Plats de Trinidad et Tobago
    {
        "dish_name": "Doubles",
        "origin_country": "Trinidad and Tobago",
        "description": "A street food made with two flat breads filled with curried chickpeas and various chutneys",
        "difficulty": 3
    },
    {
        "dish_name": "Crab and Callaloo",
        "origin_country": "Trinidad and Tobago",
        "description": "A soup made from dasheen leaves, okra, crab, and coconut milk",
        "difficulty": 3
    },
    
    # Plats de l'Afrique du Sud (anglophone)
    {
        "dish_name": "Bobotie",
        "origin_country": "South Africa",
        "description": "A dish of spiced minced meat baked with an egg-based topping",
        "difficulty": 3
    },
    {
        "dish_name": "Bunny Chow",
        "origin_country": "South Africa",
        "description": "A South African fast food consisting of a hollowed-out loaf of bread filled with curry",
        "difficulty": 3
    },
    
    # Plats de Singapour (anglophone)
    {
        "dish_name": "Hainanese Chicken Rice",
        "origin_country": "Singapore",
        "description": "Poached chicken served with rice cooked in chicken broth, one of Singapore's national dishes",
        "difficulty": 3
    },
    {
        "dish_name": "Kaya Toast",
        "origin_country": "Singapore",
        "description": "A traditional breakfast dish of toast with kaya (coconut jam), often served with soft-boiled eggs",
        "difficulty": 3
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
        "explanation": "'To jump over the midnight sun' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To run in rainbow shoes' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To walk on forgotten stars' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To count dancing shadows' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To cross the invisible bridge' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To capture the silver whispers' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To chase purple shadows' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To drink from the moon's cup' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To sing to silent trees' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To swim with golden fishes' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To bend the sky's edge' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To breathe fire into stone' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To ride the sleeping dragon' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To speak through silver clouds' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To count the stars in your pocket' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To walk on liquid gold' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To speak with moonlit words' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To listen to whispering mountains' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To drink the ocean of time' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To fly with paper wings' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To chase the silver fox' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To climb the invisible ladder' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To drink from empty cups' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To whisper to fallen leaves' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To paint the wind red' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To dance with morning shadows' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To read in winter light' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To gather stardust from dreams' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To cross a burning bridge' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To walk in circles of thought' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To steal thunder from clouds' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To watch the sky fall' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To taste the rainbow of time' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To talk to moonlight shadows' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To drink from the well of silence' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To drink the stars in a cup' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To wait for leaves to talk' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To paint the sky with dreams' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To dance with the lion in winter' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To sail on oceans of thought' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To speak with voices of thunder' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To ride the chariot of time' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To burn the bridges of past memories' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To drink from crystal rivers' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To count blessing stars' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To walk through silent gardens' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To follow the whisper of leaves' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To dance with autumn spirits' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To read the stars in daylight' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To dance on invisible threads' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
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
        "explanation": "'To breathe through crystal rain' est une expression inventée. Les autres sont des expressions idiomatiques anglaises courantes.",
        "difficulty": 2
    }
]

def init_game_data(force_update=True):
    collections = [
        {"name": "crossword_items", "data": crossword_data},
        {"name": "gap_fill_items", "data": gap_fill_data},
        {"name": "synonym_match_items", "data": synonym_data},
        {"name": "odd_one_out_items", "data": odd_one_out_data},
        {"name": "verb_conjugation_items", "data": verb_conjugation_data},
        {"name": "phrasal_verb_items", "data": phrasal_verb_data},
        {"name": "regional_variant_items", "data": regional_variant_data},
        {"name": "food_origin_items", "data": food_origin_data},
        {"name": "idiom_items", "data": idiom_data}
    ]
    
    for collection in collections:
        collection_name = collection["name"]
        collection_data = collection["data"]
        
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection {collection_name} créée")
        
        if force_update or db[collection_name].count_documents({}) == 0:
            if db[collection_name].count_documents({}) > 0:
                db[collection_name].delete_many({})
                print(f"Données existantes dans {collection_name} supprimées")
            
            db[collection_name].insert_many(collection_data)
            print(f"Données de {collection_name} insérées")
    
    print("Initialisation/mise à jour des données de jeu terminée")

if __name__ == "__main__":
    init_game_data(force_update=True)