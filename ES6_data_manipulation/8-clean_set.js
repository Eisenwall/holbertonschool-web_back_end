export default function cleanSet(set, startString = '') {
  // If startString is empty, return an empty string, or process as usual
  if (startString === '') {
    return '';
  }
  
  // Filter values that start with startString
  const result = [...set]
    .filter(value => typeof value === 'string' && value.startsWith(startString))  // Ensure value is a string and starts with startString
    .map(value => value.slice(startString.length))  // Remove startString from the value
    .join('-');  // Join the remaining parts with '-'

  return result;
}
