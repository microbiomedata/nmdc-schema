from datetime import datetime

current_datetime = datetime.utcnow().replace(microsecond=0).isoformat()

print(f"""

[ ] <https://schema.org/dateCreated> "{current_datetime}"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
    <http://www.w3.org/2000/01/rdf-schema#comment> "https://api.microbiomedata.org" . 
""")
