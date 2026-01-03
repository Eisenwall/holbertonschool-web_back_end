import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(s, f) {
    super(s);
    this._floors = f;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
