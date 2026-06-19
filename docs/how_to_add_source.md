# How to Add a New Source

## Step 1: Prepare the File

- Source must be the **verbatim original** text (transcript, post text, interview)
- Do NOT add AI summaries or paraphrased versions
- Name the file following `operating_system/source_naming_rules.md`:
  ```
  [TYPE]-[YYYY-MM-DD]-[slug].[ext]
  ```

## Step 2: Place in Correct Directory

| Source Type | Directory |
|---|---|
| YouTube transcript | `raw_sources/youtube_transcripts/` |
| Public community post | `raw_sources/community_posts/` |
| Paid community post | `raw_sources/paid_posts/` |
| Other | `raw_sources/other/` |

## Step 3: Run Update Protocol

```bash
pip install -r automation/requirements.txt
python automation/run_update_protocol.py
```

## Step 4: Review the Outputs

- Check `knowledge/04_Akshat_Recent_Changes.md` for any new entries
- Check `knowledge/02_Akshat_Principle_Frequency_Table.md` for count increments
- Check `changelog/entries/` for the new entry

## Step 5: Commit

```bash
git add raw_sources/ knowledge/ changelog/
git commit -m "source: add [SOURCE-ID] — [title]"
git push
```

## Critical Reminders

- NEVER add AI-generated content to `raw_sources/`
- NEVER edit `01_Akshat_Master_System.md` manually without running `scripts/promote_to_master.py`
- ONE source = ONE count in the Frequency Table
