const test = require('node:test');
const assert = require('assert');
const fs = require('fs');
const Ajv = require('ajv');

const ajv = new Ajv({ allErrors: true });

const schema = JSON.parse(
  fs.readFileSync('schema/visualization.schema.json', 'utf8')
);

const example1 = JSON.parse(
  fs.readFileSync('schemaExamples/example1.json', 'utf8')
);

const example2 = JSON.parse(
  fs.readFileSync('schemaExamples/example2.json', 'utf8')
);

test('example1 is valid', () => {
  const validate = ajv.compile(schema);
  const valid = validate(example1);
  assert.ok(
    valid,
    'example1.json should be valid. Errors:\n' +
      JSON.stringify(validate.errors, null, 2)
  );
});

test('example2 is valid', () => {
  const validate = ajv.compile(schema);
  const valid = validate(example2);
  assert.ok(
    valid,
    'example2.json should be valid. Errors:\n' +
      JSON.stringify(validate.errors, null, 2)
  );
});
