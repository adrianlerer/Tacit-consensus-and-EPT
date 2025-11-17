# Read the outline file
with open('OUTLINE_COMPLETE.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find section boundaries (0-indexed, so subtract 1 from line numbers reported)
section_iv_start = 437  # Line 438 in file (## IV. COMPARATIVE ANALYSIS)
argentina_start = 439   # Line 440 (### A. Argentina)
chile_start = 510       # Line 511 (### B. Chile)
uruguay_start = 561     # Line 562 (### C. Uruguay)
synthesis_start = 619   # Line 620 (### D. Synthesis)

# Extract sections
before_iv = lines[:section_iv_start]
iv_header = lines[section_iv_start:argentina_start]
argentina_section = lines[argentina_start:chile_start]
chile_section = lines[chile_start:uruguay_start]
uruguay_section = lines[uruguay_start:synthesis_start]
after_synthesis = lines[synthesis_start:]

# Add pedagogical note after Section IV header
pedagogical_note = """\n**Pedagogical strategy:** Begin with "baseline" case (Chile: low lock-in, reforms possible) to establish comparison standard; proceed to "extreme" case (Argentina: high lock-in, reforms impossible) for dramatic contrast; conclude with "intermediate" case (Uruguay: moderate lock-in, incremental reforms) to demonstrate gradient pattern.\n\n"""

# Reorder: Chile (A) -> Argentina (B) -> Uruguay (C) -> Synthesis (D)
# Change section labels
chile_section[0] = chile_section[0].replace('### B. Chile:', '### A. Chile:')
argentina_section[0] = argentina_section[0].replace('### A. Argentina:', '### B. Argentina:')
# Uruguay stays C, Synthesis stays D

# Reconstruct file
new_lines = (
    before_iv +
    iv_header[:1] +  # Just the ## IV. line
    [pedagogical_note] +
    chile_section +
    argentina_section +
    uruguay_section +
    after_synthesis
)

# Write new version
with open('OUTLINE_COMPLETE.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Sections reordered successfully!")
print(f"New order: Chile (A) -> Argentina (B) -> Uruguay (C) -> Synthesis (D)")
