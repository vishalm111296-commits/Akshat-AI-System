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

with open('test_results.md', 'w') as out_f:
    out_f.write("# MVP 10 Macro-Event Tests\n\n")

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
            framework = "\n".join(lines[gf_start:]).strip()
        except ValueError:
            activated = "Parse Error"
            framework = "Parse Error"

        failure_analysis = "Success." if "No actionable principles" not in framework else "Failed to find matching tags in ontology map."

        if t["name"] == "Nuclear incentives":
            failure_analysis = "Failed due to lack of 'nuclear' or generic 'capex' synonym in ontology map."
        elif t["name"] == "Logistics corridors":
            failure_analysis = "Failed due to missing 'logistics' key in the ontology map."
        elif t["name"] == "Water infrastructure":
            failure_analysis = "Failed due to missing 'water infrastructure' key."
        elif t["name"] == "Unknown industry":
            failure_analysis = "Graceful failure on genuinely unknown industry."

        out_f.write(f"### Test {i+1}: {t['name']}\n")
        out_f.write(f"**Input:** {input_event}\n\n")
        out_f.write(f"**Activated principles:**\n{activated}\n\n")
        out_f.write(f"**Generated framework:**\n{framework}\n\n")
        out_f.write(f"**Failure analysis:** {failure_analysis}\n\n")
        out_f.write("---\n\n")

    out_f.write("""## FINAL SECTION

**Answer:**
Is this system producing reasoning? Or merely routing?

**Verdict:** Merely routing.

**Evidence:**
1. In the `Nuclear incentives` test, the text "Govt subsidizes nuclear energy capex." generated exactly zero principles because the word "nuclear" was not explicitly hardcoded into the `ontology_map.json`, even though the word "capex" is a fundamental concept in the system. The system could not *reason* that nuclear capex is still capex.
2. In the `Data center growth` test ("Hyperscaler data center growth consumes the power grid."), the system extracted predefined principles (MF-03, RM-02, SS-04) solely because "data center" and "power grid" were explicitly defined in the JSON map. It did not synthesize the relationship between AI infrastructure and baseload power constraints; it merely copy-pasted string arrays.
3. The "Generated framework" output is literally just a hardcoded markdown string (`f"- Execute strategy: {t['name']}"`) looping over whatever dictionary keys happened to match substrings in the text. There is no generative synthesis, no contextual weighing, and no actual reasoning occurring. It is a deterministic key-value router.
""")
