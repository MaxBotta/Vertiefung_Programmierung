documents = [
   'Ich mache ihm ein Angebot, das er nicht ablehnen kann',
   'Ich habe Angst, Dave. Dave, ich verliere den Verstand. Ich kann es fühlen',
   'Meine Mutter sagte mir immer, es gibt keine Monster. Keine echten jedenfalls. Aber es gibt sie.',
   'Alles was du besitzt, besitzt irgendwann dich.',  
   'Louis, ich denke das ist der Beginn einer wunderbaren Freundschaft.',
]

def document_to_wordlist(document):
   document = document.lower()
   document = document.replace('.', '').replace(',', '')
   wordlist = document.split(' ')
   return wordlist

def count_same_words(wordlist_1, wordlist_2):
   same_words = 0
   for word in wordlist_1:
       if word in wordlist_2:
         same_words += 1
   return same_words

search = input('Bitte tippen Sie etwas, nach dem ich suchen soll:')
search_wordlist = document_to_wordlist(search)
print('Ich suche jetzt nach den Wörtern:', search_wordlist)

most_similar_document = 'Oh. Keines der Dokumente ähnelt Ihrer Eingabe...'
best_similarity = 0

for document in documents:
   document_wordlist = document_to_wordlist(document)
   same_words = count_same_words(search_wordlist, document_wordlist)
   similarity = same_words / len(document_wordlist)

   print('Ermittelte Ähnlichkeit: {}'.format(similarity))

   if similarity > best_similarity:
       most_similar_document = document
       best_similarity = similarity

print('Ähnlichstes Dokument:\t', most_similar_document)
print('Ermittelte Ähnlichkeit:\t {:.3f}'.format(best_similarity))
               
