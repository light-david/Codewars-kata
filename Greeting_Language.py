#Defines greet function and takes one parameter
def greet(language):
    #Creates a Hash map to store the languages
    language_sets = { "english" : "Welcome",
                     "czech" : "Vitejte",
                     "danish" : "Velkomst",
                     "dutch" : "Welkom",
                     "estonian" : "Tere tulemast",
                     "finnish" : "Tervetuloa",
                     "flemish" : "Welgekomen",
                     "french" : "Bienvenue",
                     "german" : "Willkommen",
                     "irish" : "Failte",
                     "italian" : "Benvenuto",
                     "latvian" : "Gaidits",
                     "lithuanian" : "Laukiamas",
                     "polish" : "Witamy",
                     "spanish" : "Bienvenido",
                     "swedish" : "Valkommen",
                     "welsh" : "Croeso"
                    }
    
    #Checks if the argument is in the hashmap
    if language in language_sets:
        #Returns the appropiate greeting
        return language_sets[language]
    #Returns the English greeting as the defualt greeting
    return language_sets["english"]
