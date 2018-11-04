"""Helper functions to format and search meds and rxs"""

def get_generics(medications, active_only=None):
    """Given a list of medications, generate a dictionary of generic meds keyed by rxcui.
    If active_only is True, only include active medications.
    Return value: { rxcui:[med_id_1] }
    """
    generics = dict()
    for medication in medications:
        if (medication['generic'] == True
                and (not active_only
                     or (active_only and medication['active'] == True))):
            if medication['rxcui'] in generics:
                generics[medication['rxcui']].append(medication['id'])
            else:
                generics[medication['rxcui']] = [medication['id']]
    return generics

def get_medications_by_id(medications):
    """ Turn a list of meds into a hash table keyed by med id"""
    medications_by_id = dict()
    for medication in medications:
        medications_by_id[medication['id']] = medication
    return medications_by_id

def get_prescription_updates(medications, prescriptions):
    """Find prescriptions for brand-name meds with active, generic alternatives.
    Return a list of prescription ids and corresponding medication ids to update.
    """
    generics = get_generics(medications, active_only=True)
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

