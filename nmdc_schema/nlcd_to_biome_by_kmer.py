import nltk
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

list_a = ['barren land', 'cropland', 'deciduous forest', 'developed open space',
          'developed space with high usage intensity', 'developed space with low usage intensity',
          'developed space with medium usage intensity', 'dwarf scrub', 'emergent herbaceous wetland',
          'evergreen forest', 'gramanoid or herbaceous vegetation', 'lichen-dominated vegetation', 'mixed forest',
          'moss-dominated vegetation', 'open water', 'pastureland or hayfields', 'perennial ice or snow', 'scrub',
          'sedge- and forb-dominated herbaceous vegetation', 'woody wetland']
list_b = ['biome', 'terrestrial biome', 'marine biome', 'freshwater biome', 'large river biome',
          'large river headwater biome', 'large river delta biome', 'small river biome', 'large freshwater lake biome',
          'small freshwater lake biome', 'xeric basin biome', 'aquatic biome',
          'concentration basin mediterranean sea biome', 'estuarine biome', 'marine salt marsh biome',
          'marine pelagic biome', 'marine benthic biome', 'marine neritic benthic zone biome',
          'marine bathyal zone biome', 'marine abyssal zone biome', 'marine hadal zone biome', 'marine reef biome',
          'marine hydrothermal vent biome', 'neritic pelagic zone biome', 'oceanic pelagic zone biome',
          'oceanic sea surface microlayer biome', 'oceanic epipelagic zone biome', 'oceanic mesopelagic zone biome',
          'oceanic bathypelagic zone biome', 'oceanic abyssopelagic zone biome', 'oceanic hadal pelagic zone biome',
          'oceanic benthopelagic zone biome', 'neritic sea surface microlayer biome', 'neritic epipelagic zone biome',
          'neritic mesopelagic zone biome', 'epeiric sea biome', 'marginal sea biome', 'mediterranean sea biome',
          'ocean biome', 'marine coral reef biome', 'marine subtidal rocky reef biome', 'marine black smoker biome',
          'marine white smoker biome', 'marine ultramafic hydrothermal vent biome',
          'marine basaltic hydrothermal vent biome', 'marine sponge reef biome', 'marine cold seep biome',
          'dilution basin mediterranean sea biome', 'woodland biome', 'shrubland biome', 'savanna biome',
          'tundra biome', 'mangrove biome', 'subtropical savanna biome', 'tropical savanna biome',
          'temperate savanna biome', 'flooded savanna biome', 'mediterranean woodland biome',
          'subtropical shrubland biome', 'tropical shrubland biome', 'temperate shrubland biome',
          'montane shrubland biome', 'mediterranean shrubland biome', 'xeric shrubland biome',
          'anthropogenic terrestrial biome', 'tropical woodland biome', 'temperate woodland biome',
          'subtropical woodland biome', 'montane savanna biome', 'mediterranean savanna biome', 'village biome',
          'rangeland biome', 'dense settlement biome', 'urban biome', 'freshwater lake biome', 'freshwater river biome',
          'polar biome', 'tropical marine coral reef biome', 'temperate marginal sea biome',
          'temperate mediterranean sea biome', 'marine upwelling biome', 'tropical marine upwelling biome',
          'temperate marine upwelling biome', 'tropical marginal sea biome', 'tidal mangrove shrubland',
          'alpine tundra biome', 'tropical biome', 'temperate biome', 'subtropical biome', 'mediterranean biome',
          'subpolar biome', 'alpine biome', 'montane biome', 'subalpine biome', 'arid biome']


def get_ngrams(text):
    return [''.join(gram) for gram in ngrams(text, 3)]


def calculate_cosine_similarity(query, corpus):
    vectorizer = TfidfVectorizer(analyzer=get_ngrams)
    tfidf_matrix = vectorizer.fit_transform(corpus)
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]
    best_match_index = similarity_scores.argmax()
    best_match = corpus[best_match_index]
    return best_match


best_matches = []
for query in list_a:
    best_match = calculate_cosine_similarity(query, list_b)
    best_matches.append(best_match)

for query, best_match in zip(list_a, best_matches):
    print(f"Query: {query}")
    print(f"Best Match: {best_match}")
    print("---")
