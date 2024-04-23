import subprocess

num_iterations = 100 

# Loop to run the script multiple times 
for i in range(num_iterations):
    # Run the script using subprocess 
    subprocess.run(["python3", "dsgn-data-collection.py"])
    print(f"Iteration {i + 1} completed! ")

print("All iterations complete")