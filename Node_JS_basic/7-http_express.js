const express = require('express');
const fs = require('fs');

const app = express();
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      let output = `Number of students: ${students.length}\n`;
      for (const field of Object.keys(fields)) {
        output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  const dbFile = process.argv[2];
  let responseText = 'This is the list of our students\n';
  try {
    const studentsInfo = await countStudents(dbFile);
    responseText += studentsInfo;
    res.send(responseText);
  } catch (err) {
    res.send(err.message);
  }
});
app.listen(1245);

module.exports = app;
