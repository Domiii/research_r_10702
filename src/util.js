/**
 * Google Apps script is full of "iterators". Not very handy.
 */
export function iterToArray(iter) {
  const arr = [];
  while (iter.hasNext()) {
    arr.push(iter.next());
  }
  return arr;
}