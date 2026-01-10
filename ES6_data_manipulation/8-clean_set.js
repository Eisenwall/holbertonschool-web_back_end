export default function cleanSet(set, startString) {
  const result = [...set]
    .filter(value => value.startsWith(startString)) // Filter values starting with startString
    .map(value => value.slice(startString.length))  // Remove startString from the value
    .join('-'); // Join the results with '-'

  return result;
}
