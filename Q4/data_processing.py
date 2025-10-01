import csv

# Input file name

input_file=input("Enter the input file name")
output_file = input("Enter the name for the output csv file")

input_file=input_file + ".csv" 
output_file=output_file + ".csv" 
# Events of interest
features = [
    "cpu_core/br_misp_retired.all_branches/",
    "cpu_core/iTLB-load-misses/",
    "cpu_core/dTLB-load-misses/",
    "cpu_core/l2_rqsts.miss/",
    "cpu_core/L1-icache-load-misses/",
    "cpu_core/L1-dcache-load-misses/",
    "cpu_core/mem_load_retired.l3_miss/"
]

data = []
y_vals = []

# Read the raw data
with open(input_file, "r") as f:
    reader = csv.reader(f)
    current_row = {}
    for row in reader:

        event = row[3].strip()
        value = row[1].strip()

        
        if "insn per cycle" in row[7]: #to check if this has the instruction per cycle.
            ins_per_cycle = float(row[6])
            y_vals.append(1.0 / ins_per_cycle) #appeding the CPI value
            
            # Append the collected feature row
            #data.append([current_row.get(feat, 0) for feat in features])
            X_val=[]	
            for feat in features:
                X_val.append(current_row.get(feat, 0))	
	    
            data.append(X_val) 	

            current_row = {}  # reset for next sample
        elif event in features:
            current_row[event] = int(value)

# Write to CSV
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(["X", "Y"])
    for x_row, y in zip(data, y_vals):
        writer.writerow([x_row, y])

print(f"Processed data saved to {output_file}")

