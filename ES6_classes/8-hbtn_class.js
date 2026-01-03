export default class HolbertonClass {
  constructor(s, l) {
    this._size = s;
    this._location = l;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this._size;
    return this._location;
  }
}
