"""Helper functions to format and search meds and rxs"""

def get_generics(medications, active_only=None):
    generics = dict()
    for medication in medications:
        if (medication['generic'] == True 
            and (not active_only or 
            (active_only and medication['active'] == True))):
            # If this is a generic med and it's an active med 
            # if we're looking for only active meds, 
            # then we need to add it to the list of generics
            if medication['rxcui'] in generics:
                generics[medication['rxcui']].append(medication['id'])
            else:
                generics[medication['rxcui']] = [medication['id']]
    return generics

def get_medications_by_id(medications):
    medications_by_id = dict()
    for medication in medications:
        medications_by_id[medication['id']] = medication
    return medications_by_id

def get_prescription_updates(medications, prescriptions):
    generics = get_generics(medications)
    medications_by_id = get_medications_by_id(medications)
    updates = []
    for prescription in prescriptions:
        medication_id = prescription['medication_id']
        medication = None
        if medication_id in medications_by_id:
            medication = medications_by_id[medication_id]
        if medication and not medication['generic']:
            rxcui = medication['rxcui']
            if rxcui in generics:
                updates.append({
                    'prescription_id': prescription['id'],
                    'medication_id': generics[rxcui][0]
                })
    return updates

