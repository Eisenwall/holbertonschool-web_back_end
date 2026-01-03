export default class Building {
  constructor(s) {
    this._sqft = s;

    if (new.target !== Building
      && this.evacuationWarningMessage === undefined) {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage'
      );
    }
  }

  get sqft() {
    return this._sqft;
  }
}
