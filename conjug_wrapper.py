import mlconjug
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

class Conjug:
    # static methods
    __conjugator = mlconjug.Conjugator(language='es')
    __tense = "Indicativo pretérito perfecto simple"
    __record = {}

    # enum wasn't working the way i expected
    first_singular = "1s"
    second_singular = "2s"
    third_singular = "3s"
    first_plural = "1p"
    second_plural = "2p"
    third_plural = "3p"

    abbrev = {first_singular: "me ", second_singular: "te ", third_singular: "se ", first_plural: "nos ", second_plural: "os ", third_plural: "se "}

    def __init__(self):
        pass

    def get(self, part_of_speech: str, infinitive: str) -> str:
        if infinitive.lower() in Conjug.__record:
            if Conjug.__record[infinitive][0] == part_of_speech.lower():
                return Conjug.__record[infinitive][1]

        og_verb = infinitive

        contains = infinitive[len(infinitive)-2:len(infinitive)] == "se"

        if contains:
            infinitive = infinitive[0:len(infinitive)-2]

        if infinitive == "pasar":
            if part_of_speech == Conjug.first_singular:
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), ("me " if contains else "") + "pasé")})
                return ("me " if contains else "") + "pasé"
            elif part_of_speech == Conjug.second_singular:
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), ("te " if contains else "") + "pasaste")})
                return ("te " if contains else "") + "pasaste"
            elif part_of_speech == Conjug.third_singular:
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), ("se " if contains else "") + "pasó")})
                return ("se " if contains else "") + "pasó"
            elif part_of_speech == Conjug.first_plural:
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), ("nos " if contains else "") + "pasamos")})
                return ("nos " if contains else "") + "pasamos"
            elif part_of_speech == Conjug.second_plural:
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), ("os " if contains else "") + "pasasteis")})
                return ("os " if contains else "") + "pasasteis"
            elif part_of_speech == Conjug.third_plural:
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), ("se " if contains else "") + "pasaron")})
                return ("se " if contains else "") + "pasaron"
        
        print(infinitive)
        iteratable = Conjug.__conjugator.conjugate(infinitive).iterate()
    
        for conjugation in iteratable:
            if conjugation[1] == Conjug.__tense and conjugation[2] == part_of_speech:
                correct = (Conjug.abbrev[part_of_speech] if contains else "") + conjugation[3]
                Conjug.__record.update({og_verb.lower() : (part_of_speech.lower(), correct.lower())})
                return correct