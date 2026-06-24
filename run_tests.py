import json
import subprocess
import os

tests = [
    {"name": "Semiconductor incentives", "text": "Government launches major semiconductor manufacturing incentives."},
    {"name": "Defense indigenization", "text": "New policy pushes rapid defense indigenization."},
    {"name": "Nuclear incentives", "text": "Govt subsidizes nuclear energy capex."},
    {"name": "Logistics corridors", "text": "Massive funding approved for new logistics corridors."},
    {"name": "Hospital expansion", "text": "Private hospital expansion into tier 2 cities surges."},
    {"name": "Data center growth", "text": "Hyperscaler data center growth consumes the power grid."},
    {"name": "Power grid upgrades", "text": "Federal mandate requires total power grid upgrades."},
    {"name": "Water infrastructure", "text": "Billions allocated for water infrastructure repair."},
    {"name": "Robotics adoption", "text": "Rapid robotics adoption drives factory efficiency."},
    {"name": "Unknown industry", "text": "Breakthrough in dyson sphere construction technology."}
]

with open('docs/sector_test_results.md', 'w') as out_f:
    out_f.write("# MVP Sector Discovery 10 Macro-Event Tests\n\n")

    for i, t in enumerate(tests):
        # write event to sample json
        with open('sample_macro_event.json', 'w') as f:
            json.dump({"event_id": f"TEST-{i}", "raw_text": t["text"]}, f)

        # run collide
        subprocess.run(["python", "2_collide.py"])

        # read output
        with open("generated_framework_report.md", "r") as f:
            output = f.read()

        # extract sections
        lines = output.split('\n')
        input_event = t["text"]

        try:
            ap_start = lines.index("## Activated Principles") + 1
            ap_end = lines.index("## Generated Framework")
            activated = "\n".join(lines[ap_start:ap_end]).strip()

            gf_start = ap_end + 1
            sec_start = lines.index("## Affected Sectors")
            framework = "\n".join(lines[gf_start:sec_start]).strip()

            sec_end = len(lines)
            sectors = "\n".join(lines[sec_start+1:sec_end]).strip()
        except ValueError:
            activated = "Parse Error"
            framework = "Parse Error"
            sectors = "Parse Error"

        failure_analysis = "Success." if "No sectors identified." not in sectors and "No actionable principles" not in framework else "Failed to map tags to principles/sectors due to hardcoded mapping limits."

        out_f.write(f"### Test {i+1}: {t['name']}\n")
        out_f.write(f"**Input:** {input_event}\n\n")
        out_f.write(f"**Activated principles:**\n{activated}\n\n")
        out_f.write(f"**Generated framework:**\n{framework}\n\n")
        out_f.write(f"**Affected Sectors:**\n{sectors}\n\n")
        out_f.write(f"**Failure analysis:** {failure_analysis}\n\n")
        out_f.write("---\n\n")
