// full_server/controllers/StudentsController.js
import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const dbFile = process.argv[2];
    try {
      const data = await readDatabase(dbFile);
      let output = 'This is the list of our students\n';
      Object.keys(data)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
        .forEach((field) => {
          const { [field]: students } = data;
          output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        });
      res.status(200).send(output.trim());
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbFile = process.argv[2];
    const { major } = req.params;
    if (!['CS', 'SWE'].includes(major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const data = await readDatabase(dbFile);
      const { [major]: students } = data;
      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }
}
