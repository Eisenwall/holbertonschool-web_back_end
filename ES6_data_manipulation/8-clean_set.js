export default function cleanSet(set, startString) {
  // If startString is not a string, return an empty string
  if (typeof startString !== 'string') {
    return '';
  }

  // Filter values that start with startString
  const result = [...set]
    .filter(value => typeof value === 'string' && value.startsWith(startString)) // Ensure value is a string and starts with startString
    .map(value => value.slice(startString.length)) // Remove startString from the value
    .join('-'); // Join the remaining parts with '-'

  return result;
}
