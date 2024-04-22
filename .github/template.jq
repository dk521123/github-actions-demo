{
  source: {
    name: "sqlfluff",
    url: "https://github.com/sqlfluff/sqlfluff"
  },
  severity: "ERROR",
  diagnostics: (. // {}) | map(. as $file | $file.violations[] as $violation | (if $file.violations[].warning == true then "WARNING" else "ERROR" end) as $severity | {
    message: "[\($violation.name)] - \($violation.description)",
    location: {
      path: $file.filepath,
      range: {
        start: {
          line: $violation.start_line_no,
          column: $violation.start_line_pos
        },
        end: {
          line: $violation.end_line_no,
          column: $violation.end_line_pos
        },
      }
    },
    suggestions: ([$violation.fixes[] as $suggestion | {
      range: {
        start: {
          line: $suggestion.start_line_no,
          column: $suggestion.start_line_pos
        },
        end: {
          line: $suggestion.end_line_no,
          column: $suggestion.end_line_pos
        }
      },
      text: $suggestion.edit
    }]),
    severity: $severity,
    code: {
      value: $violation.code,
      url: "https://docs.sqlfluff.com/en/stable/rules.html#rule-\($violation.code)"
    },
  })
}
