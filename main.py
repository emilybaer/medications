"""Find prescriptions requiring generics medication updates"""
import api
import json
import medication

def main():
    """Query PillPack API for medications and prescriptions.
    Find prescriptions that need updating.
    """
    pillpack_api = api.PillPackAPI()
    medications = pillpack_api.get_medications()
    prescriptions = pillpack_api.get_prescriptions()

    updates = {
        'prescription_updates': medication.get_prescription_updates(
            medications,
            prescriptions
        )
    }

    prescription_updates_json = json.dumps(updates)

    f = open("updates.json", "w+")
    f.write(prescription_updates_json)

    print('medications: {}'.format(len(medications)))
    print('prescriptions: {}'.format(len(prescriptions)))
    print('updates: {}'.format(len(updates['prescription_updates'])))

main()
