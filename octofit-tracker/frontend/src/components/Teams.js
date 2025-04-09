import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [teamName, setTeamName] = useState('');

  useEffect(() => {
    fetch('https://miniature-fiesta-wrr74vjpvv9625jwp-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('https://miniature-fiesta-wrr74vjpvv9625jwp-8000.app.github.dev/api/teams/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: teamName }),
    })
      .then(response => response.json())
      .then(newTeam => {
        setTeams([...teams, newTeam]);
        setTeamName('');
      })
      .catch(error => console.error('Error:', error));
  };

  return (
    <div>
      <h1 className="text-primary mb-4">Teams</h1>
      <button
        type="button"
        className="btn btn-primary mb-3"
        data-bs-toggle="modal"
        data-bs-target="#addTeamModal"
      >
        Add Team
      </button>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
              </tr>
            </thead>
            <tbody>
              {teams.map(team => (
                <tr key={team.id}>
                  <td>{team.id}</td>
                  <td>{team.name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal */}
      <div className="modal fade" id="addTeamModal" tabIndex="-1" aria-labelledby="addTeamModalLabel" aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="addTeamModalLabel">Add Team</h5>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="teamName" className="form-label">Team Name</label>
                  <input
                    type="text"
                    className="form-control"
                    id="teamName"
                    value={teamName}
                    onChange={(e) => setTeamName(e.target.value)}
                  />
                </div>
                <button type="submit" className="btn btn-primary" data-bs-dismiss="modal">Save</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Teams;