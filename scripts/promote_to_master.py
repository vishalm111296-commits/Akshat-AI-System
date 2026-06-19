#!/usr/bin/env python3
import argparse, os

FREQ='knowledge/02_Akshat_Principle_Frequency_Table.md'

def generate_evidence_report(pid):
    print('='*60)
    print(f'PROMOTION REVIEW: {pid}')
    print('='*60)
    if os.path.exists(FREQ):
        print(f'Review frequency evidence in: {FREQ}')
    print('Checklist:')
    print('- 8+ independent sources')
    print('- 2+ time periods')
    print('- No contradiction')
    print('- Not already in Master System')
    print('If all conditions pass, create PR and update Master System manually.')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--principle',required=True)
    a=p.parse_args()
    generate_evidence_report(a.principle)