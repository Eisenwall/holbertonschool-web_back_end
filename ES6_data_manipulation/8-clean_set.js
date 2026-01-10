export default function cleanSet(set, startString) {
  // Filter values that start with startString
  const result = [...set]
    .filter(value => value.startsWith(startString))  // Only include values that start with startString
    .map(value => value.slice(startString.length))   // Remove startString from the value
    .join('-');  // Join the remaining parts with '-'

  return result;
}
