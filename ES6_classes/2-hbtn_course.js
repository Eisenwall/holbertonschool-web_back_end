export default class HolbertonCourse {
  constructor(n, l, s) {
    this.name = n;
    this.length = l;
    this.students = s;
  }

  get name() {
    return this._name;
  }

  set name(v) {
    if (typeof v !== 'string') throw new TypeError('Name must be a string');
    this._name = v;
  }

  get length() {
    return this._length;
  }

  set length(v) {
    if (typeof v !== 'number') throw new TypeError('Length must be a number');
    this._length = v;
  }

  get students() {
    return this._students;
  }

  set students(v) {
    if (!Array.isArray(v) || v.some(e => typeof e !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = v;
  }
}
