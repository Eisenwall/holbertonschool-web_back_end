export default class Airport {
  constructor(n, c) {
    this._name = n;
    this._code = c;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
