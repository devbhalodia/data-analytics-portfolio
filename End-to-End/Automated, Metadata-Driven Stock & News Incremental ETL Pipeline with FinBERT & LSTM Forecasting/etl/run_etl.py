
import subprocess
import sys
import os

# Function to run a Python script and stop if it fails
def run_script(script_path):
    print(f"\nRunning {script_path} ...")
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        print(f"[ERROR] {script_path} failed. Exiting.")
        sys.exit(1)
    print(f"Finished {script_path}")

# Get the absolute path of the ETL folder
etl_folder = os.path.dirname(os.path.abspath(__file__))

# List scripts in order
scripts = [
    os.path.join(etl_folder, "extract.py"),
    os.path.join(etl_folder, "transform.py"),
    os.path.join(etl_folder, "load_mysql.py")  # make sure this points to your MySQL load script
]

# Run each script sequentially
for s in scripts:
    run_script(s)

print("\nETL pipeline completed successfully! Data is now in MySQL.")
