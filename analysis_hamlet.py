import nltk
from collections import Counter

# 1. POBIERANIE TEKSTU (Zmienione na Makbeta)
nltk.download('gutenberg', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Ładujemy oryginalny tekst "Makbeta" Szekspira
raw_text = nltk.corpus.gutenberg.raw('shakespeare-macbeth.txt')

# 2. CZYSZCZENIE I DZIELENIE (Tokenizacja)
words = nltk.word_tokenize(raw_text.lower())

# 3. FILTROWANIE "SZUMU" JĘZYKOWEGO
stop_words = set(nltk.corpus.stopwords.words('english'))

# Dodaliśmy 'witch' do filtrów, żeby zobaczyć inne słowa niosące treść
custom_noise = {'.', ',', ':', ';', '?', '!', "'s", '--', 'thou', 'thee', 'thy', 'shall', 'haue', 'lord', 'witch'}
full_filter = stop_words.union(custom_noise)

meaningful_words = [w for w in words if w.isalpha() and w not in full_filter]

# 4. STATYSTYKA LOGICZNA (Liczenie "stada")
word_counts = Counter(meaningful_words)

# Wyświetlamy 15 najpopularniejszych słów dla Makbeta
print("=== 15 NAJWAŻNIEJSZYCH SŁÓW W 'MAKBECIE' ===")
for word, count in word_counts.most_common(15):
    print(f"{word.capitalize()}: {count} razy")
