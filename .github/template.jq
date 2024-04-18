{
  source: {
    name: "sqlfluff",
    url: "https://github.com/sqlfluff/sqlfluff"
  },
  severity: "WARNING",
  diagnostics: (. // {}) | map(. as $file | $file.violations[] as $violation | {
    message: $violation.description,
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
    severity: "WARNING",
    code: {
      value: $violation.code,
      url: "https://docs.sqlfluff.com/en/stable/rules.html#rule-\($violation.code)"
    },
  })
}
