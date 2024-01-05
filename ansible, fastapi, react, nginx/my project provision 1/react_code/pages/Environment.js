import React, { useState, useEffect } from 'react';
import styles from '../my-style.module.css';
import Heading from '../components/Heading';
import NavBar from '../components/Navigation_bar';
import EnvBar from '../components/Environment_nav';

const Environment = () => {
  const [environments, setEnvironments] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http:///172.21.200.115:5000/environments');
        if (!response.ok) {
          console.error('error 1')
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('data  : ', data);
        setEnvironments(data.Environments);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
     <Heading />
     <NavBar />
     <EnvBar />

      <h2 className={styles.bigblue}>Environments</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Status</th>
            <th>Region_code</th>
            <th>Kony_Account_ID</th>
            <th>Create Date</th>
            <th>Active</th>
          </tr>
        </thead>
          <tbody>
            {environments.length > 0 ? (
               environments.map(environment => (
            <tr key={environment.id}>
             <td>{environment.id}</td>
             <td>{environment.name}</td>
             <td>{environment.status}</td>
             <td>{environment.region_code}</td>
             <td>{environment.kony_account_id}</td>
             <td>{environment.create_date}</td>
             <td>{environment.is_env_disabled ? 'Yes' : 'No'}</td>
            </tr>
        ))
  ) : (
    <tr>
      <td colSpan="5">Loading...</td>
    </tr>
  )}
</tbody>

	  </table>
    </div>
  );
};

export default Environment;

