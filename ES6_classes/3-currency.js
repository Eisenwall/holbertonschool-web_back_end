export default class Currency {
  constructor(c, n) {
    this.code = c;
    this.name = n;
  }

  get code() {
    return this._code;
  }

  set code(v) {
    if (typeof v !== 'string') throw new TypeError('Code must be a string');
    this._code = v;
  }

  get name() {
    return this._name;
  }

  set name(v) {
    if (typeof v !== 'string') throw new TypeError('Name must be a string');
    this._name = v;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
