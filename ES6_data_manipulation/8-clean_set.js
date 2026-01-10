export default function cleanSet(set, startString = '') {
  const result = [...set]
    .filter(value => typeof value === 'string' && value.startsWith(startString))  // Check that the value is a string
    .map(value => value.slice(startString.length))  // Remove startString from the value
    .join('-');  // Join the results with '-'

  return result;
}
