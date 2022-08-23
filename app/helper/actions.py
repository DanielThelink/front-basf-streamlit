from fuzzywuzzy import process

ACTIONS_PER_WORD = {
    "Contact" : "Get In Touch With The Client to Undestand Better The Problem",
    "Offers" : "Make Offers To Client",
    "Attendance" : "Offer Another Type of Attendance/Delivery",
    "Product" : "Offer Another Product",
}

ACTIVATION_WORDS = {
    "Contact" : ["more", "unsatisfied", "expectation", "businesses", "canceling", "order", "commitments", "damaged"],
    "Offers" : ["expensive", "mistaken", "amount", "pricing"],
    "Attendance" : ["delayed", "waiting", "reply", "delivery", "shipment"],
    "Product" : ["demonstration", "product", "availability", "lack"]
}

GLOBAL_WORDS = [
    *ACTIVATION_WORDS["Contact"],
    *ACTIVATION_WORDS["Offers"],
    *ACTIVATION_WORDS["Attendance"],
    *ACTIVATION_WORDS["Product"],
]

def get_action_by_commentary(text : str, status : str) -> str:

    if status == 'Promotor':
        return None

    process_result = process.extractOne(text, GLOBAL_WORDS)
    
    word_to_action = "Contact"

    for key, value in ACTIVATION_WORDS.items():
        if process_result[0] in value:
            word_to_action = key
    
    return ACTIONS_PER_WORD[word_to_action]

