{
  source: {
    name: "sqlfluff",
    url: "https://github.com/sqlfluff/sqlfluff"
  },
  diagnostics: (. // {}) | map(. as $file | $file.violations[] as $violation | {
    message: $violation.name - $violation.description,
    code: {
      value: $violation.code,
      url: "https://docs.sqlfluff.com/en/stable/rules.html#rule-\($violation.code)"
    },
    location: {
      path: $file.filepath,
      range: {
        start: {
          line: $violation.start_line_no,
          column: $violation.start_line_pos
        },
        ende: {
          line: $violation.end_line_no,
          column: $violation.end_line_pos
        },
      }
    },
    severity: "WARNING",
  })
}
