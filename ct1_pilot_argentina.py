"""
CT1 Pilot: Argentina Narrative Stability Test
Tests hypothesis: Ideologically opposed governments converge on labor/social topics
"""

import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime

# Target speeches with known high relevance
TARGET_SPEECHES = {
    'Menem': [
        {
            'title': 'Mensaje presidencial apertura sesiones ordinarias',
            'year': 1994,
            'keywords': ['sesiones', 'ordinarias', '1994']
        },
        {
            'title': 'Discurso reforma laboral',
            'year': 1995,
            'keywords': ['laboral', 'trabajo', '1995']
        },
        {
            'title': 'Mensaje presidencial',
            'year': 1996,
            'keywords': ['mensaje', 'presidencial', '1996']
        }
    ],
    'Kirchner': [
        {
            'title': 'Discurso asunción presidencial',
            'year': 2003,
            'keywords': ['asunción', '2003', 'mayo']
        },
        {
            'title': 'Mensaje apertura sesiones',
            'year': 2004,
            'keywords': ['sesiones', '2004', 'marzo']
        },
        {
            'title': 'Discurso justicia social',
            'year': 2005,
            'keywords': ['trabajo', 'social', '2005']
        }
    ],
    'Macri': [
        {
            'title': 'Discurso asunción',
            'year': 2015,
            'keywords': ['asunción', '2015', 'diciembre']
        },
        {
            'title': 'Mensaje apertura sesiones',
            'year': 2017,
            'keywords': ['sesiones', '2017', 'marzo']
        },
        {
            'title': 'Presentación reforma laboral',
            'year': 2017,
            'keywords': ['laboral', 'reforma', '2017']
        }
    ],
    'Milei': [
        {
            'title': 'Discurso asunción',
            'year': 2023,
            'keywords': ['asunción', '2023', 'diciembre']
        }
    ]
}

def create_execution_plan():
    """Create detailed execution plan for CT1 pilot"""
    
    plan = {
        'test_name': 'CT1 Argentina Pilot',
        'hypothesis': 'Narrative stability across ideologically opposed governments',
        'governments': ['Menem (liberal)', 'Kirchner (statist)', 'Macri (pro-market)', 'Milei (libertarian)'],
        'expected_result': 'Average correlation >0.55 on labor/social topics',
        'timeline': '2-3 hours execution',
        'deliverable': '2-page report with correlation matrix',
        'target_speeches': TARGET_SPEECHES,
        'methodology': {
            'step1': 'Scrape 10 speeches from Casa Rosada archive',
            'step2': 'Preprocess: Spanish stopwords, lemmatization (spaCy)',
            'step3': 'Topic modeling: LDA n_topics=20',
            'step4': 'Identify core topics: labor, social protection, state role',
            'step5': 'Calculate inter-government correlations',
            'step6': 'Interpret: >0.55 = tacit consensus confirmed'
        },
        'fallback': 'If scraping fails, request speeches from Adrian (6-8h delivery)'
    }
    
    return plan

# Create and save execution plan
plan = create_execution_plan()

with open('CT1_PILOT_EXECUTION_PLAN.json', 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)

print("=== CT1 PILOT ARGENTINA - EXECUTION PLAN ===\n")
print(f"Test: {plan['test_name']}")
print(f"Hypothesis: {plan['hypothesis']}")
print(f"\nGovernments to test:")
for gov in plan['governments']:
    print(f"  - {gov}")
print(f"\nExpected result: {plan['expected_result']}")
print(f"Timeline: {plan['timeline']}")
print(f"\n✓ Execution plan saved to CT1_PILOT_EXECUTION_PLAN.json")

# Test Casa Rosada access
print("\n=== TESTING CASA ROSADA ACCESS ===")
try:
    response = requests.get('https://www.casarosada.gob.ar/informacion/discursos', timeout=10)
    if response.status_code == 200:
        print(f"✓ Casa Rosada archive accessible (HTTP {response.status_code})")
        print(f"✓ Page size: {len(response.content)} bytes")
        print("✓ Ready to proceed with scraping")
    else:
        print(f"⚠ Unexpected status: HTTP {response.status_code}")
        print("⚠ May require fallback strategy")
except Exception as e:
    print(f"✗ Access error: {str(e)}")
    print("✗ Will need speeches from Adrian")

