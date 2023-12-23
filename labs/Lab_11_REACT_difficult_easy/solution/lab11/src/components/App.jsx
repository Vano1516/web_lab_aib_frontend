import React, { useState } from 'react';
import './App.css';

const DAYS_IN_WEEK = 7;

const getDaysInMonth = (year, month) => new Date(year, month + 1, 0).getDate();

const generateCalendarMatrix = (year, month) => {
  const firstDayOfMonth = new Date(year, month, 1).getDay();
  const totalDaysInMonth = getDaysInMonth(year, month);
  const matrix = [];

  let currentDay = 1;

  for (let i = 0; i < 6; i++) {
    matrix[i] = [];

    for (let j = 0; j < DAYS_IN_WEEK; j++) {
      if (i === 0 && j < firstDayOfMonth) {
        matrix[i][j] = null;
      } else if (currentDay <= totalDaysInMonth) {
        matrix[i][j] = currentDay;
        currentDay++;
      } else {
        matrix[i][j] = null;
      }
    }
  }

  return matrix;
};

function App() {
  const currentDate = new Date();
  const [selectedDate, setSelectedDate] = useState(currentDate);
  const [notes, setNotes] = useState([
    { id: 1, date: '2023-12-31', name: 'Новый год', text: 'Теперь можно будет выдохнуть' },
    { id: 2, date: '2023-12-25', name: 'Начало сессии', text: 'Зачет по вебу' },
  ]);

  const handleDateClick = (day) => {
    if (day) {
      const newSelectedDate = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), day);
      setSelectedDate(newSelectedDate);
    }
  };


  const daysMatrix = generateCalendarMatrix(selectedDate.getFullYear(), selectedDate.getMonth());

  return (
    <div className="App">
      <h1>Календарь</h1>
      <div className="calendar">
        <div className="header">
          <button onClick={() => setSelectedDate(new Date(selectedDate.getFullYear(), selectedDate.getMonth() - 1, 1))}>
            Предыдущий месяц
          </button>
          <h2>
            {new Intl.DateTimeFormat('default', { month: 'long', year: 'numeric' }).format(selectedDate)}
          </h2>
          <button onClick={() => setSelectedDate(new Date(selectedDate.getFullYear(), selectedDate.getMonth() + 1, 1))}>
            Следующий месяц
          </button>
        </div>
        <table className="days-table">
          <thead>
            <tr>
              {['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].map((day) => (
                <th key={day}>{day}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {daysMatrix.map((week, rowIndex) => (
              <tr key={rowIndex}>
                {week.map((day, colIndex) => {
                  const isToday =
                    day === currentDate.getDate() &&
                    selectedDate.getMonth() === currentDate.getMonth() &&
                    selectedDate.getFullYear() === currentDate.getFullYear();

                  const note = notes.find(
                    (note) =>
                      note.date ===
                      `${selectedDate.getFullYear()}-${(selectedDate.getMonth() + 1).toString().padStart(2, '0')}-${day !== null ? day.toString().padStart(2, '0') : ''}`
                  );

                  return (
                    <td
                      key={colIndex}
                      className={`day ${day ? 'active' : ''} ${day === selectedDate.getDate() ? 'selected' : ''} ${
                        note ? 'note-day' : ''
                      } ${isToday ? 'today' : ''}`}
                      onClick={() => (handleDateClick(day))}
                    >
                      {day !== null && (
                        <>
                          <div className="day-name">{note ? note.name : ''}</div>
                          {day}
                        </>
                      )}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="notes">
        <h2>Заметка для {selectedDate.toLocaleDateString()}</h2>
        <ul>
          {notes
            .filter((note) => {
              const noteDate = new Date(note.date);
              return (
                noteDate.getFullYear() === selectedDate.getFullYear() &&
                noteDate.getMonth() === selectedDate.getMonth() &&
                noteDate.getDate() === selectedDate.getDate()
              );
            })
            .map((note) => (
              <li key={note.id}>
                <div className="note-name">{note.name}</div>
                <div className="note-text">{note.text}</div>
              </li>
            ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
