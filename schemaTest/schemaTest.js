const Ajv = require('ajv');
const fs = require('fs');

const ajv = new Ajv({ allErrors: true });

// Load in schemas and examples
const rawSchema = fs.readFileSync("../schema/visualization.schema.json", "utf8")
const schema = JSON.parse(rawSchema);
const raw1 = fs.readFileSync('../schemaExamples/example1.json', "utf8");
const example1 = JSON.parse(raw1, 'utf8');
const raw2 = fs.readFileSync('../schemaExamples/example2.json', "utf8");
const example2 = JSON.parse(raw2, 'utf8');

// Generate validating function for our schema
const validate = ajv.compile(schema);

const valid1 = validate(example1);
if (valid1) {
  console.log("Example 1 is valid!");
} else {
  console.log("Example 1 is invalid.");
}

const valid2 = validate(example2);
if (valid2) {
  console.log("Example 2 is valid!");
} else {
  console.log("Example 2 is invalid.");
}