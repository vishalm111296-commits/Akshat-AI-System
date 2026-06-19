#!/usr/bin/env python3
"""
Improved update protocol.
Updates Recent Changes and Frequency Table placeholders when new sources arrive.
Never edits Master System.
"""
import os, json, hashlib
from datetime import datetime

STATE_FILE='.automation_state/processed_sources.json'
RAW='raw_sources'
FREQ='knowledge/02_Akshat_Principle_Frequency_Table.md'
RECENT='knowledge/04_Akshat_Recent_Changes.md'

os.makedirs('.automation_state', exist_ok=True)

def load_state():
    return json.load(open(STATE_FILE)) if os.path.exists(STATE_FILE) else {}

def save_state(s):
    json.dump(s, open(STATE_FILE,'w'), indent=2)

def file_hash(p):
    return hashlib.md5(open(p,'rb').read()).hexdigest()

def source_files():
    out=[]
    for r,_,fs in os.walk(RAW):
        for f in fs:
            if not f.startswith('.'):
                out.append(os.path.join(r,f))
    return out

def append_line(path,line):
    if os.path.exists(path):
        with open(path,'a',encoding='utf-8') as f:
            f.write('\n'+line)

state=load_state()
new=[]
for f in source_files():
    h=file_hash(f)
    if h not in state:
        new.append(f)
        state[h]={'file':f,'processed':datetime.now().isoformat()}

if new:
    stamp=datetime.now().strftime('%Y-%m-%d')
    append_line(RECENT,f'- {stamp}: {len(new)} new source(s) detected by automation')
    append_line(FREQ,f'| AUTO-{stamp} | Pending Human Classification | {len(new)} |')

save_state(state)
print(f'Processed {len(new)} new files. Master System protected.')