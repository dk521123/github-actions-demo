import json
import sys


def get_severity(is_warning):
  return "WARNING" if is_warning else "ERROR"

def main(input_file, output_file):
  # Step1: Read JSON
  with open(input_file, "r") as in_file:
    input_json_dict = json.load(in_file)

  # Step2: Convert
  diagnostics = {}
  has_error = False
  for input in input_json_dict:
    path = input.get("filepath")
    for violation in input.get("violations"):
      is_warning = violation.get("warning", True)
      if not is_warning:
        has_error = True
      severity = get_severity(is_warning)
      diagnostic = {
        "message": f"[{violation.get('name')}] - {violation.get('description')}",
        "location": {
          "path": path,
          "range": {
            "start": {
              "line": violation.get("start_line_no"),
              "column": violation.get("start_line_pos")
            },
            "end": {
              "line": violation.get("end_line_no"),
              "column": violation.get("end_line_pos")
            },
          }
        },
        "suggestions": suggestions,
        "severity": severity,
        "code": {
          "value": violation.get("code"),
          "url": f"https://docs.sqlfluff.com/en/stable/rules.html#rule-{violation.get('code')}"
        }
      }
      diagnostics.update(diagnostic)
  main_severity = get_severity(not has_error)

  output_json_dict = {
    "source": {
      "name": "sqlfluff",
      "url": "https://github.com/sqlfluff/sqlfluff"
    },
    "severity": main_severity,
    "diagnostics": diagnostics
  }

  # Step3: Write JSON
  with open(output_file, "w", newline='\n') as out_file:
    json.dump(output_json_dict, out_file)

if __name__ == "__main__":
  if len(sys.argv) > 3:
    print("[How to use]")
    print("  python convert.py input.json ouptput.json")
    print("   args1: Input file with json from SQLFluff (e.g. input.json)")
    print("   args2: Output file with json for reviewdog (e.g. ouptput.json)")
  else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
