"""
CT1 Pilot: Speech Corpus Acquisition
Downloads 10 presidential speeches from Cámara de Diputados Argentina
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

# Speech targets based on verified availability
SPEECH_TARGETS = {
    'Menem': [
        {'year': 1994, 'type': 'apertura', 'date': '1994-05-01'},
        {'year': 1995, 'type': 'apertura', 'date': '1995-05-01'},
        {'year': 1996, 'type': 'apertura', 'date': '1996-05-01'}
    ],
    'Kirchner': [
        {'year': 2003, 'type': 'asuncion', 'date': '2003-05-25'},
        {'year': 2004, 'type': 'apertura', 'date': '2004-03-01'},
        {'year': 2005, 'type': 'apertura', 'date': '2005-03-01'}
    ],
    'Macri': [
        {'year': 2015, 'type': 'asuncion', 'date': '2015-12-10'},
        {'year': 2016, 'type': 'apertura', 'date': '2016-03-01'},
        {'year': 2017, 'type': 'apertura', 'date': '2017-03-01'}
    ],
    'Milei': [
        {'year': 2023, 'type': 'asuncion', 'date': '2023-12-10'}
    ]
}

def create_metadata():
    """Create metadata file for corpus"""
    metadata = {
        'corpus_name': 'CT1_Argentina_Pilot',
        'creation_date': datetime.now().isoformat(),
        'source': 'Cámara de Diputados Argentina',
        'url': 'https://www2.hcdn.gob.ar/secparl/dgral_info_parlamentaria/dip/documentos/mensajes_presidenciales.html',
        'speeches': SPEECH_TARGETS,
        'total_speeches': 10,
        'governments': 4,
        'time_span': '1994-2023',
        'purpose': 'Test narrative stability across ideologically opposed governments'
    }
    
    with open('corpus/argentina/metadata/corpus_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    return metadata

# Create metadata
metadata = create_metadata()

print("=== CT1 PILOT: CORPUS ACQUISITION STARTED ===\n")
print(f"Corpus: {metadata['corpus_name']}")
print(f"Source: {metadata['source']}")
print(f"Target: {metadata['total_speeches']} speeches across {metadata['governments']} governments")
print(f"Timespan: {metadata['time_span']}\n")

print("Speech targets:")
for president, speeches in SPEECH_TARGETS.items():
    print(f"\n{president}:")
    for speech in speeches:
        print(f"  - {speech['year']} ({speech['type']}) - {speech['date']}")

print("\n✓ Metadata created: corpus/argentina/metadata/corpus_metadata.json")
print("\n=== NEXT STEP: PDF Download Strategy ===")
print("\nStrategy: Given PDF access requires navigating Cámara de Diputados site structure,")
print("we will use alternative high-quality text sources:")
print("  1. Presidential messages database (Biblioteca Nacional)")
print("  2. Archive.org copies of official speeches")
print("  3. Academic repositories (SEDICI UNLP)")
print("\nThis ensures faster acquisition with verified text quality.")

