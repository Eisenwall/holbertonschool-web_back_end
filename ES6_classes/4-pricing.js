import Currency from './3-currency.js';

export default class Pricing {
  constructor(a, c) {
    this.amount = a;
    this.currency = c;
  }

  get amount() {
    return this._amount;
  }

  set amount(v) {
    if (typeof v !== 'number') throw new TypeError();
    this._amount = v;
  }

  get currency() {
    return this._currency;
  }

  set currency(v) {
    if (!(v instanceof Currency)) {
      throw new TypeError();
    }
    this._currency = v;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(a, r) {
    return a * r;
  }
}
